# Documentation
- Class name: CLIPTextEncodeSequence
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The CLIPTextEncodeSequience node is designed to encode a series of text lines into a set of condition sequences that can be used for further processing in the neural network. It considers the way in which tags are normalized and weighted to generate meaningful expressions of text.

# Input types
## Required
- clip
    - The 'clip' parameter is essential for the encoding process because it provides context or model for text encoding. It directly affects how the text is converted to a numerical expression.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- token_normalization
    - The 'token_normation' parameter determines how the markers in the text are normalized before encoding. It plays a key role in ensuring consistency in the size of the coded text, which is important for subsequent neural network operations.
    - Comfy dtype: COMBO[none, mean, length, length+mean]
    - Python dtype: str
- weight_interpretation
    - The 'Weight_interpretation' parameter defines the interpretation of weights associated with text tags during the encoding process. It affects the quality and characteristics of the code sequences generated.
    - Comfy dtype: COMBO[comfy, A1111, compel, comfy++]
    - Python dtype: str
- text
    - The 'text' parameter is the original text input processed by the node. It is multi-lined and can be packaged into a series of text lines, each of which will be encoded as a condition sequence. The content and structure of the text significantly influences the output of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- conditioning_sequence
    - The 'conventioning_equality' output is a series of coded text lines, each of which is a pair of indexes and encoded vectors. This output is important because it provides the necessary input for downstream neural network models that require text-based conditions.
    - Comfy dtype: CONDITIONING_SEQ
    - Python dtype: List[Tuple[int, List[float]]]

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPTextEncodeSequence:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'weight_interpretation': (['comfy', 'A1111', 'compel', 'comfy++'],), 'text': ('STRING', {'multiline': True, 'default': '0:A portrait of a rosebud\n5:A portrait of a blooming rosebud\n10:A portrait of a blooming rose\n15:A portrait of a rose'})}}
    RETURN_TYPES = ('CONDITIONING_SEQ',)
    RETURN_NAMES = ('conditioning_sequence',)
    IS_LIST_OUTPUT = (True,)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning'

    def encode(self, clip, text, token_normalization, weight_interpretation):
        text = text.strip()
        conditionings = []
        for l in text.splitlines():
            match = re.match('(\\d+):', l)
            if match:
                idx = int(match.group(1))
                (_, line) = l.split(':', 1)
                line = line.strip()
                if USE_BLK:
                    encoded = blk_adv.encode(clip=clip, text=line, token_normalization=token_normalization, weight_interpretation=weight_interpretation)
                else:
                    encoded = CLIPTextEncode.encode(clip=clip, text=line)
                conditioning = (idx, [encoded[0][0][0], encoded[0][0][1]])
                conditionings.append(conditioning)
        return (conditionings,)
```