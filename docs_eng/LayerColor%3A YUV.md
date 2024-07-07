# Documentation
- Class name: ColorCorrectYUV
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Adjust the YUV channels of the image.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- Y
    - Y channel adjustment value.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -255, "max": 255, "step": 1}

- U
    - An adjustment value for the U channel.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -255, "max": 255, "step": 1}

- V
    - The adjustment value for the V channel.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -255, "max": 255, "step": 1}

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorCorrectYUV:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "Y": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "U": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "V": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'color_correct_YUV'
    CATEGORY = '😺dzNodes/LayerColor'

    def color_correct_YUV(self, image, Y, U, V):

        ret_images = []

        for i in image:
            i = torch.unsqueeze(i, 0)
            __image = tensor2pil(i)
            _y, _u, _v = tensor2pil(i).convert('YCbCr').split()
            if Y != 0 :
                _y = image_gray_offset(_y, Y)
            if U != 0 :
                _u = image_gray_offset(_u, U)
            if V != 0 :
                _v = image_gray_offset(_v, V)
            ret_image = image_channel_merge((_y, _u, _v), 'YCbCr')

            if __image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, __image.split()[-1])

            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```