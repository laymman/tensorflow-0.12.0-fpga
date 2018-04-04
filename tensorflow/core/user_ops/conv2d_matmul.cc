#include "tensorflow/core/framework/op_kernel.h"
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/core/framework/shape_inference.h"
#include "tensorflow/core/platform/logging.h"
#include<iostream>

using namespace std;
using namespace tensorflow;

REGISTER_OP("Conv2dMatmul")
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
class Conv2dMatmulOp : public OpKernel {
public:
	explicit Conv2dMatmulOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

	void Compute(OpKernelContext* ctx) override {
		DCHECK_EQ(4, ctx->num_inputs());

		const Tensor& input = ctx->input(0);
		const Tensor& filter = ctx->input(1);
		const Tensor& strides = ctx->input(2);
		const Tensor& padding = ctx->input(3);

		DCHECK_EQ(input.shape().dims(), 4);
		DCHECK_EQ(filter.shape().dims(), 4);
		DCHECK_EQ(strides.shape().dims(), 1);
		DCHECK_EQ(padding.shape().dims(), 0);
		DCHECK_EQ(input.shape().dim_size(3), filter.shape().dim_size(2));

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
		auto new_input = input.tensor<T, 4>();
		auto new_filter = filter.tensor<T, 4>();


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

        // construct output tensor: [batch, out_height, out_width, out_channels]
		Tensor* output = nullptr;
        TensorShape output_shape;
		output_shape.AddDim(batch);
		output_shape.AddDim(out_height);
		output_shape.AddDim(out_width);
		output_shape.AddDim(out_channels);
        OP_REQUIRES_OK(ctx, ctx->allocate_output(0, output_shape, &output));
        auto output_tensor = output->tensor<T, 4>();


        // reshape input and filter:
        // mat_input[batch*out_height*out_width, filter_height*filter_width*in_channels]
        // mat_filter[filter_height*filter_width*in_channels, out_channels]
        int mat_input_dim0 = batch * out_height * out_width;
        int mat_input_dim1 = filter_height * filter_width * in_channels;
        int mat_filter_dim0 = filter_height * filter_width * in_channels;
        int mat_filter_dim1 = out_channels;
        int *mat_input = new int[mat_input_dim0 * mat_input_dim1];
        int *mat_filter = new int[mat_filter_dim0 * mat_filter_dim1];
        int **mat_output = new int*[mat_input_dim0];
        for(int i = 0; i < mat_input_dim0; i++){
        	mat_output[i] = new int[mat_filter_dim1];
        }

        // construct input matrix with shape[mat_input_dim0, mat_input_dim1]
        for(int b = 0; b < batch; b++){
        	for(int i = 0; i < out_height; i++){
        		for(int j = 0; j < out_width; j++){

        			for(int di = 0; di < filter_height; di++){
        				for(int dj = 0; dj < filter_width; dj++){
        					int in_i = i*strides_vec(1) + di - pad_top;
        					int in_j = j*strides_vec(2) + dj - pad_left;
        					for(int q = 0; q < in_channels; q++){
        						int offset = (b*out_height*out_width + i*out_height+j) * mat_input_dim1 \
        									+ (di*filter_height+dj)*in_channels \
        									+ q;
        						// out of border, padding zero
        						if(in_i < 0 || in_i >= in_height || in_j < 0 || in_j >= in_width)
        							mat_input[offset] = 0;
        						else 
        							mat_input[offset] = new_input(b, in_i, in_j, q);
        					}
        				}
        			}

        		}
        	}
        }

        // construct filter matrix: [mat_filter_dim0, mat_filter_dim1]
        for(int di = 0; di < filter_height; di++){
        	for(int dj = 0; dj < filter_width; dj++){
        		for(int q = 0; q < in_channels; q++){
        			for(int k = 0; k < out_channels; k++){
        				int offset = ((di*filter_height+dj)*in_channels + q)*out_channels + k;
        				mat_filter[offset] = new_filter(di, dj, q, k);
        			}
        		}
        	}
        }

        // 2d convolution
//      sendToFpga(mat_input, mat_input_dim0, mat_input_dim1,
//                 mat_filter, mat_filter_dim0, mat_filter_dim1);
//	    recvFromFpga(mat_output, mat_input_dim0, mat_filter_dim1);

	    for(int i=0; i < mat_input_dim0; i++){
            for(int j=0; j < mat_filter_dim1; j++){
                mat_output[i][j] = 0;
                for(int k=0; k < mat_input_dim1; k++){
                    mat_output[i][j] += mat_input[i*mat_input_dim1 + k]*mat_filter[k*mat_filter_dim1 + j];
                }
            }
        }
        

        // copy result to output tensor
        for(int b = 0; b < batch; b++){
        	for(int i = 0; i < out_height; i++){
        		for(int j = 0; j < out_width; j++){
        			for(int k = 0; k < out_channels; k++){
        				int offset = b*out_height*out_width + i*out_height + j;
        				output_tensor(b, i, j, k) = mat_output[offset][k];
        			}
        		}
        	}
        }

        delete []mat_input;
        delete []mat_filter;
        for(int i = 0; i < batch; i++){
        	delete []mat_output[i];
        }
        delete []mat_output;
	}
};

#define REGISTER_KERNEL(type)                                       \
    REGISTER_KERNEL_BUILDER(                                          \
        Name("Conv2dMatmul").Device(DEVICE_CPU).TypeConstraint<type>("T"), \
        Conv2dMatmulOp<type>)

REGISTER_KERNEL(int32);
REGISTER_KERNEL(float);
REGISTER_KERNEL(double);

#undef REGISTER_KERNEL
