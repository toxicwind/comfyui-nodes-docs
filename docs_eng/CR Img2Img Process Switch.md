# Documentation
- Class name: CR_Img2ImgProcessSwitch
- Category: Comfyroll/Utils/Process
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Img2ImgProcessSwitch serves as a decision-making component in the ComfyUI workflow. It is designed to process image data by using the smart path of the type of input, be it text-to-image conversion or image-to-image conversion. This node is essential to simplify the image processing process, ensuring that appropriate treatment is applied to input data for the best results.

# Input types
## Required
- Input
    - The 'Input'parameter is essential because it determines the path of image processing in the workflow. It indicates whether the node will execute the text to the image conversion or the image to the image conversion, thereby affecting the entire processing sequence.
    - Comfy dtype: COMBO['txt2img', 'img2img']
    - Python dtype: str
## Optional
- txt2img
    - When the `Input' parameter is set to `txt2img', use the `txt2img' parameter. It represents the potential expression of the text to the image process, which is essential for the conversion.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- img2img
    - When the `Input' parameter is set to `img2img', the `img2img' parameter becomes relevant. It saves the potential data needed for image-to-image conversion processes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Output types
- LATENT
    - The `LATENT' output contains the potential post-processing data, which is the result of an image-to-image conversion based on the text of the input selection.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- show_help
    - The'show_help' output provides a URL to a document to obtain further help or guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Img2ImgProcessSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': (['txt2img', 'img2img'],)}, 'optional': {'txt2img': ('LATENT',), 'img2img': ('LATENT',)}}
    RETURN_TYPES = ('LATENT', 'STRING')
    RETURN_NAMES = ('LATENT', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Process')

    def switch(self, Input, txt2img=None, img2img=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Process-Nodes#cr-img2img-process-switch'
        if Input == 'txt2img':
            return (txt2img, show_help)
        else:
            return (img2img, show_help)
```