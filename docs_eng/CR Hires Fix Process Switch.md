# Documentation
- Class name: CR_HiResFixProcessSwitch
- Category: Comfyroll/Utils/Process
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_HiResFixProcessSwitch, as a decision-making module, selects one of the two magnification processes based on the input provided. It aims to increase the efficiency and flexibility of image processing tasks by intelligently routeing the process to potential or image magnification methods.

# Input types
## Required
- Input
    - The `Input' parameter is essential because it determines the choice of path for magnification. It determines whether the node will call for potential or image magnification, thus affecting subsequent processing and output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- latent_upscale
    - When the `Input' parameter specifies a potential magnification process, use the `latet_upscale' parameter. It is important because it carries potential expressions that will be magnified, affecting the quality and resolution of the final output.
    - Comfy dtype: LATENT
    - Python dtype: Any
- image_upscale
    - When the `Input' parameter indicates the image magnification process, use the `image_upscale' parameter. It is essential because it contains image data that will be processed to zoom in, directly influences output visual enhancement.
    - Comfy dtype: LATENT
    - Python dtype: Any

# Output types
- LATENT
    - The `LATENT' output represents the results of the selected magnification process, whether from potential or image. It contains data that have been specified for enhanced treatment and can be further used or analysed.
    - Comfy dtype: LATENT
    - Python dtype: Any
- STRING
    - The `STRING' output provides a URL link that points to the node to help the document. This is particularly useful for users seeking additional guidance or understanding of node functions and usages.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_HiResFixProcessSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': (['latent_upscale', 'image_upscale'],)}, 'optional': {'latent_upscale': ('LATENT',), 'image_upscale': ('LATENT',)}}
    RETURN_TYPES = ('LATENT', 'STRING')
    RETURN_NAMES = ('LATENT', 'STRING')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Process')

    def switch(self, Input, latent_upscale=None, image_upscale=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Process-Nodes#cr-hires-fix-process-switch'
        if Input == 'latent_upscale':
            return (latent_upscale, show_help)
        else:
            return (image_upscale, show_help)
```