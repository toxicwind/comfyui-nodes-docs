# Documentation
- Class name: PromptSimplification
- Category: ♾️Mixlab/Prompt
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node streamlines the hint by reducing the number of words to a specified length, ensuring the brevity and relevance of the input for follow-up.

# Input types
## Required
- prompt
    - The input hint is the basis for node operations and its contents directly affect the simplification process.
    - Comfy dtype: STRING
    - Python dtype: str
- length
    - This parameter determines the desired length of words required to simplify the hint, thereby controlling the simplicity of the output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- prompts
    - Output shows a refined version of the input hint to remove redundant words to meet the specified length.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptSimplification:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'default': '', 'dynamicPrompts': False}), 'length': ('INT', {'default': 5, 'min': 1, 'max': 100, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompts',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True

    def run(self, prompt, length):
        length = length[0]
        result = []
        for p in prompt:
            nps = prompt_delete_words(p, length)
            for n in nps:
                result.append(n)
        result = [elem.strip() for elem in result if elem.strip()]
        return {'ui': {'prompts': result}, 'result': (result,)}
```