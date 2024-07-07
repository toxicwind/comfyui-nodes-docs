# Documentation
- Class name: WAS_Image_Remove_Color
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Remove_Color node is designed to process images according to user-defined criteria and remove specific colours. It allows for the identification and replacement of target colours with specified replacement colours to enhance the image for further analysis or glorification.

# Input types
## Required
- image
    - The image parameter is necessary because it is the input that the node will process. It determines the content and format of the colour removal operation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- target_red
    - The target_red parameter specifies the red fraction of the colour to be removed. It plays a key role in determining the accuracy of the colour removal process.
    - Comfy dtype: INT
    - Python dtype: int
- target_green
    - The target_green parameter defines the green fraction of the colour to be removed, affecting the ability of the node to isolate and replace the target colour.
    - Comfy dtype: INT
    - Python dtype: int
- target_blue
    - The target_blue parameter sets the blue fraction of the colour to be replaced, which is essential to achieve the result required in the colour removal task.
    - Comfy dtype: INT
    - Python dtype: int
- replace_red
    - Replace_red parameters determine the red fraction of the replacement colour, which is important for the final appearance of the modified image.
    - Comfy dtype: INT
    - Python dtype: int
- replace_green
    - Replace_green parameters set the green fractions used to replace the colour of the target colour, affecting the output of the node.
    - Comfy dtype: INT
    - Python dtype: int
- replace_blue
    - The replace_blue parameter specifies the blue fraction that will replace the original colour, which is essential for the colour change function of the node.
    - Comfy dtype: INT
    - Python dtype: int
- clip_threshold
    - The clip_threshold parameter sets a threshold for colour differences, which is essential to the ability of nodes to distinguish between target colours and other colours.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - Output_image represents the processed image, in which the specified colour has been removed, showing the ability of nodes to change visual content.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Remove_Color:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'target_red': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'target_green': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'target_blue': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'replace_red': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'replace_green': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'replace_blue': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'clip_threshold': ('INT', {'default': 10, 'min': 0, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_remove_color'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_remove_color(self, image, clip_threshold=10, target_red=255, target_green=255, target_blue=255, replace_red=255, replace_green=255, replace_blue=255):
        return (pil2tensor(self.apply_remove_color(tensor2pil(image), clip_threshold, (target_red, target_green, target_blue), (replace_red, replace_green, replace_blue))),)

    def apply_remove_color(self, image, threshold=10, color=(255, 255, 255), rep_color=(0, 0, 0)):
        color_image = Image.new('RGB', image.size, color)
        diff_image = ImageChops.difference(image, color_image)
        gray_image = diff_image.convert('L')
        mask_image = gray_image.point(lambda x: 255 if x > threshold else 0)
        mask_image = ImageOps.invert(mask_image)
        result_image = Image.composite(Image.new('RGB', image.size, rep_color), image, mask_image)
        return result_image
```