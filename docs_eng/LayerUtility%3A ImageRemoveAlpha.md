# Documentation
- Class name: ImageRemoveAlpha
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Removes the alpha channel of the picture and converts the picture to RGB mode. You can choose to fill the background and set the background colour.

# Input types

## Required

- RGBA_image
    - Enter the image that supports the RGBA or RGB mode.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- fill_background
    - Fills the background.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- background_color
    - Background colour.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- mask
    - Select to enter the mask. If you have the input mask, priority is given to using it, ignoring the alpha that RGBA_image carries.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- RGB_image
    - Processed RGB pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class ImageRemoveAlpha:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "RGBA_image": ("IMAGE", ),  #
                "fill_background": ("BOOLEAN", {"default": False}),
                "background_color": ("STRING", {"default": "#000000"}),
            },
            "optional": {
                "mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("RGB_image", )
    FUNCTION = 'image_remove_alpha'
    CATEGORY = '😺dzNodes/LayerUtility'

    def image_remove_alpha(self, RGBA_image, fill_background, background_color, mask=None):

        ret_images = []

        for index, img in enumerate(RGBA_image):
            _image = tensor2pil(img)

            if fill_background:
                if mask is not None:
                    m = mask[index].unsqueeze(0) if index < len(mask) else mask[-1].unsqueeze(0)
                    alpha = tensor2pil(m).convert('L')
                elif _image.mode == "RGBA":
                    alpha = _image.split()[-1]
                else:
                    log(f"Error: {NODE_NAME} skipped, because the input image is not RGBA and mask is None.",
                        message_type='error')
                    return (RGBA_image,)
                ret_image = Image.new('RGB', size=_image.size, color=background_color)
                ret_image.paste(_image, mask=alpha)
                ret_images.append(pil2tensor(ret_image))

            else:
                ret_images.append(pil2tensor(tensor2pil(i).convert('RGB')))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), )
```