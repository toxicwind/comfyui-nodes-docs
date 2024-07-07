# Documentation
- Class name: InitNodeFrame
- Category: FizzNodes 📅🅕🅝/FrameNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

Method `create_frame'is responsible for initializing and managing the framework in the node. It constructs a new framework by combining positive and negative text input, as well as the context of optional general emotions and earlier frameworks. The function of the node focuses on creating a structured expression, enclosed text data, for further processing and analysis within the framework.

# Input types
## Required
- frame
    - The parameter 'frame' is essential for a specific framework in the operation of the identification node. It plays a key role in organizing and distinguishing different frameworks, thus influencing the implementation of the node and the structured expression it creates.
    - Comfy dtype: INT
    - Python dtype: int
- positive_text
    - The parameter 'positive_text' is a key component in defining positive emotions in the framework. It significantly influences the ability of nodes to process and express emotions in text data and shapes the results of overall emotional analysis.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- negative_text
    - While the 'negative_text' parameter is optional, it contributes to comprehensive emotional analysis by providing a negative context. It enriches node understanding of the emotional spectrum and improves the accuracy of emotional expressions.
    - Comfy dtype: STRING
    - Python dtype: str
- general_positive
    - The parameter 'general_positive' allows for general positive statements that can be linked to the framework. It adds depth to emotional analysis by integrating broader positive emotions into the context of the framework.
    - Comfy dtype: STRING
    - Python dtype: str
- general_negative
    - The parameter 'general_negative' is used to encompass general negative emotions that may affect the framework. It is important to provide a balanced perspective of emotions, ensuring that nodes capture the full range of emotional expressions.
    - Comfy dtype: STRING
    - Python dtype: str
- previous_frame
    - The parameter 'previous_frame' is used to quote the previous frame, allowing nodes to inherit and to set them in their context. It is important to maintain continuity and consistency between the node operations.
    - Comfy dtype: FIZZFRAME
    - Python dtype: FIZZFRAME
- clip
    - The parameter 'clip' is essential for a marked format that can be processed by encoding text data into nodes. It serves as a tool in transforming the original text into a structured expression of emotional analysis.
    - Comfy dtype: CLIP
    - Python dtype: CLIP

# Output types
- FIZZFRAME
    - The output 'FIZZFRAME' provides the newly created framework and its associated emotional and contextual context. It is important because it represents the outcome of node operations, and it wraps up structured data for further use.
    - Comfy dtype: FIZZFRAME
    - Python dtype: FIZZFRAME
- CONDITIONING
    - The output 'conditioning' includes the input of derived code positive and negative reconciliation data from text. It is essential for emotional analysis, as it provides the structured expression required for downstream processing.
    - Comfy dtype: COMBO[torch.Tensor, Dict[str, torch.Tensor]]
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class InitNodeFrame:

    def __init__(self):
        self.frames = {}
        self.thisFrame = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'frame': ('INT', {'default': 0, 'min': 0}), 'positive_text': ('STRING', {'multiline': True})}, 'optional': {'negative_text': ('STRING', {'multiline': True}), 'general_positive': ('STRING', {'multiline': True}), 'general_negative': ('STRING', {'multiline': True}), 'previous_frame': ('FIZZFRAME', {'forceInput': True}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('FIZZFRAME', 'CONDITIONING', 'CONDITIONING')
    FUNCTION = 'create_frame'
    CATEGORY = 'FizzNodes 📅🅕🅝/FrameNodes'

    def create_frame(self, frame, positive_text, negative_text=None, general_positive=None, general_negative=None, previous_frame=None, clip=None):
        new_frame = {'positive_text': positive_text, 'negative_text': negative_text}
        if previous_frame:
            prev_frame = previous_frame.thisFrame
            new_frame['general_positive'] = prev_frame['general_positive']
            new_frame['general_negative'] = prev_frame['general_negative']
            new_frame['clip'] = prev_frame['clip']
            self.frames = previous_frame.frames
        if general_positive:
            new_frame['general_positive'] = general_positive
        if general_negative:
            new_frame['general_negative'] = general_negative
        new_positive_text = f"{positive_text}, {new_frame['general_positive']}"
        new_negative_text = f"{negative_text}, {new_frame['general_negative']}"
        if clip:
            new_frame['clip'] = clip
        pos_tokens = new_frame['clip'].tokenize(new_positive_text)
        (pos_cond, pos_pooled) = new_frame['clip'].encode_from_tokens(pos_tokens, return_pooled=True)
        new_frame['pos_conditioning'] = {'cond': pos_cond, 'pooled': pos_pooled}
        neg_tokens = new_frame['clip'].tokenize(new_negative_text)
        (neg_cond, neg_pooled) = new_frame['clip'].encode_from_tokens(neg_tokens, return_pooled=True)
        new_frame['neg_conditioning'] = {'cond': neg_cond, 'pooled': neg_pooled}
        self.frames[frame] = new_frame
        self.thisFrame = new_frame
        return (self, [[pos_cond, {'pooled_output': pos_pooled}]], [[neg_cond, {'pooled_output': neg_pooled}]])
```