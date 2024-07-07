# Documentation
- Class name: WAS_Text_To_String
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `text_to_string' method of the WAS_Text_Text_String' is designed to convert the input text into a standardized string format. It ensures that the text is processed and returns in a consistent form that can be used to follow the workflow.

# Input types
## Required
- text
    - The 'text' parameter is essential to the operation of the node because it defines the content that needs to be converted to a string. Its function is to provide node with raw material to be processed, which is essential to the execution and outcome of the node.
    - Comfy dtype: STRING
    - Python dtype: Union[str, List[str]]

# Output types
- output
    - The 'output' parameter represents the result of the 'text_to_string' method, i.e. the converted string. It is important because it is the main output of the node and contains the processed text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_To_String:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'text_to_string'
    CATEGORY = 'WAS Suite/Text/Operations'

    def text_to_string(self, text):
        return (text,)
```