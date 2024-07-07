# Documentation
- Class name: WAS_Boolean
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The SAS_Boolean node is the basic component of the logical operation, designed to process and return the boolean value. It plays a key role in the decision-making process of the workflow, ensuring that the next steps are carried out in accordance with the results of the logical conditions.

# Input types
## Required
- boolean_number
    - The parameter 'boolean_number' is essential for determining the boolean result. It influences the execution of the node by providing a value rounded to the nearest integer, thus defining the boolean state.
    - Comfy dtype: FLOAT
    - Python dtype: Union[float, int]

# Output types
- result
    - The'reult' output represents the derived boolean value from the input. It is important because it determines the process of subsequent operation according to the logical terms of the assessment.
    - Comfy dtype: INT
    - Python dtype: Tuple[int, int]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Boolean:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'boolean_number': ('FLOAT', {'default': 1, 'min': 0, 'max': 1, 'step': 1})}}
    RETURN_TYPES = ('NUMBER', 'INT')
    FUNCTION = 'return_boolean'
    CATEGORY = 'WAS Suite/Logic'

    def return_boolean(self, boolean_number=True):
        return (int(round(boolean_number)), int(round(boolean_number)))
```