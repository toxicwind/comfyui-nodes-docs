# Documentation
- Class name: UnsamplerHookProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

UnsamplerHookProvider is designed to enhance the magnification process by applying the sampler hook in the image generation process. It adjusts the sampling strategy to the current dynamic step of the magnification process, allowing for fine-tuning of image quality. The node plays a key role in the image enhancement workflow, ensuring the highest quality of the image that is eventually exported, using the power of dynamic sampling techniques.

# Input types
## Required
- model
    - Model parameters are essential for UnsamplerHookProvider nodes, as they define the models to be used for image magnifying. The selection of models significantly influences the execution of nodes and the quality of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- steps
    - The step parameters determine the number of steps to be taken during the magnification process. It is a key factor in controlling the level of detail and the total time of implementation of the nodes.
    - Comfy dtype: INT
    - Python dtype: int
- start_end_at_step
    - Start_end_at_step parameters specify the initial steps to go to the sampler's hook operation. It is important to define the initial conditions under which the sampler's hook begins to influence the magnification process.
    - Comfy dtype: INT
    - Python dtype: int
- end_end_at_step
    - End_end_at_step parameters mark the final step in the decoupling of the sampler's hook. It is the key parameter for setting the endpoint of the decoder's hook for the magnifying process.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is used to configure the configuration of the sampler's hook. It plays an important role in customizing the magnification process to meet specific quality requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter identifies the sampling method to be used for the sampler's hook. It is a key component in determining the sampling strategy during the magnification process.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The Scheduler parameter determines the dispatch strategy to go to the sampler's hook operation. It is essential to manage the timing and sequence of sampling steps during the magnification process.
    - Comfy dtype: STRING
    - Python dtype: str
- normalize
    - The normalize parameter indicates whether input data should be standardized before processing. It affects node execution by possibly changing the scaling of input values.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positionive parameter provides positive reconciliation data for the decoder hooks, and influences the magnification process in the direction of desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - The nigative parameter provides negative rebalancing data for the decoder hook, leading the magnification process away from the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- schedule_for_iteration
    - The schedule_for_iteration parameter specifies the type of dispatch strategy to be used in the current magnification process over time. It is essential for the different strategies to be repeated to achieve the best results.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- hook
    - Hook output provides a sampler's hook object that is configured according to input parameters. It is important because it represents the core function of the node and allows the magnification process to be operated.
    - Comfy dtype: PK_HOOK
    - Python dtype: PixelKSampleHook

# Usage tips
- Infra type: CPU

# Source code
```
class UnsamplerHookProvider:
    schedules = ['simple']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'steps': ('INT', {'default': 25, 'min': 1, 'max': 10000}), 'start_end_at_step': ('INT', {'default': 21, 'min': 0, 'max': 10000}), 'end_end_at_step': ('INT', {'default': 24, 'min': 0, 'max': 10000}), 'cfg': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'normalize': (['disable', 'enable'],), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'schedule_for_iteration': (s.schedules,)}}
    RETURN_TYPES = ('PK_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, model, steps, start_end_at_step, end_end_at_step, cfg, sampler_name, scheduler, normalize, positive, negative, schedule_for_iteration):
        try:
            hook = None
            if schedule_for_iteration == 'simple':
                hook = hooks.UnsamplerHook(model, steps, start_end_at_step, end_end_at_step, cfg, sampler_name, scheduler, normalize, positive, negative)
            return (hook,)
        except Exception as e:
            print("[ERROR] UnsamplerHookProvider: 'ComfyUI Noise' custom node isn't installed. You must install 'BlenderNeko/ComfyUI Noise' extension to use this node.")
            print(f'\t{e}')
            pass
```