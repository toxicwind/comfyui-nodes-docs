# Documentation
- Class name: WAS_Text_to_Conditioning
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_to_Conditioning node is designed to convert text input into a condition format that can be used to generate a model. It uses the ability of the text encoder to process text and creates a condition signal that can guide the generation process. The node abstractes the complexity of text encoding and provides a simple interface for users to integrate text elements into their workflows.

# Input types
## Required
- clip
    - The `clip' parameter is essential to the process of text-to-condition, as it represents the context information to which the text will relate. This parameter is essential for the implementation of nodes, as it forms the basis for the coding process.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.sd.CLIP]
- text
    - The `text' parameter is a mandatory input that provides text content that is to be encoded as a condition format. It is important because it directly affects the conditions of output, which is used to guide the generation process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- encoded_conditioning
    - `encoded_conventioning' output is a processed version of the input text, which is converted into a format suitable for the conditions to produce a model. It encapsulates the semantic content of the text in a way that the model can be used to produce the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_to_Conditioning:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'clip': ('CLIP',), 'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'text_to_conditioning'
    CATEGORY = 'WAS Suite/Text/Operations'

    def text_to_conditioning(self, clip, text):
        encoder = nodes.CLIPTextEncode()
        encoded = encoder.encode(clip=clip, text=text)
        return (encoded[0], {'ui': {'string': text}})
```