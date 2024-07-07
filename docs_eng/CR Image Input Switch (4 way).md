# Documentation
- Class name: CR_ImageInputSwitch4way
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImageInputSwitch4way node is designed to select image input conditionally based on integer input. It facilitates the route of image data through the logical switch mechanism to ensure that appropriate images are selected and transmitted. This node is essential in situations where dynamic selection of images is required and no additional conditions are desired.

# Input types
## Required
- Input
    - The 'Input'parameter is essential because it determines which of the four possible images will be selected. As a switch operation, the whole value corresponds to the index of the image that is to be routed through node.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image1
    - The `image1'parameter represents the first optional image input that can be selected by the node based on the `Input' parameter. When `Input' is set to 1, it plays an important role in the operation of the node and becomes the main output image.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image2
    - The `image2'parameter is the second optional image input that node can select according to the `Input'value. When `Input' is 2, it becomes relevant, and it is the image that node produces.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image3
    - The `image3'parameter is the third optional image input in the node selection process. When the `Input' value is 3, it is used as the selected image through the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image4
    - The `image4'parameter is the fourth and last optional image input for which node can be exported. It is only considered when `Input' is set to 4. In this case, it becomes the output image of the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]

# Output types
- IMAGE
    - The `IMAGE'output parameter represents an image selected on the basis of input values. It is the main result of node operations and is essential for the continuation of the image processing workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - The'show_help'output provides a URL that points to the node document and provides guidance to users on how to use the node effectively. It is a useful resource for understanding the function and purpose of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageInputSwitch4way:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 4})}, 'optional': {'image1': ('IMAGE',), 'image2': ('IMAGE',), 'image3': ('IMAGE',), 'image4': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, image1=None, image2=None, image3=None, image4=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-text-input-switch-4-way'
        if Input == 1:
            return (image1, show_help)
        elif Input == 2:
            return (image2, show_help)
        elif Input == 3:
            return (image3, show_help)
        else:
            return (image4, show_help)
```