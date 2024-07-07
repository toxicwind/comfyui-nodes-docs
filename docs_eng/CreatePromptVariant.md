# Documentation
- Class name: CreatePromptVariant
- Category: OneButtonPrompt
- Output node: False
- Repo Ref: https://github.com/AIrjen/OneButtonPrompt

The CreativePromptVariant node is designed to generate a diverse and creative texttip based on user input and additional parameters. It operates and combines elements, such as objects, roles and scenes, to build unique and attractive texttips that apply to the wider application of content creation and creative creation.

# Input types
## Required
- prompt_input
    - The input hint is the basis of the node operation and provides the context and theme for generating the content. It is essential for setting the initial direction and scope for generating the content.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- insanitylevel
    - Crazy grade parameter controls apply to changes in input tips and creativity. Higher levels produce more diverse and possibly non-conventional outputs, introducing broader ideas and possibilities.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters are used to ensure the replicability of node output. By specifying a torrent, users can produce consistent results in different operations, which is very useful for testing and debugging.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- prompt
    - The output is a version of the original hint that is modified and enhanced on the basis of input parameters. It contains elements and adjustments that represent new creative directions that can stimulate further development and exploration.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CreatePromptVariant:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_input': ('STRING', {'default': '', 'multiline': True})}, 'optional': {'insanitylevel': ('INT', {'default': 5, 'min': 1, 'max': 10, 'step': 1}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'Comfy_OBP_PromptVariant'
    CATEGORY = 'OneButtonPrompt'

    def Comfy_OBP_PromptVariant(self, prompt_input, insanitylevel, seed):
        generatedprompt = createpromptvariant(prompt_input, insanitylevel)
        print(generatedprompt)
        return (generatedprompt,)
```