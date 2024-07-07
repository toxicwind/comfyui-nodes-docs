# Documentation
- Class name: WAS_Image_Flip
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The image flip method is designed to convert a set of images either horizontally or vertically. This operation is essential for data enhancement in machine learning missions, providing a diversity of training data that can enhance the robustness and generalization of models.

# Input types
## Required
- images
    - The parameter 'images' is a collection of images that are to be flipped. It plays a central role in the operation of nodes, because conversion is applied directly to those images. The results of the nodes depend heavily on the content and format of the input images.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- mode
    - The parameter'mode'determines the direction in which the input image will be flipped. It is very important because it determines the type of conversion applied to the image. The selection between 'horizontal' and'vertical' directly affects the final result of image processing.
    - Comfy dtype: COMBO['horizontal', 'vertical']
    - Python dtype: str

# Output types
- images
    - Output 'images' represents the transformational image. It is important because it is a direct result of node operations and is used for further processing or analysis during the follow-up phase of the workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Flip:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'mode': (['horizontal', 'vertical'],)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'image_flip'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_flip(self, images, mode):
        batch_tensor = []
        for image in images:
            image = tensor2pil(image)
            if mode == 'horizontal':
                image = image.transpose(0)
            if mode == 'vertical':
                image = image.transpose(1)
            batch_tensor.append(pil2tensor(image))
        batch_tensor = torch.cat(batch_tensor, dim=0)
        return (batch_tensor,)
```