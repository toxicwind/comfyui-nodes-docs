# Documentation
- Class name: DWPreprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The DWPreprocessor_Provider_for_SEGS category aims to facilitate semantic pre-processing of images by using advanced attitude estimation techniques. It is integrated with the ComfyUI platform to enhance the accuracy of partitions by detecting and processing key features such as hands, bodies and faces. This node enhances the quality of output partitions by providing detailed and refined input for partition models, contributing to the overall image analysis process.

# Input types
## Required
- detect_hand
    - This parameter controls whether hand-checking is enabled during the pre-processing phase. This function can significantly improve the accuracy of splits by identifying and processing hand-related features.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- detect_body
    - This parameter enables or disables body testing during pre-processing. Physical testing is essential for semantic division, as it helps to identify the overall structure and layout of the image, which is essential for accurate partitioning.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- detect_face
    - The facial test parameters allow for the identification and processing of facial features during the pre-treatment phase. This is particularly useful for applications where facial features are key components of the split mission.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- resolution_upscale_by
    - This parameter adjusts the resolution of the image input by the specified zoom factor. Magnification enhances the details and clarity of the image, which may lead to better partitioning results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS_PREPROCESSOR
    - The output of the node is a dictionary containing pre-processed image data, which is now ready for semantic division. Pre-treatment includes hand, body, and facial tests, and may involve resolution magnification, all of which contribute to the quality of the split.
    - Comfy dtype: DICTIONARY
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class DWPreprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detect_hand': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'detect_body': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'detect_face': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'resolution_upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.5, 'max': 100, 'step': 0.1})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, detect_hand, detect_body, detect_face, resolution_upscale_by):
        obj = DWPreprocessor_wrapper(detect_hand, detect_body, detect_face, upscale_factor=resolution_upscale_by, bbox_detector='yolox_l.onnx', pose_estimator='dw-ll_ucoco_384_bs5.torchscript.pt')
        return (obj,)
```