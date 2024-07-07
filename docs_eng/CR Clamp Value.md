# Documentation
- Class name: CR_ClampValue
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ClampValue node is designed to ensure that a given value is kept within the specified range. It ensures that output remains within the acceptable limits defined by the user by limiting the input value 'a' to "range_min' and 'range_max'. This function is essential for maintaining numerical stability and preventing extreme values that may lead to errors or unintended behaviors in subsequent operations.

# Input types
## Required
- a
    - The parameter 'a' indicates the value to be restricted. This is a key input, because the primary function of the node is to ensure that the value is subject to the specified range limit. The operation of the node is directly influenced by the size of the node, making it a central component of the limitation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- range_min
    - The parameter'range_min' defines the lower limit of the acceptable range of the input value'a'. It plays an important role in limiting operations because it sets the minimum limit that'a' can achieve. This parameter is essential to prevent output from falling below the desired threshold.
    - Comfy dtype: FLOAT
    - Python dtype: float
- range_max
    - The parameter'range_max' sets the upper limit of the input value 'a' in the restriction operation. It is vital because it determines the maximum value that'a' can take, thus preventing output from exceeding the set limit and controlling the outcome of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- a
    - The output 'a' is a restricted value, which has been adjusted to fall within the specified range. It is a direct result of the node limitation function, representing the value of 'a' after being restricted by 'range_min' and 'range_max'. This output is important because it is the main result of node operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Output'show_help' provides a URL link to a document to obtain further help or information about node use. It is a useful resource for users who may need additional guidance to use node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ClampValue:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'a': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'range_min': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'range_max': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('FLOAT', 'STRING')
    RETURN_NAMES = ('a', 'show_help')
    FUNCTION = 'clamp_value'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def clamp_value(self, a, range_min, range_max):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-clamp-value'
        a = max(range_min, min(a, range_max))
        return (a, show_help)
```