# Documentation
- Class name: ImageCaption
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The ImageCaption node is designed to generate and superimpose the title on the image. It accepts an image, a font and a caption string as input, and produces an image with a packaged title text below the original image. This node is particularly suitable for creating an annotated image with a descriptive title or a social media post.

# Input types
## Required
- image
    - The image parameter is the basic image that will be added to the title. This is a key component, because the entire title process is visually anchored on this image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- font
    - Font parameters specify the type of font that you want to use for the title text. It affects the style and readability of the text, which is essential for the validity of the title in communicating information.
    - Comfy dtype: STRING
    - Python dtype: str
- caption
    - Title parameter is the text that will be placed on the image. It is a core element because it provides descriptive or explanatory content accompanying the image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- extra_pnginfo
    - Extra_pnginfo parameters are used to provide additional information, such as metadata or specific instructions for the title process, that may be required for certain operations.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict
- prompt
    - A hint parameter is used to guide the header process and may be used to provide a context or node with specific instructions to be followed in generating the header.
    - Comfy dtype: PROMPT
    - Python dtype: dict

# Output types
- image
    - Output images are the result of the title process, which includes original images that have been added to the title text. This is the final product that can be used for presentation or further processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageCaption:

    @classmethod
    def INPUT_TYPES(cls):
        if os.path.exists(os.path.join(folder_paths.base_path, 'fonts')):
            cls.font_dir = os.path.join(folder_paths.base_path, 'fonts')
            cls.font_files = [os.path.join(cls.font_dir, f) for f in os.listdir(cls.font_dir) if os.path.isfile(os.path.join(cls.font_dir, f))]
            cls.font_file_names = [os.path.basename(f) for f in cls.font_files]
            return {'required': {'image': ('IMAGE',), 'font': (cls.font_file_names, {'default': cls.font_file_names[0]}), 'caption': ('STRING', {'multiline': True, 'default': 'Caption'})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
        else:
            cls.font_dir = None
            cls.font_files = None
            cls.font_file_names = None
            return {'required': {'image': ('IMAGE',), 'font': ('STRING', {'default': 'Path to font file'}), 'caption': ('STRING', {'multiline': True, 'default': 'Caption'})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'caption'
    CATEGORY = 'Mikey/Image'

    def get_text_size(self, font, text):
        """
        Get width and height of a text string with given font.

        Parameters:
            font (ImageFont.FreeTypeFont): A font object.
            text (str): Text to measure.

        Returns:
            (int, int): Width and height of the text.
        """
        (left, top, right, bottom) = font.getbbox(text)
        width = right - left
        height = bottom - top
        return (width, height)

    def wrap_text(self, text, font, max_width):
        """Wrap text to fit inside a specified width when rendered."""
        wrapped_lines = []
        for line in text.split('\n'):
            words = line.split(' ')
            new_line = words[0]
            for word in words[1:]:
                if int(font.getlength(new_line + ' ' + word)) <= max_width:
                    new_line += ' ' + word
                else:
                    wrapped_lines.append(new_line)
                    new_line = word
            wrapped_lines.append(new_line)
        return wrapped_lines

    @apply_to_batch
    def caption(self, image, font, caption, extra_pnginfo=None, prompt=None):
        if extra_pnginfo is None:
            extra_pnginfo = {}
        caption = search_and_replace(caption, extra_pnginfo, prompt)
        orig_image = tensor2pil(image)
        (width, height) = orig_image.size
        if self.font_dir is None:
            font_file = font
            if not os.path.isfile(font_file):
                raise Exception('Font file does not exist: ' + font_file)
        else:
            font_file = os.path.join(self.font_dir, font)
        font = ImageFont.truetype(font_file, 32)
        max_width = width
        wrapped_lines = self.wrap_text(caption, font, max_width)
        (_, text_height) = self.get_text_size(font, 'Hg')
        wrapped_text_height = len(wrapped_lines) * text_height
        padding = 15
        caption_height = wrapped_text_height + padding * 2
        text_image = Image.new('RGB', (width, caption_height), (0, 0, 0))
        draw = ImageDraw.Draw(text_image)
        line_spacing = 5
        y_position = padding
        for line in wrapped_lines:
            text_width = font.getlength(line)
            x_position = (width - int(text_width)) // 2
            draw.text((x_position, y_position), line, (255, 255, 255), font=font)
            (_, text_height) = self.get_text_size(font, line)
            y_position += text_height + line_spacing
        combined_image = Image.new('RGB', (width, height + caption_height + line_spacing), (0, 0, 0))
        combined_image.paste(text_image, (0, height))
        combined_image.paste(orig_image, (0, 0))
        return pil2tensor(combined_image)
```