# Documentation
- Class name: StringConstantMultiline
- Category: KJNodes/constants
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The `StringConstantMultiline'node is designed to process and operate multi-line strings. It provides the function of converting multi-line input into a single string and selectively strips a line break to create a continuous text block. This node is particularly suitable for tasks that need to be further processed or displayed for clean, formatted text.

# Input types
## Required
- string
    - The String parameter is the main input of the node, which is expected to have a multiline string. It plays a key role in the operation of the node, as it is the text to be processed. The ability of the node to process the multiline input is important for applications that require multiline text operations.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- strip_newlines
    - The'strip_newlines'parameter is an optional boolean sign to determine whether line breaks should be removed from the input string. When set to True, it ensures that the output is a single consecutive text block without line breaks, which is important for some text-processing tasks.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- new_string
    - The " new_string " output is a processing version of the input string, which may delete line breaks according to the'strip_newlines'parameter. This output is important because it represents the final formatted text that can be used for follow-up operations or analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StringConstantMultiline:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'string': ('STRING', {'default': '', 'multiline': True}), 'strip_newlines': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'stringify'
    CATEGORY = 'KJNodes/constants'

    def stringify(self, string, strip_newlines):
        new_string = []
        for line in io.StringIO(string):
            if not line.strip().startswith('\n') and strip_newlines:
                line = line.replace('\n', '')
            new_string.append(line)
        new_string = '\n'.join(new_string)
        return (new_string,)
```