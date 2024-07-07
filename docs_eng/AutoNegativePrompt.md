# Documentation
- Class name: AutoNegativePrompt
- Category: OneButtonPrompt
- Output node: False
- Repo Ref: https://github.com/AIrjen/OneButtonPrompt

The node is designed to automatically generate negative hints based on a given positive hint, which enhances the contrast between the two. It creatively changes the text by replacing the positive emotions in the input text with negative ones, with a view to providing a clear contrast or antagonism. The function of the node is not limited to direct text reversals, but also includes the use of predefined lists of negative attributes to enhance the ability of negative emotions.

# Input types
## Required
- postive_prompt
    - A positive hint is the basis of a node operation. It is a text that will be converted into a negative relativity. This parameter is essential because it determines the context and subject matter in which the negative node is generated.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- base_negative
    - This parameter provides a default negative hint to be used as a starting point for the conversion process. It is important to create an initial negative context where nodes can be further refined and enhanced.
    - Comfy dtype: STRING
    - Python dtype: str
- enhancenegative
    - This parameter control is applied to the enhancement level of the negative hint to strengthen the negative properties and make the comparison with the positive hint more visible. It affects the overall tone and severity of the negative hint generated.
    - Comfy dtype: INT
    - Python dtype: int
- insanitylevel
    - Crazy grade parameters introduce random elements in the conversion process, simulate more confusing or unpredictable negative hints. It affects the diversity and creativity of negative terms contained in the final output.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters ensure the repeatability of results by setting a fixed point for a random number generator. It is essential to maintain the consistency of node operations, especially when multiple operations are required to be tested or compared.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- negative_prompt
    - The output of the node is a refined negative hint in contrast to the original front. It encapsulates the essence of the conversion process and provides creative and subtle negative emotional expression.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class AutoNegativePrompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'postive_prompt': ('STRING', {'default': '', 'multiline': True})}, 'optional': {'base_negative': ('STRING', {'multiline': True, 'default': 'text, watermark'}), 'enhancenegative': ('INT', {'default': 0, 'min': 0, 'max': 1, 'step': 1}), 'insanitylevel': ('INT', {'default': 0, 'min': 0, 'max': 10, 'step': 1}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('negative_prompt',)
    FUNCTION = 'Comfy_OBP_AutoNegativePrompt'
    CATEGORY = 'OneButtonPrompt'

    def Comfy_OBP_AutoNegativePrompt(self, postive_prompt, insanitylevel, enhancenegative, base_negative, seed):
        generatedprompt = build_dynamic_negative(postive_prompt, insanitylevel, enhancenegative, base_negative)
        print('Generated negative prompt: ' + generatedprompt)
        return (generatedprompt,)
```