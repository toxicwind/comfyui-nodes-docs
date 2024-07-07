# Documentation
- Class name: WAS_Text_List
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node organizes and structures the entered text string into a uniform list format for subsequent processing and analysis of text data.

# Input types
## Required
- text_a
    - The first text input is essential for running the node because it provides the initial data from the list.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- text_b
    - Additional text input further enriches the list and allows for more comprehensive text analysis.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- text_c
    - Subsequent text entry increases the diversity of text lists and their usefulness in various text-processing scenarios.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- text_d
    - More text input expands the ability of nodes and adapts to a broader text data set.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- text_e
    - Additional text input ensures that nodes can handle a wide variety of text input, increasing their flexibility.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- text_f
    - The existence of multiple text input points highlights the ability of nodes to effectively manage complex text data.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- text_g
    - Including more text input shows the ability to expand nodes and adapt to various text-processing needs.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]

# Output types
- list_of_texts
    - Output is an integrated list of text string that provides a structured format for further analysis and processing.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_List:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'text_a': ('STRING', {'forceInput': True}), 'text_b': ('STRING', {'forceInput': True}), 'text_c': ('STRING', {'forceInput': True}), 'text_d': ('STRING', {'forceInput': True}), 'text_e': ('STRING', {'forceInput': True}), 'text_f': ('STRING', {'forceInput': True}), 'text_g': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = ('LIST',)
    FUNCTION = 'text_as_list'
    CATEGORY = 'WAS Suite/Text'

    def text_as_list(self, **kwargs):
        text_list: list[str] = []
        for k in sorted(kwargs.keys()):
            v = kwargs[k]
            if isinstance(v, str):
                text_list.append(v)
        return (text_list,)
```