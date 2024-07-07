# Documentation
- Class name: ImageFromBatch
- Category: image/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageFromBatch node is designed to extract a series of images from a group of images. It serves as a key component in the image-processing workflow, enabling users to isolate and operate specific image data segments efficiently. The function of the node is essential when processing large volumes of image data and allows for centralized analysis and processing of specific image subsets.

# Input types
## Required
- image
    - The 'image'parameter is the main input of the node, which represents the batch of images to be processed. It is essential because it forms the basis for all subsequent operations within the node. The performance of the node and the quality of the image extracted depend heavily on the integrity and format of the batch of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- batch_index
    - The 'batch_index'parameter specifies the initial index that begins to be extracted in the image batch. It plays an important role in determining the subset of images to be processed, allowing accurate control over which images to select for further analysis.
    - Comfy dtype: INT
    - Python dtype: int
- length
    - The 'legth' parameter indicates the number of continuous images taken from the batch, starting with the specified 'batch_index'. It is important because it determines the size of the image sequence that the node will output and affects the scope of the subsequent image processing task.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image_sequence
    - The 'image_security'output is based on a collection of images that are extracted from the input batch by the specified index and length. It represents the main output of nodes and is important for downstream tasks requiring analysis or operation of a dedicated set of images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageFromBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'batch_index': ('INT', {'default': 0, 'min': 0, 'max': 4095}), 'length': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'frombatch'
    CATEGORY = 'image/batch'

    def frombatch(self, image, batch_index, length):
        s_in = image
        batch_index = min(s_in.shape[0] - 1, batch_index)
        length = min(s_in.shape[0] - batch_index, length)
        s = s_in[batch_index:batch_index + length].clone()
        return (s,)
```