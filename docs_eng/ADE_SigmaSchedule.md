# Create Sigma Schedule 🎭🅐🅓
## Documentation
- Class name: ADE_SigmaSchedule
- Category: Animate Diff 🎭🅐🅓/sample settings/sigma schedule
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The ADE_SigmaSchedule node is designed to generate a sigma plan based on the given Beta plan. It abstractes the complexity of the sigma project creation and provides a simple way to obtain a sigma plan that corresponds to the specific model sample type and configuration.

## Input types
### Required
- beta_schedule
    - Specifies the Beta plan for generating the sigma plan. This parameter is critical because it determines the basic configuration of the derivative sigma plan.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: BetaSchedules.ALIAS_ACTIVE_LIST

## Output types
- sigma_schedule
    - Comfy dtype: SIGMA_SCHEDULE
    - Output of a sigma project object is essential for defining the noise level process in proliferation-based generation models.
    - Python dtype: SigmaSchedule (custom type from the animatediff package)

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class SigmaScheduleNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "beta_schedule": (BetaSchedules.ALIAS_ACTIVE_LIST,),
            }
        }
    
    RETURN_TYPES = ("SIGMA_SCHEDULE",)
    CATEGORY = "Animate Diff 🎭🅐🅓/sample settings/sigma schedule"
    FUNCTION = "get_sigma_schedule"

    def get_sigma_schedule(self, beta_schedule: str):
        model_type = ModelSamplingType.from_alias(ModelSamplingType.EPS)
        new_model_sampling = BetaSchedules._to_model_sampling(alias=beta_schedule,
                                                              model_type=model_type)
        return (SigmaSchedule(model_sampling=new_model_sampling, model_type=model_type),)