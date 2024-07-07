# Documentation
- Class name: SeargeImage2ImageAndInpainting
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeImage2ImageAdInpainting node is intended to facilitate image-to-image conversion and restoration tasks. It accepts parameters that define the level of noise reduction and repair mask features, and produces structured data streams suitable for further processing in image processing workflows.

# Input types
## Required
- denoise
    - The `denoise' parameter controls the level of noise reduction applied to the image. It is essential to enhance image quality by reducing unwanted noise while retaining important details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- inpaint_mask_blur
    - The `inpaint_mask_blur' parameter determines the blurry radius of the repair mask, which is important for the smoothness of the area to be repaired in the image.
    - Comfy dtype: INT
    - Python dtype: int
- inpaint_mask_mode
    - The `inpaint_mask_mode' parameter selects the operating mode for repairing the mask to influence how the restoration process is applied to the image.
    - Comfy dtype: UI.MASK_MODES
    - Python dtype: str
- data
    - The `data' parameter is optional and allows users to process existing data streams for nodes, increasing the flexibility of node applications.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: dict

# Output types
- data
    - The `data' output is a structured data stream that covers images to the results of image conversion and restoration processes and is prepared for downstream tasks.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: dict

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeImage2ImageAndInpainting:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'inpaint_mask_blur': ('INT', {'default': 16, 'min': 0, 'max': 24, 'step': 4}), 'inpaint_mask_mode': (UI.MASK_MODES,)}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(denoise, inpaint_mask_blur, inpaint_mask_mode):
        return {UI.F_DENOISE: round(denoise, 3), UI.F_INPAINT_MASK_BLUR: inpaint_mask_blur, UI.F_INPAINT_MASK_MODE: inpaint_mask_mode}

    def get(self, denoise, inpaint_mask_blur, inpaint_mask_mode, data=None):
        if data is None:
            data = {}
        data[UI.S_IMG2IMG_INPAINTING] = self.create_dict(denoise, inpaint_mask_blur, inpaint_mask_mode)
        return (data,)
```