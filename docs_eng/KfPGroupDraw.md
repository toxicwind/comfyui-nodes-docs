# Documentation
- Class name: KfPGroupDraw
- Category: experimental
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node visualizes a set of parameters into a curve map that allows for the analysis of changes in parameters over time or in other variables. It is designed to provide a graphical indication of the evolution of parameters, which is essential to understand the dynamics of the modeled system.

# Input types
## Required
- parameter_group
    - This parameter preserves a collection of a series of parameters, whose dynamics will be visualized. It is essential because it forms the basis for node operations, determines how the data are drawn and how visualizes the behaviour of the system.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, Any]
## Optional
- n
    - This parameter specifies the number of points to assess the curve. It affects the resolution of the chart, and the higher value can lead to a more smooth expression of the evolution of the parameter.
    - Comfy dtype: INT
    - Python dtype: int
- show_legend
    - This parameter controls whether the legend is shown in the chart. When you can visualize multiple groups of parameters, it is important to identify different curves.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- img_tensor
    - Output is the volume of a curved image that provides a visual summary of the evolution of parameters within the specified range.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class KfPGroupDraw:
    CATEGORY = f'{CATEGORY}/experimental'
    FUNCTION = 'main'
    RETURN_TYPES = ('IMAGE',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True}), 'n': ('INT', {'default': 64}), 'show_legend': ('BOOLEAN', {'default': True})}}

    def main(self, parameter_group, n, show_legend):
        img_tensor = plot_curve(parameter_group, n, show_legend, is_pgroup=True)
        return (img_tensor,)
```