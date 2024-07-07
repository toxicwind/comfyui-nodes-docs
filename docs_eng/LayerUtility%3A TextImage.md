# Documentation
- Class name: TextJoin
- Category: 😺dzNodes/LayerUtility/Data
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates pictures and masks from text. Supports word spacing and vertical rowing adjustments to set random changes in text, including random changes in size and location.

*Only input Image and mask, which would cause node error if you forced access to other types of input. **font folders are defined in source_dir.ini, which is located under the plugin root directory with the default name of source_dir.ini.example, the initial use of which requires the postfixing of the file to.ini. Open with text editing software, find this line at the beginning of “FONT_dir=” and edit the folder path after “=”. All of the.tttf and.otf files in this folder will be collected and displayed in the list of nodes at the time of the initialization of ComfyUI. If the folder set in Mini is invalid, the font folder* will be enabled.

# Input types

## Required

- text
    - text.
    - Comfy dtype: STRING
    - Python dtype: str

- font_file
    - This lists the font files available in the Font folder. The selected font files will be used to generate images.
    - Comfy dtype: STRING
    - Python dtype: str

- spacing
    - word spacing in pixels.
    - Comfy dtype: INT
    - Python dtype: int

- leading
    - Line spacing in pixels.
    - Comfy dtype: INT
    - Python dtype: int

- horizontal_border
    - side margin. The value here is a percentage, e.g. 50 indicates that the starting point is in the centre of both sides. If the text is horizontal, it is left, and the vertical row is right.
    - Comfy dtype: FLOAT
    - Python dtype: float

- vertical_border
    - . The value here is a percentage, e.g. 10 indicates a starting point of 10% from the top.
    - Comfy dtype: FLOAT
    - Python dtype: float

- scale
    - text size. The initial size of the text is automatically calculated according to the size of the image and text content, default being the longest row or column fit image width or height. The value here is adjusted to zoom in and down the text as a whole. The value here is a percentage, e.g. 60 for scaling to 60%.
    - Comfy dtype: FLOAT
    - Python dtype: float

- variation_range
    - character random change range. When the value is greater than 0, the character will cause a random change in size and location. The greater the value, the greater the variation.
    - Comfy dtype: INT
    - Python dtype: int

- variation_seed
    - Seeds that change randomly. Sets this value, and the changes in individual text do not change every time they occur.
    - Comfy dtype: INT
    - Python dtype: int

- layout
    - text layout. There is a choice between horizontal and vertical rows.
    - Comfy dtype: STRING
    - Python dtype: str

- width
    - The width of the image. If you have size_as input, this setting is ignored.
    - Comfy dtype: INT
    - Python dtype: int

- height
    - The height of the image. If you have size_as input, this setting is ignored.
    - Comfy dtype: INT
    - Python dtype: int

- text_color
    - text colour.
    - Comfy dtype: STRING
    - Python dtype: str

- background_color
    - Background colour.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- size_as
    - Enter the image or mask here, which will generate the output image and the mask according to its size. Note that this input is higher than the width and height below.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class TextImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        layout_list = ['horizontal', 'vertical']
        random_seed = int(time.time())
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Text"}),
                "font_file": (FONT_LIST,),
                "spacing": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
                "leading": ("INT", {"default": 0, "min": -9999, "max": 9999, "step": 1}),
                "horizontal_border": ("FLOAT", {default": 5, "min" -100, "max": 100, "step" ), # left-hand percentage, side-left, vertically right-hand
                "Vertical_border":, # (FLOAT, {default": 5, "min" -100, "max": 100, "step": 0.3), #
                "scale": ("FLOAT", {default" 80, "min" : 0.1, "max" :999, "step" :0.0), # Total size versus image width, horizontal versus width, vertical versus height ratio
                # Random size and location range #
                "variation_seed": ("INT", {default": random_seed, "min": 0, "max": 99999999999999, "step" ), # random seeds
                "layout": (layout_list,), #twice orthopaedic
                "width": ("INT", {"default": 512, "min": 4, "max": 999999, "step": 1}),
                "height": ("INT", {"default": 512, "min": 4, "max": 999999, "step": 1}),
                "text_color": # text colour
                "background_color": # Background colour
            },
            "optional": {
                "size_as": (any, {}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = 'text_image'
    CATEGORY = '😺dzNodes/LayerUtility'

    def text_image(self, text, font_file, spacing, leading, horizontal_border, vertical_border, scale,
                  variation_range, variation_seed, layout, width, height, text_color, background_color,
                  size_as=None
                  ):

        # spacing -= 20
        # leading += 20
        # scale *= 0.7
        if size_as is not None:
            width, height = tensor2pil(size_as).size
        text_table = []
        max_char_in_line = 0
        total_char = 0
        spacing = int(spacing * scale / 100)
        leading = int(leading * scale / 100)
        lines = []
        text_lines = text.split("\n")
        for l in text_lines:
            if len(l) > 0:
                lines.append(l)
                total_char += len(l)
                if len(l) > max_char_in_line:
                    max_char_in_line = len(l)
            else:
                lines.append(" ")
        if layout == 'vertical':
            char_horizontal_size = width // len(lines)
            char_vertical_size = height // max_char_in_line
            char_size = min(char_horizontal_size, char_vertical_size)
            if char_size < 1:
                char_size = 1
            start_x = width - int(width * horizontal_border/100) - char_size
        else:
            char_horizontal_size = width // max_char_in_line
            char_vertical_size = height // len(lines)
            char_size = min(char_horizontal_size, char_vertical_size)
            if char_size < 1:
                char_size = 1
            start_x = int(width * horizontal_border/100)
        start_y = int(height * vertical_border/100)

        # calculate every char position and size to a table list
        for i in range(len(lines)):
            _x = start_x
            _y = start_y
            line_table = []
            line_random = random_numbers(total=len(lines[i]),
                                         random_range=int(char_size * variation_range / 25),
                                         seed=variation_seed, sum_of_numbers=0)
            for j in range(0, len(lines[i])):
                offset = int((char_size + line_random[j]) * variation_range / 250)
                offset = int(offset * scale / 100)
                font_size = char_size + line_random[j]
                font_size = int(font_size * scale / 100)
                if font_size < 4:
                    font_size = 4
                axis_x = _x + offset // 3 if random.random() > 0.5 else _x - offset // 3
                axis_y = _y + offset // 3 if random.random() > 0.5 else _y - offset // 3
                char_dict = {'char':lines[i][j],
                             'axis':(axis_x, axis_y),
                             'size':font_size}
                line_table.append(char_dict)
                if layout == 'vertical':
                    _y += char_size + line_random[j] + spacing
                else:
                    _x += char_size + line_random[j] + spacing
            if layout == 'vertical':
                start_x -= leading * (i+1) + char_size
            else:
                start_y += leading * (i+1) + char_size
            text_table.append(line_table)

        # draw char
        _mask = Image.new('RGB', size=(width, height), color='black')
        draw = ImageDraw.Draw(_mask)
        for l in range(len(lines)):
            for c in range(len(lines[l])):
                font_path = FONT_DICT.get(font_file)
                font_size = text_table[l][c].get('size')
                font = ImageFont.truetype(font_path, font_size)
                draw.text(text_table[l][c].get('axis'), text_table[l][c].get('char'), font=font, fill='white')
        _canvas = Image.new('RGB', size=(width, height), color=background_color)
        _color = Image.new('RGB', size=(width, height), color=text_color)
        _canvas.paste(_color, mask=_mask.convert('L'))
        _canvas = RGB2RGBA(_canvas, _mask)
        log(f"{NODE_NAME} Processed.", message_type='finish')
        return (pil2tensor(_canvas), image2mask(_mask),)
```