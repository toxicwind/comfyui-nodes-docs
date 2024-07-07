# Documentation
- Class name: SeargeIntegerConstant
- Category: Searge/_deprecated_/Integers
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeIntegerConstant node provides a constant integer value in the workflow. It is intended to provide a stable and constant integer that can be used in various calculations or comparisons without external input or data processing.

# Input types
## Required
- value
    - The parameter 'value' is the core of the SeergeIntegerConstant node, which represents the fixed integer number that will always be returned. It serves as the base component in the workflow, ensuring that downstream operations can access a consistent and predefined integer value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- value
    - The output 'value' is the only result provided by the SeergeIntegerConstant node, i.e., the constant integer number as input settings. It is important to ensure that the whole number remains constant throughout the workflow, thus contributing to predictable and stable operations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeIntegerConstant:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Integers'

    def get_value(self, value):
        return (value,)
```