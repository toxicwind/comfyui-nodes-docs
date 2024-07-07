# Documentation
- Class name: EncodeBlindWaterMark
- Category: 😺dzNodes/LayerUtility/SystemIO
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Adds an invisible watermark to the image. Adds a watermark in a way that is undetectable to the naked eye and decodes the watermark using the ShowBlind Watermark node.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- watermark_image
    - Watermark pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class EncodeBlindWaterMark:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "watermark_image": ("IMAGE",),  #
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'watermark_encode'
    CATEGORY = '😺dzNodes/LayerUtility/SystemIO'

    def watermark_encode(self, image, watermark_image):

        NODE_NAME = 'Add BlindWaterMark'

        l_images = []
        w_images = []
        ret_images = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
        for w in watermark_image:
            w_images.append(torch.unsqueeze(w, 0))

        for i in range(len(l_images)):
            _image = tensor2pil(l_images[i])
            wm_size = watermark_image_size(_image)
            _wm_image = w_images[i] if i < len(w_images) else w_images[-1]
            _wm_image = tensor2pil(_wm_image)
            _wm_image = _wm_image.resize((wm_size, wm_size), Image.LANCZOS)
            _wm_image = _wm_image.convert("L")

            y, u, v, _ = image_channel_split(_image, mode='YCbCr')
            _u = add_invisibal_watermark(u, _wm_image)
            ret_image = image_channel_merge((y, _u, v), mode='YCbCr')

            if _image.mode == "RGBA":
                ret_image = RGB2RGBA(ret_image, _image.split()[-1])
            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```