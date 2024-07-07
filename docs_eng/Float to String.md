# Documentation
- Class name: FLOATtoSTRING
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The FLOATTOSTRING node is designed to convert floating points into string expressions. It provides the function of formatting numbers, allowing for the selection of comma, which is very useful in displaying digital data and makes the data easier to read.

# Input types
## Required
- float_
    - The 'float_' parameter is the number of floating points that need to be converted to a string. It plays a key role in the operation of the node, as it is the main input to the conversion process.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- use_commas
    - The 'use_commas'parameter determines whether the output string should contain a comma as a thousands separator. This increases the readability of numbers, especially for larger values.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str

# Output types
- STRING
    - The output of the FLOATTOSTRING node is a string for which you enter the number of floating points. The format of the string is influenced by the 'use_commas' parameter. If set to 'true', you can include comma as a thousands separator.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class FLOATtoSTRING:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'float_': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1000000.0}), 'use_commas': (['true', 'false'], {'default': 'false'})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'convert'
    CATEGORY = 'Mikey/Utils'

    def convert(self, float_, use_commas):
        if use_commas == 'true':
            return (f'{float_:,}',)
        else:
            return (f'{float_}',)
```