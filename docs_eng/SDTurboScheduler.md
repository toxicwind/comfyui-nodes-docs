# Documentation
- Class name: SDTurboScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SDturboScheduler is a node used to efficiently manage and schedule sampling operations within the framework of the diffusion model. It abstractes the complexity of sampling steps and noise processes and provides a simplified interface for generating the sigma values essential to the sampling process. This node ensures that the sampling process follows the specified parameters and allows for advanced control of the diffuse sampling process without going into the details of individual sampling steps.

# Input types
## Required
- model
    - Model parameters are essential because they represent the diffusion model that the scheduler will operate. This is the underlying element of the node to perform its sampling task, and the structure and parameters of the model determine the results of the sampling process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- steps
    - The step parameter is essential to define the number of turns that the sampling process will experience. It directly affects the particle size of the sampling process and is a key factor in controlling the trade-off between the time of calculation and the quality of the result.
    - Comfy dtype: INT
    - Python dtype: int
- denoise
    - Noise parameters are important because they control the level of noise reduction applied in the sampling process. They are a key component in achieving the required balance between detail preservation and noise elimination, thus affecting the visual authenticity of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sigmas
    - The sigmas output is a key component of the sampling process, representing the standard deviation used to guide the diffusion process. It is a key determinant of the quality of the sample, and its value directly affects the results of the sample generation.
    - Comfy dtype: SIGMAS
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SDTurboScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'steps': ('INT', {'default': 1, 'min': 1, 'max': 10}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, model, steps, denoise):
        start_step = 10 - int(10 * denoise)
        timesteps = torch.flip(torch.arange(1, 11) * 100 - 1, (0,))[start_step:start_step + steps]
        comfy.model_management.load_models_gpu([model])
        sigmas = model.model.model_sampling.sigma(timesteps)
        sigmas = torch.cat([sigmas, sigmas.new_zeros([1])])
        return (sigmas,)
```