# Documentation
- Class name: WAS_String_To_Text
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `string_to_text'is designed to convert a given string into a text format that can be further processed or analysed. It plays a key role in text operations to ensure that the input string is properly formatted for subsequent tasks, such as text analysis or machine learning models requiring text data.

# Input types
## Required
- string
    - The parameter'string' is necessary because it represents the original text input that the node will process. Its proper formatting and content significantly influences the ability of the node to convert it into a usable text format.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text
    - Output 'text' is the result of node operations that provide text formats that are converted from input strings. It is important because it is the main output used in downstream text-related processes.
    - Comfy dtype: TEXT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_String_To_Text:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'string': ('STRING', {})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'string_to_text'
    CATEGORY = 'WAS Suite/Text/Operations'

    def string_to_text(self, string):
        return (string,)
```