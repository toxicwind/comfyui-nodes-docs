# Documentation
- Class name: WLSH_CLIP_Text_Positive_Negative
- Category: WLSH Nodes/conditioning
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `encode'method of the WLSH_CLIP_Text_Positive_Negative node uses the CLIP model to process text input and encode it as an embedded vector. This node plays a key role in converting text data into a form that can be used for further analysis or as a machine learning model input. It emphasizes the ability of nodes to handle both positive and negative text samples, which is essential to the task of learning through emotional analysis or comparison.

# Input types
## Required
- positive
    - The parameter 'positive' is a text input that represents positive emotions or context. It is the basis for node operations, as it forms the basis for emotional analysis and comparative learning, in which nodes distinguish between positive and negative text samples.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The parameter 'negative' is a text input that represents negative emotions or context. It is used in conjunction with the 'positive' parameter and provides a comparative basis for coding and analysis within the node.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The parameter 'clip' is an example of the CLIP model used to encode text input into embedded vectors. It is the key component of the node because it directly affects the quality and accuracy of the coding process.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module

# Output types
- positive
    - Output 'positive' is the code for text input. It is a key element of a machine learning mission that follows with emotional analysis or understanding of the context.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Output 'negative' is a code for negative text input. It is important for applications involving negative context understanding in the context of emotional analysis or models.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- positive_text
    - Output 'positive_text' is the original positive text input to the node. It helps to keep the original text data together with the embedded vector of the code when further processed or analysed.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_text
    - Output 'negative_text' is the original negative text input to the node. It retains the original text data, which may be combined with the embedded vector of the code for follow-on tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_CLIP_Text_Positive_Negative:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('STRING', {'multiline': True}), 'negative': ('STRING', {'multiline': True}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative', 'positive_text', 'negative_text')
    FUNCTION = 'encode'
    CATEGORY = 'WLSH Nodes/conditioning'

    def encode(self, clip, positive, negative):
        return ([[clip.encode(positive), {}]], [[clip.encode(negative), {}]], positive, negative)
```