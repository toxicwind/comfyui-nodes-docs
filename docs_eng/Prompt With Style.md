# Documentation
- Class name: PromptWithStyle
- Category: Mikey
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

The node is designed to generate creative tips by combining positive and negative text input and specified styles, thus generating diverse outputs that meet various demands for style and subject matter.

# Input types
## Required
- positive_prompt
    - The positionive_prompt parameter is essential for setting a positive tone for generating content. It is the basis for node construction of creative output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - The nigative_prompt parameters add to the mass and depth of the output by introducing comparative elements in the content generation process.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter determines the thematic direction and aesthetic quality of the content. It is a key factor in achieving an output with built-in coherence and style consistency.
    - Comfy dtype: COMBO
    - Python dtype: str
- ratio_selected
    - The profile influences the structural composition of the content to ensure that the output generated is consistent with the desired width ratio and formatting requirements.
    - Comfy dtype: STRING
    - Python dtype: str
- batch_size
    - Match_size parameters determine the number of unique outputs generated in a single operation, which is essential for the efficiency and scalability of content generation.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters introduce controlled randomity in the content generation process, ensuring that outputs are diverse and replicable to facilitate consistent experiments.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The samples output is a potential expression of content generation and provides a multifunctional basis for further processing and analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- positive_prompt_text_g
    - The postive_prompt_text_g output shows a processed version of the final positive hint, which has been customized for node creative objectives.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output, which provides refined negative hints, adds positive content and adds depth and contrast to overall output.
    - Comfy dtype: STRING
    - Python dtype: str
- positive_style_text_l
    - The output contains style elements associated with positive tips, which help to generate thematic consistency in content.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_style_text_l
    - Negative_style_text_l output reflects the style aspects of negative hints and enhances the diversity and richness of content.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The content output specifies the horizontal dimensions of the content structure and plays a key role in determining the layout and presentation of the output generated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height output defines the vertical dimensions of the content structure and is essential for the overall composition of the output and for visual appeal.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_width
    - Refiner_width output adjusts the width parameters to optimize the refining process and to ensure that the output is grinded and meets quality standards.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_height
    - The output of refiner_height sets vertical parameters for the refining process, which helps to improve the accuracy and detail of the final output.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class PromptWithStyle:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        (s.styles, s.pos_style, s.neg_style) = read_styles()
        return {'required': {'positive_prompt': ('STRING', {'multiline': True, 'default': 'Positive Prompt'}), 'negative_prompt': ('STRING', {'multiline': True, 'default': 'Negative Prompt'}), 'style': (s.styles,), 'ratio_selected': (s.ratio_sizes,), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('LATENT', 'STRING', 'STRING', 'STRING', 'STRING', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('samples', 'positive_prompt_text_g', 'negative_prompt_text_g', 'positive_style_text_l', 'negative_style_text_l', 'width', 'height', 'refiner_width', 'refiner_height')
    FUNCTION = 'start'
    CATEGORY = 'Mikey'
    OUTPUT_NODE = True

    def start(self, positive_prompt, negative_prompt, style, ratio_selected, batch_size, seed, prompt=None, extra_pnginfo=None):
        positive_prompt = search_and_replace(positive_prompt, extra_pnginfo, prompt)
        negative_prompt = search_and_replace(negative_prompt, extra_pnginfo, prompt)
        positive_prompt = process_random_syntax(positive_prompt, seed)
        negative_prompt = process_random_syntax(negative_prompt, seed)
        pos_prompt = find_and_replace_wildcards(positive_prompt, seed, debug=True)
        neg_prompt = find_and_replace_wildcards(negative_prompt, seed, debug=True)
        if pos_prompt != '' and pos_prompt != 'Positive Prompt' and (pos_prompt is not None):
            if '{prompt}' in self.pos_style[style]:
                pos_prompt = self.pos_style[style].replace('{prompt}', pos_prompt)
            elif self.pos_style[style]:
                pos_prompt = pos_prompt + ', ' + self.pos_style[style]
        else:
            pos_prompt = self.pos_style[style]
        if neg_prompt != '' and neg_prompt != 'Negative Prompt' and (neg_prompt is not None):
            if '{prompt}' in self.neg_style[style]:
                neg_prompt = self.neg_style[style].replace('{prompt}', neg_prompt)
            elif self.neg_style[style]:
                neg_prompt = neg_prompt + ', ' + self.neg_style[style]
        else:
            neg_prompt = self.neg_style[style]
        width = self.ratio_dict[ratio_selected]['width']
        height = self.ratio_dict[ratio_selected]['height']
        ratio = min([width, height]) / max([width, height])
        (target_width, target_height) = (4096, 4096 * ratio // 8 * 8) if width > height else (4096 * ratio // 8 * 8, 4096)
        refiner_width = target_width
        refiner_height = target_height
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({'samples': latent}, str(pos_prompt), str(neg_prompt), str(self.pos_style[style]), str(self.neg_style[style]), width, height, refiner_width, refiner_height)
```