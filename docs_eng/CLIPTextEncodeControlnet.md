# Documentation
- Class name: CLIPTextEncodeControlnet
- Category: _for_testing/conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIPTextEncodeContronet node is designed to encode text input into a format that can be used to control image generation. It uses the CLIP model to understand text and convert it into a potential spatial expression that can guide the image generation process. The node is central to the application that is essential for achieving text-based guidance in image synthesis.

# Input types
## Required
- clip
    - The `clip' parameter is essential because it represents the CLIP model that will be used for text coding. It is a key component that allows nodes to convert text descriptions into forms that can influence downstream image generation tasks.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- conditioning
    - The `conventioning' parameter plays a crucial role in the operation of the node, as it determines the conditions for applying text encoding. It is a key input that helps to shape the final output of the encoded process and ensures that the images generated meet the required specifications.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]
- text
    - The `text' parameter is the text input processed by the node. It is important because it directly affects the content and style of the code expression and, in turn, the characteristics that generate the image.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- conditioning
    - `conventioning' output is represented by a set of codes derived from the input text. It is important because it forms the basis for controlling the image generation process and ensuring that the image produced is consistent with the text description provided.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPTextEncodeControlnet:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'conditioning': ('CONDITIONING',), 'text': ('STRING', {'multiline': True, 'dynamicPrompts': True})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = '_for_testing/conditioning'

    def encode(self, clip, conditioning, text):
        tokens = clip.tokenize(text)
        (cond, pooled) = clip.encode_from_tokens(tokens, return_pooled=True)
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]['cross_attn_controlnet'] = cond
            n[1]['pooled_output_controlnet'] = pooled
            c.append(n)
        return (c,)
```