# Documentation
- Class name: ColorAdapter
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Automatically adjusts the colour of the picture to make it similar to the reference picture.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- color_ref_image
    - Reference picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- opacity
    - Opacity after image-adjusted colour.
    - Comfy dtype: INT
    - Python dtype: int
    - Value range: 0-100

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorAdapter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "color_ref_image": ("IMAGE", ),  #
                "opacity": ("INT", {default" : 75, "min" : 0, "max" : 100, "step" ), # Transparency
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'color_adapter'
    CATEGORY = '😺dzNodes/LayerColor'

    def color_adapter(self, image, color_ref_image, opacity):
        ret_images = []

        l_images = []
        r_images = []
        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
        for r in color_ref_image:
            r_images.append(torch.unsqueeze(r, 0))
        for i in range(len(l_images)):
            _image = l_images[i]
            _ref = r_images[i] if len(ret_images) > i else r_images[-1]

            __image = tensor2pil(_image)
            _canvas = __image.convert('RGB')
            ret_image = color_adapter(_canvas, tensor2pil(_ref).convert('RGB'))
            ret_image = chop_image(_canvas, ret_image, blend_mode='normal', opacity=opacity)
            if __image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, __image.split()[-1])
            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```