# Documentation
- Class name: LimitNumber
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node limits the given number to a specified range, ensuring that it does not exceed the defined minimum and maximum boundary. It is primarily used to maintain the integrity of the number and to prevent invalid values from affecting downstream processes.

# Input types
## Required
- number
    - Enter numbers that need to be limited to the specified range. This is a key parameter, as it is the core value for node operations to ensure that they remain within an acceptable range.
    - Comfy dtype: any_type
    - Python dtype: Union[int, float]
- min_value
    - Enter the lower limit of the acceptable range of the number. It plays a key role in setting the minimum limit below which the input value is not allowed to fall.
    - Comfy dtype: INT
    - Python dtype: int
- max_value
    - Enter the upper limit of the acceptable range of the number. It is essential in defining the maximum maximum limit of the input value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- number
    - An output number that is limited to the specified range. It is the result of a node operation that ensures that the value is within the acceptable boundary defined by the input parameter.
    - Comfy dtype: any_type
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class LimitNumber:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': (any_type,), 'min_value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'step': 1, 'display': 'number'}), 'max_value': ('INT', {'default': 1, 'min': 1, 'max': 18446744073709551615, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('number',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, number, min_value, max_value):
        nn = number
        if isinstance(number, int):
            min_value = int(min_value)
            max_value = int(max_value)
        if isinstance(number, float):
            min_value = float(min_value)
            max_value = float(max_value)
        if number < min_value:
            nn = min_value
        elif number > max_value:
            nn = max_value
        return (nn,)
```