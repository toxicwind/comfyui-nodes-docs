# Documentation
- Class name: CR_SetValueOnBoolean
- Category: Comfyroll/Utils/Conditional
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SetValueOnBoolean node is designed to allocate a value according to the assessment of the Boolean condition. It provides a simple mechanism for returning one of the two values based on the input of the boolean value for real or false, thus promoting the logic of conditions in the workflow.

# Input types
## Required
- boolean
    - The " boolean " parameter is essential because it determines the process of node logic. It determines which value to return on the basis of its true value.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- value_if_true
    - The " value_if_true" parameter defines the values that are returned when the "boolean" parameter is assessed as true. It plays a key role in the condition output of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- value_if_false
    - The " value_if_false " parameter sets the values to be returned when the " boolean" parameter is evaluated as false. It is essential for the output of alternative conditions at the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- INT
    - The “INT” output represents the integer value of the parameters “value_if_true” or “value_if_f_false” corresponding to the Boolean condition.
    - Comfy dtype: INT
    - Python dtype: int
- FLOAT
    - The FLOAT output provides a floating point representation based on a return value based on a Boolean condition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - The “show_help” output provides a URL link to the node document for further guidance and information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SetValueOnBoolean:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'boolean': ('BOOLEAN', {'default': True, 'forceInput': True}), 'value_if_true': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'value_if_false': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('INT', 'FLOAT', 'show_help')
    FUNCTION = 'set_value'
    CATEGORY = icons.get('Comfyroll/Utils/Conditional')

    def set_value(self, boolean, value_if_true, value_if_false):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-set-value-on-boolean'
        if boolean == True:
            return (int(value_if_true), value_if_true, show_help)
        else:
            return (int(value_if_false), value_if_false, show_help)
```