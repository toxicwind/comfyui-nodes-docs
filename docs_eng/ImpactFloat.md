# Documentation
- Class name: ImpactFloat
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactFloat node is used as a basic processing module to operate floating point numbers. It is designed to process value input in a precise manner to ensure that node calculations are robust and reliable, which is essential for mathematical operations and data analysis in the ImpactPack package.

# Input types
## Required
- value
    - The parameter 'value' is a floating number on which the node operates. It is essential for the function of the node, because it directly affects the results of the 'doit' method. The parameter is essential for the mathematical calculation to be performed, and it must be provided for the proper execution of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The output of the 'doit' method is a floating number, which is the result of the input 'value' process. This output is important because it represents the result of node calculations and can be used for further analysis or as input for subsequent nodes in the workflow.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactFloat:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('FLOAT', {'default': 1.0, 'min': -3.402823466e+38, 'max': 3.402823466e+38})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('FLOAT',)

    def doit(self, value):
        return (value,)
```