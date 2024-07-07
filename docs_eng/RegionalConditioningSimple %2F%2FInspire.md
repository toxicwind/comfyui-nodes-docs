# Documentation
- Class name: RegionalConditioningSimple
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

Such nodes provide a method of applying regional conditions to images using CLIP and the specified mask. They allow fine-tuning of images based on user input in order to focus on certain areas and improve the relevance and accuracy of the content generated.

# Input types
## Required
- clip
    - The 'clip' parameter is essential for the operation of the node because it defines the visual context on which the image is generated. It is the main input into the condition process.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- mask
    - The " mask " parameter is essential to specify the areas of interest in the image. It guides nodes to apply conditions selectively and ensures that the content generated is consistent with the focus area that the user expects.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image
- strength
    - The “strength” parameter adjusts the intensity of the regional conditions to allow the user to control the emphasis on the specified area. It directly affects the visibility of the condition characteristics in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - The "set_cond_area " parameter determines the way in which a regional condition area is defined. It can be set by default or based on a masked boundary, which affects how the mask is applied to the image.
    - Comfy dtype: COMBO
    - Python dtype: str
- prompt
    - The 'prompt' parameter provides a text description that guides the image generation process. It is an integral part of the condition because it provides AI with the context and direction to create content that matches the desired output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- conditioning
    - The "conventioning" output represents the regional condition data that has been applied to the image. It contains the effects of input parameters and is a key component of further image operation or analysis.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalConditioningSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'mask': ('MASK',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'set_cond_area': (['default', 'mask bounds'],), 'prompt': ('STRING', {'multiline': True, 'placeholder': 'prompt'})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, clip, mask, strength, set_cond_area, prompt):
        conditioning = nodes.CLIPTextEncode().encode(clip, prompt)[0]
        conditioning = nodes.ConditioningSetMask().append(conditioning, mask, set_cond_area, strength)[0]
        return (conditioning,)
```