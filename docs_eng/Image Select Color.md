# Documentation
- Class name: WAS_Image_Select_Color
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Select_Color node is designed to process images by selecting pixels that match the specified colour range and its range. It enhances images by focusing on the required colour range, allowing thematic or style emphasis on specific visual elements.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, as it is the input that will be processed. It determines the visual content that the node will analyse and operate according to the specified colour criteria.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- red
    - The red parameter defines the red fraction of the colour to be selected in the image. It plays a key role in determining the final visual result by specifying the range of red values to be considered.
    - Comfy dtype: INT
    - Python dtype: int
- green
    - The green parameter specifies the green fraction of the target colour. It is important to achieve the required colour selection and helps the overall colour filtering process.
    - Comfy dtype: INT
    - Python dtype: int
- blue
    - Blue parameters set the blue fraction of the colour to be selected. It is a key factor in the colour selection process, ensuring that only pixels within the specified blue range are included.
    - Comfy dtype: INT
    - Python dtype: int
- variance
    - The tolerance parameter allows for some flexibility in colour selection by defining the acceptable colour deviation range. It is important for processing minor changes in colour intensity in the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- selected_image
    - The selected image output represents the processed image, where only pixels that meet the specified colour criteria are retained. It is the result of node operations and reflects the intended thematic focus.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Select_Color:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'red': ('INT', {'default': 255.0, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'green': ('INT', {'default': 255.0, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'blue': ('INT', {'default': 255.0, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'variance': ('INT', {'default': 10, 'min': 0, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'select_color'
    CATEGORY = 'WAS Suite/Image/Process'

    def select_color(self, image, red=255, green=255, blue=255, variance=10):
        image = self.color_pick(tensor2pil(image), red, green, blue, variance)
        return (pil2tensor(image),)

    def color_pick(self, image, red=255, green=255, blue=255, variance=10):
        image = image.convert('RGB')
        selected_color = Image.new('RGB', image.size, (0, 0, 0))
        (width, height) = image.size
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                (r, g, b) = pixel
                if r >= red - variance and r <= red + variance and (g >= green - variance) and (g <= green + variance) and (b >= blue - variance) and (b <= blue + variance):
                    selected_color.putpixel((x, y), (r, g, b))
        return selected_color
```