# Documentation
- Class name: FontInput
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node retrieves font files according to the specified font name and provides a simplified method for accessing and using fonts in various graphic or text-processing tasks.

# Input types
## Required
- font
    - The 'font' parameter is essential because it identifies the specific fonts to be used in the system. It directly affects the operation of nodes and the output of results, ensuring that the correct fonts are applied to the current task.
    - Comfy dtype: list
    - Python dtype: list

# Output types
- font_file
    - Output `font_file' is a searchable font file associated with input font parameters, which is essential for further graphic or text processing in the application.
    - Comfy dtype: list
    - Python dtype: list

# Usage tips
- Infra type: CPU

# Source code
```
class FontInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'font': (list(font_files.keys()),)}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, font):
        return (font_files[font],)
```