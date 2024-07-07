# Documentation
- Class name: WAS_Image_Gradient_Map
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Gradient_Map Node is designed to apply gradients to input images, allowing the creation of visible and diverse colour effects. It uses PIL libraries to process images in several groups, achieving a high degree of flexibility and control over image operations. The main function of the node is to obtain input images and gradients, which can be selectively flipped, and then produce an outcome in which gradients are mapted according to the brightness of the input image. This function is particularly suitable for generating image effects that require smooth colour transitions, or for creating textures that respond to bottom image content.

# Input types
## Required
- image
    - Enter the image, the colour of which will be replaced by a gradient. This parameter is vital because it defines the underlying image that will experience a gradient mapping process. Node will apply the gradient in a way that reflects the brightness value of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- gradient_image
    - This image determines the colour transition that will be applied to the input image. It should be carefully selected to ensure the desired visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- flip_left_right
    - A boolean flag, set to true, reverses left and right input and gradient images before processing. This can be used to create mirror effects in the final output.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: bool

# Output types
- output_image
    - Generates an image after a gradient map process. This image shows the brightness value of the input image to the gradient colour provided for the gradient image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Gradient_Map:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'gradient_image': ('IMAGE',), 'flip_left_right': (['false', 'true'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_gradient_map'
    CATEGORY = 'WAS Suite/Image/Filter'

    def image_gradient_map(self, image, gradient_image, flip_left_right='false'):
        image = tensor2pil(image)
        gradient_image = tensor2pil(gradient_image)
        WTools = WAS_Tools_Class()
        image = WTools.gradient_map(image, gradient_image, True if flip_left_right == 'true' else False)
        return (pil2tensor(image),)
```