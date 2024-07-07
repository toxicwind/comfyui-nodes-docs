# Documentation
- Class name: TESTNODE_TOKEN
- Category: ♾️Mixlab/__TEST
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node uses the clip model to process text input and converts the text into a structured expression for further use in various applications.

# Input types
## Required
- text
    - Text input is essential for the node to perform its tagging function. It is the raw material for extraction and construction of the mark.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- clip
    - The clip model is an optional input that allows nodes to tag text more effectively, using the model's understanding of the language structure.
    - Comfy dtype: CLIP
    - Python dtype: module

# Output types
- tokens
    - Output is a JSON string that represents a text-marking structure. It is a key component for further analysis and processing in downstream tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TESTNODE_TOKEN:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'forceInput': True}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/__TEST'
    OUTPUT_NODE = True
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, text, clip=None):
        tokens = clip.tokenize(text)
        tokens = [v for v in tokens.values()][0][0]
        tokens = json.dumps(tokens)
        return (tokens,)
```