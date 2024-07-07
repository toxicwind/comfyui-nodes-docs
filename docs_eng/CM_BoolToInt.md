# Documentation
- Class name: BoolToInt
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

BoolToInt nodes are designed to convert the boolean value to its integer equivalent.

# Input types
## Required
- a
    - The 'a' parameter is the boolean input expected from the node. It is essential for the conversion process, because the node is intended to convert the boolean value to an integer. The entered boolean properties directly affect the output integer value, with the 'True' map to 1,'False' map to zero.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Output types
- op
    - The 'op' output provides an integer conversion to enter a boolean value. It is important because it represents the direct result of node operations and summarizes the essence of the transformation process from Boolean to Integer.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class BoolToInt:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('BOOL', {'default': False})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: bool) -> tuple[int]:
        return (int(a),)
```