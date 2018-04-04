import tensorflow as tf
import numpy as np

class Conv2dMatmulTest(tf.test.TestCase):
  def testConv2dMatmul(self):
    conv2d_im2col_module = tf.load_op_library('/home/jxiao/tensorflow/tensorflow-0.12.0-fpga/bazel-bin/tensorflow/core/user_ops/conv2d_im2col.so')
    conv2d_matmul_module = tf.load_op_library('/home/jxiao/tensorflow/tensorflow-0.12.0-fpga/bazel-bin/tensorflow/core/user_ops/conv2d_matmul.so')
    with self.test_session():
      input_ = np.random.randint(0, 9, size=(1, 3, 3, 2))
      filter_ = np.random.randint(0, 5, size=(2, 2, 2, 1))
      #print input_
      #print filter_
      result1 = conv2d_im2col_module.conv2d_im2col(input_.astype(float), filter_.astype(float), [1, 1, 1, 1], 0)
      output1 = result1.eval()
      result2 = conv2d_matmul_module.conv2d_matmul(input_.astype(float), filter_.astype(float), [1, 1, 1, 1], 0)
      output2 = result2.eval()
      self.assertAllEqual(output1, output2)

if __name__ == "__main__":
  tf.test.main()
