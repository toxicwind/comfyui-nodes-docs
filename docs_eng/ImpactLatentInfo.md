# Documentation
- Class name: ImpactLatentInfo
- Category: ImpactPack/Logic/_for_test
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The "doit" method of the ImpactLatentInfo node is designed to process potential information by determining the dimensions of the given input sample. It operates the potential space in the abstract to provide a derivative space dimension, which is essential in the further processing or visualization of image-related tasks.

# Input types
## Required
- value
    - The parameter 'value' is essential because it contains a potential sample for node operations. It directly affects the ability of node to calculate the spatial dimensions of the input data.
    - Comfy dtype: Dict[str, torch.Tensor]
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- batch
    - The parameter 'batch' represents the number of samples in the batch, which is an essential aspect of batch processing in machine learning applications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The parameter 'height' represents the vertical dimension of the processed image, which is a key factor in image resolution and spatial analysis.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The parameter 'width' indicates the horizontal dimensions of the image, which together with altitude determines the overall spatial range of the image.
    - Comfy dtype: INT
    - Python dtype: int
- channel
    - The parameter 'channel' represents the number of colour channels in the image, which is essential for understanding the complexity and composition of the image data.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactLatentInfo:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('LATENT',)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('batch', 'height', 'width', 'channel')

    def doit(self, value):
        shape = value['samples'].shape
        return (shape[0], shape[2] * 8, shape[3] * 8, shape[1])
```