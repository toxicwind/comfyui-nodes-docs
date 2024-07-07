# Documentation
- Class name: StyleModelApply
- Category: conditioning/style_model
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `StyleModelApply'node is designed to integrate the style of the image into the production model. It accepts the output of the visual model and applies the style model to the conditions generation process, thus allowing for the creation of style output. The node plays a key role in the overall system by integrating the style elements into the production process seamlessly.

# Input types
## Required
- clip_vision_output
    - The parameter `clip_vision_output'is a volume representing the visual features extracted from the image. It is essential for the node, because it forms the basis for the conversion of the applied style. This input directly influences how the style is integrated into the production model and influences the aesthetic quality of the final output.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- style_model
    - Parameters `style_model'is a neural network module that captures and applies style features to the production process. It is a necessary component for node operations, as it defines the style that you want to integrate into the production of content.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- conditioning
    - Parameters `conventioning'is a list of multiple widgets, each containing two volumes representing different aspects of the condition data. These lengths are essential for guiding the generation model to produce outputs that fit the style and subject matter elements required.
    - Comfy dtype: List[Tuple[torch.Tensor, torch.Tensor]]
    - Python dtype: List[Tuple[torch.Tensor, torch.Tensor]]

# Output types
- CONDITIONING
    - Output `Conditioning'is a list of multiple widgets, each containing two lengths, which have been styled and conditioned for modelling. This output is very important because it is entered directly into the generation process to influence the style and thematic consistency of the content generated.
    - Comfy dtype: List[Tuple[torch.Tensor, torch.Tensor]]
    - Python dtype: List[Tuple[torch.Tensor, torch.Tensor]]

# Usage tips
- Infra type: GPU

# Source code
```
class StyleModelApply:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'style_model': ('STYLE_MODEL',), 'clip_vision_output': ('CLIP_VISION_OUTPUT',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'apply_stylemodel'
    CATEGORY = 'conditioning/style_model'

    def apply_stylemodel(self, clip_vision_output, style_model, conditioning):
        cond = style_model.get_cond(clip_vision_output).flatten(start_dim=0, end_dim=1).unsqueeze(dim=0)
        c = []
        for t in conditioning:
            n = [torch.cat((t[0], cond), dim=1), t[1].copy()]
            c.append(n)
        return (c,)
```