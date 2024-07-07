# Documentation
- Class name: StringConstant
- Category: KJNodes/constants
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

StringConstant node is designed to provide a fixed string value in the data processing workflow. It is used as a tool for cases where a fixed string is required to be entered as a follow-up operation and no dynamic changes are required.

# Input types
## Required
- string
    - The `string' parameter is essential to define the constant string values to be exported by the node. It plays a key role in the operation of the node, as it directly determines the data to be transmitted to the downstream process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output
    - The 'output'parameter represents the string value returned by the node. It is important because it is the only output of the node and ensures that the string provided is correctly used in the next step of the workflow.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StringConstant:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'string': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'passtring'
    CATEGORY = 'KJNodes/constants'

    def passtring(self, string):
        return (string,)
```