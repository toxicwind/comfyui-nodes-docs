# Documentation
- Class name: KSamplerBasicPipe
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

KSamplerBavicPipe node is designed to perform sampling with the specified sampler and scheduler. It plays a key role in generating new potential expressions from the initial image that can be further processed or used to create new images. The node covers the complexity of sampling and provides a simple visual interface for users to obtain high-quality potential samples.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is a composite structure that contains the basic components required for sampling, including models, clips, vae, and positive/negative samples. It plays a key role in the sampling process and provides context for the generation of potential images.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, torch.nn.Module, Any, Any]
- seed
    - The Seed parameter initializes the random number generator to ensure the repeatability of the sampling process. It is essential for obtaining consistent results in different operations, which is particularly important in experimental and comparative studies.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters determine the number of turns to be performed during the sampling process. An increase in the number of steps can lead to a more refined potential indication, but also increases the costing.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameter, which is configured to control the sampling process. It affects the quality of the potential images collected and generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used in the sampling process. Different samplers may produce different results and select particular features that can be based on desired results or data.
    - Comfy dtype: KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the dispatch strategy for the sampling process. It is essential to manage the progress of the sampling process and can affect the efficiency and effectiveness of the sampling process.
    - Comfy dtype: KSampler.SCHEDULERS
    - Python dtype: str
- latent_image
    - The latent_image parameter is the initial potential indication that the sampling process will act. It is the starting point for generating new potential images.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- denoise
    - The denoise parameter controls the noise level of the potential image generated. Adjusting this value will help improve the quality of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- basic_pipe
    - Basic_pipe output contains original components for sampling and can be used for further processing or analysis.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, torch.nn.Module, Any, Any]
- latent
    - The output of latents represents potential images newly generated from the sampling process and can be used for various downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The vae output provides a variable coder model used in the sampling process, which can be used for additional operations or insights.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class KSamplerBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('BASIC_PIPE', 'LATENT', 'VAE')
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, basic_pipe, seed, steps, cfg, sampler_name, scheduler, latent_image, denoise=1.0):
        (model, clip, vae, positive, negative) = basic_pipe
        latent = nodes.KSampler().sample(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise)[0]
        return (basic_pipe, latent, vae)
```