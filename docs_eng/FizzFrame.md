# Documentation
- Class name: NodeFrame
- Category: FizzNodes 📅🅕🅝/FrameNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The NodeFrame class is designed to manage and create a framework in a structured data stream. It facilitates the integration of text into existing frameworks, generating a new framework that contains both positive and negative text-based emotions. The node plays a key role in the narrative process that shapes data through systems, combining and comparing different text perspectives.

# Input types
## Required
- frame
    - The `frame' parameter is essential because it identifies the specific frame in the data structure that the node will operate. It ensures that the correct frame is located for operation or data retrieval, thereby preserving the integrity and sequencing of the data stream.
    - Comfy dtype: INT
    - Python dtype: int
- previous_frame
    - The `previous_frame' parameter is necessary because it provides the context of the previous frame, which is constructed by nodes. It is a mandatory input that ensures continuity and consistency in the framework creation process.
    - Comfy dtype: FIZZFRAME
    - Python dtype: NodeFrame
- positive_text
    - The `positive_text' parameter is a key element in the process of introducing positive emotions to frame creation. It allows optimistic or positive views to be expressed in a constructive way to enrich the narrative.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- negative_text
    - The `negative_text' parameter, while optional, is used to introduce a comparative perspective into the framework, providing a balanced perspective by including potential criticism or shortcomings next to positive emotions.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- FIZZFRAME
    - The output 'FIZZFRAME' represents the newly created framework, which contains integrated positive and negative textual feelings. This is an important output because it provides the basis for subsequent data processing and analysis.
    - Comfy dtype: FIZZFRAME
    - Python dtype: NodeFrame
- CONDITIONING
    - The `conditioning' output provides a code for both positive and negative text, which is essential for further processing within the system. These modem outputs allow for the operation and refinement of data based on text input.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Union[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class NodeFrame:

    def __init__(self):
        self.frames = {}
        self.thisFrame = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'frame': ('INT', {'default': 0, 'min': 0}), 'previous_frame': ('FIZZFRAME', {'forceInput': True}), 'positive_text': ('STRING', {'multiline': True})}, 'optional': {'negative_text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('FIZZFRAME', 'CONDITIONING', 'CONDITIONING')
    FUNCTION = 'create_frame'
    CATEGORY = 'FizzNodes 📅🅕🅝/FrameNodes'

    def create_frame(self, frame, previous_frame, positive_text, negative_text=None):
        self.frames = previous_frame.frames
        prev_frame = previous_frame.thisFrame
        new_positive_text = f"{positive_text}, {prev_frame['general_positive']}"
        new_negative_text = f"{negative_text}, {prev_frame['general_negative']}"
        pos_tokens = prev_frame['clip'].tokenize(new_positive_text)
        (pos_cond, pos_pooled) = prev_frame['clip'].encode_from_tokens(pos_tokens, return_pooled=True)
        neg_tokens = prev_frame['clip'].tokenize(new_negative_text)
        (neg_cond, neg_pooled) = prev_frame['clip'].encode_from_tokens(neg_tokens, return_pooled=True)
        new_frame = {'positive_text': positive_text, 'negative_text': negative_text, 'general_positive': prev_frame['general_positive'], 'general_negative': prev_frame['general_negative'], 'clip': prev_frame['clip'], 'pos_conditioning': {'cond': pos_cond, 'pooled': pos_pooled}, 'neg_conditioning': {'cond': neg_cond, 'pooled': neg_pooled}}
        self.thisFrame = new_frame
        self.frames[frame] = new_frame
        return (self, [[pos_cond, {'pooled_output': pos_pooled}]], [[neg_cond, {'pooled_output': neg_pooled}]])
```