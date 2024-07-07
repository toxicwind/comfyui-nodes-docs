# Documentation
- Class name: AddGrain
- Category: 😺dzNodes/LayerFilter
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Add noise to the picture.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- grain_power
    - Noise intensity.
    - Comfy dtype: FLOAT
    - Python dtype: float

- grain_scale
    - The size of the noise.
    - Comfy dtype: FLOAT
    - Python dtype: float

- grain_sat
    - Noise color saturation.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Optional

- None

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class AddGrain:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "grain_power": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),
                "grain_scale": ("FLOAT", {"default": 1, "min": 0.1, "max": 10, "step": 0.1}),
                "grain_sat": ("FLOAT", {"default": 1, "min": 0, "max": 1, "step": 0.01}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'add_grain'
    CATEGORY = '😺dzNodes/LayerFilter'

    def add_grain(self, image, grain_power, grain_scale, grain_sat):

        ret_images = []

        for i in image:
            _canvas = tensor2pil(torch.unsqueeze(i, 0)).convert('RGB')
            _canvas = image_add_grain(_canvas, grain_scale, grain_power, grain_sat, toe=0, seed=int(time.time()))
            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```