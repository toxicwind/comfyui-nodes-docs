# Documentation
- Class name: ImpactInt
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactInt node is designed to perform a basic logical operation. It is designed to receive an integer input and returns the same integer value as the basic transmission function in the ImpactPack package. This node is essential in a scenario where the data integrity of the input must be maintained, ensuring that the flow of information remains constant during the calculation process.

# Input types
## Required
- value
    - The `value' parameter is an integral part of the ImpactInt operation. It is the only input required for the node and is essential for the node to perform its transfer function. The ability of the node to maintain the input integrity depends on the correct provision of this parameter, highlighting its important role in the function of the node as a whole.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The `resource' output parameter of the ImpactInt node is a direct reflection of the input `value'. It marks the successful execution and maintenance of the integrity of the input data. The output is important because it provides a reliable and unmodified version of the integer input that ensures continuity and accuracy in the computational workflow for subsequent operations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactInt:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('INT',)

    def doit(self, value):
        return (value,)
```