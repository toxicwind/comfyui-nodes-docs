# Documentation
- Class name: KfCurveDraw
- Category: experimental
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is visualized by drawing a given curve and generating an image of it. It is designed to give an abstract view of trends and fluctuations within the curve data point and to provide a visual analysis tool for understanding its behaviour over time.

# Input types
## Required
- curve
    - Curve parameters are essential for the running of nodes because they define data sets that are to be visualized. They contain key frames that represent a given point in time, each with a corresponding value.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
## Optional
- n
    - This parameter determines the number of points drawn on the curve, which affects the visible particle size. It ensures that the curve is adequately expressed for analysis.
    - Comfy dtype: INT
    - Python dtype: int
- show_legend
    - When this parameter is enabled, an example is added to the chart, which provides a reference for each curve and enhances visual clarity.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- img_tensor
    - Output is an image length that represents a curved curve. As a visual summary of data, it allows simple interpretation and further processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurveDraw:
    CATEGORY = f'{CATEGORY}/experimental'
    FUNCTION = 'main'
    RETURN_TYPES = ('IMAGE',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'curve': ('KEYFRAMED_CURVE', {'forceInput': True}), 'n': ('INT', {'default': 64}), 'show_legend': ('BOOLEAN', {'default': True})}}

    def main(self, curve, n, show_legend):
        img_tensor = plot_curve(curve, n, show_legend, is_pgroup=False)
        return (img_tensor,)
```