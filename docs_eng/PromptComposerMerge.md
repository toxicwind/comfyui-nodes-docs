# Documentation
- Class name: PromptComposerMerge
- Category: AI WizArt/Prompt Composer Tools
- Output node: False
- Repo Ref: https://github.com/florestefano1975/comfyui-prompt-composer.git

The PromptComposerMrage node is designed to integrate two different texts seamlessly and consolidate them into a coherent output. It is a key tool in applications that need to combine text information from different sources into a uniform format. The node is coloured in the text consolidation process, ensuring that the resulting text remains logical and readable.

# Input types
## Required
- text_a
    - The parameter 'text_a' indicates the first text input that will be merged with another text. It plays a key role in the operation of the node, as it constitutes the initial part of the final output. The quality and content of the 'text_a' has a significant impact on the overall consistency and context of the merged text.
    - Comfy dtype: STRING
    - Python dtype: str
- text_b
    - Parameter 'text_b' is the second text input that will be associated with 'text_a '. Although not necessary, it is usually used to add additional context or information to the merged text. Inclusion of 'text_b' enhances the comprehensiveness of the final output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text_out
    - The parameter 'text_out' means the combined output entered in 'text_a'and 'text_b'. It is the final result of the node consolidation process and reflects the consolidated text information in a single, coherent format.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptComposerMerge:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_a': ('STRING', {'forceInput': True}), 'text_b': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_out',)
    FUNCTION = 'promptComposerMerge'
    CATEGORY = 'AI WizArt/Prompt Composer Tools'

    def promptComposerMerge(self, text_a='', text_b=''):
        return (text_a + ', ' + text_b,)
```