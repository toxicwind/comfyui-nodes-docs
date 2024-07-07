# Documentation
- Class name: HEDPreprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The HEDPreprocessor_Provider_for_SEGS class is designed to provide HED (a fully embedded edge test) algorithms for image partition applications. It enhances the edge of the image using the HED preprocessor, which is essential for dividing and identifying the area within the image. This node is essential for tasks requiring detailed margin detection and is part of the SEGS (semantic edge-directed partition) workflow.

# Input types
## Required
- safe
    - The `safe' parameter is a boolean symbol used to determine whether certain security features are enabled or disabled during the pre-processing phase. It plays a key role in ensuring the stability and reliability of image processing, while preventing potential errors or hypotheses that may arise in the margin detection process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- SEGS_PREPROCESSOR
    - The HEDPreprocessor_Provider_for_SEGS output is a pre-processing image using the HED algorithm to enhance the edges. This output is a crucial step in the process of partitioning, as it provides a detailed indication of the image structure, which is essential for accurate partitions.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class HEDPreprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'safe': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, safe):
        obj = HED_Preprocessor_wrapper(safe, 'HEDPreprocessor')
        return (obj,)
```