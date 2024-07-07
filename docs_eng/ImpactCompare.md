# Documentation
- Class name: ImpactCompare
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactCompare node is designed to evaluate and compare two input `a' and `b' based on the specified comparative operator. It is a basic logical tool that enables users to perform various relationship checks and to return the boolean results corresponding to the comparison made.

# Input types
## Required
- cmp
    - The parameter 'cmp' defines the type of comparison between input 'a' and 'b'. It is vital because it determines the logic to be applied to comparison and directly affects the results of node execution.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first number of operations in the comparison. Its values and data types can significantly influence the performance of nodes and the boolean results returned by nodes.
    - Comfy dtype: any
    - Python dtype: Any
- b
    - The parameter 'b' is the second operation in the comparison. It works with 'a' to determine the final boolean result based on the specified comparative operator.
    - Comfy dtype: any
    - Python dtype: Any

# Output types
- result
    - The'redult' output reflects the results of the comparison between 'a' and 'b' as a boolean value. It is important because it is a direct output of node logical operations and is used to inform subsequent processes or decisions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactCompare:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'cmp': (['a = b', 'a <> b', 'a > b', 'a < b', 'a >= b', 'a <= b', 'tt', 'ff'],), 'a': (any_typ,), 'b': (any_typ,)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('BOOLEAN',)

    def doit(self, cmp, a, b):
        if cmp == 'a = b':
            return (a == b,)
        elif cmp == 'a <> b':
            return (a != b,)
        elif cmp == 'a > b':
            return (a > b,)
        elif cmp == 'a < b':
            return (a < b,)
        elif cmp == 'a >= b':
            return (a >= b,)
        elif cmp == 'a <= b':
            return (a <= b,)
        elif cmp == 'tt':
            return (True,)
        else:
            return (False,)
```