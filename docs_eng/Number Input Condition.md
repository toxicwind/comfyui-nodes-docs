# Documentation
- Class name: WAS_Number_Input_Condition
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `number_input_convention'is designed to assess numerical conditions based on a set of input parameters. It performs logical calculations and comparisons to determine the results, which can be either a boolean value or a type of value, depending on the type of return specified. This node has a variety of functions that can handle various mathematical and logical calculations and applies to a wide range of numerical analysis tasks.

# Input types
## Required
- number_a
    - The first number used to compare operations. It plays a key role in determining the results of the logical conditions assessed.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
- number_b
    - A second figure for the comparison. It is essential for the logical operation of the node.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
## Optional
- return_boolean
    - Determines whether the method should return the boolean value (real or false) or the type of value based on the results of the comparison.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: str
- comparison
    - Specifies the type of logical comparison or operation that you want to perform for two numbers.
    - Comfy dtype: COMBO['and', 'or', 'greater-than', 'greater-than or equals', 'less-than', 'less-than or equals', 'equals', 'does not equal', 'divisible by', 'if A odd', 'if A even', 'if A prime', 'factor of']
    - Python dtype: str

# Output types
- result
    - The result of the logical condition assessment may be a value or a boolean value based on the'return_boolean'parameter.
    - Comfy dtype: COMBO['NUMBER', 'FLOAT', 'INT']
    - Python dtype: Union[int, float, bool]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_Input_Condition:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number_a': ('NUMBER',), 'number_b': ('NUMBER',), 'return_boolean': (['false', 'true'],), 'comparison': (['and', 'or', 'greater-than', 'greater-than or equals', 'less-than', 'less-than or equals', 'equals', 'does not equal', 'divisible by', 'if A odd', 'if A even', 'if A prime', 'factor of'],)}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    FUNCTION = 'number_input_condition'
    CATEGORY = 'WAS Suite/Logic'

    def number_input_condition(self, number_a, number_b, return_boolean='false', comparison='greater-than'):
        if comparison:
            if return_boolean == 'true':
                if comparison == 'and':
                    result = 1 if number_a != 0 and number_b != 0 else 0
                elif comparison == 'or':
                    result = 1 if number_a != 0 or number_b != 0 else 0
                elif comparison == 'greater-than':
                    result = 1 if number_a > number_b else 0
                elif comparison == 'greater-than or equals':
                    result = 1 if number_a >= number_b else 0
                elif comparison == 'less-than':
                    result = 1 if number_a < number_b else 0
                elif comparison == 'less-than or equals':
                    result = 1 if number_a <= number_b else 0
                elif comparison == 'equals':
                    result = 1 if number_a == number_b else 0
                elif comparison == 'does not equal':
                    result = 1 if number_a != number_b else 0
                elif comparison == 'divisible by':
                    result = 1 if number_b % number_a == 0 else 0
                elif comparison == 'if A odd':
                    result = 1 if number_a % 2 != 0 else 0
                elif comparison == 'if A even':
                    result = 1 if number_a % 2 == 0 else 0
                elif comparison == 'if A prime':
                    result = 1 if self.is_prime(number_a) else 0
                elif comparison == 'factor of':
                    result = 1 if number_b % number_a == 0 else 0
                else:
                    result = 0
            elif comparison == 'and':
                result = number_a if number_a != 0 and number_b != 0 else number_b
            elif comparison == 'or':
                result = number_a if number_a != 0 or number_b != 0 else number_b
            elif comparison == 'greater-than':
                result = number_a if number_a > number_b else number_b
            elif comparison == 'greater-than or equals':
                result = number_a if number_a >= number_b else number_b
            elif comparison == 'less-than':
                result = number_a if number_a < number_b else number_b
            elif comparison == 'less-than or equals':
                result = number_a if number_a <= number_b else number_b
            elif comparison == 'equals':
                result = number_a if number_a == number_b else number_b
            elif comparison == 'does not equal':
                result = number_a if number_a != number_b else number_b
            elif comparison == 'divisible by':
                result = number_a if number_b % number_a == 0 else number_b
            elif comparison == 'if A odd':
                result = number_a if number_a % 2 != 0 else number_b
            elif comparison == 'if A even':
                result = number_a if number_a % 2 == 0 else number_b
            elif comparison == 'if A prime':
                result = number_a if self.is_prime(number_a) else number_b
            elif comparison == 'factor of':
                result = number_a if number_b % number_a == 0 else number_b
            else:
                result = number_a
        return (result, float(result), int(result))

    def is_prime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
```