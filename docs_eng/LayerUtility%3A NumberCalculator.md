# Documentation
- Class name: NumberCalculator
- Category: 😺dzNodes/LayerUtility/Data
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Boolean calculations of two values and output results*. Supported calculations include =, =, =, =, =, =, and, or, xor, not, min, max.

* Enter only booleans, integers and floats, and forcing access to other data results in errors.

# Input types
## Required

- a
    - Enter the value a.
    - Comfy dtype: BOOLEAN, INT, FLOAT
    - Python dtype: bool, int, float

- b
    - Enter the value b.
    - Comfy dtype: BOOLEAN, INT, FLOAT
    - Python dtype: bool, int, float

- operator
    - Operator.
    - Comfy dtype: STRING
    - Python dtype: str
    - Optional value: "=", "", "and", "or", "xor", "not(a)", "min", "max"

# Output types

- output
    - Calculating results.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class NumberCalculator:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(self):
        operator_list = ["+", "-", "*", "/", "**", "//", "%" ]
        return {"required": {
                "a": (any, {}),
                "b": (any, {}),
                "operator": (operator_list,),
            },}

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("int", "float",)
    FUNCTION = 'number_calculator_node'
    CATEGORY = '😺dzNodes/LayerUtility/Data'

    def number_calculator_node(self, a, b, operator):
        ret_value = 0
        if operator == "+":
            ret_value = a + b
        if operator == "-":
            ret_value = a - b
        if operator == "*":
            ret_value = a * b
        if operator == "/":
            ret_value = a / b
        if operator == "**":
            ret_value = a ** b
        if operator == "//":
            ret_value = a // b
        if operator == "%":
            ret_value = a % b

        return (int(ret_value), float(ret_value),)
```