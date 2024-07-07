# Timesteps Conditioning 🎭🅐🅓
## Documentation
- Class name: ADE_TimestepsConditioning
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node focuses on adjusting the application time of certain conditions during the animation or diffusion process, allowing for precise control over the time when certain effects or modifications are introduced in the animation process. This makes the application of conditions more dynamic and detailed, thus increasing the overall quality and flexibility of the content generated.

## Input types
### Required
- start_percent
    - Specifies the starting point for the application of the given conditions (as a percentage of the length of the total animation), allowing precise time control.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - Defines the end point of the application of the condition (as a percentage of the length of the total animation), allowing the effect to be customized to the specific stage of the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- timesteps_cond
    - Comfy dtype: TIMESTEPS_COND
    - The condition is time-adjusted and enclosed as a specific type, indicating the condition schedule throughout the animation or diffusion process.
    - Python dtype: TimestepsCond

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class ConditioningTimestepsNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "end_percent": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001})
            }
        }
    
    RETURN_TYPES = ("TIMESTEPS_COND",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning"
    FUNCTION = "create_schedule"

    def create_schedule(self, start_percent: float, end_percent: float):
        return (TimestepsCond(start_percent=start_percent, end_percent=end_percent),)