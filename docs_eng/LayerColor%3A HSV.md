# Documentation
- Class name: ColorCorrectHSV
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Adjust the HSV channels of the image.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- H
    - Image channel H.
    - Comfy dtype: INT
    - Python dtype: int

- S
    - Image of the S-channel.
    - Comfy dtype: INT
    - Python dtype: int

- V
    - Image of the V channel.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorCorrectHSV:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "H": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "S": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "V": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'color_correct_HSV'
    CATEGORY = '😺dzNodes/LayerColor'

    def color_correct_HSV(self, image, H, S, V):

        ret_images = []

        for i in image:
            i = torch.unsqueeze(i,0)
            __image = tensor2pil(i)
            _h, _s, _v = tensor2pil(i).convert('HSV').split()
            if H != 0 :
                _h = image_hue_offset(_h, H)
            if S != 0 :
                _s = image_gray_offset(_s, S)
            if V != 0 :
                _v = image_gray_offset(_v, V)
            ret_image = image_channel_merge((_h, _s, _v), 'HSV')

            if __image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, __image.split()[-1])

            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)


```