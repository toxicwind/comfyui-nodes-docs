# Documentation
- Class name: Canny_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The Canny_Preprocessor_Provider_for_SEGS node is designed to pre-process images by applying the Canny margin detection algorithm in order to divide tasks. It enhances the edge of images, which can significantly improve their performance by providing more detailed structural information for subsequent partition models.

# Input types
## Required
- low_threshold
    - The low_threshold parameter is essential for the Canny margin detection algorithm because it determines the lower limit of the margin detection. It affects the sensitivity of the algorithm to noise and the precision of the edge detected.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_threshold
    - The high_threshold parameter plays a key role in the examination of Canny's edge, setting the upper limit of the edge link. It defines how strong the evidence of the edge must be in order to be considered significant.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS_PREPROCESSOR
    - The SEGS_PREPROCESSOR output is a pre-processed image with an enhanced edge, applicable to split tasks. It is the result of applying a specific threshold to the Canny edge test.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: Canny_Preprocessor_wrapper

# Usage tips
- Infra type: CPU

# Source code
```
class Canny_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'low_threshold': ('FLOAT', {'default': 0.4, 'min': 0.01, 'max': 0.99, 'step': 0.01}), 'high_threshold': ('FLOAT', {'default': 0.8, 'min': 0.01, 'max': 0.99, 'step': 0.01})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, low_threshold, high_threshold):
        obj = Canny_Preprocessor_wrapper(low_threshold, high_threshold)
        return (obj,)
```