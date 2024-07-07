# Documentation
- Class name: PromptSlide
- Category: ♾️Mixlab/Prompt
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The PromptSlide node is designed to adjust the impact of the given hint keyword by applying the weight factor. This process allows fine-tuning of the hint to enhance the relevance and emphasis of particular keywords in the text. The primary function of the node is to modify the input node to better accommodate the desired output without changing its basic meaning or context.

# Input types
## Required
- prompt_keyword
    - Prompt_keyword parameters are essential because they define the core text around which the node function revolves. They are the basis for weighting adjustments to ensure that the results are consistent with the expected emphasis and focus.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- weight
    - The weight parameter plays a key role in determining the level of emphasis to be applied to prompt_keyword. It changes the impact of the keywords to allow for fine control of output according to the expected level of importance.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- prompt
    - The output parameter 'prompt' is the result of a node operation that reflects a hint of a post-weight adjustment. It is the key element because it conveys the final form of the reminder, which directly influences the follow-up process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptSlide:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_keyword': ('STRING', {'multiline': False, 'default': '', 'dynamicPrompts': False}), 'weight': ('FLOAT', {'default': 1, 'min': -3, 'max': 3, 'step': 0.01, 'display': 'slider'})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)
    OUTPUT_NODE = False

    def run(self, prompt_keyword, weight):
        p = addWeight(prompt_keyword, weight)
        return (p,)
```