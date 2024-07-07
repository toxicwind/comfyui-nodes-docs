# Documentation
- Class name: WLSH_CLIP_Text_Positive_Negative_XL
- Category: WLSH Nodes/conditioning
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_CLIP_Text_Positive_Negative_XL node is designed to process text input and encode text into the format applicable to condition-generated models. It receives positive and negative text examples and converts them into coded expressions that can be used to guide the generation process. The node plays a key role in shaping the output of the generation model by providing context clues based on text input.

# Input types
## Required
- width
    - The width parameter defines the width dimension of the image processing component of the node. It is essential for setting the appropriate resolution and ensuring that the output image meets the required specifications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters specify the vertical dimensions of the image that you want to process. It works with the width parameters to determine the overall resolution of the image.
    - Comfy dtype: INT
    - Python dtype: int
- target_width
    - The target_width parameter sets the desired width of the final output image. It is a key factor for resizing and scaling operations within the node.
    - Comfy dtype: INT
    - Python dtype: int
- target_height
    - The target_height parameter sets the desired height for the final output of the image to ensure that the image meets the required dimensions after processing.
    - Comfy dtype: INT
    - Python dtype: int
- positive_g
    - The positionive_g parameter accepts the string that represents the positive lead text. It is essential to guide the direction of the generation process to a more favourable result.
    - Comfy dtype: STRING
    - Python dtype: str
- positive_l
    - The positionive_l parameter provides additional text to supplement the positive guide text. It helps to fine-tune the positive conditions for the model.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_g
    - The negative_g parameter contains negative guiding text that guides the generation process to avoid undesirable outcomes.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_l
    - The negative_l parameter supplements the negative guiding text and further defines the limits of the content to be avoided in the output generated.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The clip parameter should be an example of the CLIP model, which is essential for text coding in the node. It allows text input to be converted into a form that can be used to generate the model.
    - Comfy dtype: CLIP
    - Python dtype: Any
## Optional
- crop_w
    - The crop_w parameter is used to define the width of the crop area in the image. It allows selective attention to specific areas of the image for further processing.
    - Comfy dtype: INT
    - Python dtype: int
- crop_h
    - The crop_h parameter determines the height of the area in which the image is cropped. It is used for more detailed analysis or processing of specific parts of the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- positive
    - Positive output provides a code for the positive lead text, which is used to guide the generation process towards the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- negative
    - Negative output is coded to include negative guidance text, which is used to guide the generation process in a direction that is not desired.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- positive_text
    - The positionive_text output is a connection string for the positive lead text, which provides a readable form of the positive thread used in the generation process.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_text
    - Negative_text output is a connection string for negative-guiding text that provides a readable form of negative threads used to avoid certain outcomes during generation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_CLIP_Text_Positive_Negative_XL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'positive_g': ('STRING', {'multiline': True, 'default': 'POS_G'}), 'positive_l': ('STRING', {'multiline': True, 'default': 'POS_L'}), 'negative_g': ('STRING', {'multiline': True, 'default': 'NEG_G'}), 'negative_l': ('STRING', {'multiline': True, 'default': 'NEG_L'}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative', 'positive_text', 'negative_text')
    FUNCTION = 'encode'
    CATEGORY = 'WLSH Nodes/conditioning'

    def encode(self, clip, width, height, crop_w, crop_h, target_width, target_height, positive_g, positive_l, negative_g, negative_l):
        tokens = clip.tokenize(positive_g)
        tokens['l'] = clip.tokenize(positive_l)['l']
        if len(tokens['l']) != len(tokens['g']):
            empty = clip.tokenize('')
            while len(tokens['l']) < len(tokens['g']):
                tokens['l'] += empty['l']
            while len(tokens['l']) > len(tokens['g']):
                tokens['g'] += empty['g']
        (condP, pooledP) = clip.encode_from_tokens(tokens, return_pooled=True)
        tokensN = clip.tokenize(negative_g)
        tokensN['l'] = clip.tokenize(negative_l)['l']
        if len(tokensN['l']) != len(tokensN['g']):
            empty = clip.tokenize('')
            while len(tokensN['l']) < len(tokensN['g']):
                tokensN['l'] += empty['l']
            while len(tokensN['l']) > len(tokensN['g']):
                tokensN['g'] += empty['g']
        (condN, pooledN) = clip.encode_from_tokens(tokensN, return_pooled=True)
        positive_text = positive_g + ', ' + positive_l
        negative_text = negative_g + ', ' + negative_l
        return ([[condP, {'pooled_output': pooledP, 'width': width, 'height': height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]], [[condN, {'pooled_output': pooledP, 'width': width, 'height': height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]], positive_text, negative_text)
```