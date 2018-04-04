#include "tensorflow/core/platform/logging.h"

template <typename T>
void matmul(T *a, int a_dim0, int a_dim1,
       		T *b, int b_dim0, int b_dim1, 
       		T *c){

	for(int i = 0; i < a_dim0; i++){
		for(int j = 0; j < b_dim1; j++){
			c[i*b_dim1 + j] = 0;
			for(int k = 0; k < b_dim0; k++){
				c[i*b_dim1 + j] += a[i*a_dim1 + k] * b[k*b_dim1 + j];
			}
		}
	}
	return ;
}

template <typename T>
void im2col(const T *input, const T *filter, 
	        int batch,
	        int in_h, int in_w,
	        int in_channels, 
	        int filter_h, int filter_w, 
	        int out_channels, 
	        int strides_h, int strides_w,
	        int pad_top, int pad_left, 
	        int out_h, int out_w,
	        T *output){

	// mat_input[out_height*out_width, filter_height*filter_width*in_channels]
  // mat_filter[filter_height*filter_width*in_channels, out_channels]
  int mat_input_dim0 = out_h * out_w;
  int mat_input_dim1 = filter_h * filter_w * in_channels;
  int mat_filter_dim0 = mat_input_dim1;
  int mat_filter_dim1 = out_channels;
  T *mat_input = new T[mat_input_dim0 * mat_input_dim1];
  T *mat_filter = new T[mat_filter_dim0 * mat_filter_dim1];
    
	// construct filter matrix: [mat_filter_dim0, mat_filter_dim1]
  for(int di = 0; di < filter_h; di++){
   	for(int dj = 0; dj < filter_w; dj++){
   		for(int q = 0; q < in_channels; q++){
   			for(int k = 0; k < out_channels; k++){
   				int offset0 = ((di*filter_h+dj)*in_channels + q)*out_channels + k;
   				int offset1 = di * filter_w*in_channels*out_channels \
   							      + dj * in_channels*out_channels          \
   							      + q  * out_channels                      \
   							      + k;
   				mat_filter[offset0] = filter[offset1];
     			}
     		}
     	}
  }


	// construct input matrix: [mat_input_dim0, mat_input_dim1]
  for(int b = 0; b < batch; b++){

   	for(int i = 0; i < out_h; i++){
   		for(int j = 0; j < out_w; j++){
        //LOG(INFO)<<"--------b="<<b<<", (i, j)="<<"("<<i<<","<<j<<")--------";
   			for(int di = 0; di < filter_h; di++){
   				for(int dj = 0; dj < filter_w; dj++){
   					int in_i = i*strides_h + di - pad_top;
     					int in_j = j*strides_w + dj - pad_left;
              //LOG(INFO)<<"("<<in_i<<','<<in_j<<'|'<<di<<','<<dj<<") ";
     					for(int q = 0; q < in_channels; q++){
     						int offset0 = (i*out_h+j) * mat_input_dim1 \
     									      + (di*filter_h+dj)*in_channels \
     									      + q;
     						int offset1 = b * in_h*in_w*in_channels \
     									      + in_i * in_w*in_channels    \
     									      + in_j * in_channels          \
     									      + q;
     						// out of border, padding zero
     						if(in_i < 0 || in_i >= in_h || in_j < 0 || in_j >= in_w)
     							mat_input[offset0] = 0;
     						else 
     							mat_input[offset0] = input[offset1];
       					}
     				}
     			}
     		}
     	}
      // LOG(INFO)<<mat_input[0]<<','<<mat_input[1]<<','<<mat_input[2]<<','<<mat_input[3]<<','<<mat_input[4]<<','<<mat_input[5]<<','<<mat_input[6]<<','<<mat_input[7];
      // LOG(INFO)<<mat_input[8]<<','<<mat_input[9]<<','<<mat_input[10]<<','<<mat_input[11]<<','<<mat_input[12]<<','<<mat_input[13]<<','<<mat_input[14]<<','<<mat_input[15];
      // LOG(INFO)<<mat_input[16]<<','<<mat_input[17]<<','<<mat_input[18]<<','<<mat_input[19]<<','<<mat_input[20]<<','<<mat_input[21]<<','<<mat_input[22]<<','<<mat_input[23];
      // LOG(INFO)<<mat_input[24]<<','<<mat_input[25]<<','<<mat_input[26]<<','<<mat_input[27]<<','<<mat_input[28]<<','<<mat_input[29]<<','<<mat_input[30]<<','<<mat_input[31];
      // LOG(INFO)<<" ";
      // LOG(INFO)<<mat_filter[0]<<','<<mat_filter[1]<<','<<mat_filter[2]<<','<<mat_filter[3]<<','<<mat_filter[4]<<','<<mat_filter[5]<<','<<mat_filter[6]<<','<<mat_filter[7];
     	matmul<T>(mat_input, mat_input_dim0, mat_input_dim1,
         		    mat_filter, mat_filter_dim0, mat_filter_dim1, 
       		      &(output[b*out_h*out_w*out_channels]));
    }

    delete []mat_input;
    delete []mat_filter;

    return ;
}
