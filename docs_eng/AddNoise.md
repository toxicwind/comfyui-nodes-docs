# Documentation
- Class name: AddNoise
- Category: _for_testing/custom_sampling/noise
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

AddNoise nodes are designed to introduce random noise to potential images, which is a key step in the process of generating synthetic images. By scaling noises according to the designated sigmas, it then combines noise with potential images to produce noise output. This node is essential to simulate the noise properties inherent in image data, thus enhancing the diversity and authenticity of the images generated.

# Input types
## Required
- model
    - Model parameters are essential for Addnoise nodes because they determine models for sampling and processing potential images. They are the basis for node execution and directly affect the quality and properties of the noise images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- noise
    - Noise parameters are essential for AddNoise nodes because they provide random sources that will be integrated into potential images. The type and properties of noise can significantly influence the diversity and unpredictability of the output images.
    - Comfy dtype: NOISE
    - Python dtype: Callable[..., torch.Tensor]
- sigmas
    - The sigmas parameter determines the volume of noise to be added to a potential image. It plays a key role in controlling noise levels and the visual appearance of synthetic images.
    - Comfy dtype: SIGMAS
    - Python dtype: List[float]
- latent_image
    - The latent_image parameter is the core input of the AddNoise node, which represents the image data that will be modified by adding noise. Its structure and content are essential to the function of the node and to the final outcome of the image synthesis process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- latent
    - The output item parameter represents the noise image obtained after applying the AddNoise node. It encapsifies the composite data with the desired noise properties for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class AddNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'noise': ('NOISE',), 'sigmas': ('SIGMAS',), 'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'add_noise'
    CATEGORY = '_for_testing/custom_sampling/noise'

    def add_noise(self, model, noise, sigmas, latent_image):
        if len(sigmas) == 0:
            return latent_image
        latent = latent_image
        latent_image = latent['samples']
        noisy = noise.generate_noise(latent)
        model_sampling = model.get_model_object('model_sampling')
        process_latent_out = model.get_model_object('process_latent_out')
        process_latent_in = model.get_model_object('process_latent_in')
        if len(sigmas) > 1:
            scale = torch.abs(sigmas[0] - sigmas[-1])
        else:
            scale = sigmas[0]
        if torch.count_nonzero(latent_image) > 0:
            latent_image = process_latent_in(latent_image)
        noisy = model_sampling.noise_scaling(scale, noisy, latent_image)
        noisy = process_latent_out(noisy)
        noisy = torch.nan_to_num(noisy, nan=0.0, posinf=0.0, neginf=0.0)
        out = latent.copy()
        out['samples'] = noisy
        return (out,)
```