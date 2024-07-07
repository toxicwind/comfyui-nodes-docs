# Documentation
- Class name: SeargeControlnetAdapterV2
- Category: UI_PROMPTING
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the adaptation of the control network mechanism to enhance image processing tasks. It selects and applies a variety of peripheral detection and image enhancement algorithms according to the dynamic input parameters and aims to improve visual output according to specific requirements.

# Input types
## Required
- controlnet_mode
    - The identification of the type of control network to be used significantly affects the processing method and the quality of the final image.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- controlnet_preprocessor
    - Enables or disables pre-processing of network images and optimizes subsequent image processing steps.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- strength
    - Adjust the intensity of the impact of the control network on the image, directly affecting the final visual results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- low_threshold
    - Sets the lower limit of the sensitivity of the edge detection to influence the particle size of the edge detected in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_threshold
    - Define the upper limit of the sensitivity of the margin test, affecting the visibility of the edge in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - Specifies the starting percentage of the image processing range and determines the initial segment of the image affected.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - Indicates the end percentage of the image processing range and establishes the final segment of the image affected.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_augmentation
    - Control of the level of noise enhancement applied to the image enhances the robustness of the control network.
    - Comfy dtype: FLOAT
    - Python dtype: float
- revision_enhancer
    - Activate or deactivate the modified booster, which refines and controls the output of the network to improve accuracy.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- source_image
    - Provides the basic images that control network processing as the basic input for all subsequent image operations.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- data
    - Provide additional data flow information to control networks for more complex processing.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: List[Dict[str, Any]]

# Output types
- data
    - The data flow information, which includes control network processing updates, can be further utilized downstream.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]
- preview
    - Displays a visual preview of the processed image and the effects of the control network adjustments.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeControlnetAdapterV2:

    def __init__(self):
        self.expected_size = None
        self.hed_annotator = 'ControlNetHED.pth'
        self.leres_annotator = 'res101.pth'
        self.hed_annotator_full_path = get_full_path('annotators', self.hed_annotator)
        self.leres_annotator_full_path = get_full_path('annotators', self.leres_annotator)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'controlnet_mode': (UI.CONTROLNET_MODES, {'default': UI.NONE}), 'controlnet_preprocessor': ('BOOLEAN', {'default': False}), 'strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 10.0, 'step': 0.05}), 'low_threshold': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'high_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'end_percent': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'noise_augmentation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'revision_enhancer': ('BOOLEAN', {'default': False})}, 'optional': {'data': ('SRG_DATA_STREAM',), 'source_image': ('IMAGE',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM', 'IMAGE')
    RETURN_NAMES = ('data', 'preview')
    FUNCTION = 'get_value'
    CATEGORY = UI.CATEGORY_UI_PROMPTING

    def process_image(self, image, mode, low_threshold, high_threshold):
        if mode == UI.CN_MODE_CANNY:
            image = canny(image, low_threshold, high_threshold)
        elif mode == UI.CN_MODE_DEPTH:
            image = leres(image, low_threshold, high_threshold, self.leres_annotator_full_path)
        elif mode == UI.CN_MODE_SKETCH:
            image = hed(image, self.hed_annotator_full_path)
        else:
            pass
        return image

    def create_dict(self, stack, source_image, controlnet_mode, controlnet_preprocessor, strength, low_threshold, high_threshold, start, end, noise_augmentation, revision_enhancer):
        if controlnet_mode is None or controlnet_mode == UI.NONE:
            cn_image = None
        else:
            cn_image = source_image
        low_threshold = round(low_threshold, 3)
        high_threshold = round(high_threshold, 3)
        if controlnet_mode == UI.CN_MODE_REVISION or controlnet_mode == UI.CUSTOM:
            controlnet_preprocessor = False
        if controlnet_preprocessor and cn_image is not None:
            cn_image = self.process_image(cn_image, controlnet_mode, low_threshold, high_threshold)
        stack += [{UI.F_REV_CN_IMAGE: cn_image, UI.F_REV_CN_IMAGE_CHANGED: True, UI.F_REV_CN_MODE: controlnet_mode, UI.F_CN_PRE_PROCESSOR: controlnet_preprocessor, UI.F_REV_CN_STRENGTH: round(strength, 3), UI.F_CN_LOW_THRESHOLD: low_threshold, UI.F_CN_HIGH_THRESHOLD: high_threshold, UI.F_CN_START: round(start, 3), UI.F_CN_END: round(end, 3), UI.F_REV_NOISE_AUGMENTATION: round(noise_augmentation, 3), UI.F_REV_ENHANCER: revision_enhancer}]
        return ({UI.F_CN_STACK: stack}, cn_image)

    def get_value(self, controlnet_mode, controlnet_preprocessor, strength, low_threshold, high_threshold, start_percent, end_percent, noise_augmentation, revision_enhancer, source_image=None, data=None):
        if data is None:
            data = {}
        stack = retrieve_parameter(UI.F_CN_STACK, retrieve_parameter(UI.S_CONTROLNET_INPUTS, data), [])
        if self.expected_size is None:
            self.expected_size = len(stack)
        elif self.expected_size == 0:
            stack = []
        elif len(stack) > self.expected_size:
            stack = stack[:self.expected_size]
        (stack_entry, image) = self.create_dict(stack, source_image, controlnet_mode, controlnet_preprocessor, strength, low_threshold, high_threshold, start_percent, end_percent, noise_augmentation, revision_enhancer)
        data[UI.S_CONTROLNET_INPUTS] = stack_entry
        return (data, image)
```