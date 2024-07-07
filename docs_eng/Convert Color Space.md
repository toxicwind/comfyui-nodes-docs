# Documentation
- Class name: ConvertColorSpace
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

ConvertColorSpace nodes are designed to convert images from one colour space to another. It provides an advanced interface for seamless conversion of images between RGB, HSV and HSL colour spaces, allowing for more efficient operation and analysis of image data.

# Input types
## Required
- in_space
    - The 'in_space'parameter defines the current colour space for the input image, which is essential for determining the appropriate conversion algorithm. It influences the execution of the node by specifying the starting point for the colour space conversion.
    - Comfy dtype: COMBO['RGB', 'HSV', 'HSL']
    - Python dtype: str
- out_space
    - The 'out_space'parameter specifies the colour space required for the output of the image. It is the key determinant of node operations, as it determines the target format of the colour space conversion process.
    - Comfy dtype: COMBO['RGB', 'HSV', 'HSL']
    - Python dtype: str
- image
    - The 'image'parameter indicates the input image data to be converted. It is essential for the function of the node, as it is the main data object for colour space conversion.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- IMAGE
    - Output 'IMAGE'means the image converted in the specified colour space. It is the final result of the node operation and is valuable for further image processing or analysis tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ConvertColorSpace:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'in_space': (['RGB', 'HSV', 'HSL'],), 'out_space': (['RGB', 'HSV', 'HSL'],), 'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'convert_color_space'
    CATEGORY = 'Masquerade Nodes'

    def convert_color_space(self, in_space, out_space, image):
        if in_space == out_space:
            return (image,)
        image = tensor2rgb(image)
        if in_space == 'HSV':
            hsv = image
        if in_space == 'RGB':
            hsv = rgb2hsv(image)
        elif in_space == 'HSL':
            hsv = hsl2hsv(image)
        if out_space == 'HSV':
            return (hsv,)
        elif out_space == 'RGB':
            return (hsv2rgb(hsv),)
        else:
            assert out_space == 'HSL'
            return (hsv2hsl(hsv),)
```