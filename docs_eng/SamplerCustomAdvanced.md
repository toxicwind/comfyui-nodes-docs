# Documentation
- Class name: SamplerCustomAdvanced
- Category: sampling/custom_sampling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SamplerCustomAdvanced is designed to perform advanced sampling operations for potential images. It uses various components, such as noise generation, guidance and sampling mechanisms, to produce high-quality output. This node is essential in the custom sampling workflow and provides a complex method for generating and refining potential expressions.

# Input types
## Required
- noise
    - Noise parameters are essential to the sampling process because they introduce randomity in potential spaces, allowing for diversified output. They play an important role in determining the quality and diversity of sample images.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor
- guider
    - The lead parameter is essential to guide the sampling process to the desired result. It helps to refine potential indications by providing guidance based on specific criteria or targets.
    - Comfy dtype: GUIDER
    - Python dtype: torch.nn.Module
- sampler
    - Sampler parameters determine the sampling strategy to be used by nodes. It is a key determinant of the efficiency and effectiveness of the sampling process and affects the ability of nodes to generate high-real potential images.
    - Comfy dtype: SAMPLER
    - Python dtype: torch.nn.Module
- sigmas
    - The sigmas parameter represents the level or scale of noise used in the sampling process. It is important to control the volume and detail of noise in the generation of the image, thus affecting the overall quality of the output.
    - Comfy dtype: SIGMAS
    - Python dtype: torch.Tensor
- latent_image
    - The latent_image parameter is the input of the sampling process, representing the initial state of the potential expression. It is the basis for node operations, as it is the basis for generating the final sample image.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- output
    - The output parameter of the SamplerCustomAdvanced node contains potential images for sampling. It is the main result of node operations and is valuable for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- denoised_output
    - The denoised_output parameter provides a version of the decoupled sample of potential images. This output is particularly useful for priority applications for noise reduction.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerCustomAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'noise': ('NOISE',), 'guider': ('GUIDER',), 'sampler': ('SAMPLER',), 'sigmas': ('SIGMAS',), 'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('output', 'denoised_output')
    FUNCTION = 'sample'
    CATEGORY = 'sampling/custom_sampling'

    def sample(self, noise, guider, sampler, sigmas, latent_image):
        latent = latent_image
        latent_image = latent['samples']
        noise_mask = None
        if 'noise_mask' in latent:
            noise_mask = latent['noise_mask']
        x0_output = {}
        callback = latent_preview.prepare_callback(guider.model_patcher, sigmas.shape[-1] - 1, x0_output)
        disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
        samples = guider.sample(noise.generate_noise(latent), latent_image, sampler, sigmas, denoise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=noise.seed)
        samples = samples.to(comfy.model_management.intermediate_device())
        out = latent.copy()
        out['samples'] = samples
        if 'x0' in x0_output:
            out_denoised = latent.copy()
            out_denoised['samples'] = guider.model_patcher.model.process_latent_out(x0_output['x0'].cpu())
        else:
            out_denoised = out
        return (out, out_denoised)
```