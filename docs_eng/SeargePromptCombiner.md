# Documentation
- Class name: SeargePromptCombiner
- Category: Searge/_deprecated_/Prompting
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the connection between the two text alerts and enhances the subsequent processing of input data by aligning them to the required format.

# Input types
## Required
- prompt1
    - The first text hint is the initial input of the grouping process.
    - Comfy dtype: STRING
    - Python dtype: str
- separator
    - The string is used to distinguish between the two hints and to ensure that they are structured in a way.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt2
    - The second text tip, which will be linked to the first tip, helps to form the final combination tip.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- combined prompt
    - The final hint after two input combinations is prepared for further processing.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePromptCombiner:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt1': ('STRING', {'default': '', 'multiline': True}), 'separator': ('STRING', {'default': ', ', 'multiline': False}), 'prompt2': ('STRING', {'default': '', 'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('combined prompt',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Prompting'

    def get_value(self, prompt1, separator, prompt2):
        len1 = len(prompt1)
        len2 = len(prompt2)
        prompt = ''
        if len1 > 0 and len2 > 0:
            prompt = prompt1 + separator + prompt2
        elif len1 > 0:
            prompt = prompt1
        elif len2 > 0:
            prompt = prompt2
        return (prompt,)
```