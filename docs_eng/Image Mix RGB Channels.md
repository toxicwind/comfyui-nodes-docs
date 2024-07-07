# Documentation
- Class name: WAS_Image_RGB_Merge
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_RGB_Merge node is designed to merge a separate colour channel into a single RGB image. By combining red, green, and blue channels, it generates a full colour image, thus playing a key role in image processing and enhancing visual output when further analysis or displaying takes place.

# Input types
## Required
- red_channel
    - The red_channel parameter is vital because it represents the red fraction of the final RGB image. It significantly affects the colour balance and overall appearance of the merged image, contributing to the core function of the node.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- green_channel
    - The green_channel parameter is essential for creating the RGB image because it determines the green weight. It is essential for achieving the required colour expression and the visual quality of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- blue_channel
    - The blue_channel parameter defines the blue fraction of the RGB image. It is the key element in node operations, ensures the right tone and enhances the image reality in the final merger results.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Output types
- merged_image
    - The merged_image output parameter represents the final product of the node, a fully integrated RGB image. It is important because it sums up the node's purpose and presents the combined visual data in a consistent and visually pleasurable way.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_RGB_Merge:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'red_channel': ('IMAGE',), 'green_channel': ('IMAGE',), 'blue_channel': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'merge_channels'
    CATEGORY = 'WAS Suite/Image/Process'

    def merge_channels(self, red_channel, green_channel, blue_channel):
        image = self.mix_rgb_channels(tensor2pil(red_channel).convert('L'), tensor2pil(green_channel).convert('L'), tensor2pil(blue_channel).convert('L'))
        return (pil2tensor(image),)

    def mix_rgb_channels(self, red, green, blue):
        (width, height) = red.size
        merged_img = Image.new('RGB', (width, height))
        merged_img = Image.merge('RGB', (red, green, blue))
        return merged_img
```