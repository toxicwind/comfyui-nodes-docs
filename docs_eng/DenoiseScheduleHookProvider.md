# Documentation
- Class name: DenoiseScheduleHookProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DenoiseScheduleHookProvider node is designed to manage and apply the noise plan to the image processing task. It provides a simple plan to adjust the noise level during the magnification process to improve image quality.

# Input types
## Required
- schedule_for_iteration
    - The schedule_for_itation parameters determine which noise plan to apply in the magnification process. It is essential to select the right strategy to improve image quality.
    - Comfy dtype: STRING
    - Python dtype: str
- target_denoise
    - The target_denoise parameter sets the desired level of noise to be achieved. It is a key factor in magnifying the final quality of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- hook
    - Hook output provides a well-positioned de-noise plan hook to control noise levels in the magnification process.
    - Comfy dtype: PK_HOOK
    - Python dtype: PixelKSampleHook

# Usage tips
- Infra type: CPU

# Source code
```
class DenoiseScheduleHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule_for_iteration': (s.schedules,), 'target_denoise': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('PK_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, schedule_for_iteration, target_denoise):
        hook = None
        if schedule_for_iteration == 'simple':
            hook = hooks.SimpleDenoiseScheduleHook(target_denoise)
        return (hook,)
```