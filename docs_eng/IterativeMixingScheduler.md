# Documentation
- Class name: IterativeMixingScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

An iterative mixed scheduler node is designed to generate a range of noise levels, i.e. sigmas, which are used in the process of mixing noise levels from models. It uses the scheduler to control the progress of noise levels and can fine-tune the sampling process by adjusting the number of steps to the noise parameters.

# Input types
## Required
- model
    - Model parameters are essential because they represent the production model from which the sample is extracted. They are the building blocks that determine the underlying structure and capacity of the sampling process.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- scheduler
    - The scheduler parameter defines the strategy for adjusting noise levels during the sampling process. It plays an important role in determining the quality and condensability of the samples generated.
    - Comfy dtype: SCHEDULER_NAMES
    - Python dtype: str
- steps
    - The steps parameters specify the number of turns during the sampling process. It directly affects the particle size of the noise level, and thus the details and accuracy of the final sample.
    - Comfy dtype: INT
    - Python dtype: int
- denoise
    - Noise parameters allow fine-tuning of the sampling process by adjusting the rate at which the noise is removed. It may significantly affect the clarity and detail in which the samples are generated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sigmas
    - The sigmas output provides a sequence of calculated noise levels that guide the iterative sampling process. This is a key output that directly influences the generation of the final sample.
    - Comfy dtype: SIGMAS
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IterativeMixingScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'scheduler': (comfy.samplers.SCHEDULER_NAMES,), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    @torch.no_grad()
    def get_sigmas(self, model, scheduler, steps, denoise):
        sigmas = None
        cs = comfy.samplers.calculate_sigmas_scheduler
        if denoise is None or denoise > 0.9999:
            sigmas = cs(model.model, scheduler, steps).cpu()
        else:
            new_steps = int(steps / denoise)
            sigmas = cs(model.model, scheduler, new_steps).cpu()
            sigmas = sigmas[-(steps + 1):]
        return (sigmas,)
```