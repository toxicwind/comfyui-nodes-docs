# Documentation
- Class name: OpenPose_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

OpenPose_Preprocessor_Provider_for_SEGS is designed to facilitate semantic pre-processing of images by using OpenPose technology to detect and analyse human postures. It allows for the identification of hands, bodies and faces in images, which is essential for understanding the application of human postures and interactions in the landscape.

# Input types
## Required
- detect_hand
    - This parameter controls whether the node tries to detect the hand in the input image. Enables this function to provide valuable data for applications that need to understand hand position and interaction.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- detect_body
    - This parameter enables or disables human testing in the image. Physical testing is essential for applications that require an understanding of the overall structure and posture of the individual in the scene.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- detect_face
    - By switching this parameter, the node can be instructed to detect facial features. This capability is essential for the analysis of facial expressions and interactive applications.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- resolution_upscale_by
    - This parameter adjusts the resolution of the input image to improve the accuracy of attitude testing. An enhanced resolution provides more detailed information, which is useful for complex scenarios or high-resolution split tasks.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS_PREPROCESSOR
    - The output of the node is a pre-processed image that contains human attitude notes, which can be used as the basis for semantic division of tasks. These notes are essential for the accurate identification and classification of the different elements in the scenario.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class OpenPose_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detect_hand': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'detect_body': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'detect_face': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'resolution_upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.5, 'max': 100, 'step': 0.1})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, detect_hand, detect_body, detect_face, resolution_upscale_by):
        obj = OpenPose_Preprocessor_wrapper(detect_hand, detect_body, detect_face, upscale_factor=resolution_upscale_by)
        return (obj,)
```