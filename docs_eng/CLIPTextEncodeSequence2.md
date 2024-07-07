# Documentation
- Class name: CLIPTextEncodeSequence2
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The CLIPTextEncodeSequience 2 node is designed to encode the text sequence into a condition sequence that can be used in generating the model for further processing. It processes the text of each line to create a set of conditional vectors, which are then converted according to the specified key frame type to match the number of frames required.

# Input types
## Required
- clip
    - The clip parameter is essential because it provides the necessary context for the text coding process. It affects how the text is converted into a conditional vector sequence.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- frame_count
    - Frame number parameters specify the total number of frames that you want to generate. It is a basic parameter that directly affects the size of the output condition sequence.
    - Comfy dtype: INT
    - Python dtype: int
- text
    - The text parameter is the original input to the encoded process. It is the source of information that will be converted into a condition sequence.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- token_normalization
    - Harmonization is a technique used to stabilize the coding process. It determines the way in which the coding is assimilated, which may affect the quality of the condition sequence generated.
    - Comfy dtype: COMBO[none, mean, length, length+mean]
    - Python dtype: str
- weight_interpretation
    - The weight interpretation parameters are defined in terms of how to understand the encoded text weights. It is essential for the accuracy and reliability of the coding process.
    - Comfy dtype: COMBO[comfy, A1111, compel, comfy++]
    - Python dtype: str
- cond_keyframes_type
    - Cond_keyframes_type parameters determine how the key frame of the condition is distributed over frame numbers. It is important to align the text code with the required time structure.
    - Comfy dtype: COMBO[linear, sinus, sinus_inverted, half_sinus, half_sinus_inverted]
    - Python dtype: str

# Output types
- conditioning_sequence
    - Conditional series is a list of coding text expressions that are used as input to generate models. It is a key component to guide the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[int, torch.Tensor]]
- cond_keyframes
    - Cond_keyframes represents a specific frame in the sequence that corresponds to the encoded text. They are important for synchronizing text encoding and visual output.
    - Comfy dtype: INT
    - Python dtype: List[int]
- frame_count
    - Frame numbers represent the total number of frames generated and provide a measure of the range of output.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPTextEncodeSequence2:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'clip': ('CLIP',), 'token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'weight_interpretation': (['comfy', 'A1111', 'compel', 'comfy++'],), 'cond_keyframes_type': (['linear', 'sinus', 'sinus_inverted', 'half_sinus', 'half_sinus_inverted'],), 'frame_count': ('INT', {'default': 100, 'min': 1, 'max': 1024, 'step': 1}), 'text': ('STRING', {'multiline': True, 'default': 'A portrait of a rosebud\nA portrait of a blooming rosebud\nA portrait of a blooming rose\nA portrait of a rose'})}}
    RETURN_TYPES = ('CONDITIONING', 'INT', 'INT')
    RETURN_NAMES = ('conditioning_sequence', 'cond_keyframes', 'frame_count')
    IS_LIST_OUTPUT = (True, True, False)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning'

    def encode(self, clip, text, cond_keyframes_type, frame_count, token_normalization, weight_interpretation):
        text = text.strip()
        conditionings = []
        for line in text.splitlines():
            if USE_BLK:
                encoded = blk_adv.encode(clip=clip, text=line, token_normalization=token_normalization, weight_interpretation=weight_interpretation)
            else:
                encoded = CLIPTextEncode.encode(clip=clip, text=line)
            conditionings.append([encoded[0][0][0], encoded[0][0][1]])
        conditioning_count = len(conditionings)
        cond_keyframes = self.calculate_cond_keyframes(cond_keyframes_type, frame_count, conditioning_count)
        return (conditionings, cond_keyframes, frame_count)

    def calculate_cond_keyframes(self, type, frame_count, conditioning_count):
        if type == 'linear':
            return np.linspace(frame_count // conditioning_count, frame_count, conditioning_count, dtype=int).tolist()
        elif type == 'sinus':
            t = np.linspace(0, np.pi, conditioning_count)
            sinus_values = np.sin(t)
            normalized_values = (sinus_values - sinus_values.min()) / (sinus_values.max() - sinus_values.min())
            scaled_values = normalized_values * (frame_count - 1) + 1
            unique_keyframes = np.round(scaled_values).astype(int)
            unique_keyframes = np.unique(unique_keyframes, return_index=True)[1]
            return sorted(unique_keyframes.tolist())
        elif type == 'sinus_inverted':
            return (np.cos(np.linspace(0, np.pi, conditioning_count)) * (frame_count - 1) + 1).astype(int).tolist()
        elif type == 'half_sinus':
            return (np.sin(np.linspace(0, np.pi / 2, conditioning_count)) * (frame_count - 1) + 1).astype(int).tolist()
        elif type == 'half_sinus_inverted':
            return (np.cos(np.linspace(0, np.pi / 2, conditioning_count)) * (frame_count - 1) + 1).astype(int).tolist()
        else:
            raise ValueError('Unsupported cond_keyframes_type: ' + type)
```