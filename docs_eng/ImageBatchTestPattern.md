# Documentation
- Class name: ImageBatchTestPattern
- Category: KJNodes/text
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The ImageBatchTestPatten node is designed to generate a collection of images with text patterns. It creates images by drawing numbers on a black background using specified fonts and fonts. This node is particularly suitable for testing and visualizing how different fonts and sizes affect the appearance of the text in the image.

# Input types
## Required
- batch_size
    - The catch_size parameter determines the number of images to be generated. It is essential to control the volume of the output data and is directly related to the calculated load executed by the node.
    - Comfy dtype: INT
    - Python dtype: int
- start_from
    - The start_from parameter sets the starting number of the number series that you want to draw on the image. It is important to define the range of numbers that will be displayed in the generated model.
    - Comfy dtype: INT
    - Python dtype: int
- text_x
    - The text_x parameter specifies the x coordinates the text will draw on the image. It is an important parameter because it determines the horizontal position of the text in the image.
    - Comfy dtype: INT
    - Python dtype: int
- text_y
    - The text_y parameter specifies the y-coordinate the text will be drawn on the image. It controls the vertical position of the text, which is essential for aligning text within the image.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width parameter defines the width in which the image is generated. It is a key parameter that affects the overall size of the output image and is closely related to the vertical ratio and visual presentation of the text.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header parameter defines the height at which the image is generated. It works with the width parameter to determine the overall size and shape of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- font
    - The font parameter selects the font type for the text in the image. It is a key parameter because it significantly affects the style and readability of the text in the image.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - The font_size parameter sets the font size of the text used in the image. It is an important factor in determining the prominence and visibility of the text in the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The IMAGE output contains a collection of generated images with specified text patterns. Each image is a stack of visual data that can be used for further processing or visualization.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageBatchTestPattern:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 255, 'step': 1}), 'start_from': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'text_x': ('INT', {'default': 256, 'min': 0, 'max': 4096, 'step': 1}), 'text_y': ('INT', {'default': 256, 'min': 0, 'max': 4096, 'step': 1}), 'width': ('INT', {'default': 512, 'min': 16, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 16, 'max': 4096, 'step': 1}), 'font': (folder_paths.get_filename_list('kjnodes_fonts'),), 'font_size': ('INT', {'default': 255, 'min': 8, 'max': 4096, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'generatetestpattern'
    CATEGORY = 'KJNodes/text'

    def generatetestpattern(self, batch_size, font, font_size, start_from, width, height, text_x, text_y):
        out = []
        numbers = np.arange(start_from, start_from + batch_size)
        font_path = folder_paths.get_full_path('kjnodes_fonts', font)
        for number in numbers:
            image = Image.new('RGB', (width, height), color='black')
            draw = ImageDraw.Draw(image)
            font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            font = ImageFont.truetype(font_path, font_size)
            text = str(number)
            try:
                draw.text((text_x, text_y), text, font=font, fill=font_color, features=['-liga'])
            except:
                draw.text((text_x, text_y), text, font=font, fill=font_color)
            image_np = np.array(image).astype(np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np).unsqueeze(0)
            out.append(image_tensor)
        out_tensor = torch.cat(out, dim=0)
        return (out_tensor,)
```