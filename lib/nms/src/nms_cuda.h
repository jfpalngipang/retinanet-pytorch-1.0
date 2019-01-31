// int gpu_nms(THLongTensor * keep_out, THLongTensor* num_out, THCudaTensor * boxes, float nms_overlap_thresh);

int nms_cuda(THCudaIntTensor *keep_out, THCudaTensor *boxes_host,
             THCudaIntTensor *num_out, float nms_overlap_thresh);