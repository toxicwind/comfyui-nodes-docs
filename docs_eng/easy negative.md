# Documentation
- Class name: negativePrompt
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The negativPrompt node is designed to manage and process negative hints within the system. It plays a key role in refining output by removing elements or features that are not needed. The function of the node is centred on the negation concept, and by actively designating what should be avoided, it aims to improve the accuracy and relevance of the results.

# Input types
## Required
- negative
    - The `negative' parameter is essential for defining which aspects should be omitted from the final output. It allows users to specify the elements they wish to exclude, thereby guiding the system to produce more targeted and refined results.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- negative
    - Output ‘negative’ represents a processed negative hint that has already been used for the output of the refining system. It marks the successful application of the user-defined exclusions to ensure that the end result meets the required criteria.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class negativePrompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'negative': ('STRING', {'default': '', 'multiline': True, 'placeholder': 'Negative'})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('negative',)
    FUNCTION = 'main'
    CATEGORY = 'EasyUse/Prompt'

    @staticmethod
    def main(negative):
        return (negative,)
```