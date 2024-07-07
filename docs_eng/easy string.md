# Documentation
- Class name: String
- Category: EasyUse/Logic/Type
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node facilitates the processing and operation of string data, enabling users to perform various operations for text input. It is designed to process string conversion, conversion and analysis in a direct manner, making it a basic component of the text data task.

# Input types
## Required
- value
    - The 'value'parameter is essential for the operation of the node, which represents the text input to be processed. It is the basis for all string operations and conversions and directly affects the validity of output results and node execution.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- string
    - Outputs the result of the string processing performed by'string'for the node. It contains the results of the operation performed for the input text, marking the main function of the node and its contribution to the workflow.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class String:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('STRING', {'default': ''})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('string',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic/Type'

    def execute(self, value):
        return (value,)
```