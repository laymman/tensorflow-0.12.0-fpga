#include "tensorflow/core/framework/op_kernel.h"
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/core/framework/shape_inference.h"
#include "tensorflow/core/platform/logging.h"
#include <iostream>

#include "im2col.h"

using namespace std;
using namespace tensorflow;

#define OPNAME Conv2dIm2col
#define OPNAME_S "Conv2dIm2col"
#define OPNAME_OP Conv2dIm2colOp

REGISTER_OP(OPNAME_S)
	.Input("float: input")
	.Input("float: filter")
	.Input("int: stride")
	.Input("int: padding")
	.Output("float: output")
;

template <typename T>
class OPNAME_OP : public OpKernel {
public:
    explicit OPNAME_OP(OpKernelConstruction* ctx) : OpKernel(ctx) {}

    void Compute(OpKernelContext* ctx) override {
        DCHECK_EQ(4, ctx->num_inputs());

        // inputs
        const Tensor& input = ctx->input(0);
        const Tensor& filter = ctx->input(1);
        const Tensor& stride = ctx->input(2);
        const Tensor& padding = ctx->input(3);
        
        // inter params
        int output_dim_0 = 0;
        int output_dim_1 = 0;
        int output_dim_2 = 0;
        int output_dim_3 = 0;
        int pad_top = 0;
        int pad_left = 0;
      
        // calls
        void* padding(
        			reinterpret_cast<int*>(stride),
        			input.shape().dim_size(1),
        			input.shape().dim_size(2),
        			filter.shape().dim_size(1),
        			filter.shape().dim_size(2),
        			reinterpret_cast<int*>(output_dim_0),
        			reinterpret_cast<int*>(output_dim_1),
        			reinterpret_cast<int*>(output_dim_2),
        			reinterpret_cast<int*>(output_dim_3),
        			reinterpret_cast<int*>(pad_top),
        			reinterpret_cast<int*>(pad_left));

        Tensor *output = nullptr;
        TensorShape output_shape;
        output_shape.AddDim(output_dim_0);
        output_shape.AddDim(output_dim_1);
        output_shape.AddDim(output_dim_2);
        output_shape.AddDim(output_dim_3);
        OP_REQUIRES_OK(ctx, ctx->allocate_output(0, output_shape, &output));

        void* im2col_gemm(
        			reinterpret_cast<float*>(input),
        			reinterpret_cast<float*>(filter),
        			input.shape().dim_size(0),
        			input.shape().dim_size(1),
        			input.shape().dim_size(2),
        			input.shape().dim_size(3),
        			filter.shape().dim_size(1),
        			filter.shape().dim_size(2),
        			filter.shape().dim_size(3),
        			reinterpret_cast<char*>(stride),
        			pad_top,
        			pad_left,
        			output_dim_1,
        			output_dim_2,
        			reinterpret_cast<float*>(output));
    }
};

#define REGISTER_KERNEL(type)                                              \
    REGISTER_KERNEL_BUILDER(                                               \
        Name(OPNAME_S).Device(DEVICE_CPU).TypeConstraint<type>("T"),       \
        OPNAME_OP<type>)

REGISTER_KERNEL(int32);
REGISTER_KERNEL(float);
REGISTER_KERNEL(double);

#undef REGISTER_KERNEL
