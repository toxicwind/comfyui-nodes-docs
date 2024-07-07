# Documentation
- Class name: IPAAdapterFaceIDBatch
- Category: Adapter
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAAadapterFaceIDBatch node serves as an intermediary between input data and FaceID models to ensure the efficient processing of bulk data. It aims to simplify the application of FaceID models to data batches and to improve the overall performance and throughput of the system.

# Input types
## Required
- input_data
    - The input_data parameter is essential because it represents the image batch that the node will process. Its organization and quality directly affect the ability of the node to correctly apply the FaceyID model and produce accurate results.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- output_data
    - Output_data represents the application of the FaceID model to post-batch processing results. It contains the prediction or identification of the model, which is important for further analysis or downstream tasks.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IPAAdapterFaceIDBatch(IPAdapterFaceID):

    def __init__(self):
        self.unfold_batch = True
```