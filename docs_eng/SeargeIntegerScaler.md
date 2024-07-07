# Documentation
- Class name: SeargeIntegerScaler
- Category: Searge/_deprecated_/Integers
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is based on the factors and multipliers provided to scale and round the input integer values. It ensures that the output values remain within the range and particle size required.

# Input types
## Required
- value
    - The initial integer value will be scaled by the node operation. It is the basis for the node's purpose, as it is the basis for the conversion.
    - Comfy dtype: INT
    - Python dtype: int
- factor
    - Applies to the multiplier of the input value to determine the scale. It is important because it directly affects the size of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- multiple_of
    - The scaling result should be its multiple value, ensuring that the output is rounded to the most recent acceptable value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- value
    - The processed whole value has been scaled and rounded to represent the final output of the node based on the input parameter.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeIntegerScaler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'factor': ('FLOAT', {'default': 1.0, 'step': 0.01}), 'multiple_of': ('INT', {'default': 1, 'min': 0, 'max': 65536})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Integers'

    def get_value(self, value, factor, multiple_of):
        return (int(value * factor // multiple_of) * multiple_of,)
```