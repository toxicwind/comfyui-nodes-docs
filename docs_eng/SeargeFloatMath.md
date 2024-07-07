# Documentation
- Class name: SeargeFloatMath
- Category: Searge/_deprecated_/Floats
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeFloatMath node is designed to perform basic arithmetic calculations of floating points. It provides a range of operations, such as multiplying, adding, subtracting, dividing, and multiplying and adding. The objective of the node is to provide a direct means of implementing these basic mathematical functions, thereby promoting the manipulation of floating point values in a broader computational environment.

# Input types
## Required
- op
    - The parameter 'op' determines the arithmetic operation to be performed. It is vital because it directs the mathematical program that the node will execute, thereby influencing the result of the calculation.
    - Comfy dtype: STRING
    - Python dtype: str
- a
    - The parameter 'a' represents a number of operations for arithmetic operations. Its value significantly influences the end result and makes it an important part of the node function.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b
    - The parameter 'b' is used as one of the operations for which two inputs are required (e.g. by multiplying or dividing). Its existence depends on the operation chosen, but it plays a vital role in the calculation when needed.
    - Comfy dtype: FLOAT
    - Python dtype: float
- c
    - The parameter 'c' is another operating number, which is involved in particular arithmetic operations, such as additions or subtractions. When necessary, it contributes to the final calculation, highlighting its importance in some cases.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The output'reult' provides the results of the arithmetic operations performed by the node. It is a direct reflection of the input parameters and the selected operation and outlines the purpose of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeFloatMath:
    OPERATIONS = ['a * b + c', 'a + c', 'a - c', 'a * b', 'a / b']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'op': (SeargeFloatMath.OPERATIONS, {'default': 'a * b + c'}), 'a': ('FLOAT', {'default': 0.0, 'step': 0.01}), 'b': ('FLOAT', {'default': 1.0, 'step': 0.01}), 'c': ('FLOAT', {'default': 0.0, 'step': 0.01})}}
    RETURN_TYPES = ('FLOAT',)
    RETURN_NAMES = ('result',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Floats'

    def get_value(self, op, a, b, c):
        res = 0.0
        if op == 'a * b + c':
            res = a * b + c
        elif op == 'a + c':
            res = a + c
        elif op == 'a - c':
            res = a - c
        elif op == 'a * b':
            res = a * b
        elif op == 'a / b':
            res = a / b
        return (res,)
```