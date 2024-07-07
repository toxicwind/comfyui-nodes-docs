# Documentation
- Class name: CR_PromptMixer
- Category: Comfyroll/Essential/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_PromptMixer is a node designed to mix different hints and styles to generate refined output. It receives both positive and negative hints and style input, and then applies the selected preset to mix these inputs in a particular way. The function of the node is focused on improving the quality and consistency of the text generation by combining various text elements intelligently.

# Input types
## Optional
- prompt_positive
    - A positive reminder is the key input in the text generation process, which provides a constructive example or guideline. It plays a crucial role in guiding output towards desired quality and attributes.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_negative
    - Negative hints are used to provide examples or guidelines that should be avoided in text generation. They play an important role in shaping output by specifying what to exclude.
    - Comfy dtype: STRING
    - Python dtype: str
- style_positive
    - Positive style input is used to refine text generation by adding the desired style element. It enhances output with specific style features.
    - Comfy dtype: STRING
    - Python dtype: str
- style_negative
    - Negative style input allows the specification of style elements that should be omitted from the text generation. This is important to ensure that the final output is consistent with the desired style.
    - Comfy dtype: STRING
    - Python dtype: str
- preset
    - Preset parameters determine the specific mix of strategies to be applied to input. Each preset represents a different method to combine both positive and negative hints and styles.
    - Comfy dtype: COMBO['preset 1', 'preset 2', 'preset 3', 'preset 4', 'preset 5']
    - Python dtype: str

# Output types
- pos_g
    - The 'pos_g'output represents a mixed positive hint generated from the selected preset. It is a key component of the final output and reflects the combined effect of the input.
    - Comfy dtype: STRING
    - Python dtype: str
- pos_l
    - The output 'pos_l' is another mixed positive hint, reflecting different aspects of the input mix process. It contributes to overall consistency and the quality of the text generated.
    - Comfy dtype: STRING
    - Python dtype: str
- pos_r
    - The 'pos_r' output represents a further change in the mix of positive hints, providing additional depth to the text generation process.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_g
    - The 'neg_g' output is a mixed negative hint that has been processed to exclude elements that are not required in the final text generation.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_l
    - The 'neg_l' output represents another mixed negative hint to ensure that specific unwanted style elements are excluded from text generation.
    - Comfy dtype: STRING
    - Python dtype: str
- neg_r
    - The 'neg_r' output is the final change in the mixture of negative hints, providing elements for text generation that are fully excluded from need.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PromptMixer:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'prompt_positive': ('STRING', {'multiline': True, 'default': 'BASE_POSITIVE'}), 'prompt_negative': ('STRING', {'multiline': True, 'default': 'BASE_NEGATIVE'}), 'style_positive': ('STRING', {'multiline': True, 'default': 'REFINER_POSTIVE'}), 'style_negative': ('STRING', {'multiline': True, 'default': 'REFINER_NEGATIVE'}), 'preset': (['preset 1', 'preset 2', 'preset 3', 'preset 4', 'preset 5'],)}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING', 'STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('pos_g', 'pos_l', 'pos_r', 'neg_g', 'neg_l', 'neg_r')
    FUNCTION = 'mixer'
    CATEGORY = icons.get('Comfyroll/Essential/Legacy')

    def mixer(self, prompt_positive, prompt_negative, style_positive, style_negative, preset):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Legacy-Nodes#cr-prompt-mixer'
        if preset == 'preset 1':
            pos_g = prompt_positive
            pos_l = prompt_positive
            pos_r = prompt_positive
            neg_g = prompt_negative
            neg_l = prompt_negative
            neg_r = prompt_negative
        elif preset == 'preset 2':
            pos_g = prompt_positive
            pos_l = style_positive
            pos_r = prompt_positive
            neg_g = prompt_negative
            neg_l = style_negative
            neg_r = prompt_negative
        elif preset == 'preset 3':
            pos_g = style_positive
            pos_l = prompt_positive
            pos_r = style_positive
            neg_g = style_negative
            neg_l = prompt_negative
            neg_r = style_negative
        elif preset == 'preset 4':
            pos_g = prompt_positive + style_positive
            pos_l = prompt_positive + style_positive
            pos_r = prompt_positive + style_positive
            neg_g = prompt_negative + style_negative
            neg_l = prompt_negative + style_negative
            neg_r = prompt_negative + style_negative
        elif preset == 'preset 5':
            pos_g = prompt_positive
            pos_l = prompt_positive
            pos_r = style_positive
            neg_g = prompt_negative
            neg_l = prompt_negative
            neg_r = style_negative
        return (pos_g, pos_l, pos_r, neg_g, neg_l, neg_r)
```