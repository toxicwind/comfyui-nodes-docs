# Documentation
- Class name: WAS_Image_Analyze
- Category: WAS Suite/Image/Analyze
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Analyze nodes are designed to perform a variety of image analysis operations, including black and white level adjustments, RGB channel frequency analysis and seamless texture generation. It is a comprehensive tool for enhancing image quality and preparing images for further processing or visualization.

# Input types
## Required
- image
    - Enter the image as the image that the node will process. It is the basic data for all analysis and conversion operations performed by the node.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- mode
    - Model parameters determine the specific analysis or conversion to be applied to input images. It affects the operation of nodes and directs them to perform tasks such as adjusting black and white levels or analysing channel frequencies.
    - Comfy dtype: COMBO['Black White Levels', 'RGB Levels']
    - Python dtype: str

# Output types
- result_image
    - As a result, the image is the output of the node analysis or conversion process. It contains changes to the input image according to the specified pattern and parameters.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Analyze:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'mode': (['Black White Levels', 'RGB Levels'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_analyze'
    CATEGORY = 'WAS Suite/Image/Analyze'

    def image_analyze(self, image, mode='Black White Levels'):
        image = tensor2pil(image)
        WTools = WAS_Tools_Class()
        if mode:
            if mode == 'Black White Levels':
                image = WTools.black_white_levels(image)
            elif mode == 'RGB Levels':
                image = WTools.channel_frequency(image)
            else:
                image = image
        return (pil2tensor(image),)
```