# Documentation
- Class name: MiDaS_DepthMap_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node improves the quality of the split output by using the MiDaS model to generate depth maps of semantic split tasks.

# Input types
## Required
- a
    - The parameter `a' is a key input to the process of estimating the depth of the impact, affecting the overall accuracy and detail of the depth map.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bg_threshold
    - The `bg_threshold' parameter is essential to distinguish the outlook from the background in the depth map, thus increasing the accuracy of the split.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS_PREPROCESSOR
    - The output provides a pre-processed depth map, which is used as input to the split model and significantly improves the quality of the split results.
    - Comfy dtype: NODE
    - Python dtype: MiDaS_DepthMapPreprocessor

# Usage tips
- Infra type: GPU

# Source code
```
class MiDaS_DepthMap_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'a': ('FLOAT', {'default': np.pi * 2.0, 'min': 0.0, 'max': np.pi * 5.0, 'step': 0.05}), 'bg_threshold': ('FLOAT', {'default': 0.1, 'min': 0, 'max': 1, 'step': 0.05})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, a, bg_threshold):
        obj = MiDaS_DepthMap_Preprocessor_wrapper(a, bg_threshold)
        return (obj,)
```