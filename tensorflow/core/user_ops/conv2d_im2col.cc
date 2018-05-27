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
		const int input_dim_0 = input.shape().dim_size(0);
		const int input_dim_1 = input.shape().dim_size(1);
		const int input_dim_2 = input.shape().dim_size(2);
		const int input_dim_3 = input.shape().dim_size(3);
		//const int filter_dim_0 = filter.shape().dim_size(0);
		const int filter_dim_1 = filter.shape().dim_size(1);
        const int filter_dim_2 = filter.shape().dim_size(2);
		const int filter_dim_3 = filter.shape().dim_size(3);

        // enable to access tensors directly
		//auto padding_scalar = padding.scalar<int>();
		//auto strides_vec = strides.vec<int>();

        // get padding border
        int pad_top = 0, pad_left = 0;
		int out_dim_0 = 0, out_dim_1 = 0, out_dim_2 = 0, out_dim_3 = 0;
        
        get_padding(reinterpret_cast<const int*>(padding.tensor_data().data()), 
					reinterpret_cast<const int*>(strides.tensor_data().data()),
				    input_dim_0,
				    input_dim_1, input_dim_2,
				    filter_dim_1, filter_dim_2,
				    filter_dim_3,
				    &pad_top, 
					&pad_left,
				    &out_dim_0, 
                    &out_dim_1,
				    &out_dim_2, 
                    &out_dim_3);
		LOG(INFO)<<"out_h"<<out_dim_1<<endl;
		LOG(INFO)<<"out_w"<<out_dim_2<<endl;
		LOG(INFO)<<"out_dim_0"<<out_dim_0<<endl;
		LOG(INFO)<<"out_dim_1"<<out_dim_1<<endl;
		LOG(INFO)<<"out_dim_2"<<out_dim_2<<endl;
		LOG(INFO)<<"out_dim_3"<<out_dim_3<<endl;

        Tensor *output = nullptr;
        TensorShape output_shape;
        output_shape.AddDim(out_dim_0);
        output_shape.AddDim(out_dim_1);
        output_shape.AddDim(out_dim_2);
        output_shape.AddDim(out_dim_3);
        OP_REQUIRES_OK(ctx, ctx->allocate_output(0, output_shape, &output));

        // im2col and convolution
		im2col_gemm<T>(reinterpret_cast<const T*>(input.tensor_data().data()), 
					   reinterpret_cast<const T*>(filter.tensor_data().data()), 
	        		   input_dim_0,
	        		   input_dim_1, input_dim_2,
	        		   input_dim_3, 
	        		   filter_dim_1, filter_dim_2, 
	        		   filter_dim_3, 
	        		   reinterpret_cast<const int*>(strides.tensor_data().data()),
	       			   pad_top, pad_left, 
	        		   out_dim_1,
				       out_dim_2, 
	        		   reinterpret_cast<T*>(const_cast<char*>(output->tensor_data().data())));
/*
        im2col_gemm<T>(reinterpret_cast<const T*>(input.tensor_data().data()), 
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
*/
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
