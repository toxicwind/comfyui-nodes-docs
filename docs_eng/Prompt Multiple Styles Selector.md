# Documentation
- Class name: WAS_Prompt_Multiple_Styles_Selector
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Prompt_Mulcle_Styles_Selector class `load_style'method is designed to integrate multiple style tips into a single, coherent hint string. This is achieved by selecting and collating style-specific tips from predefined style files, allowing customizing the text generation process using a variety of style nuances.

# Input types
## Required
- style1
    - The parameter `style1'is essential to specify the first style to be loaded from a style file. It directly influences the composition of the final hint by identifying the style features that will be included.
    - Comfy dtype: str
    - Python dtype: str
- style2
    - Parameters `style2'allow the second unique style to be included in the hint. Their selection helps to increase the diversity and richness of the text-generation process.
    - Comfy dtype: str
    - Python dtype: str
- style3
    - Parameter `style3'allows a third style to be added to the hint, further enhancing the style options available for text generation.
    - Comfy dtype: str
    - Python dtype: str
- style4
    - The parameter `style4'is used to specify the fourth style that you can mix to the hint. It provides an additional style level for text generation output.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- positive_string
    - Output parameter `positive_string'means the compiled hint, which combines the selected style into a coherent and stylish text-generation tip.
    - Comfy dtype: str
    - Python dtype: str
- negative_string
    - Output parameter `negative_string'captures negative hints derived from the selected style that can be used to fine-tune and guide the text generation process away from desired properties.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Prompt_Multiple_Styles_Selector:

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
        return {'required': {'style1': (style_list,), 'style2': (style_list,), 'style3': (style_list,), 'style4': (style_list,)}}
    RETURN_TYPES = (TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ('positive_string', 'negative_string')
    FUNCTION = 'load_style'
    CATEGORY = 'WAS Suite/Text'

    def load_style(self, style1, style2, style3, style4):
        styles = {}
        if os.path.exists(STYLES_PATH):
            with open(STYLES_PATH, 'r') as data:
                styles = json.load(data)
        else:
            cstr(f'The styles file does not exist at `{STYLES_PATH}`. Unable to load styles! Have you imported your AUTOMATIC1111 WebUI styles?').error.print()
            return ('', '')
        selected_styles = [style1, style2, style3, style4]
        for style in selected_styles:
            if style not in styles:
                print(f"Style '{style}' was not found in the styles file.")
                return ('', '')
        prompt = ''
        negative_prompt = ''
        for style in selected_styles:
            prompt += styles[style]['prompt'] + ' '
            negative_prompt += styles[style]['negative_prompt'] + ' '
        return (prompt.strip(), negative_prompt.strip())
```