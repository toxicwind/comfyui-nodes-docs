# Documentation
- Class name: WLSH_CLIP_Positive_Negative_XL
- Category: WLSH Nodes/conditioning
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is designed to process and encode positive and negative images for comparative learning. It uses the CLIP model to extract visual features and align them to text descriptions, facilitating the creation of meaningful image-text connections.

# Input types
## Required
- width
    - Width is the key parameter for defining the resolution of the level of the image that you enter. It is essential for the correct processing and adjustment of the size of the image at the node, ensuring that the encoded feature is extracted from the correct dimension.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude is similar to width and is an important parameter that specifies the vertical resolution of the input image. It works with width to ensure accurate image processing and feature coding.
    - Comfy dtype: INT
    - Python dtype: int
- positive_g
    - The positionive_g parameter is a text description associated with a positive image. It is essential for node to create semantic connections between image content and text, which is important for the encoding process.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_g
    - Negative_g is a text description of negative images. This parameter is important because it provides the necessary comparison of positive images and enhances the ability of nodes to distinguish and learn from two different images - text pairs.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- positive
    - Positive output contains coding features and metadata for positive images. It is a key part of node output because it represents one aspect of the learning process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Union[str, torch.Tensor]]]
- negative
    - Negative output corresponds to positive output, but it targets negative images. It is equally important because it provides the comparative perspective necessary to effectively compare learning.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Union[str, torch.Tensor]]]

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_CLIP_Positive_Negative_XL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'positive_g': ('STRING', {'multiline': True, 'default': 'POS_G'}), 'positive_l': ('STRING', {'multiline': True, 'default': 'POS_L'}), 'negative_g': ('STRING', {'multiline': True, 'default': 'NEG_G'}), 'negative_l': ('STRING', {'multiline': True, 'default': 'NEG_L'}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('positive', 'negative')
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
        return ([[condP, {'pooled_output': pooledP, 'width': width, 'height': height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]], [[condN, {'pooled_output': pooledP, 'width': width, 'height': height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]])
```