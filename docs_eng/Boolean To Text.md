# Documentation
- Class name: WAS_Boolean_To_Text
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Boolean_To_Text node is designed to convert the boolean value to the text expression 'True' or 'False'. It serves as a simple and effective bridge linking the boolean logic to the text output, facilitating the integration of the boolean operation with a text-based system or process.

# Input types
## Required
- boolean
    - The parameter 'boolean' is essential to the operation of the node, because it is the input that determines the output of the node. It directly influences the execution of the node by directing the return of the text 'True' or 'False'.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- text
    - The output parameter'text' represents the text equivalent for which the boolean value is entered. It is important because it provides a clear and direct way to convert the boolean logic into a human readable format.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Boolean_To_Text:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'boolean': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'do'
    CATEGORY = 'WAS Suite/Logic'

    def do(self, boolean):
        if boolean:
            return ('True',)
        return ('False',)
```