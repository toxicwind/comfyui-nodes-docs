# Documentation
- Class name: Color_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The Color_Preprocessor_Provider_for_SEGS class is designed to enhance image partition tasks by applying colour pre-processing techniques. The node intelligence adjusts the colour properties of the input image to improve the function of the partition model and ensures that the processed image is optimized for subsequent splits.

# Input types
## Required
- image
    - Image parameters are essential for the Color_Preprocessor_Provider_for_SEGS node, as it is inputted as a pre-processing algorithm. The quality and resolution of the image directly influences the validity of pre-processing and the accuracy of the partition of results.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray
## Optional
- mask
    - The mask parameter, while optional, can provide additional context for the pre-processing step, allowing for more targeted adjustments to the image. It can help to fine-tune the partitioning process by focusing on specific areas of the image.
    - Comfy dtype: mask
    - Python dtype: numpy.ndarray

# Output types
- SEGS_PREPROCESSOR
    - The output of the Color_Preprocessor_Provider_for_SEGS node is a pre-processed image for the optimum partitioning of tasks. This output is the input for the subsequent partition node to ensure that the split process benefits from the enhanced colour properties.
    - Comfy dtype: preprocessor
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class Color_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self):
        obj = Color_Preprocessor_wrapper()
        return (obj,)
```