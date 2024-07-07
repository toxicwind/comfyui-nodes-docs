# Documentation
- Class name: WAS_Text_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `text_input_switch' method of the WAS_Text_Input_Switch node is designed to select conditionally between text inputes based on the Boolean sign. It serves as a logical switch that guides the flow of text data in a process or workflow that requires decision-making. This node plays a key role in managing the logic of conditions in text-based operations.

# Input types
## Required
- text_a
    - The 'text_a' parameter is the first text input that node can switch to according to the boolean conditions. It is essential for the node decision-making process, as it represents one of the likely outcomes of the boolean mark when true.
    - Comfy dtype: STRING
    - Python dtype: str
- text_b
    - The 'text_b' parameter is the alternative text input that you can choose when the Boolean mark is false. It is essential because it defines the alternative path to text data when conditions are not met.
    - Comfy dtype: STRING
    - Python dtype: str
- boolean
    - The 'boolean' parameter is used as a sign to determine which text input is returned. It is a key component of the node function because its true value directly influences the output of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- output_text
    - 'output_text' is the result of the node operation, either 'text_a' or 'text_b' according to the value entered by 'boolean'. It represents the text selected after the node decision-making process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text_a': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'text_b': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def text_input_switch(self, text_a, text_b, boolean=True):
        if boolean:
            return (text_a,)
        else:
            return (text_b,)
```