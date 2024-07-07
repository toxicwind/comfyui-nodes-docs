# Documentation
- Class name: GaussianBlur
- Category: 😺dzNodes/LayerFilter
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Gaussian fuzzy.

# Input types
## Required

- image
    - Enter the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- blur
    - The level of ambiguity.
    - Comfy dtype: INT
    - Python dtype: int


# Output types

- image
    - Generates the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class GaussianBlur:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "blur": ("INT", {default" : 20, "min" : 1, "max" : 999, "step" ): # fuzzy
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'gaussian_blur'
    CATEGORY = '😺dzNodes/LayerFilter'

    def gaussian_blur(self, image, blur):

        ret_images = []

        for i in image:
            _canvas = tensor2pil(torch.unsqueeze(i, 0)).convert('RGB')

            ret_images.append(pil2tensor(gaussian_blur(_canvas, blur)))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```