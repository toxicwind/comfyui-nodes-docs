# Documentation
- Class name: WAS_Debug_Number_to_Console
- Category: WAS Suite/Debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The " debug_to_console " method is a practical tool for developers that allows them to print numbers to the control table with custom tags for debugging. It increases the visibility of the test information by applying colour coding to the output.

# Input types
## Required
- number
    - The " number " parameter is essential to the operation of the node because it is the value that will be printed to the control table. It plays a key role in the debugging process by providing a particular data point that needs to be checked.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
## Optional
- label
    - The " label " parameter is used to add descriptive text before numbers, making it easier to identify the context of debugging messages. It is particularly useful when using multiple debugging statements in scripts.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - The “redault” parameter represents the original number used for debugging. It is returned to maintain the flow of data through nodes and allows further processing if required.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Debug_Number_to_Console:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',), 'label': ('STRING', {'default': 'Debug to Console', 'multiline': False})}}
    RETURN_TYPES = ('NUMBER',)
    OUTPUT_NODE = True
    FUNCTION = 'debug_to_console'
    CATEGORY = 'WAS Suite/Debug'

    def debug_to_console(self, number, label):
        if label.strip() != '':
            cstr(f'\x1b[33m{label}\x1b[0m:\n{number}\n').msg.print()
        else:
            cstr(f'\x1b[33mDebug to Console\x1b[0m:\n{number}\n').msg.print()
        return (number,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```