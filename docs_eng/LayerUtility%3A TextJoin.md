# Documentation
- Class name: TextJoin
- Category: 😺dzNodes/LayerUtility/Data
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Combines the text into one paragraph.

# Input types

## Required

- text_1
    - Text 1.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- text_2
    - Text 2.
    - Comfy dtype: STRING
    - Python dtype: str

- text_3
    - Text 3.
    - Comfy dtype: STRING
    - Python dtype: str

- text_4
    - Text 4.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types

- text
    - text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TextJoin:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_1": ("STRING", {"multiline": False}),

            },
            "optional": {
                "text_2": ("STRING", {"multiline": False}),
                "text_3": ("STRING", {"multiline": False}),
                "text_4": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "text_join"
    CATEGORY = '😺dzNodes/LayerUtility/Data'

    def text_join(self, **kwargs):

        texts = [kwargs[key] for key in kwargs if key.startswith('text')]
        combined_text = ', '.join(texts)
        return (combined_text,)
```