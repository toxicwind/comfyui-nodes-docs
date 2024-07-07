# Documentation
- Class name: CR_MultiplyIndex
- Category: Comfyroll/Utils/Index
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_MultipullyIndex is designed to multiply index values and calculate them by the given factor. This is a practical tool node that enhances the functionality of indexing in workflows and provides a direct way to expand or adjust index values as needed.

# Input types
## Required
- index
    - The `index' parameter is the base that will be multiplied by `factor'. It plays a key role in determining the final output of the node, as it is the starting point for the multiplication operation.
    - Comfy dtype: INT
    - Python dtype: int
- factor
    - The `factor' parameter is the multiplier that will be applied to `index'. It is essential for the operation of the node, as it determines the extent to which the multiplier will affect the index value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- index
    - The `index' output represents the result of a multiply operation between `index' and `factor'. It represents a new scaling index value after the multiplication process.
    - Comfy dtype: INT
    - Python dtype: int
- factor
    - The 'factor'output is the multiplier used in the multiplying operation. It is included in the output to maintain consistency with input parameters and to provide transparency in the execution operation.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The ‘show_help’ output provides a URL link to a document to obtain additional guidance or help on the use of nodes. This is a useful resource for users seeking more information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_MultiplyIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 1, 'min': 0, 'max': 10000, 'forceInput': True}), 'factor': ('INT', {'default': 1, 'min': 0, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'INT', 'STRING')
    RETURN_NAMES = ('index', 'factor', 'show_help')
    FUNCTION = 'multiply'
    CATEGORY = icons.get('Comfyroll/Utils/Index')

    def multiply(self, index, factor):
        index = index * factor
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Index-Nodes#cr-index-multiply'
        return (index, factor, show_help)
```