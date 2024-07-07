# Documentation
- Class name: SamplerCustom
- Category: sampling/custom_sampling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SamplerCustom is designed to facilitate sampling processes in models. It integrates components such as noise additions, model processing and potential image operations to produce high-quality output. The node is designed to provide a customable and efficient sampling method that allows fine-tuning and control of the generation process.

# Input types
## Required
- model
    - Model parameters are essential for nodes because they define the production models used for sampling. They directly affect the quality and type of output generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - The positionive parameter provides information on the positive conditions that guide the sampling process towards the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative parameters provide information on negative orientation conditions in order to avoid undesirable features in the resulting samples.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- sampler
    - The sampler parameter specifies the sampling method to be used, which can significantly affect the efficiency and effectiveness of the sampling process.
    - Comfy dtype: SAMPLER
    - Python dtype: str
- sigmas
    - The sigmas parameter defines the level of noise to be used for each step of the sampling process, affecting noise reduction and image clarity.
    - Comfy dtype: SIGMAS
    - Python dtype: List[float]
- latent_image
    - The latent_image parameter is essential as it represents the potential input space from which the sampling process begins.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- add_noise
    - The add_noise parameter determines whether noise should be added to a potential image during the sampling period. This affects the diversity and randomity of the samples generated.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - The noise_seed parameter is used in the initial noise generation process to ensure the replicability of the sampling results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the sampling process to allow the user to control the level of authenticity and detail that generates the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - Output parameters represent the main result of the sampling process and include the potential samples generated.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- denoised_output
    - The denoised_output parameter provides a denoise version for the generation of the sample, which may provide clearer and more refined results.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerCustom:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': ('BOOLEAN', {'default': True}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'sampler': ('SAMPLER',), 'sigmas': ('SIGMAS',), 'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('output', 'denoised_output')
    FUNCTION = 'sample'
    CATEGORY = 'sampling/custom_sampling'

    def sample(self, model, add_noise, noise_seed, cfg, positive, negative, sampler, sigmas, latent_image):
        latent = latent_image
        latent_image = latent['samples']
        if not add_noise:
            noise = Noise_EmptyNoise().generate_noise(latent)
        else:
            noise = Noise_RandomNoise(noise_seed).generate_noise(latent)
        noise_mask = None
        if 'noise_mask' in latent:
            noise_mask = latent['noise_mask']
        x0_output = {}
        callback = latent_preview.prepare_callback(model, sigmas.shape[-1] - 1, x0_output)
        disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
        samples = comfy.sample.sample_custom(model, noise, cfg, sampler, sigmas, positive, negative, latent_image, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=noise_seed)
        out = latent.copy()
        out['samples'] = samples
        if 'x0' in x0_output:
            out_denoised = latent.copy()
            out_denoised['samples'] = model.model.process_latent_out(x0_output['x0'].cpu())
        else:
            out_denoised = out
        return (out, out_denoised)
```