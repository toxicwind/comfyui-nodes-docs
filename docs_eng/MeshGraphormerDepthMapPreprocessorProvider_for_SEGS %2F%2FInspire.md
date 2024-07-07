# Documentation
- Class name: MeshGraphormerDepthMapPreprocessorProvider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is used to generate depth maps from images, which is essential for modelling and severing tasks in 3D. It uses advanced algorithms to estimate the depth of a single image and improves the quality expressed in 3D.

# Input types
## Required
- image
    - The input image is critical for generating the depth map, which serves as the basis for generating the depth map. Node processing the image to extract the depth information is essential for the subsequent 3D modelling and partitioning process.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray
## Optional
- mask
    - When providing mask parameters, it allows for selective processing of images. It allows nodes to focus on specific areas of interest in the image, thereby increasing the accuracy and relevance of the depth maps generated.
    - Comfy dtype: mask
    - Python dtype: numpy.ndarray

# Output types
- SEGS_PREPROCESSOR
    - The output is a pre-processor object that contains the resulting bathymetric chart. This bathymetric chart is a key intermediate product used in various 3Ds and split workflows as a basis for further processing.
    - Comfy dtype: preprocessor
    - Python dtype: object

# Usage tips
- Infra type: GPU

# Source code
```
class MeshGraphormerDepthMapPreprocessorProvider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self):
        obj = MeshGraphormerDepthMapPreprocessorProvider_wrapper()
        return (obj,)
```