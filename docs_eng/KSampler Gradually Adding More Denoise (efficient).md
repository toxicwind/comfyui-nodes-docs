# Documentation
- Class name: Gradually_More_Denoise_KSampler
- Category: ComfyUI-Frame-Interpolation/others
- Output node: True
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The Gradually_More_Denoise_KSampler node is designed to refine the noise process of potential images. It increases the noise intensity by applying a series of noise steps to achieve clearer output. This node is essential in a scenario that requires progressive enhancement of image quality, such as a smooth transition to the creation of animations or a gradual improvement in image clarity.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the generation models used to generate potential samples. They directly affect the quality and type of images generated and are a key component of the process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - It plays an important role in guiding model output towards more favourable or specific outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative condition parameters are used to inhibit some of the results during generation. It is important for fine-tuning model output to avoid undesirable features or characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- latent_image
    - The potential image parameter is the key input that contains the initial potential expression used to generate the noise output. It is the basis of the node function, as the quality of the final image depends to a large extent on the initial potential state.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- seed
    - The feed parameter is used to initialize the random number generator to ensure repeatability during the sampling process. While it is optional, it is important to obtain a consistent result when the node is rerun.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the number of turns during the sampling process. It affects the time of execution of the node and may affect the recovery of the sample to the desired result.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter, which represents the non-classifier steering ratio, is a key factor in controlling the balance between potential space exploration of the model and compliance with the conditions provided.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used in the node. It is important because it changes the properties that produce the sample and may lead to different visual outcomes.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - Scheduler parameters define the learning rate scheduler to be applied during the sampling process. It plays a role in optimizing the generation of samples, which may affect their quality.
    - Comfy dtype: STRING
    - Python dtype: str
- start_denoise
    - The start_denoise parameter sets the initial noise intensity, which is essential for generating the initial clarity of the image. It is a key factor in the ability of nodes to produce high-quality noise output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise_increment
    - The denoise_increment parameter indicates an increase in noise intensity in each next step. It is important to control the speed of image clarity.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise_increment_steps
    - The denoise_increment_steps parameter specifies the number of steps that will increase noise intensity. It is important to determine the total duration of the denoise process.
    - Comfy dtype: INT
    - Python dtype: int
- optional_vae
    - The optional_vae parameter allows the provision of optional variable self-codifiers, which can be used for additional processing or operation of potential indications.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Output types
- model
    - Model output parameters represent the generation models used in the sampling process. It is important because it is the basis on which potential samples are generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Information on the conditions that guide the generation process towards a favourable outcome is being provided to the condition output parameters.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative condition output parameters represent the condition information used to inhibit certain outcomes during generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- latent
    - Potential output parameters include potential expressions of images refined through sampling processes. These refined potential states are essential for generating high-quality images.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- vae
    - If provided as input, the vae output parameter represents the variable-based encoder for the additional processing used for the potential expression. It represents the result of the introduction of advanced technology for improvement.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class Gradually_More_Denoise_KSampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'start_denoise': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'denoise_increment': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.1}), 'denoise_increment_steps': ('INT', {'default': 20, 'min': 1, 'max': 10000})}, 'optional': {'optional_vae': ('VAE',)}}
    RETURN_TYPES = ('MODEL', 'CONDITIONING', 'CONDITIONING', 'LATENT', 'VAE')
    RETURN_NAMES = ('MODEL', 'CONDITIONING+', 'CONDITIONING-', 'LATENT', 'VAE')
    OUTPUT_NODE = True
    FUNCTION = 'sample'
    CATEGORY = 'ComfyUI-Frame-Interpolation/others'

    def sample(self, model, positive, negative, latent_image, optional_vae, seed, steps, cfg, sampler_name, scheduler, start_denoise, denoise_increment, denoise_increment_steps):
        if start_denoise + denoise_increment * denoise_increment_steps > 1.0:
            raise Exception(f"Max denoise strength can't over 1.0 (start_denoise={start_denoise}, denoise_increment={denoise_increment}, denoise_increment_steps={denoise_increment_steps}")
        copied_latent = latent_image.copy()
        out_samples = []
        for latent_sample in copied_latent['samples']:
            latent = {'samples': einops.rearrange(latent_sample, 'c h w -> 1 c h w')}
            gradually_denoising_samples = [common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=start_denoise + denoise_increment * i)[0]['samples'] for i in range(denoise_increment_steps)]
            out_samples.extend(gradually_denoising_samples)
        copied_latent['samples'] = torch.cat(out_samples, dim=0)
        return (model, positive, negative, copied_latent, optional_vae)
```