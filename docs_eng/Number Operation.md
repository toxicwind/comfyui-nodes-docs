# Documentation
- Class name: WAS_Number_Operation
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Number_Organization node is designed to perform multiple mathematical calculations for two input numbers. It supports additions, subtractions, divides, etc., and provides a multifunctional tool for numerical calculations.

# Input types
## Required
- number_a
    - The first number of operations for mathematical operations can be integer or floating points. It plays a key role in determining the results of the calculations.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
- number_b
    - The second operation of a mathematical operation is also an integer or floating point number. It is essential for the calculation and influences the final result.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
## Optional
- operation
    - Specifies the type of mathematical operation that you want to perform. The choice of operation directly affects the calculation and result type.
    - Comfy dtype: COMBO['addition', 'subtraction', 'division', 'floor division', 'multiplication', 'exponentiation', 'modulus', 'greater-than', 'greater-than or equals', 'less-than', 'less-than or equals', 'equals', 'does not equal']
    - Python dtype: str

# Output types
- result
    - The result of a mathematical operation can be a number, a floating point value or an integer, depending on the operation performed.
    - Comfy dtype: COMBO[NUMBER, FLOAT, INT]
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_Operation:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number_a': ('NUMBER',), 'number_b': ('NUMBER',), 'operation': (['addition', 'subtraction', 'division', 'floor division', 'multiplication', 'exponentiation', 'modulus', 'greater-than', 'greater-than or equals', 'less-than', 'less-than or equals', 'equals', 'does not equal'],)}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    FUNCTION = 'math_operations'
    CATEGORY = 'WAS Suite/Number/Operations'

    def math_operations(self, number_a, number_b, operation='addition'):
        if operation:
            if operation == 'addition':
                result = number_a + number_b
                return (result, result, int(result))
            elif operation == 'subtraction':
                result = number_a - number_b
                return (result, result, int(result))
            elif operation == 'division':
                result = number_a / number_b
                return (result, result, int(result))
            elif operation == 'floor division':
                result = number_a // number_b
                return (result, result, int(result))
            elif operation == 'multiplication':
                result = number_a * number_b
                return (result, result, int(result))
            elif operation == 'exponentiation':
                result = number_a ** number_b
                return (result, result, int(result))
            elif operation == 'modulus':
                result = number_a % number_b
                return (result, result, int(result))
            elif operation == 'greater-than':
                result = +(number_a > number_b)
                return (result, result, int(result))
            elif operation == 'greater-than or equals':
                result = +(number_a >= number_b)
                return (result, result, int(result))
            elif operation == 'less-than':
                result = +(number_a < number_b)
                return (result, result, int(result))
            elif operation == 'less-than or equals':
                result = +(number_a <= number_b)
                return (result, result, int(result))
            elif operation == 'equals':
                result = +(number_a == number_b)
                return (result, result, int(result))
            elif operation == 'does not equal':
                result = +(number_a != number_b)
                return (result, result, int(result))
            else:
                cstr('Invalid number operation selected.').error.print()
                return (number_a, number_a, int(number_a))
```