# Documentation
- Class name: IntNumber
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node classifies and limits the input of numbers to ensure that the output meets the defined scope and increment.

# Input types
## Required
- number
    - The central input of the node assessment ensures that it falls within the specified minimum and maximum limit.
    - Comfy dtype: INT
    - Python dtype: int
- min_value
    - The lower limit used for the node is limited to the lower limit if the input number is below this threshold.
    - Comfy dtype: INT
    - Python dtype: int
- max_value
    - Node's upper limit is limited if the input number exceeds this limit.
    - Comfy dtype: INT
    - Python dtype: int
- step
    - Node is the value of the increment that is taken into account when adjusting the input number within the specified range.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- number
    - Limited and adjusted digital output, which falls within the definition and follows the specified incremental steps.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class IntNumber:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'number': ('INT', {'default': 0, 'min': -1, 'max': 18446744073709551615, 'step': 1, 'display': 'number'}), 'min_value': ('INT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 1, 'display': 'number'}), 'max_value': ('INT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 1, 'display': 'number'}), 'step': ('INT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, number, min_value, max_value, step):
        if number < min_value:
            number = min_value
        elif number > max_value:
            number = max_value
        return (number,)
```