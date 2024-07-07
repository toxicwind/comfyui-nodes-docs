# Documentation
- Class name: KfSetKeyframe
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to manage and modify the planned key frame conditions to allow dynamic adjustment of parameters during model training.

# Input types
## Required
- keyframed_condition
    - This parameter is essential because it defines the conditions for setting the key frame, which are essential for controlling the behaviour of the model at a given interval.
    - Comfy dtype: KEYFRAMED_CONDITION
    - Python dtype: Dict[str, Any]
## Optional
- schedule
    - The plan parameter is important for defining the timing and frequency of model updates, which, combined with the key frame conditions, optimizes the training process.
    - Comfy dtype: SCHEDULE
    - Python dtype: Optional[kf.ParameterGroup]

# Output types
- schedule
    - The output is a modified plan with updated framework conditions, which is essential to guide the progress and performance of the model.
    - Comfy dtype: SCHEDULE
    - Python dtype: Tuple[kf.ParameterGroup, Dict[str, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSetKeyframe:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('SCHEDULE',)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'keyframed_condition': ('KEYFRAMED_CONDITION', {})}, 'optional': {'schedule': ('SCHEDULE', {})}}

    def main(self, keyframed_condition, schedule=None):
        schedule = set_keyframed_condition(keyframed_condition, schedule)
        return (schedule,)
```