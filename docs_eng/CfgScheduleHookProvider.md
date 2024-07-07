# Documentation
- Class name: CfgScheduleHookProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

CfgScheduleHookProvider is designed to manage and provide a configuration schedule for the iterative process. By providing a simple interface, it retrieves hooks based on specified overlaps and target configurations, thus abstracting the complexity of dealing with different dispatch strategies.

# Input types
## Required
- schedule_for_iteration
    - The schedule_for_itation parameter determines the schedule to be used in the iterative process. It is crucial because it determines the method of configuration to be adjusted over time and influences the final outcome of the process.
    - Comfy dtype: STRING
    - Python dtype: str
- target_cfg
    - The target_cfg parameter sets the desired configuration value that the process aims to achieve. It is important because it directly affects the final configuration applied during the iterative process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- hook
    - Hook output provides a configured hook object that can be used to manage scheduling in an iterative process. It covers the logic needed to adjust the configuration over time.
    - Comfy dtype: PK_HOOK
    - Python dtype: PixelKSampleHook

# Usage tips
- Infra type: CPU

# Source code
```
class CfgScheduleHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_iteration': (s.schedules,), 'target_cfg': ('FLOAT', {'default': 3.0, 'min': 0.0, 'max': 100.0})}}
    RETURN_TYPES = ('PK_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, schedule_for_iteration, target_cfg):
        hook = None
        if schedule_for_iteration == 'simple':
            hook = hooks.SimpleCfgScheduleHook(target_cfg)
        return (hook,)
```