# Documentation
- Class name: ColorImage
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates a picture of the specified colour and size. ColorImage's V2 upgrade.

# Input types

## Required

- size
    - size presets. Presets can be customised by the user. If you have size_as input, this option is ignored.
    - Comfy dtype: STRING
    - Python dtype: str
    - Options: {"default": "custom", "options": ["custom", "512x512", "1024x1024", "2048x2048", "4096x4096", "8192x8192", "16384x16384", "32768x32768"]}

- custom_width
    - image width. This option is ignored if you have size_as input.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 512, "min": 4, "max": 99999, "step": 1}

- custom_height
    - image height. This option is ignored if you have size_as input.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 512, "min": 4, "max": 99999, "step": 1}

- color
    - The color of the picture.
    - Comfy dtype: STRING
    - Python dtype: str
    - Options: {"default": "#000000"}

## Optional

- size_as
    - Pictures for reference. If this is set, the size option is ignored.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorImageV2:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        size_list = ['custom']
        size_list.extend(load_custom_size())
        return {
            "required": {
                "size": (size_list,),
                "custom_width": ("INT", {"default": 512, "min": 4, "max": 99999, "step": 1}),
                "custom_height": ("INT", {"default": 512, "min": 4, "max": 99999, "step": 1}),
                "color": ("STRING", {"default": "#000000"},),
            },
            "optional": {
                "size_as": (any, {}),
            }
        }

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("image", )
    FUNCTION = 'color_image_v2'
    CATEGORY = '😺dzNodes/LayerUtility'

    def color_image_v2(self, size, custom_width, custom_height, color, size_as=None ):

        if size_as is not None:
            if size_as.shape[0] > 0:
                _asimage = tensor2pil(size_as[0])
            else:
                _asimage = tensor2pil(size_as)
            width, height = _asimage.size
        else:
            if size == 'custom':
                width = custom_width
                height = custom_height
            else:
                try:
                    _s = size.split('x')
                    width = int(_s[0].strip())
                    height = int(_s[1].strip())
                except Exception as e:
                    log(f"Warning: {NODE_NAME} invalid size, check {custom_size_file}", message_type='warning')
                    width = custom_width
                    height = custom_height

        ret_image = Image.new('RGB', (width, height), color=color)
        return (pil2tensor(ret_image), )
```