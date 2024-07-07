# Documentation
- Class name: positivePrompt
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

Such nodes encapsulate the functions of handling and generating positive hints, with the aim of enhancing creativity and motivation to generate content. It is used as a tool for users to introduce positive language in their projects, thereby influencing the tone and mood of the output.

# Input types
## Required
- positive
    - The "positive" parameter is essential because it defines the positive messages or themes that the nodes will focus on. It directly influences the nature of the content and ensures that the output is filled with positive emotions.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- positive
    - The output `positive' represents a refined and processed positive reminder that can be used in various applications to promote optimistic and constructive communication.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class positivePrompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('STRING', {'default': '', 'multiline': True, 'placeholder': 'Positive'})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('positive',)
    FUNCTION = 'main'
    CATEGORY = 'EasyUse/Prompt'

    @staticmethod
    def main(positive):
        return (positive,)
```