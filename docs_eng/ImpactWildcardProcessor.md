# Documentation
- Class name: ImpactWildcardProcessor
- Category: ImpactPack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Impact WildcardProcessor node is designed to manage and process wildcards in text input. It promotes dynamic insertion or filling of wildcards based on a given model, which enhances the flexibility of text-handling tasks. The node plays a key role in the production of tips that can be adapted to various types of input using the wildcard concept.

# Input types
## Required
- wildcard_text
    - The wildcard text parameter is essential for defining placeholders in the text, which can be filled dynamically. It affects the structure of the final output text and allows custom tips to be tailored to specific needs.
    - Comfy dtype: STRING
    - Python dtype: str
- populated_text
    - Filled text as an initial input to text that may contain wildcards. This parameter is important because it determines the underlying text that will be treated with wildcards and affects the result of the wildcard processing text.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- mode
    - Model parameters determine whether a wildcard should be filled or kept fixed. It is important because it controls the behaviour processed by wildcards and allows dynamic content to generate or retain static text.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- seed
    - Seed parameters are used to initialize random number generators to ensure that the results are repeated when processing wildcards. They play an important role in maintaining consistency in multiple nodes, especially for debugging and testing purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- processed_text
    - The processed text is the main output of the Impact WildcardProcessor node, representing the final text after all wildcards have been properly filled or maintained under the specified mode.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactWildcardProcessor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'wildcard_text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'populated_text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'Populate', 'label_off': 'Fixed'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],)}}
    CATEGORY = 'ImpactPack/Prompt'
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'doit'

    @staticmethod
    def process(**kwargs):
        return impact.wildcards.process(**kwargs)

    def doit(self, *args, **kwargs):
        populated_text = kwargs['populated_text']
        return (populated_text,)
```