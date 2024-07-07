# Documentation
- Class name: WAS_Prompt_Styles_Selector
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Prompt_Styles_Selector node is designed to manage and retrieve the style of text tips. It plays a key role in loading predefined styles that are essential for generating text output that is relevant and consistent in context.

# Input types
## Required
- style
    - The'style'parameter is essential to determine which style configuration you want to load. It affects the operation of the node by specifying a particular style that you want to apply from the available style to texttips.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- positive_string
    - The `positive_string' output provides a positive hint linked to the chosen style, which is essential to guide the text generation process in the desired direction.
    - Comfy dtype: str
    - Python dtype: str
- negative_string
    - The `negative_string' output provides a negative hint of the style chosen to improve text generation by blocking elements that do not want to appear.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Prompt_Styles_Selector:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        style_list = []
        if os.path.exists(STYLES_PATH):
            with open(STYLES_PATH, 'r') as f:
                if len(f.readlines()) != 0:
                    f.seek(0)
                    data = f.read()
                    styles = json.loads(data)
                    for style in styles.keys():
                        style_list.append(style)
        if not style_list:
            style_list.append('None')
        return {'required': {'style': (style_list,)}}
    RETURN_TYPES = (TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ('positive_string', 'negative_string')
    FUNCTION = 'load_style'
    CATEGORY = 'WAS Suite/Text'

    def load_style(self, style):
        styles = {}
        if os.path.exists(STYLES_PATH):
            with open(STYLES_PATH, 'r') as data:
                styles = json.load(data)
        else:
            cstr(f'The styles file does not exist at `{STYLES_PATH}`. Unable to load styles! Have you imported your AUTOMATIC1111 WebUI styles?').error.print()
        if styles and style != None or style != 'None':
            prompt = styles[style]['prompt']
            negative_prompt = styles[style]['negative_prompt']
        else:
            prompt = ''
            negative_prompt = ''
        return (prompt, negative_prompt)
```