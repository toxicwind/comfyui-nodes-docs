# Documentation
- Class name: WAS_Text_Contains
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `text_contains'method is designed to determine whether a given substring exists in a larger text string. It indicates the existence or absence of a substring by comparing the two strings and returning a boolean value. This method is essential for text analysis and data validation tasks, and the existence of a particular text mode is of interest.

# Input types
## Required
- text
    - The 'text 'parameter represents the method that will search the larger text subjects of'sub_text'. It is essential for the operation of nodes, as it defines the scope of the search and directly influences the results of the method.
    - Comfy dtype: STRING
    - Python dtype: str
- sub_text
    - The'sub_text' parameter is a specific string that the method will search for in the 'text' parameter. Its presence in the larger text is a key input to the node function.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- case_insensitive
    - The 'case_insentive'argument decides whether the'sub_text' search in 'text' should ignore the capital case. This may be important to ensure that the search is not hindered by the difference in case.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - "Result' output instruction found'sub_text' in 'text'. It is a binary indicator that provides clear and concise answers to the questions posed by the method.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Contains:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': False}), 'sub_text': ('STRING', {'default': '', 'multiline': False})}, 'optional': {'case_insensitive': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('BOOLEAN',)
    FUNCTION = 'text_contains'
    CATEGORY = 'WAS Suite/Logic'

    def text_contains(self, text, sub_text, case_insensitive):
        if case_insensitive:
            sub_text = sub_text.lower()
            text = text.lower()
        return (sub_text in text,)
```