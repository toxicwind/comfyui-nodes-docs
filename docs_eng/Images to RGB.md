# Documentation
- Class name: WAS_Images_To_RGB
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `image_to_rgb'method at WAS_Images_To_RGB nodes is designed to convert a series of images into their RGB expression form. It converts each image to the RGB format by converting it to a volume, and eventually, if multiple images are provided, stacks the results. This process is essential for preparing the image for further processing or analysis within the SAS package.

# Input types
## Required
- images
    - The 'image'parameter is essential for the operation of the node, as it represents a collection of images that need to be converted to RGB format. The node processes each image on a case-by-case basis and ensures that the final output is an expression of the volume appropriate for the downstream task.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Output types
- tensors
    - The 'tensors' output is a volume or volume stack that represents input to the image RGB format. This output is important because it allows seamless integration with other nodes in the WAS package that require further processing of RGB image data.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Images_To_RGB:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_to_rgb'
    CATEGORY = 'WAS Suite/Image'

    def image_to_rgb(self, images):
        if len(images) > 1:
            tensors = []
            for image in images:
                tensors.append(pil2tensor(tensor2pil(image).convert('RGB')))
            tensors = torch.cat(tensors, dim=0)
            return (tensors,)
        else:
            return (pil2tensor(tensor2pil(images).convert('RGB')),)
```