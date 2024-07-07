# Documentation
- Class name: GradientImage
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates a picture of the specified size and colour gradient. GradientImage V2 upgrade.

*Text to input message and mask only, and if you force access to other types of input, you will cause node errors.
* Preset dimensions are defined incustom_size.ini. This file is located under the plugin root directory with the default namecustom_size.ini.example. The initial use of this file requires that the postfix be changed to.ini. Open with text editing software and edit custom dimensions. Each line indicates a size, the first value is width, the second is height, and the middle is separated by lower "x". Do not enter extra characters to avoid errors.

# Input types
## Required

- size
    - Picture size.
    - Comfy dtype: STRING
    - Python dtype: str
    - Optional value: 'custom',

- custom_width
    - image width. This option is ignored if you have size_as input.
    - Comfy dtype: INT
    - Python dtype: int

- custom_height
    - image height. This option is ignored if you have size_as input.
    - Comfy dtype: INT
    - Python dtype: int

- angle
    - Gradual angle.
    - Comfy dtype: INT
    - Python dtype: int

- start_color
    - Gradual start-up color.
    - Comfy dtype: STRING
    - Python dtype: str

- end_color
    - Gradual end color.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- size_as
    - Enter an image or mask to generate an output image according to its size. Note that this input priority is higher than the other size settings.
    - Comfy dtype: IMAGE, MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Generates the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class GradientImageV2:

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
                "angle": ("INT", {"default": 0, "min": -360, "max": 360, "step": 1}),
                "start_color": ("STRING", {"default": "#FFFFFF"},),
                "end_color": ("STRING", {"default": "#000000"},),
            },
            "optional": {
                "size_as": (any, {}),
            }
        }

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("image", )
    FUNCTION = 'gradient_image_v2'
    CATEGORY = '😺dzNodes/LayerUtility'

    def gradient_image_v2(self, size, custom_width, custom_height, angle, start_color, end_color, size_as=None):

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


        ret_image = gradient(start_color, end_color, width, height, angle)

        return (pil2tensor(ret_image), )
```