# Documentation
- Class name: TilePreprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The TilePreprocessor_Provider_for_SEGS class aims to improve the accuracy of the image split task by pre-processing the input image. It uses sampling methods on the pyramid to fine-tune image details to ensure that the partition model receives optimal data processing. This node contributes to the overall workflow by ensuring that the split process is as efficient and accurate as possible.

# Input types
## Required
- pyrUp_iters
    - The `pyrUp_iters' parameter is essential to control the number of overlaps used in sampling on the pyramid. It directly affects the detail and resolution level of the pre-processed image, and consequently the quality of the split output. Appropriately adjusted parameter significantly improves the split result.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- SEGS_PREPROCESSOR
    - The output of the TilePreprocessor_Provider_for_SEGS node is a pre-processing image for partitioning task optimization. This output is used as input for subsequent partition models to ensure that they receive the most accurate data in order to obtain reliable and accurate results.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: PIL.Image or numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class TilePreprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pyrUp_iters': ('INT', {'default': 3, 'min': 1, 'max': 10, 'step': 1})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, pyrUp_iters):
        obj = TilePreprocessor_wrapper(pyrUp_iters)
        return (obj,)
```