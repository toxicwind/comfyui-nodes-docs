# Documentation
- Class name: CR_BinaryPatternSimple
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_BinaryPattenSimple node is designed to solve binary patterns and render them visible grids. It accepts a binary number string and converts it into an image, each of which represents the colour of a square in the grid, thus creating visualization expressions of binary data.

# Input types
## Required
- binary_pattern
    - Binary mode is a string consisting of binary numbers (0 and 1) that defines the pattern to be drawn. Each line of the bit corresponds to one line in the output image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- width
    - Width determines the width of the output image in pixels. It should be a positive integer and affect the size of each block in the grid.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height determines the height of the output image in pixels. Similar to width, it should be a positive integer and define the vertical size of the grid.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output image is a visual expression of the binary mode that you enter. It is made up of a grid of squares, each corresponding to one of the bits in the pattern.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Provides a URL link to the document for more information and help in using the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_BinaryPatternSimple:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'binary_pattern': ('STRING', {'multiline': True, 'default': '10101'}), 'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw_pattern'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw_pattern(self, binary_pattern, width, height):
        rows = binary_pattern.strip().split('\n')
        grid = [[int(bit) for bit in row.strip()] for row in rows]
        square_width = width // len(rows[0])
        square_height = height // len(rows)
        image = Image.new('RGB', (width, height), color='black')
        draw = ImageDraw.Draw(image)
        for (row_index, row) in enumerate(grid):
            for (col_index, bit) in enumerate(row):
                x1 = col_index * square_width
                y1 = row_index * square_height
                x2 = x1 + square_width
                y2 = y1 + square_height
                color = 'black' if bit == 1 else 'white'
                draw.rectangle([x1, y1, x2, y2], fill=color, outline='black')
        image_out = pil2tensor(image)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes-2#cr-simple-binary-pattern'
        return (image_out, show_help)
```