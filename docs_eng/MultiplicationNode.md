# Documentation
- Class name: MultiplicationNode
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node performs arithmetic calculations of input values, scaling and adjusting them according to the multipliers and additions provided. It emphasizes the ability to convert and process numerical data in a direct manner, providing flexible output type options.

# Input types
## Required
- numberA
    - The base value to be used for multiplying and adding operations. It plays a key role in determining the final output, as it is the subject of conversion.
    - Comfy dtype: any_type
    - Python dtype: Union[int, float, torch.Tensor]
- multiply_by
    - The multiplier applied to the base value significantly influences the size of the result. It is critical in modifying the size of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- add_by
    - Adds the value to the multiplier result and adjusts the final output. It plays a role in fine-tuning the result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- a
    - Arithmetic operations float results, representing the scaling and adjustment version of the input value.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b
    - The integer result of the arithmetic operation provides a discrete version of the conversion of the input value.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class MultiplicationNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'numberA': (any_type,), 'multiply_by': ('FLOAT', {'default': 1, 'min': -2, 'max': 18446744073709551615, 'step': 0.01, 'display': 'number'}), 'add_by': ('FLOAT', {'default': 0, 'min': -2000, 'max': 18446744073709551615, 'step': 0.01, 'display': 'number'})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False)

    def run(self, numberA, multiply_by, add_by):
        b = int(numberA * multiply_by + add_by)
        a = float(numberA * multiply_by + add_by)
        return (a, b)
```