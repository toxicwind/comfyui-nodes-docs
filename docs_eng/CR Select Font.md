# Documentation
- Class name: CR_SelectFont
- Category: Comfyroll/Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SelectFont node is designed to allow users to select fonts from the predefined list of available TrueType fonts. It plays a vital role in setting fonts in text rendering. By providing a direct interface for the fonts they need, this node abstractes the complexity of font management and ensures compatibility and ease of use between different operating systems.

# Input types
## Required
- font_name
    - The 'font_name'parameter is essential to specify the exact font that the user wishes to use for text rendering. It directly affects the visual output and style of the rendering text and is the key option for achieving the aesthetic and readability required.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- font_name
    - The 'font_name'output parameter indicates the selected font to be used in subsequent text rendering. It represents a successful selection of a font that is essential for continuity and consistency of text styles throughout the workflow.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help'output provides a document URL link for further help. It is particularly useful for users who need additional guidance on how to use the selected font or more information about the font selection process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SelectFont:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        if platform.system() == 'Windows':
            system_root = os.environ.get('SystemRoot')
            font_dir = os.path.join(system_root, 'Fonts') if system_root else None
        elif platform.system() == 'Linux':
            font_dir = '/usr/share/fonts/truetype'
        elif platform.system() == 'Darwin':
            font_dir = '/System/Library/Fonts'
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'font_name': (file_list,)}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('font_name', 'show_help')
    FUNCTION = 'select_font'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def select_font(self, font_name):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-select-font'
        return (font_name, show_help)
```