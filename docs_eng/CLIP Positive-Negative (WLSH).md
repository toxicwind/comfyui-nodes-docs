# Documentation
- Class name: WLSH_CLIP_Positive_Negative
- Category: WLSH Nodes/conditioning
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is designed to process text input and generate encoded expressions that can be used for further analysis or comparison. It plays a key role in the workflow and provides a basis for text-based feature extraction.

# Input types
## Required
- clip
    - The clip parameter is essential to the operation of the node, which provides the mechanism for encoded text. It is the core component for converting the original text into a structured format.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- positive_text
    - This parameter is a text input that is relevant to the positive aspects of the coding process. It is important because it sets the context for the coding and affects the final expression.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_text
    - Similar to positionive_text, this parameter introduces a negative context into the coding process. It is critical to the comparison in the coding expression, which is useful for some types of analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- positive
    - Positive output represents the coding form of the positive text as a reference for comparison or further processing within the system.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative output is the coding of negative text, which provides insight into differences and nuances in the coding process compared to the positive output.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_CLIP_Positive_Negative:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'positive_text': ('STRING', {'default': f'', 'multiline': True}), 'negative_text': ('STRING', {'default': f'', 'multiline': True})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('positive', 'negative')
    FUNCTION = 'encode'
    CATEGORY = 'WLSH Nodes/conditioning'

    def encode(self, clip, positive_text, negative_text):
        return ([[clip.encode(positive_text), {}]], [[clip.encode(negative_text), {}]])
```