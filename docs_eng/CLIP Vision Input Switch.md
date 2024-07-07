# Documentation
- Class name: WAS_CLIP_Vision_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method'clip_vision_switch' is to select two input images conditionally based on the Boolean Mark. It acts as a decision node in the workflow, allowing the image data route to be traced to different parts of the system on the basis of the given boolean value.

# Input types
## Required
- clip_vision_a
    - The parameter'clip_vision_a' represents the first image option that nodes can choose. It is essential for the decision-making process because it determines one of the potential outputs based on the Boolean logo.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Union[Image.Image, PIL.PngImagePlugin.PngImageFile]
- clip_vision_b
    - Parameter'clip_vision_b' is the alternative image option that you can choose when the boolean sign is a false. It plays an important role in the function of the node by providing secondary output options.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Union[Image.Image, PIL.PngImagePlugin.PngImageFile]
## Optional
- boolean
    - The parameter 'boolean' acts as a switch to determine which image the node returns. It is essential to control the flow of image data in the system.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- CLIP_VISION
    - The output of the method'clip_vision_switch' is a single image determined by the Boolean logo. It represents the outcome of the node decision-making process and is essential for downstream processing.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Union[Image.Image, PIL.PngImagePlugin.PngImageFile]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_CLIP_Vision_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'clip_vision_a': ('CLIP_VISION',), 'clip_vision_b': ('CLIP_VISION',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('CLIP_VISION',)
    FUNCTION = 'clip_vision_switch'
    CATEGORY = 'WAS Suite/Logic'

    def clip_vision_switch(self, clip_vision_a, clip_vision_b, boolean=True):
        if boolean:
            return (clip_vision_a,)
        else:
            return clip_vision_b
```