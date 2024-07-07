# Documentation
- Class name: SeargeFloatConstant
- Category: Searge/_deprecated_/Floats
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

SeergeFloatConstant is a node designed to provide a constant floating point value in the workflow. It ensures that consistent and constant values are used in different parts of the system or experiment, which helps to improve the reliability and replicability of the results.

# Input types
## Required
- value
    - The parameter 'value' is the constant float number that this node will provide. It plays a key role in maintaining system stability by providing a fixed reference point for calculation and comparison.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- value
    - Output 'value'is the constant float number for input settings. It is important because it represents the unaltered and predefined constant to be used in subsequent operations or analyses.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeFloatConstant:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('FLOAT', {'default': 0.0, 'step': 0.01})}}
    RETURN_TYPES = ('FLOAT',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Floats'

    def get_value(self, value):
        return (value,)
```