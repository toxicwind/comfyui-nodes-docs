# Documentation
- Class name: BooleanOperator
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

# Output types

- output
    - Calculating results.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```

class BooleanOperator:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(self):
        operator_list = ["==", "!=", "and", "or", "xor", "not(a)", "min", "max"]
        return {"required": {
                "a": (any, {}),
                "b": (any, {}),
                "operator": (operator_list,),
            },}

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("output",)
    FUNCTION = 'bool_operator_node'
    CATEGORY = '😺dzNodes/LayerUtility/Data'

    def bool_operator_node(self, a, b, operator):
        ret_value = False
        if operator == "==":
            ret_value = a == b
        if operator == "!=":
            ret_value = a != b
        if operator == "and":
            ret_value = a and b
        if operator == "or":
            ret_value = a or b
        if operator == "xor":
            ret_value = not(a == b)
        if operator == "not(a)":
            ret_value = not a
        if operator == "min":
            ret_value = a or b
        if operator == "max":
            ret_value = a and b

        return (ret_value,)

```