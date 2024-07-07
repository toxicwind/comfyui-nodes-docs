# Documentation
- Class name: BatchUnsampler
- Category: tests
- Output node: False
- Repo Ref: https://github.com/deroberon/demofusion-comfyui

The BatchUnsampler node is designed to generate a series of inverse expressions, starting with a given potential image. It uses the model's noise plan to gradually add noise to simulate the counter-prolife potential described in the original paper. The node is essential for testing and analysing the behaviour of spreading models under various noise conditions and sampling strategies.

# Input types
## Required
- model
    - Model parameters are essential for the BatchUnsampler node, as they provide a basic diffusion model that will be used to generate potential expressions. Model noise planning is particularly important for modelling reverse diffusion processes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- steps
    - The step parameter determines the number of potential intermediates to be generated. It is a key factor in controlling the particle size of the reverse diffusion process and the level of detail of the potential sequence to be generated.
    - Comfy dtype: INT
    - Python dtype: int
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used at the MatchUnsampler node. This selection effect is added to the noise method in the potential expression, thus influencing the characteristics of the generation sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- latent_image
    - The latent_image parameter is the key input for the BatchUnsampler node because it represents a potential image of the source that will generate the potential sequence of noise. This image is the starting point for the reverse diffusion process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- latent_batch
    - The flatt_batch output of BatchUnsampler nodes contains a number of potential expressions generated through reverse diffusion processes. These potential expressions are important for further analysis or as input to other nodes in the diffusion model pipeline.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class BatchUnsampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'end_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'step_increment': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'normalize': (['disable', 'enable'],), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latent_batch',)
    FUNCTION = 'unsampler'
    CATEGORY = 'tests'

    def unsampler(self, model, cfg, sampler_name, steps, end_at_step, step_increment, scheduler, normalize, positive, negative, latent_image):
        """
        Generate a batch of latents representing each z[i] in the
        progressively noised sequence of latents stemming from the
        source latent_image, using the model's noising schedule (sigma)
        in reverse and applying normal noise at each step in the manner
        prescribed by the original latent diffusion paper.
        """
        normalize = normalize == 'enable'
        device = comfy.model_management.get_torch_device()
        latent = latent_image
        latent_image = latent['samples']
        batch_of_latents = []
        end_at_step = min(end_at_step, steps - 1)
        end_at_step = steps - end_at_step
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device='cpu')
        noise_mask = None
        if 'noise_mask' in latent:
            noise_mask = comfy.sampler_helpers.prepare_mask(latent['noise_mask'], noise, device)
        real_model = model.model
        noise = noise.to(device)
        latent_image = latent_image.to(device)
        positive = comfy.sampler_helpers.convert_cond(positive)
        negative = comfy.sampler_helpers.convert_cond(negative)
        (models, inference_memory) = comfy.sampler_helpers.get_additional_models({'positive': positive, 'negative': negative}, model.model_dtype())
        comfy.model_management.load_models_gpu([model] + models, model.memory_required(noise.shape) + inference_memory)
        sampler = comfy.samplers.KSampler(real_model, steps=steps, device=device, sampler=sampler_name, scheduler=scheduler, denoise=1.0, model_options=model.model_options)
        sigmas = sampler.sigmas.flip(0)
        z = generate_noised_latents(latent_image, sigmas)
        logger.warning(f'latent_image.shape={latent_image.shape}')
        logger.warning(f'z.shape={z.shape}')
        out = {'samples': z}
        comfy.sampler_helpers.cleanup_additional_models(models)
        return (out,)
```