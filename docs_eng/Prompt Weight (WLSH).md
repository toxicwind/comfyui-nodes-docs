# Documentation
- Class name: WLSH_Prompt_Weight
- Category: WLSH Nodes/text
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node aims to fine-tune the output of the generation model by applying weights to adjust the impact of the hint. It allows users to highlight or reduce certain hints in a set of hints, thereby controlling the overall direction in which the content is generated.

# Input types
## Required
- prompt
    - The hint is the text input that guides the production of model output. It is essential because it sets the context and theme for the content generated.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- weight
    - The effect of the weight parameter adjustment hint is allowed to micro-control the model response. It affects the visibility of the hint in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- prompt
    - A modified hint with the application weight can be used as a follow-on node or model input and is now carrying the adjusted effect.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Prompt_Weight:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'forceInput': True}), 'weight': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 5.0, 'step': 0.1})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'add_weight'
    CATEGORY = 'WLSH Nodes/text'

    def add_weight(self, prompt, weight):
        if weight == 1.0:
            new_string = prompt
        else:
            new_string = '(' + prompt + ':' + str(weight) + ')'
        return (new_string,)
```