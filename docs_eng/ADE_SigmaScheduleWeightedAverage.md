# Sigma Schedule Weighted Mean 🎭🅐🅓
## Documentation
- Class name: ADE_SigmaScheduleWeightedAverage
- Category: Animate Diff 🎭🅐🅓/sample settings/sigma schedule
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to create a new sigma plan by calculating the weighted averages of the two sigma plans provided. It allows for a mix of the characteristics of the two plans into a new plan based on the specified weighting factors.

## Input types
### Required
- schedule_A
    - The first sigma plan to mix. It's one of the bases for weighted averages.
    - Comfy dtype: SIGMA_SCHEDULE
    - Python dtype: SigmaSchedule
- schedule_B
    - The second sigma plan is mixed with the first. It contributes to the weighted average, supplementing the first plan.
    - Comfy dtype: SIGMA_SCHEDULE
    - Python dtype: SigmaSchedule
- weight_A
    - The weighting factor for the first sigma plan. It determines the ratio of characteristics for the first plan in the final mix plan.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- sigma_schedule
    - Comfy dtype: SIGMA_SCHEDULE
    - The results of the sigma plan are mixed with the two input plans according to the assigned weighting factors.
    - Python dtype: SigmaSchedule

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class WeightedAverageSigmaScheduleNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "schedule_A": ("SIGMA_SCHEDULE",),
                "schedule_B": ("SIGMA_SCHEDULE",),
                "weight_A": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.001}),
            }
        }
    
    RETURN_TYPES = ("SIGMA_SCHEDULE",)
    CATEGORY = "Animate Diff 🎭🅐🅓/sample settings/sigma schedule"
    FUNCTION = "get_sigma_schedule"

    def get_sigma_schedule(self, schedule_A: SigmaSchedule, schedule_B: SigmaSchedule, weight_A: float):
        validate_sigma_schedule_compatibility(schedule_A, schedule_B)
        new_sigmas = schedule_A.model_sampling.sigmas * weight_A + schedule_B.model_sampling.sigmas * (1-weight_A)
        combo_schedule = schedule_A.clone()
        combo_schedule.model_sampling.set_sigmas(new_sigmas)
        return (combo_schedule,)