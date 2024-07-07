# Documentation
- Class name: IntegerAndString
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The IntegerAnd String node is designed to convert integer input into the form of a string expression corresponding to it. It emphasizes the utility of converting numerical data into a more human-friendly format, which allows for the operation of a string operation or interaction between the value and the text data.

# Input types
## Required
- seed
    - The parameter'seed' is essential for the node, because it is the initial integer value that will be converted into a string. It plays a key role in determining the output, because the function of the node revolves around the conversion process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- seed
    - The output parameter'seed' represents the original integer value provided to the node. It marks the continuity of the whole value in the operation of the node, ensuring that the initial value input is retained.
    - Comfy dtype: INT
    - Python dtype: int
- seed_string
    - The output parameter'seed_string' is a string expression for an integer. It highlights the main conversion function of the node and shows the result of converting the numerical data into a more accessible text format.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class IntegerAndString:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('seed', 'seed_string')
    FUNCTION = 'output'
    CATEGORY = 'Mikey/Utils'

    def output(self, seed):
        seed_string = str(seed)
        return (seed, seed_string)
```