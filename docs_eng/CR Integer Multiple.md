# Documentation
- Class name: CR_IntegerMultipleOf
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_IntegerMulpleof is a node designed to multiply the integer by a specified multiplier to ensure that the result is a multiple of the integer of the given factor. This node is particularly useful in cases where there is a need for consistent increment or scaling factors, such as in mathematical calculations or data-processing tasks. It contributes to the workflow by providing a simple and efficient way of operating the integer number on the basis of predefined multipliers.

# Input types
## Required
- integer
    - The `integer' parameter is multiplied by the base of the `multiple' parameter. It plays a fundamental role in the operation of the node, as it determines the starting point of the multiplication process. The execution and results of the node are directly influenced by the value of the parameter.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- multiple
    - The `multiple' parameter defines the factor by which `integer' will be multiplied. It is important because it determines the scale of the base integer. The outcome of the node depends heavily on this parameter, which allows control of the required level of increment in the calculation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- INT
    - The `INT' output is the result of an integer multiplied by the specified multiplier. It is the main output of the node, reflecting the core function of the integer multiplier based on the given factor.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The ‘show_help’ output provides a URL link to the node document, providing additional information and guidance to users on how to use the node effectively. It enhances user experience by providing easily accessible help resources.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IntegerMultipleOf:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'integer': ('INT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'multiple': ('FLOAT', {'default': 8, 'min': 1, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'int_multiple_of'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def int_multiple_of(self, integer, multiple=8):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-integer-multiple'
        if multiple == 0:
            return (int(integer), show_help)
        integer = integer * multiple
        return (int(integer), show_help)
```