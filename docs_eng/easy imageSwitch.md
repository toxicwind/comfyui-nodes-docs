# Documentation
- Class name: imageSwitch
- Category: EasyUse/Logic/Switch
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The ImageSwitch node is designed to select between two images on the basis of the boolean value. It is the basic component of the image processing workflow and is used for decision-making under certain conditions. The node operates by evaluating the boolean input and then returning the corresponding image.

# Input types
## Required
- image_a
    - The image_a parameter is the first image that the node may return. It plays a key role in the operation of the node, as it is one of the two options that the Boolean input will determine.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_b
    - The image_b parameter represents the second image option that may be exported by the node. It is as important as the image_a because it depends on the boolean input to be returned by the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- boolean
    - The boolean parameter is essential to the decision-making process of the node. It directly affects which of the two images, image_a or image_b, will be the output of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_image
    - The selected_image output is an image based on a Boolean input selection. It is the ultimate expression of the node function and contains the logic of the conditions applied.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class imageSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'boolean': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_switch'
    CATEGORY = 'EasyUse/Logic/Switch'

    def image_switch(self, image_a, image_b, boolean):
        if boolean:
            return (image_a,)
        else:
            return (image_b,)
```