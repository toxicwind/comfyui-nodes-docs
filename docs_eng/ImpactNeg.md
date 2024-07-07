# Documentation
- Class name: ImpactNeg
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactNeg node is designed to reverse the logical state of the boolean input. It is the basic building block in the logical operation, providing direct but vital functionality in the ImpactPack package. The function of this node is to ensure that the output is the opposite of the input, contributing to a broader logical framework by providing a negative condition.

# Input types
## Required
- value
    - The 'value'parameter is a core component of the ImpactNeg node function. It represents the boolean condition that node is about to deny. The significance of this parameter is that it directly influences the output of node, because the result depends entirely on the logical state of the input value.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - The `redult' parameter is the result of the ImpactNeg operation. It is the logical non-bullet value for `value'. This output is important because it directly reflects the negative purpose of the node and provides a clear and concise Boolean result for the further use of logical expressions or conditions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactNeg:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('BOOLEAN', {'forceInput': True})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('BOOLEAN',)

    def doit(self, value):
        return (not value,)
```