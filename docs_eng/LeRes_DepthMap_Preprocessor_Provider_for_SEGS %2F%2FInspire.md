# Documentation
- Class name: LeReS_DepthMap_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

This node class is used to pre-process depth maps for split tasks, optimize input data using the Leres algorithm and improve the quality of split output.

# Input types
## Required
- rm_nearest
    - This parameter adjusts the removal threshold for nearby pixels, which is essential to define the accuracy of the depth map and the clarity of the dividing boundary.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rm_background
    - This parameter sets a threshold to remove background noise, which is essential to isolate the subject and ensure the accuracy of the split.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- boost
    - When this parameter is enabled, enhancing the features of the depth map may improve the split result, but may increase processing time.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- SEGS_PREPROCESSOR
    - The output provides a refined basis for further processing by pre-processing depth maps for the optimization of split tasks.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: LeReS_DepthMapPreprocessor

# Usage tips
- Infra type: CPU

# Source code
```
class LeReS_DepthMap_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'rm_nearest': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100, 'step': 0.1}), 'rm_background': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100, 'step': 0.1})}, 'optional': {'boost': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, rm_nearest, rm_background, boost=False):
        obj = LeReS_DepthMap_Preprocessor_wrapper(rm_nearest, rm_background, boost)
        return (obj,)
```