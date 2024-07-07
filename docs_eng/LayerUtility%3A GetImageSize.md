# Documentation
- Class name: GetImageSize
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Get the width and height of the picture.

# Input types
## Required

- image
    - Enter the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor


# Output types

- width
    - The width of the picture.
    - Comfy dtype: INT
    - Python dtype: int

- height
    - The height of the picture.
    - Comfy dtype: INT
    - Python dtype: int

- original_size
    - The original size of the picture.
    - Comfy dtype: BOX
    - Python dtype: list

# Usage tips
- Infra type: CPU

# Source code
```
class GetImageSize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("INT", "INT", "BOX")
    RETURN_NAMES = ("width", "height",  "original_size")
    FUNCTION = 'get_image_size'
    CATEGORY = '😺dzNodes/LayerUtility'

    def get_image_size(self, image,):

        if image.shape[0] > 0:
            image = torch.unsqueeze(image[0], 0)
        _image = tensor2pil(image)

        return (_image.width, _image.height, [_image.width, _image.height],)
```