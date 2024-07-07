# Documentation
- Class name: RegionalConditioningColorMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalConditioningColorMask node is designed to apply colour masks to the CLIP model's text code, increasing the model's attention to specific areas of the image. It does this by converting the colour mask image into a binary mask, which is then used for conditional text encoding. This allows for more sophisticated control of the image generation process, ensuring that the images generated are closely aligned with the subject elements required.

# Input types
## Required
- clip
    - The parameter 'clip' is the input text hint that the CLIP model will encode. It is essential to define the semantic content that the model should focus on during image generation. The validity of the node depends to a large extent on the relevance and specificity of the input clip.
    - Comfy dtype: CLIP
    - Python dtype: str
- color_mask
    - Parameter 'color_mask' is the image that defines the area of interest in the image. The image is used to create a mask that directs the model to the specified area. The quality and accuracy of the colour mask directly influences the accuracy of the regional conditions.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- mask_color
    - The parameter'mask_color' specifies the colour to be used for the mask in the 'color_mask'image. It is important for identifying the target area in the image and should be provided in a valid RGB colour format. The color selection of the mask affects the ability of the node to isolate the area required.
    - Comfy dtype: STRING
    - Python dtype: str
- strength
    - Parameter'strength' controls the intensity of mask effects on text code. Higher values increase the emphasis on masked areas, which may lead to more visible features in the images generated. It is a key factor in fine-tuning the balance between regional focus and overall image consistency.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prompt
    - The parameter 'prompt' is a detailed text description that further refines the image-generation process. It provides additional context and guidance to the model to ensure that the images generated are more in line with the creative vision of the user. The content of the hint has a significant impact on the final output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- set_cond_area
    - Parameter'set_cond_area' determines how the mask should be applied to the condition. It can use default behaviour or visible setting of the mask boundary. This option can affect the ability of nodes to enhance regional conditions for specific areas within the image.
    - Comfy dtype: COMBO['default', 'mask bounds']
    - Python dtype: str

# Output types
- conditioning
    - Output 'conventioning' means that the text code has been modified by the colour mask. It is used to guide the image generation process and to ensure that the image generated reflects the subject element specified in the input hint.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- mask
    - The output'mask'is a binary mask derived from the 'color_mask' image. It is used inside the node to apply regional conditions to text encoding and allows for more accurate control of the image generation process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalConditioningColorMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'color_mask': ('IMAGE',), 'mask_color': ('STRING', {'multiline': False, 'default': '#FFFFFF'}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'set_cond_area': (['default', 'mask bounds'],), 'prompt': ('STRING', {'multiline': True, 'placeholder': 'prompt'})}}
    RETURN_TYPES = ('CONDITIONING', 'MASK')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, clip, color_mask, mask_color, strength, set_cond_area, prompt):
        mask = color_to_mask(color_mask, mask_color)
        conditioning = nodes.CLIPTextEncode().encode(clip, prompt)[0]
        conditioning = nodes.ConditioningSetMask().append(conditioning, mask, set_cond_area, strength)[0]
        return (conditioning, mask)
```