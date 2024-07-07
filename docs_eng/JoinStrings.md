# Documentation
- Class name: JoinStrings
- Category: KJNodes/constants
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The Join Strings node is designed to merge two input strings into a single string. It does this by inserting a given separator between two strings, effectively combining them into a coherent character series. This node plays a key role in the operation of string tasks that require the consolidation of multiple strings into one, such as data formatting or further processing.

# Input types
## Required
- string1
    - The first string that you want to connect. It is essential to determine the outcome of the connection process as the initial part of the ultimate connection string.
    - Comfy dtype: STRING
    - Python dtype: str
- string2
    - The second string that you want to connect. It contributes to the overall structure of the output by following the first string and separator in the final connection string.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- delimiter
    - The character or character series between the two input strings will be inserted. The separator plays an important role in defining the reading of the final string and can be adjusted to the specific requirements of the task at hand.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- joined_string
    - The output of the Join Strings node is a post-connection string that links two input strings to the specified separator. This output is important because it represents the final product of the node operation and is ready for follow-up tasks or processes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class JoinStrings:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'string1': ('STRING', {'default': '', 'forceInput': True}), 'string2': ('STRING', {'default': '', 'forceInput': True}), 'delimiter': ('STRING', {'default': ' ', 'multiline': False})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'joinstring'
    CATEGORY = 'KJNodes/constants'

    def joinstring(self, string1, string2, delimiter):
        joined_string = string1 + delimiter + string2
        return (joined_string,)
```