# Documentation
- Class name: OutputString
- Category: utils
- Output node: True
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

The node is intended to process and produce text data and to serve as an important practical tool in the various workflows that require string operations or displays.

# Input types
## Required
- text
    - Text input is essential because it is the primary data for node operations. It affects the entire output of node and determines the content and structure of the result string.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ui.string
    - Output is the result of a node action for the input string. It is important because it conveys the final result of the node function.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class OutputString:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {})}}
    RETURN_TYPES = ()
    FUNCTION = 'output_string'
    OUTPUT_NODE = True
    CATEGORY = 'utils'

    def output_string(self, string):
        return ({'ui': {'string': string}},)
```