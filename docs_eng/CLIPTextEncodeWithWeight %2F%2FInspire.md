# Documentation
- Class name: CLIPTextEncodeWithWeight
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to process text data using the CLIP model, with the ability to adjust the encoded strength and apply extra weights to markings, thus allowing for fine control of the text encoding process.

# Input types
## Required
- text
    - Text parameters are necessary because it provides the original text input for node processing. It is the basis for encoding and weighting adjustments.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The clip parameter represents the CLIP model that will be used to tag and encode text input. It is essential for the function of the node, as it determines the encoding process.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
## Optional
- strength
    - The strength parameter allows you to adjust the encoded strength of the text mark. It changes the encoding process to better accommodate the specific requirements of the task at hand.
    - Comfy dtype: FLOAT
    - Python dtype: float
- add_weight
    - The add_weight parameter provides the ability to apply extra weights to markings during the encoding process. This can be used to fine-tune the encoding further to the task.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pooled_output
    - The pooled_output parameter represents the aggregation and enrichment of the coded text, which is the result of node processing. It encapsulates the essence of the text for further use.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPTextEncodeWithWeight:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'add_weight': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'InspirePack/Util'

    def encode(self, clip, text, strength, add_weight):
        tokens = clip.tokenize(text)
        if add_weight != 0 or strength != 1:
            for v in tokens.values():
                for vv in v:
                    for i in range(0, len(vv)):
                        vv[i] = (vv[i][0], vv[i][1] * strength + add_weight)
        (cond, pooled) = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {'pooled_output': pooled}]],)
```