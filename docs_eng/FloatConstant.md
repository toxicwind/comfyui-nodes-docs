# Documentation
- Class name: FloatConstant
- Category: KJNodes/constants
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The FloatConstant node is designed to provide a constant floating point value in the data processing or machine learning process. It ensures that a consistent and predefined value can be used for follow-up operations and contributes to the stability and predictability of systemic performance.

# Input types
## Required
- value
    - The parameter 'value' is the core of the FloatConstant node, defining the number of specific floating points to be exported. It plays a key role in the operation of the node, as it directly affects the outcome of the node and does not need to be further calculated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- value
    - The output'value' represents the constant float number provided by the floatConstant node. It is important because it is a reliable and constant input for downstream processes in the workflow.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class FloatConstant:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('FLOAT', {'default': 0.0, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.001})}}
    RETURN_TYPES = ('FLOAT',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'get_value'
    CATEGORY = 'KJNodes/constants'

    def get_value(self, value):
        return (value,)
```