# Documentation
- Class name: TextInput
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

TextInput node is designed to process text input and provides a simple interface for processing string data. It can accept multiple lines of text and provides flexibility for various text-processing tasks. In processes that require text analysis or operation, this node plays a key role in ensuring that the text is properly formatted and ready for follow-up.

# Input types
## Required
- text
    - The `text' parameter is the main input for the TextInput node. This is where the actual text to be processed is provided. This input is essential because it directly affects the operation of the node and the subsequent output. The text can cross multiple lines and adapt to a wide range of text input.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output_text
    - `output_text' is the result of text entered by TextInput node processing. It represents a conversion or analytical version of the input, depending on the operation performed by the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TextInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': ''})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, text):
        return (text,)
```