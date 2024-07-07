# Documentation
- Class name: PromptBuilder
- Category: InspirePack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

PromptBuilder nodes are designed to construct and operate tips easily for various applications. It processes input text according to predefined configurations or user-defined parameters, and produces refined tips.

# Input types
## Required
- category
    - The 'category'parameter is essential because it determines the preset categories available to the reminder builder. It affects the range of options that can be used to build the hint, and thus influences the final output.
    - Comfy dtype: COMBO[category]
    - Python dtype: List[str]
- text
    - The `text' parameter is PromptBuilder's main input. It is the original material that will be processed and shaped according to the specified configuration and will have a significant impact on the results of the operation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output
    - 'output'represents the last-processed hint from PromptBuilder operations. It contains conversions and refinements applied to input text, reflecting the core function of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptBuilder:

    @classmethod
    def INPUT_TYPES(s):
        global prompt_builder_preset
        presets = ['#PRESET']
        return {'required': {'category': (list(prompt_builder_preset.keys()) + ['#PLACEHOLDER'],), 'preset': (presets,), 'text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'

    def doit(self, **kwargs):
        return (kwargs['text'],)
```