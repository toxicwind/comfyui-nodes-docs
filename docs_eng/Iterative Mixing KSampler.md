# Documentation
- Class name: IterativeMixingKSampler
- Category: test
- Output node: False
- Repo Ref: https://github.com/deroberon/demofusion-comfyui

The node refines a group of potential indications through the gradual introduction of a set of reference potential indications aimed at improving the quality of the samples generated through an iterative mix.

# Input types
## Required
- model
    - Generating models to denoise and fine-tune potential expressions.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seed values for random number generators for initial noise generation.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters that affect the noise removal process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The name of the sampler used for the iterative noise removal process.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - A schedule strategy to adjust the noise removal process over time.
    - Comfy dtype: ENUM
    - Python dtype: str
- step_increment
    - The number of steps that are added to each de-noise process.
    - Comfy dtype: INT
    - Python dtype: int
- positive
    - Positive reconciliation data used to guide the noise process.
    - Comfy dtype: CONDITIONING
    - Python dtype: dict
- negative
    - Negative reconciliation data used to further refine the noise removal process.
    - Comfy dtype: CONDITIONING
    - Python dtype: dict
- latent_image_batch
    - Potential batches need to be denominated and refined.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- denoise
    - Controls the parameters of the noise level applied at each step.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha_1
    - Parameters of the mixing rate between the potential indication of impact and the denoise sample.
    - Comfy dtype: FLOAT
    - Python dtype: float
- reverse_batch
    - A sign indicating whether batches should be reversed before processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latent_image_batch
    - Potential batches are fine-tuned after an iterative process of noise elimination.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IterativeMixingKSampler:
    """
    Take a batch of latents, z_prime, and progressively de-noise them
    step by step from z_prime[0] to z_prime[steps], mixing in a weighted
    fraction of z_prime[i] at each step so that de-noising is guided by
    the z_prime latents. This batch sampler assumes that the number of steps
    is just the length of z_prime, so there is no steps parameter. The parameter
    latent_image_batch should come from the Batch Unsampler node.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'step_increment': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image_batch': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'alpha_1': ('FLOAT', {'default': 3.0, 'min': 0.1, 'max': 10.0}), 'reverse_batch': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'test'

    def sample(self, model, seed, cfg, sampler_name, scheduler, step_increment, positive, negative, latent_image_batch, denoise=1.0, alpha_1=3.0, reverse_batch=True):
        if reverse_batch:
            latent_image_batch['samples'] = torch.flip(latent_image_batch['samples'], [0])
        return batched_ksampler(model, seed, cfg, sampler_name, scheduler, step_increment, positive, negative, latent_image_batch, denoise=denoise, alpha_1=alpha_1)
```