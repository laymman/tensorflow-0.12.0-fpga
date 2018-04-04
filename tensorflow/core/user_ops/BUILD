load("//tensorflow:tensorflow.bzl", "tf_custom_op_library")

#tf_custom_op_library(
#    name = "cal_mat_mul.so",
#    srcs = ["cal_mat_mul.cc"],
#)

#cc_library(
#   name = "Matrix",
#   srcs = ["Matrix.h"],
#   linkopts = ["-lriffa"],
#)

cc_library(
   name = "im2col",
   srcs = ["im2col.h"],
)

tf_custom_op_library(
   name = "conv2d_im2col.so",
   srcs = ["conv2d_im2col.cc"],
   deps = [":im2col"],
)

tf_custom_op_library(
   name = "conv2d_matmul.so",
   srcs = ["conv2d_matmul.cc"],
#   deps = [":Matrix"],
)

tf_custom_op_library(
    name = "conv2d_manual.so",
    srcs = ["conv2d_manual.cc"],
)
