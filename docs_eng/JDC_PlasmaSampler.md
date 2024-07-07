# Documentation
- Class name: PlasmaSampler
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

PlasmaSampler covers the process of generating samples from a given model, using a variety of parameters to control the sampling process, such as noise, number of steps and de-noise factors. It is designed to provide flexibility in sampling methods and to allow random and determinative methods for sample generation.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basic generation model from which the sample is extracted. It is the core of the sampling process and directly affects the quality and characteristics of the samples generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- noise_seed
    - Noise seed parameter initializes the random number generator to ensure that noise added to model input is recognizable. This parameter is essential for consistent results and control experiments.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the number of turns that the sampling process will experience. An increase in the number of steps can lead to more fine and detailed samples, but it will also increase the calculation time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the sampling process to affect the balance between the exploration and use of the potential space of the model. It is a key factor in determining the diversity and quality of the output samples.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Noise parameters control the level of noise reduction applied during the sampling process. It is important to improve the clarity and quality of the final sample, and a balance needs to be found between the noise and the signal.
    - Comfy dtype: FLOAT
    - Python dtype: float
- latent_noise
    - Potential noise parameters introduce additional noise in potential space, which encourages the production of more diverse and creative samples. It is a key factor in enhancing the diversity of output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - Sampler name parameters have selected the particular sampling method to be used, which significantly affects the efficiency and effectiveness of the sample generation process.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameters set out a schedule strategy for adjusting the parameters of the sampling process over time, which would improve the collection and stability of the samples generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - Positive parameters provide conditional data to guide the sampling process to produce samples that meet specific desired characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative parameters provide conditional data that help to remove features that are not needed in the generation of the sample and refine the overall results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - Potential image parameters are input indications of the potential space of the model and are essential for the sampling process to produce meaningful and consistent samples.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- distribution_type
    - The distribution type parameters provide a choice between default and random sampling strategies, affecting the diversity and uniqueness of the samples generated.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- latent
    - The potential parameter contains an output sample that represents the results of the sampling process. It is a key component because it contains generated data consistent with input parameters and model constraints.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class PlasmaSampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 100.0, 'step': 0.1}), 'denoise': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'latent_noise': ('FLOAT', {'default': 0.05, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'distribution_type': (['default', 'rand'],), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, model, noise_seed, steps, cfg, denoise, sampler_name, scheduler, positive, negative, latent_image, latent_noise, distribution_type):
        rand = False
        if distribution_type == 'rand':
            rand = True
        return common_ksampler(model, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, latent_noise, use_rand=rand)
```