# Documentation
- Class name: EvalFloats
- Category: Mikey/Math
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The EvalFloats node is designed to assess the mathematical expression provided as a string, using two floating points as variables in the formula. As a multifunctional tool, it is used to perform dynamically defined calculations, providing flexibility in mathematical calculations without the need for hard-coding expressions.

# Input types
## Required
- a
    - The parameter 'a' is a floating number that represents a variable in the mathematical formula. It is essential for defining the initial state of the calculation and directly affects the results of the evaluation expression.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b
    - The parameter 'b' is another floating point, used with 'a' in the mathematical expression. It plays an important role in the calculation because it helps to derive the final result from the formula.
    - Comfy dtype: FLOAT
    - Python dtype: float
- formula
    - The parameter 'formula' is a string containing mathematical expressions to be evaluated. It is vital because it determines the operation of input variables 'a' and 'b' and determines the nature of the calculation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result_float
    - Output'resource_float' provides a floating point result for assessing mathematical expressions. It is important because it represents a direct result of calculations based on input variables and formulae.
    - Comfy dtype: FLOAT
    - Python dtype: float
- result_int
    - The output'reult_int' is an integer of the results of the assessment. When an integer is needed from the calculation, it is useful and provides a discrete version of the result.
    - Comfy dtype: INT
    - Python dtype: int
- result_str
    - Output'reult_str' is a string for the results of the assessment. It is especially suitable for displaying the results in a human readable format or for use in the further processing of the string that is required.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class EvalFloats:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'a': ('FLOAT', {'default': 0.0}), 'b': ('FLOAT', {'default': 0.0}), 'formula': ('STRING', {'multiline': False, 'default': 'a + b'})}}
    RETURN_TYPES = ('FLOAT',)
    RETURN_NAMES = ('result_float', 'result_int', 'result_str')
    FUNCTION = 'process'
    CATEGORY = 'Mikey/Math'

    def process(self, a, b, formula):
        formula = formula.replace('a', str(a))
        formula = formula.replace('b', str(b))
        result = eval(formula)
        return (result, int(result), str(result))
```