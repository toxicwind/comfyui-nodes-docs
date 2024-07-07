# Documentation
- Class name: ImpactConditionalBranch
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactConditionalBranch node 'doit' method is designed to implement logic on the basis of the conditions provided for booleans. It allows one of the two values to be selected on the basis of the true value of the conditions, thus facilitating the realization of the control flow in the process.

# Input types
## Required
- cond
    - The 'cond' parameter is a boolean value that determines the direction of the execution process within the 'doit' method. It is vital because it determines whether it returns 'tt_value' or 'ff_value'.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tt_value
    - The 'tt_value' parameter indicates the value to be returned if the 'cond' parameter is assessed as true. It plays an important role in the node's conditionality logic.
    - Comfy dtype: any_typ
    - Python dtype: Any
- ff_value
    - The 'ff_value' parameter is the value returned when the 'cond' parameter is false. It is essential to define alternative results in the operation of node conditions.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- result
    - The'reult' parameter is the result of the 'doit' method and will be assessed as one of 't_value' or 'ff_value' according to the 'cond' parameter.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactConditionalBranch:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'cond': ('BOOLEAN',), 'tt_value': (any_typ,), 'ff_value': (any_typ,)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = (any_typ,)

    def doit(self, cond, tt_value, ff_value):
        if cond:
            return (tt_value,)
        else:
            return (ff_value,)
```