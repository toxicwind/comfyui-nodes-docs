# Documentation
- Class name: UnsamplerDetailerHookProvider
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

UnsamplerDetailer HookProvider is designed to enhance the details of the sampling data by taking samples. It operates through the application of detailed anti-sampling hooks during the sampling process, allowing for more fine output. This node is essential for tasks requiring high detail quality, for example in image or signal processing applications.

# Input types
## Required
- model
    - Model parameters are essential for the UnsamplerDetailer HookProvider node, as it defines the bottom model that will be used to counter-sampling. Model selection can significantly influence the quality and properties of the sample data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- steps
    - The step parameter determines the number of steps to be used in the anti-sampling process. It is a key factor that affects the level of detail and the complexity of the calculation of the operation.
    - Comfy dtype: INT
    - Python dtype: int
- start_end_at_step
    - Start_end_at_step parameters specify steps in which the sampling process should begin to reduce detail enhancements over time.
    - Comfy dtype: INT
    - Python dtype: int
- end_end_at_step
    - End_end_at_step parameters mark the end of the anti-sampling process and mark the end of the detail enhancement phase.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the sampler to allow fine-tuning of the sampling process to achieve the desired result.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter identifies the specific sampler to be used in the cross-sampling process, which changes the nature of the sampling data.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - Scheduler parameters determine the dispatch strategy for the anti-sampling step, which optimizes the process to improve efficiency or quality.
    - Comfy dtype: STRING
    - Python dtype: str
- normalize
    - The normalize parameter determines whether data should be standardized during the cross-sampling process, which may improve consistency of results.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positionive parameters provide positive information on conditions that guide the anti-sampling process towards the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - The nigative parameter provides information on negative-introduction conditions in order to avoid undesirable results during the back-sampling process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- schedule_for_cycle
    - Schedule_for_cycle parameters specify whether the anti-sampling process should follow a circular plan, which is very useful for iterative refinement.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- DETAILER_HOOK
    - The output of the Unsampler Detailer HookProvider node is a detailed anti-sampling hook that can be used to inject additional details into the sampling process and improve the quality of the final output.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: DetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class UnsamplerDetailerHookProvider:
    schedules = ['skip_start', 'from_start']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'steps': ('INT', {'default': 25, 'min': 1, 'max': 10000}), 'start_end_at_step': ('INT', {'default': 21, 'min': 0, 'max': 10000}), 'end_end_at_step': ('INT', {'default': 24, 'min': 0, 'max': 10000}), 'cfg': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'normalize': (['disable', 'enable'],), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'schedule_for_cycle': (s.schedules,)}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, model, steps, start_end_at_step, end_end_at_step, cfg, sampler_name, scheduler, normalize, positive, negative, schedule_for_cycle):
        try:
            hook = hooks.UnsamplerDetailerHook(model, steps, start_end_at_step, end_end_at_step, cfg, sampler_name, scheduler, normalize, positive, negative, from_start='from_start' in schedule_for_cycle)
            return (hook,)
        except Exception as e:
            print("[ERROR] UnsamplerDetailerHookProvider: 'ComfyUI Noise' custom node isn't installed. You must install 'BlenderNeko/ComfyUI Noise' extension to use this node.")
            print(f'\t{e}')
            pass
```