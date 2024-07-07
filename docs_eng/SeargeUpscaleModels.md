# Documentation
- Class name: SeargeUpscaleModels
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node coordinates the selection and configuration of image enhancement magnification models, with a focus on integrating amplifiers to achieve desired output quality.

# Input types
## Required
- detail_processor
    - The detail processor is essential for improving image quality and plays a key role in the overall magnification process.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- high_res_upscaler
    - High-resolution amplifiers are essential for increasing the resolution of images and contribute significantly to the ultimate visual effects.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- primary_upscaler
    - Major amplifiers are critical during the initial scaling phase, setting the basis for further enhancement.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- secondary_upscaler
    - Secondary amplifiers further fine-tune images after major scalings to improve detail and clarity.
    - Comfy dtype: COMBO[str]
    - Python dtype: str

# Output types
- data
    - The output data cover the configuration of the magnification model, which is essential for subsequent processing and final image output.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeUpscaleModels:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'detail_processor': (UI.UPSCALERS_1x_WITH_NONE(),), 'high_res_upscaler': (UI.UPSCALERS_4x_WITH_NONE(),), 'primary_upscaler': (UI.UPSCALERS_4x_WITH_NONE(),), 'secondary_upscaler': (UI.UPSCALERS_4x_WITH_NONE(),)}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(detail_processor, high_res_upscaler, primary_upscaler, secondary_upscaler):
        return {UI.F_DETAIL_PROCESSOR: detail_processor, UI.F_HIGH_RES_UPSCALER: high_res_upscaler, UI.F_PRIMARY_UPSCALER: primary_upscaler, UI.F_SECONDARY_UPSCALER: secondary_upscaler}

    def get(self, detail_processor, high_res_upscaler, primary_upscaler, secondary_upscaler, data=None):
        if data is None:
            data = {}
        data[UI.S_UPSCALE_MODELS] = self.create_dict(detail_processor, high_res_upscaler, primary_upscaler, secondary_upscaler)
        return (data,)
```