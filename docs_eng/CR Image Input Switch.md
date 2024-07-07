# Documentation
- Class name: CR_ImageInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImageInputSwitch node is designed to select conditionally one of the two image inputs from a single integer input. It operates by assessing the whole value and returning the corresponding image to ensure that the output is consistent with the input selection. This node is particularly useful in scenarios that require a change in the flow of image data according to the logical dynamics of the user's input or other conditions.

# Input types
## Required
- Input
    - The 'Input'parameter is a key integer that determines which image to select as an output. It directly influences the decision-making process at the node, allowing conditional access to image data.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image1
    - The `image1'parameter indicates the first image option that the node can choose. When the `Input' value makes `image1' a specified output, it plays an important role.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- image2
    - The `image2'parameter is the second image option that nodes can choose. It becomes important when the `Input' indicator `image2' should be to produce the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- IMAGE
    - The 'IMAGE'output is an image based on the 'Input'parameter selection. It represents the result of node condition logic and is essential for further processing in the workflow.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- show_help
    - The'show_help'output provides a URL that points to the node document and provides guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'image1': ('IMAGE',), 'image2': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, image1=None, image2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-image-input-switch'
        if Input == 1:
            return (image1, show_help)
        else:
            return (image2, show_help)
```