# Documentation
- Class name: WAS_Images_To_Linear
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Images_To_Linear node is designed to convert image data into linear formats. It plays a key role in image processing workflows to ensure that image data are properly converted to facilitate subsequent computing tasks. The function of the node is essential when preparing images for analysis or for operation within an online algebra framework.

# Input types
## Required
- images
    - The “images” parameter is essential for the operation of the node because it is used as an input into the image-linear conversion process. It directly influences the execution of the node by determining the origin of the image to be converted.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]

# Output types
- linear_images
    - The linear_images output parameter represents the result of a linear conversion of the image. It is important because it provides ready image data for further linear analysis or operation.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Images_To_Linear:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_to_linear'
    CATEGORY = 'WAS Suite/Image'

    def image_to_linear(self, images):
        if len(images) > 1:
            tensors = []
            for image in images:
                tensors.append(pil2tensor(tensor2pil(image).convert('L')))
            tensors = torch.cat(tensors, dim=0)
            return (tensors,)
        else:
            return (pil2tensor(tensor2pil(images).convert('L')),)
```