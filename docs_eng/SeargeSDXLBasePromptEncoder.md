# Documentation
- Class name: SeargeSDXLBasePromptEncoder
- Category: Searge/_deprecated_/ClipEncoding
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeSDXLBasePromptEncoder class is used as an intermediary for processing and encoding text into the format available in the CLIP model. It is designed to process text encoding tasks by balancing and aligning the length of texttips, both positive and negative, to ensure compatibility with model requirements.

# Input types
## Required
- base_clip
    - Base_clip parameters are essential to the function of the node because they provide the basis for text tagging and encoding. It is an example of a CLIP model that is used to tag and encode input text tips.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- pos_g
    - Positive global text input is essential for generating positive condition data. It affects the overall emotional and direction of the coding process.
    - Comfy dtype: STRING
    - Python dtype: str
- pos_l
    - Positive local text input is important to fine-tune the positive condition data. It helps to add particle size and specificity to the encoding process.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_g
    - Negative text input across the board is critical to generating negative conditionality data. It shapes the contrast and boundary of the encoded process.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_l
    - Negative local text input is important for detailing the negative condition data. It helps to improve the accuracy and focus of the coding process.
    - Comfy dtype: STRING
    - Python dtype: str
- base_width
    - The base_width parameter determines the width of the underlying image during the encoding process. It is an important part of the data spatial configuration.
    - Comfy dtype: INT
    - Python dtype: int
- base_height
    - The base_height parameter sets the height of the underlying image during the encoding process. It is essential to maintain the vertical ratio and structural integrity of the data.
    - Comfy dtype: INT
    - Python dtype: int
- crop_w
    - The crop_w parameter is used to determine the width of the area that is cropped from the base image. It affects the focus and frame of the coded data.
    - Comfy dtype: INT
    - Python dtype: int
- crop_h
    - The crop_h parameter specifies the height of the area to be cropped from the base image. It is important for the configuration and layout of the coded data.
    - Comfy dtype: INT
    - Python dtype: int
- target_width
    - The target_width parameter outlines the desired width of the final output. It is essential to guide the coding process in resizing and scaling operations.
    - Comfy dtype: INT
    - Python dtype: int
- target_height
    - The target_height parameter defines the desired level of the final output. It is important for matching the dimensions and proportions of the data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- base_positive
    - Base_positive output containing coded positive condition data is essential for building a positive context and emotion during the follow-up phase.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[str, Dict[str, Union[str, int, torch.Tensor]]]
- base_negative
    - Base_negative output provides post-coded negative condition data that are essential for defining boundaries and comparisons in the coding process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[str, Dict[str, Union[str, int, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeSDXLBasePromptEncoder:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_clip': ('CLIP',), 'pos_g': ('STRING', {'multiline': True, 'default': 'POS_G'}), 'pos_l': ('STRING', {'multiline': True, 'default': 'POS_L'}), 'neg_g': ('STRING', {'multiline': True, 'default': 'NEG_G'}), 'neg_l': ('STRING', {'multiline': True, 'default': 'NEG_L'}), 'base_width': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'base_height': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'target_width': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'target_height': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('base_positive', 'base_negative')
    FUNCTION = 'encode'
    CATEGORY = 'Searge/_deprecated_/ClipEncoding'

    def encode(self, base_clip, pos_g, pos_l, neg_g, neg_l, base_width, base_height, crop_w, crop_h, target_width, target_height):
        empty = base_clip.tokenize('')
        tokens1 = base_clip.tokenize(pos_g)
        tokens1['l'] = base_clip.tokenize(pos_l)['l']
        if len(tokens1['l']) != len(tokens1['g']):
            while len(tokens1['l']) < len(tokens1['g']):
                tokens1['l'] += empty['l']
            while len(tokens1['l']) > len(tokens1['g']):
                tokens1['g'] += empty['g']
        (cond1, pooled1) = base_clip.encode_from_tokens(tokens1, return_pooled=True)
        res1 = [[cond1, {'pooled_output': pooled1, 'width': base_width, 'height': base_height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]]
        tokens2 = base_clip.tokenize(neg_g)
        tokens2['l'] = base_clip.tokenize(neg_l)['l']
        if len(tokens2['l']) != len(tokens2['g']):
            while len(tokens2['l']) < len(tokens2['g']):
                tokens2['l'] += empty['l']
            while len(tokens2['l']) > len(tokens2['g']):
                tokens2['g'] += empty['g']
        (cond2, pooled2) = base_clip.encode_from_tokens(tokens2, return_pooled=True)
        res2 = [[cond2, {'pooled_output': pooled2, 'width': base_width, 'height': base_height, 'crop_w': crop_w, 'crop_h': crop_h, 'target_width': target_width, 'target_height': target_height}]]
        return (res1, res2)
```