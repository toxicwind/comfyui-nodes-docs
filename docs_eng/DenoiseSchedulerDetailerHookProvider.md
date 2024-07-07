# Documentation
- Class name: DenoiseSchedulerDetailerHookProvider
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DenoiseSchedulerDetaler HookProvider node is designed to manage the noise plan for the process of fine-tuning. It provides a mechanism for adjusting the level of noise applied at different stages of the process to ensure a smooth transition from noise to detail.

# Input types
## Required
- schedule_for_cycle
    - The schedule_for_cycle parameter determines the noise plan to be followed during the fine-tuning cycle. It is vital because it determines the sequence of the noise steps, thus affecting the quality of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- target_denoise
    - The target_denoise parameter specifies the required noise level. It is important because it directly affects the clarity and detail of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- DETAILER_HOOK
    - The output of Denoise Scheduler Detailer HookProvider is a thin hook that covers the noise program. It's important because it directly affects the behaviour of the finer during the noise process.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: DetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class DenoiseSchedulerDetailerHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_cycle': (s.schedules,), 'target_denoise': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, schedule_for_cycle, target_denoise):
        hook = hooks.SimpleDetailerDenoiseSchedulerHook(target_denoise)
        return (hook,)
```