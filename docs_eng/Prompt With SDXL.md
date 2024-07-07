# Documentation
- Class name: PromptWithSDXL
- Category: Mikey
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

PromptWithSDXL node is designed to process and generate instructions for style and content generation tasks. It receives both positive and negative tips and styles, and uses various conversions to improve the quality of the content generated. The node is able to handle complex reminder structures and optimizes the generation of high-quality output.

# Input types
## Required
- positive_prompt
    - A positive reminder is the key input that guides the generation of content with the desired characteristics. It plays a crucial role in guiding the output towards the desired style and theme.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - Negative hints help refine the generation process by specifying what should be avoided. It is important to ensure that the final output does not contain unwanted elements.
    - Comfy dtype: STRING
    - Python dtype: str
- positive_style
    - Positive style parameters define the elements of style that you want to emphasize in generating content. This is essential for a harmonious aesthetic.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_style
    - The input allows the user to specify styles that should be minimized or excluded from generating content to ensure that the final output is consistent with the user's preferences.
    - Comfy dtype: STRING
    - Python dtype: str
- ratio_selected
    - The selected scale parameters determine the horizontal and vertical ratio of the content generated, which is essential for maintaining the visual integrity of the output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- batch_size
    - The batch size is an optional parameter that allows the user to control the number of samples generated in a single operation. It can be adjusted according to the computational resources available.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters are used to introduce randomity in a controlled manner, which is very useful for generating diversified output sets.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The sample output contains the potential expressions generated, which are at the core of the content generation process. These expressions can be further refined to produce the final output.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- positive_prompt_text_g
    - The positive hint text output provides the final form of the positive hint after all conversions have been applied. It reflects the required characteristics to be included in the creation content.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - This output presents a negative hint text after processing, detailing the elements that should be omitted from the generated content.
    - Comfy dtype: STRING
    - Python dtype: str
- positive_style_text_l
    - Positive style text output represents the final style preference that is processed and prepared to influence content generation.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_style_text_l
    - This output contains the negative style text that you want to avoid in creating the content.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - Width parameters indicate the width of the content generated, which is essential for maintaining the required vertical ratio and visual representation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters specify the height of the content generated and are used in conjunction with the width to ensure proper display and vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_width
    - The width of the finer output determines the width of the finer process, which is important for generating the final quality of the content.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_height
    - This output specifies the height of the fine-tuning process to ensure that the content details generated are appropriate and correspond to the required specifications.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class PromptWithSDXL:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        return {'required': {'positive_prompt': ('STRING', {'multiline': True, 'default': 'Positive Prompt'}), 'negative_prompt': ('STRING', {'multiline': True, 'default': 'Negative Prompt'}), 'positive_style': ('STRING', {'multiline': True, 'default': 'Positive Style'}), 'negative_style': ('STRING', {'multiline': True, 'default': 'Negative Style'}), 'ratio_selected': (s.ratio_sizes,), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('LATENT', 'STRING', 'STRING', 'STRING', 'STRING', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('samples', 'positive_prompt_text_g', 'negative_prompt_text_g', 'positive_style_text_l', 'negative_style_text_l', 'width', 'height', 'refiner_width', 'refiner_height')
    FUNCTION = 'start'
    CATEGORY = 'Mikey'
    OUTPUT_NODE = True

    def start(self, positive_prompt, negative_prompt, positive_style, negative_style, ratio_selected, batch_size, seed, prompt=None, extra_pnginfo=None):
        positive_prompt = search_and_replace(positive_prompt, extra_pnginfo, prompt)
        negative_prompt = search_and_replace(negative_prompt, extra_pnginfo, prompt)
        positive_prompt = process_random_syntax(positive_prompt, seed)
        negative_prompt = process_random_syntax(negative_prompt, seed)
        positive_prompt = find_and_replace_wildcards(positive_prompt, seed)
        negative_prompt = find_and_replace_wildcards(negative_prompt, seed)
        width = self.ratio_dict[ratio_selected]['width']
        height = self.ratio_dict[ratio_selected]['height']
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        ratio = min([width, height]) / max([width, height])
        (target_width, target_height) = (4096, 4096 * ratio // 8 * 8) if width > height else (4096 * ratio // 8 * 8, 4096)
        refiner_width = target_width
        refiner_height = target_height
        return ({'samples': latent}, str(positive_prompt), str(negative_prompt), str(positive_style), str(negative_style), width, height, refiner_width, refiner_height)
```