# Documentation
- Class name: CR_SetValueOnBinary
- Category: Comfyroll/Utils/Conditional
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SetValueOnBinary node is designed to distribute a value conditionally according to the status entered in the binary system. Its working principle is very simple: if the binary is entered as true (1), it returns the value specified for the true situation; if it is false (0), it returns the value of the false situation. This function is essential for achieving the logic of conditions in the workflow, allowing simple operation of the data flow based on binary conditions.

# Input types
## Required
- binary
    - The `binary' parameter is a key input, which determines the behaviour of the node. It determines which value to return as a node. The binary input must be an integer, can be 0 or 1, does not accept other values, ensuring a clear and clear condition check.
    - Comfy dtype: INT
    - Python dtype: int
- value_if_1
    - The `value_if_1' parameter defines the value that will return when binary input is true. It is a floating number that can be expressed as a wide range of values allowing flexibility in the allocation of conditions based on binary conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- value_if_0
    - The `value_if_0' parameter sets the value to be returned when binary input is false. Like `value_if_1', it is also a floating number that ensures consistency in the type of value that nodes can return, regardless of the binary condition.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- INT
    - The `INT' output provides an integer of the binary input value as a direct and clear reflection of the result of the condition.
    - Comfy dtype: INT
    - Python dtype: int
- FLOAT
    - The `FLOAT' output returns the value associated with the binary input condition. It is based on the value that the binary input is true or false and used downstream in the workflow.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - The `show_help' output provides a URL link to the node document page, allowing users easy access to more detailed information on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SetValueOnBinary:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'binary': ('INT', {'default': 1, 'min': 0, 'max': 1, 'forceInput': True}), 'value_if_1': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'value_if_0': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('INT', 'FLOAT', 'show_help')
    FUNCTION = 'set_value'
    CATEGORY = icons.get('Comfyroll/Utils/Conditional')

    def set_value(self, binary, value_if_1, value_if_0):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-set-value-on-boolean'
        if binary == 1:
            return (int(value_if_1), value_if_1, show_help)
        else:
            return (int(value_if_0), value_if_0, show_help)
```