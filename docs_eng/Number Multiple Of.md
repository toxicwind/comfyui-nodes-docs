# Documentation
- Class name: WAS_Number_Multiple_Of
- Category: WAS Suite/Number/Functions
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method 'number_multiple_of' is designed to determine whether a given number is a multiple of another given number. If not, the method calculates the most recent multiples. This function is essential in a multiple scenario that requires further processing or mathematical operation.

# Input types
## Required
- number
    - The parameter 'number 'is to check if it is a multiple value of'multiple '. It plays a key role in the operation of the node, as it is the subject of multiple checks and subsequent calculations.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
## Optional
- multiple
    - The parameter'multiple'defines the divide used to determine whether 'number' is multiple. It is important because it determines the specific number of times 'number 'to compare. The default value is 8, which ensures that nodes can be used without specifying this parameter.
    - Comfy dtype: INT
    - Python dtype: Optional[int]

# Output types
- result
    - The parameter'resource'means the result of the 'number_multiple_of' method. If the 'number' is not originally a multiple of'multiple', it is the nearest multiple. This result is important for any multi-digit follow-up.
    - Comfy dtype: COMBO[NUMBER, FLOAT, INT]
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_Multiple_Of:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',), 'multiple': ('INT', {'default': 8, 'min': -18446744073709551615, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    FUNCTION = 'number_multiple_of'
    CATEGORY = 'WAS Suite/Number/Functions'

    def number_multiple_of(self, number, multiple=8):
        if number % multiple != 0:
            return (number // multiple * multiple + multiple,)
        return (number, number, int(number))
```