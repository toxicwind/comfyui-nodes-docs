# Documentation
- Class name: INTtoSTRING
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The InttoSTRING node is intended to convert the whole value into their string expression. It provides the function of formatting the string, selecting whether to use commas to adapt to different cases, and providing a multifunctional approach to the numerical data presentation.

# Input types
## Required
- int_
    - The parameter 'int_' is the integer number that needs to be converted to a string. It plays a key role in the operation of the node, as it is the main input to the conversion process.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- use_commas
    - Parameter 'use_commas' determines whether an output string should contain a comma as a thousands separator. It affects the readability of digital data in string formats.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str

# Output types
- STRING
    - The output of the InttoSTRING node is an integer string. It is important because it directly reflects the conversion of the node's main function.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class INTtoSTRING:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'int_': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'use_commas': (['true', 'false'], {'default': 'false'})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'convert'
    CATEGORY = 'Mikey/Utils'

    def convert(self, int_, use_commas):
        if use_commas == 'true':
            return (f'{int_:,}',)
        else:
            return (f'{int_}',)
```