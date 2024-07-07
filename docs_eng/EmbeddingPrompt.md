# Documentation
- Class name: EmbeddingPrompt
- Category: ♾️Mixlab/Prompt
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node class is based on embedded and associated weight generation tips, which enable the user to adjust the effects of particular embedding in the output.

# Input types
## Required
- embedding
    - Embedding parameters are essential because it defines the context or theme on which the hint is generated. It selects from the list that can be embedded to ensure that the hint is relevant to the selected context.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- weight
    - The weight parameter adjusts the effect of the selected embedding on the final hint, allowing for fine control of the output to emphasize the embedding of the context.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- prompt
    - The output hint is a string that integrates the selected embedded and its weight, forming a concise and targeted statement that can be inputted for various applications.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class EmbeddingPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'embedding': (get_files_with_extension(embeddings_path, '.pt'),), 'weight': ('FLOAT', {'default': 1, 'min': -2, 'max': 2, 'step': 0.01, 'display': 'slider'})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'
    OUTPUT_IS_LIST = (False,)

    def run(self, embedding, weight):
        weight = round(weight, 3)
        prompt = 'embedding:' + embedding
        if weight != 1:
            prompt = '(' + prompt + ':' + str(weight) + ')'
        prompt = ' ' + prompt + ' '
        return (prompt,)
```