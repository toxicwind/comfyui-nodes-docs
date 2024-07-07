# Documentation
- Class name: SeargeSDXLPromptEncoder
- Category: Searge/_deprecated_/ClipEncoding
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to process text input and encode it as the condition data for the generation of the model. It focuses on converting tips into structured formats that can guide the generation process, emphasizing the role of nodes in preparing input for creative tasks.

# Input types
## Required
- base_clip
    - This parameter is essential because it provides the basic CLIP model used to encode texttips. It is essential for the operation of nodes and affects the quality of the condition data generated.
    - Comfy dtype: CLIP
    - Python dtype: CLIPModel
- refiner_clip
    - The fine-tuning of the CLIP model is used to further process and refine texttips to improve the validity of conditional data. Its role in node execution and final output quality is essential.
    - Comfy dtype: CLIP
    - Python dtype: CLIPModel
- base_width
    - Basic width parameters are essential to define the input space size of the model, directly affecting the scope and resolution of the content generated.
    - Comfy dtype: INT
    - Python dtype: int
- base_height
    - Similar to the basic width, the basic altitude parameters are essential in setting the vertical dimensions of the input space, affecting the overall structure and structure of the output.
    - Comfy dtype: INT
    - Python dtype: int
- crop_w
    - The width parameters determine the horizontal range of the crop area, which is essential to concentrate the generation in the particular interest area in the input.
    - Comfy dtype: INT
    - Python dtype: int
- crop_h
    - Crop height parameters set the vertical dimensions of the crop area and play a key role in isolating specific elements during generation.
    - Comfy dtype: INT
    - Python dtype: int
- target_width
    - The target width parameters define the desired width of the output, which is a key factor in ensuring that the content is generated to meet the required specifications and dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- target_height
    - The target height parameters specify the desired level of output, which directly affects the final size and layout of the content generated.
    - Comfy dtype: INT
    - Python dtype: int
- pos_ascore
    - Positive weight parameters are used to weigh the importance of the positives in the generation process to ensure that the output reflects the desired aesthetic quality.
    - Comfy dtype: FLOAT
    - Python dtype: float
- neg_ascore
    - Negative weight parameters help to reduce undesired dollars in the output and improve the accuracy and relevance of the content generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_width
    - The thinner width parameters are important for setting the size of the fine input space, which is essential for achieving detailed and high-quality fine-tuning in the output.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_height
    - The finer height parameters are essential for defining the vertical dimensions of the fine-tuning input space, affecting the particle size and accuracy of the fine-tuning in the output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- pos_g
    - This parameter contains a positive global reminder that influences the overall theme and direction of the content. It is important to set the creative background for node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- pos_l
    - Positive local tips provide detailed guidance on specific aspects of generation and help nodes produce targeted and nuanced outputs.
    - Comfy dtype: STRING
    - Python dtype: str
- pos_r
    - Positive fine-tuning tips are used to fine-tune the generation process to ensure that outputs are closely aligned with desired aesthetic and thematic objectives.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_g
    - Negative global reminders help to remove undesirable elements from the creation of content and play a key role in shaping the identity of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_l
    - Negative local hints are used to specify specific aspects that should be avoided in generation and to guide nodes to produce content that meets specific exclusion criteria.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_r
    - Negative fine-tuning tips are used to further refine the removal of undesirable elements and to ensure a high level of accuracy in node output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- base_positive
    - This output provides data on conditions derived from the underlying positive cues, which serve as the basis for guiding the generation of models towards the desired creative direction.
    - Comfy dtype: CONDITIONING
    - Python dtype: ConditioningData
- base_negative
    - The underlying negative output contains condition data from the underlying negative hint, which helps to remove undesirable elements from the creation of content.
    - Comfy dtype: CONDITIONING
    - Python dtype: ConditioningData
- refiner_positive
    - This output consists of condition data from the front tip of the nuancer and focuses on fine-tuning the aesthetic and thematic aspects of content generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: ConditioningData
- refiner_negative
    - The negative output of the nuancer provides conditional data based on the negative hint of the nuancer to ensure that the final output is nuanced to avoid undesirable characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: ConditioningData

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeSDXLPromptEncoder:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_clip': ('CLIP',), 'refiner_clip': ('CLIP',), 'pos_g': ('STRING', {'multiline': True, 'default': 'POS_G'}), 'pos_l': ('STRING', {'multiline': True, 'default': 'POS_L'}), 'pos_r': ('STRING', {'multiline': True, 'default': 'POS_R'}), 'neg_g': ('STRING', {'multiline': True, 'default': 'NEG_G'}), 'neg_l': ('STRING', {'multiline': True, 'default': 'NEG_L'}), 'neg_r': ('STRING', {'multiline': True, 'default': 'NEG_R'}), 'base_width': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'base_height': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'target_width': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'target_height': ('INT', {'default': 4096, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'pos_ascore': ('FLOAT', {'default': 6.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}), 'neg_ascore': ('FLOAT', {'default': 2.5, 'min': 0.0, 'max': 1000.0, 'step': 0.01}), 'refiner_width': ('INT', {'default': 2048, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'refiner_height': ('INT', {'default': 2048, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('base_positive', 'base_negative', 'refiner_positive', 'refiner_negative')
    FUNCTION = 'encode'
    CATEGORY = 'Searge/_deprecated_/ClipEncoding'

    def encode(self, base_clip, refiner_clip, pos_g, pos_l, pos_r, neg_g, neg_l, neg_r, base_width, base_height, crop_w, crop_h, target_width, target_height, pos_ascore, neg_ascore, refiner_width, refiner_height):
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
        tokens3 = refiner_clip.tokenize(pos_r)
        (cond3, pooled3) = refiner_clip.encode_from_tokens(tokens3, return_pooled=True)
        res3 = [[cond3, {'pooled_output': pooled3, 'aesthetic_score': pos_ascore, 'width': refiner_width, 'height': refiner_height}]]
        tokens4 = refiner_clip.tokenize(neg_r)
        (cond4, pooled4) = refiner_clip.encode_from_tokens(tokens4, return_pooled=True)
        res4 = [[cond4, {'pooled_output': pooled4, 'aesthetic_score': neg_ascore, 'width': refiner_width, 'height': refiner_height}]]
        return (res1, res2, res3, res4)
```