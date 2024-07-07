# Documentation
- Class name: ImpactMinMax
- Category: ImpactPack/Logic/_for_test
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactMinmax node 'doit' method is designed to perform a basic operation, i.e. to determine the maximum or minimum value between two input values. It plays a key role in decision-making and comparison in the workflow and provides a direct but vital function.

# Input types
## Required
- mode
    - The `mode' parameter is essential for the operation of the node, because it determines whether to return the maximum or the minimum value. It directly influences the decision-making process of the node, enabling it to perform the correct comparison according to the specified model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- a
    - The `a' parameter represents the first number of operations in the comparison. It is an essential part of the node function, because the comparison between `a' and `b' determines the output. The `a' character can be very broad and allows for high flexibility in application.
    - Comfy dtype: any_typ
    - Python dtype: Any
- b
    - The `b' parameter represents the second number of operations in the comparison. Like `a', it is a key component of node operations, because the comparison between `a' and `b' produces node output. The diversity of `b' ensures that nodes can adapt to the various types of input in the comparison.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- result
    - The `redult' output provides the results of a comparison between the two inputs. It is important because it represents the final output of the node, which is based on the `mode' parameter, which is the maximum or minimum value.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactMinMax:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mode': ('BOOLEAN', {'default': True, 'label_on': 'max', 'label_off': 'min'}), 'a': (any_typ,), 'b': (any_typ,)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = ('INT',)

    def doit(self, mode, a, b):
        if mode:
            return (max(a, b),)
        else:
            return (min(a, b),)
```