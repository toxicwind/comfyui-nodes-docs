# Documentation
- Class name: KfGetScheduleConditionAtTime
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is designed to extract and process condition data from the schedule at the given time point and provides a seamless analysis and use of the schedule at that time.

# Input types
## Required
- schedule
    - Schedule parameters are essential because they contain structured data and configurations that are necessary to determine the state of the specified time conditions. It is the main input that drives node operations.
    - Comfy dtype: SCHEDULE
    - Python dtype: dict
- time
    - Time parameters are essential, and it directs nodes to assess the exact timing of the schedule. It directly influences the output by determining which set of conditions will be extracted and processed.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONDITIONING
    - The output provides a detailed set of conditional data reflecting the status of the schedule of assigned times. It is a key information for further analysis and decision-making.
    - Comfy dtype: CONDITIONING
    - Python dtype: tuple

# Usage tips
- Infra type: CPU

# Source code
```
class KfGetScheduleConditionAtTime:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('CONDITIONING',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'schedule': ('SCHEDULE', {}), 'time': ('FLOAT', {})}}

    def main(self, schedule, time):
        lerped_cond = evaluate_schedule_at_time(schedule, time)
        return (lerped_cond,)
```