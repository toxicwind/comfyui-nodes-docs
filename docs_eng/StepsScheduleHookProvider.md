# Documentation
- Class name: StepsScheduleHookProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The StepsScheduleHookProvider node is designed to facilitate the creation and management of an iterative process's dispatch hook. It provides an abstract definition of the complexity of the plan, allowing users to specify the type of plan and target steps of the iterative process. The primary function of the node is to simplify the process of setting up an iterative workflow based on the user's choice of example.

# Input types
## Required
- schedule_for_iteration
    - The parameter'schedule_for_itation' is essential for determining the type of dispatch hook to be used. It determines the behaviour of the iterative process by choosing from a predefined plan. This parameter directly influences the execution strategy of the node and the mode of distribution generated.
    - Comfy dtype: STRING
    - Python dtype: str
- target_steps
    - The parameter'target_steps' defines the number of steps to take in the iterative process. It is a key factor in controlling the duration and scope of the process. This parameter is essential for adjusting the operation of nodes to meet the specific requirements or constraints of the current task.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- hook
    - The output 'hook' is a dispatch hook object that encapsifies the logic of managing the iterative process according to the specified plan and target steps. It is important because it represents the main output of the node and is used to control the iterative workflow.
    - Comfy dtype: PK_HOOK
    - Python dtype: PixelKSampleHook

# Usage tips
- Infra type: CPU

# Source code
```
class StepsScheduleHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_iteration': (s.schedules,), 'target_steps': ('INT', {'default': 20, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('PK_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, schedule_for_iteration, target_steps):
        hook = None
        if schedule_for_iteration == 'simple':
            hook = hooks.SimpleStepsScheduleHook(target_steps)
        return (hook,)
```