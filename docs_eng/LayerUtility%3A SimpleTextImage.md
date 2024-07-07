# Documentation
- Class name: SimpleTextImage
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates a simple layout of pictures and masks from text. This node refers to [ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite] (https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite), thanks to the original author.

*Only input Image and mask, which would cause node error if you forced access to other types of input. **font folders are defined in source_dir.ini, which is located under the plugin root directory with the default name of source_dir.ini.example, the initial use of which requires the postfixing of the file to.ini. Open with text editing software, find this line at the beginning of FONT_dir=, edit the folder path after "= ". All.tttf and.otf files in this folder will be collected and displayed in the list of nodes at the time of the initialization of ComfyUI. If the folder set in Mini is invalid, the font folder will be enabled.

# Input types

## Required

- text
    - text.
    - Comfy dtype: STRING
    - Python dtype: str

- font_file
    - font file.
    - Comfy dtype: FONT_LIST
    - Python dtype: str

- align
    - Alignment.
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str

- char_per_line
    - Number of characters per row.
    - Comfy dtype: INT
    - Python dtype: int

- leading
    - Line spacing.
    - Comfy dtype: INT
    - Python dtype: int

- font_size
    - Font size.
    - Comfy dtype: INT
    - Python dtype: int

- text_color
    - text colour.
    - Comfy dtype: STRING
    - Python dtype: str

- stroke_width
    - Draw side width.
    - Comfy dtype: INT
    - Python dtype: int

- stroke_color
    - Draw side colours.
    - Comfy dtype: STRING
    - Python dtype: str

- x_offset
    - x offset.
    - Comfy dtype: INT
    - Python dtype: int

- y_offset
    - y offset.
    - Comfy dtype: INT
    - Python dtype: int

- width
    - The width of the image. If you have size_as input, this setting is ignored.
    - Comfy dtype: INT
    - Python dtype: int

- height
    - The height of the image. If you have size_as input, this setting is ignored.
    - Comfy dtype: INT
    - Python dtype: int

## Optional

- size_as
    - Enter the image or mask here, which will generate the output image and the mask according to its size. Note that this input is higher than the width and height below.
    - Comfy dtype: ANY
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
- Infra type: CPU

# Source code

```python
class SimpleTextImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "text": ("STRING",{"default": "text", "multiline": True},
                ),
                "font_file": (FONT_LIST,),
                "align": (["center", "left", "right"],),
                "char_per_line": ("INT", {"default": 80, "min": 1, "max": 8096, "step": 1},),
                "leading": ("INT",{"default": 8, "min": 0, "max": 8096, "step": 1},),
                "font_size": ("INT",{"default": 72, "min": 1, "max": 2500, "step": 1},),
                "text_color": ("STRING", {"default": "#FFFFFF"},),
                "stroke_width": ("INT",{"default": 0, "min": 0, "max": 8096, "step": 1},),
                "stroke_color": ("STRING",{"default": "#FF8000"},),
                "x_offset": ("INT", {"default": 0, "min": 0, "max": 8096, "step": 1},),
                "y_offset": ("INT", {"default": 0, "min": 0, "max": 8096, "step": 1},),
                "width": ("INT", {"default": 512, "min": 1, "max": 8096, "step": 1},),
                "height": ("INT", {"default": 512, "min": 1, "max": 8096, "step": 1},),
            },
            "optional": {
                "size_as": (any, {}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = 'simple_text_image'
    CATEGORY = '😺dzNodes/LayerUtility'

    def simple_text_image(self, text, font_file, align, char_per_line,
                          leading, font_size, text_color,
                          stroke_width, stroke_color, x_offset, y_offset,
                          width, height, size_as=None
                          ):

        ret_images = []
        ret_masks = []
        if size_as is not None:
            if size_as.dim() == 2:
                size_as_image = torch.unsqueeze(mask, 0)
            if size_as.shape[0] > 0:
                size_as_image = torch.unsqueeze(size_as[0], 0)
            else:
                size_as_image = copy.deepcopy(size_as)
            width, height = tensor2pil(size_as_image).size
        font_path = FONT_DICT.get(font_file)
        (_, top, _, _) = ImageFont.truetype(font=font_path, size=font_size, encoding='unic').getbbox(text)
        font = cast(ImageFont.FreeTypeFont, ImageFont.truetype(font_path, font_size))
        if char_per_line == 0:
            char_per_line = int(width / font_size)
        paragraphs = text.split('\n')

        img_height = height  # line_height * len(lines)
        img_width = width  # max(font.getsize(line)[0] for line in lines)

        img = Image.new("RGBA", size=(img_width, img_height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        y_text = y_offset + stroke_width
        for paragraph in paragraphs:
            lines = textwrap.wrap(paragraph, width=char_per_line, expand_tabs=False,
                                  replace_whitespace=False, drop_whitespace=False)
            for line in lines:
                width = font.getbbox(line)[2] - font.getbbox(line)[0]
                height = font.getbbox(line)[3] - font.getbbox(line)[1]
                # Recalculate x-coordinates based on align parameters
                if align == "left":
                    x_text = x_offset
                elif align == "center":
                    x_text = (img_width - width) // 2
                elif align == "right":
                    x_text = img_width - width - x_offset
                else:
                    x_text = x_offset# Default to Left Alignment

                draw.text(
                    xy=(x_text, y_text),
                    text=line,
                    fill=text_color,
                    font=font,
                    stroke_width=stroke_width,
                    stroke_fill=stroke_color,
                    )
                y_text += height + leading
            y_text += leading * 2

        if size_as is not None:
            for i in size_as:
                ret_images.append(pil2tensor(img))
                ret_masks.append(image2mask(img.split()[3]))
        else:
            ret_images.append(pil2tensor(img))
            ret_masks.append(image2mask(img.split()[3]))

        log(f"{NODE_NAME} Processed.", message_type='finish')
        return (torch.cat(ret_images, dim=0),torch.cat(ret_masks, dim=0),)
```