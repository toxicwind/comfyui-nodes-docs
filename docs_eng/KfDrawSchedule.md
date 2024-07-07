# Documentation
- Class name: KfDrawSchedule
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to visualize the schedule as defined in Keyframed and to abstract the complex schedule process into an easy-to-understand graphic expression. It converts the schedule plan into a series of weight curves, each corresponding to the contribution of a key frame that allows for analysis and understanding of movement dynamics.

# Input types
## Required
- schedule
    - The schedule parameter is essential because it defines the keyframed curve and its associated parameters, which are to be visualized by nodes. It is the main input that generates the weight curve and the result chart.
    - Comfy dtype: SCHEDULE
    - Python dtype: kf.Keyframed
## Optional
- n
    - The parameter 'n' is important for determining the resolution of the graphic. It affects the number of points in the curve sample, which may affect the clarity and detail of visualization.
    - Comfy dtype: INT
    - Python dtype: int
- show_legend
    - The parameter'show_legend' controls whether to display legends on the chart. This helps to distinguish different weight curves and to understand their respective contributions to the entire schedule.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- img_tensor
    - The output img_tensor represents a visualized image of the schedule entered as the result of the drawing. It encapsulates the weight curve and its dynamics and provides a clear and concise graphic summary of the schedule process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class KfDrawSchedule:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('IMAGE',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'schedule': ('SCHEDULE', {'forceInput': True}), 'n': ('INT', {'default': 64}), 'show_legend': ('BOOLEAN', {'default': True})}}

    def main(self, schedule, n, show_legend):
        curves = schedule_to_weight_curves(schedule)
        img_tensor = plot_curve(curves, n, show_legend, is_pgroup=True)
        return (img_tensor,)
```