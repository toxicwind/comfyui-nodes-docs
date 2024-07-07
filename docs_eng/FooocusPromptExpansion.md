# Documentation
- Class name: FooocusPromptExpansion
- Category: prompt
- Output node: True
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The node is intended to expand and generate new text based on input text and seed values, and the seed value introduces randomity to enhance diversity and creativity in generating content, while maintaining a certain degree of controlability through seed values.

# Input types
## Required
- text
    - Text parameters are the source material of the node extension process. It is essential because it provides context and basis for the generation of new content.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seed
    - Seed parameters introduce randomity for text extension processes, allowing for diversified output from the same input text.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The result parameters contain the expanded text, which is the output of the node text extension process.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class FooocusPromptExpansion:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'main'
    CATEGORY = 'prompt'
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True

    @staticmethod
    def scale_seed(seed):
        return seed % (2 ** 32 - 1)

    def main(self, text, seed):
        seed = FooocusPromptExpansion.scale_seed(seed)
        res = do_expansion(text, seed)
        logger.info(f'[FooocusPromptExpansion] (seed={seed}) expand |{text}| to |{res}|')
        return {'ui': {'result': [res]}, 'result': ([res],)}
```