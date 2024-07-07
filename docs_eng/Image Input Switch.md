# Documentation
- Class name: WAS_Image_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `image_input_switch'is designed to select conditionally between two image inputes according to the Boolean sign. It acts as a logical switch in the image processing workflow and allows dynamic routed image data according to the provided boolean conditions.

# Input types
## Required
- image_a
    - The first image that returns when the Boolean mark is true is entered. This is a key parameter because it determines the result when the switch is on.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- image_b
    - When the boolean sign is false, the second image that will be returned is entered. When the switch is in the " switch " state, it plays a key role in determining the output of the situation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- boolean
    - Determines which image to enter. When true, returns `image_a'; when false, returns `image_b '. This parameter is essential to the decision-making process of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_image
    - Output image as determined by the Boolean flag. It represents the result of the logical switch operation and provides the selected image according to the input conditions.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def image_input_switch(self, image_a, image_b, boolean=True):
        if boolean:
            return (image_a,)
        else:
            return (image_b,)
```