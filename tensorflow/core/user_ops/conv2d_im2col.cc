#include "tensorflow/core/framework/op_kernel.h"
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/core/framework/shape_inference.h"
#include "tensorflow/core/platform/logging.h"
#include<iostream>

#include "im2col.h"

using namespace std;
using namespace tensorflow;

REGISTER_OP("Conv2dIm2col")
	.Attr("T: {int32, float, double}")
	.Input("input: T")
	.Input("filter: T")
	.Input("strides: int32")
	.Input("padding: int32") // 1: SAME, 0: VALID
	.Output("output: T")
	.SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c){
		shape_inference::ShapeHandle input_shape, filter_shape, strides_shape, pad_shape;
		TF_RETURN_IF_ERROR(c->WithRank(c->input(0), 4, &input_shape));
		TF_RETURN_IF_ERROR(c->WithRank(c->input(1), 4, &filter_shape));
		TF_RETURN_IF_ERROR(c->WithRank(c->input(2), 1, &strides_shape));
		TF_RETURN_IF_ERROR(c->WithRank(c->input(3), 0, &pad_shape));

		shape_inference::DimensionHandle in_channels_0 = c->Dim(input_shape, 3);
		shape_inference::DimensionHandle in_channels_1 = c->Dim(filter_shape, 2);
		shape_inference::DimensionHandle merged;
		TF_RETURN_IF_ERROR(c->Merge(in_channels_0, in_channels_1, &merged));

		c->set_output(0, c->UnknownShapeOfRank(4));
		return Status::OK();
	});

template <typename T>
class Conv2dIm2colOp : public OpKernel {
public:
	explicit Conv2dIm2colOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

	void Compute(OpKernelContext* ctx) override {
		DCHECK_EQ(4, ctx->num_inputs());

		const Tensor& input = ctx->input(0);
		const Tensor& filter = ctx->input(1);
		const Tensor& strides = ctx->input(2);
		const Tensor& padding = ctx->input(3);

        // shape info
		const int batch = input.shape().dim_size(0);
		const int in_height = input.shape().dim_size(1);
		const int in_width = input.shape().dim_size(2);
		const int in_channels = input.shape().dim_size(3);
		const int filter_height = filter.shape().dim_size(0);
		const int filter_width = filter.shape().dim_size(1);
		const int out_channels = filter.shape().dim_size(3);

        // enable to access tensors directly
		auto padding_scalar = padding.scalar<int>();
		auto strides_vec = strides.vec<int>();


        // get padding border
		int out_height = 0, out_width = 0;
        int pad_along_height = 0, pad_along_width = 0;
        int pad_top = 0, pad_left = 0;
        
        //[reference]: https://www.tensorflow.org/api_guides/python/nn#convolution
        if (padding_scalar(0) == 1){
        	// SAME
        	out_height = ceil(float(in_height) / float(strides_vec(1)));
			out_width  = ceil(float(in_width) / float(strides_vec(2)));

			if (in_height % int(strides_vec(1)) == 0)
  				pad_along_height = max(filter_height - int(strides_vec(1)), 0);
			else
  				pad_along_height = max(filter_height - (in_height % int(strides_vec(1))), 0);
			if (in_width % int(strides_vec(2)) == 0)
  				pad_along_width = max(filter_width - int(strides_vec(2)), 0);
			else
  				pad_along_width = max(filter_width - (in_width % int(strides_vec(2))), 0);

  			pad_top = pad_along_height / 2;
			//pad_bottom = pad_along_height - pad_top;
			pad_left = pad_along_width / 2;
			//pad_right = pad_along_width - pad_left;
        }else{
        	// VALID
        	out_height = ceil(float(in_height - filter_height + 1) / float(strides_vec(1)));
			out_width  = ceil(float(in_width - filter_width + 1) / float(strides_vec(2)));
        }

        Tensor *output = nullptr;
        TensorShape output_shape;
        output_shape.AddDim(batch);
        output_shape.AddDim(out_height);
        output_shape.AddDim(out_width);
        output_shape.AddDim(out_channels);
        OP_REQUIRES_OK(ctx, ctx->allocate_output(0, output_shape, &output));

        // im2col and convolution
        im2col<T>(reinterpret_cast<const T*>(input.tensor_data().data()), 
                  reinterpret_cast<const T*>(filter.tensor_data().data()), 
                  batch,
                  in_height, in_width,
                  in_channels, 
                  filter_height, filter_width, 
                  out_channels, 
                  strides_vec(1), strides_vec(2),
                  pad_top, pad_left, 
                  out_height, out_width,
                  reinterpret_cast<T*>(const_cast<char*>(output->tensor_data().data())));

        // col2im(mat_output);
	}
};

#define REGISTER_KERNEL(type)                                              \
    REGISTER_KERNEL_BUILDER(                                               \
        Name("Conv2dIm2col").Device(DEVICE_CPU).TypeConstraint<type>("T"), \
        Conv2dIm2colOp<type>)

REGISTER_KERNEL(int32);
REGISTER_KERNEL(float);
REGISTER_KERNEL(double);

#undef REGISTER_KERNEL