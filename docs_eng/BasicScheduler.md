# Documentation
- Class name: BasicScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

BasicScheduler nodes are designed to manage and calculate the sigma values used in the diffusion of images. It deals in abstraction with the complexity of determining the appropriate sigmas for each step, ensuring a smooth and consistent sampling process.

# Input types
## Required
- model
    - Model parameters are essential because they represent the basic model used for sampling. It affects how the scheduler calculates sigmas and is essential for the implementation of nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- scheduler
    - The scheduler parameter defines the type of plan used for sigma calculations. It is the key determinant of the sampling process and directly affects the output sigmas.
    - Comfy dtype: STRING
    - Python dtype: str
- steps
    - Step parameters specify the number of steps to be taken during the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- denoise
    - By influencing the clarity and detail of the output, it plays an important role in the quality of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sigmas
    - The sigmas output provides a calculation schedule of sigma values for each step of the sampling process. These values are essential to the diffusion process and directly affect the quality of the final image.
    - Comfy dtype: FLOAT[1]
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BasicScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'scheduler': (comfy.samplers.SCHEDULER_NAMES,), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, model, scheduler, steps, denoise):
        total_steps = steps
        if denoise < 1.0:
            if denoise <= 0.0:
                return (torch.FloatTensor([]),)
            total_steps = int(steps / denoise)
        sigmas = comfy.samplers.calculate_sigmas(model.get_model_object('model_sampling'), scheduler, total_steps).cpu()
        sigmas = sigmas[-(steps + 1):]
        return (sigmas,)
```