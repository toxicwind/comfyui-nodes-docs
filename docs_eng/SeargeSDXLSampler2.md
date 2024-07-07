# Documentation
- Class name: SeargeSDXLSampler2
- Category: Searge/_deprecated_/Sampling
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeSDXLSampler2 class enhances the quality and detail of the output by fine-tuning a potential image over a series of models. It uses a combination of basic models and fine-tuning models to gradually improve the expression form, adjust parameters to control the process and achieve the required level of detail and noise reduction.

# Input types
## Required
- base_model
    - The basic model is the basic neural network used for initial sampling. It is essential for building the general structure and quality of potential images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- base_positive
    - The underlying reconciliation is providing the base model with the critical context needed to generate accurate and relevant potential images.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- base_negative
    - The underlying negative regulation helps to fine-tune the sampling process by removing features or characteristics that are not required.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- refiner_model
    - The fine-tuning model improves the quality of potential images by applying advanced technology and fine-tuning outputs.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_positive
    - The fine-tuning is further fine-tuning the image by focusing on the particular details and characteristics required in the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- refiner_negative
    - The fine-tuning of negative adjustments ensures that the final image does not contain unwanted elements and maintains the integrity and quality of the fine-tuning process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - Potential images are initial indications and will be improved through an iterative sampling process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_seed
    - Noise seeds play an important role in controlling the randomity and variability of noise introduced in the sampling process, which affects the diversity and quality of results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps in the sampling process determines the level of detail and detail achieved by the final image.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration parameter is a key value that influences the overall behaviour and performance of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - Sampler name identification is a particular algorithm used in the sampling process, which can significantly affect the efficiency and effectiveness of the sampling.
    - Comfy dtype: SAMPLER_NAME
    - Python dtype: str
- scheduler
    - The scheduler determines the rhythm and progress of the sampling process and ensures a balanced and controlled fine-tuning.
    - Comfy dtype: SCHEDULER_NAME
    - Python dtype: str
- base_ratio
    - The basic scale parameters adjust the balance between the base model and the refined model to influence the focus and emphasis of the different stages of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Noise parameters control the level of noise reduction applied during the sampling process, directly affecting the clarity and sharpness of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- refiner_prep_steps
    - The refinement of preparatory steps for the pre-processing of potential images prior to the main sampling process may improve the quality and consistency of outputs.
    - Comfy dtype: INT
    - Python dtype: int
- noise_offset
    - Noise offset parameters introduce variations in noise seeds for fine-tuning models and contribute to the diversity of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_strength
    - The intensity of the process of fine-tuning the strength of the strength parameters, with higher values leading to more visible changes in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent_image
    - The output of potential images is the result of the sampling process, showing enhanced detail and reduced noise.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SeargeSDXLSampler2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'base_positive': ('CONDITIONING',), 'base_negative': ('CONDITIONING',), 'refiner_model': ('MODEL',), 'refiner_positive': ('CONDITIONING',), 'refiner_negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551600}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 200}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 30.0, 'step': 0.5}), 'sampler_name': ('SAMPLER_NAME', {'default': 'ddim'}), 'scheduler': ('SCHEDULER_NAME', {'default': 'ddim_uniform'}), 'base_ratio': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'refiner_prep_steps': ('INT', {'default': 0, 'min': 0, 'max': 10}), 'noise_offset': ('INT', {'default': 1, 'min': 0, 'max': 1}), 'refiner_strength': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 1.0, 'step': 0.05})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'Searge/_deprecated_/Sampling'

    def sample(self, base_model, base_positive, base_negative, refiner_model, refiner_positive, refiner_negative, latent_image, noise_seed, steps, cfg, sampler_name, scheduler, base_ratio, denoise, refiner_prep_steps=None, noise_offset=None, refiner_strength=None):
        base_steps = int(steps * (base_ratio + 0.0001))
        if noise_offset is None:
            noise_offset = 1
        if refiner_strength is None:
            refiner_strength = 1.0
        if refiner_strength < 0.01:
            refiner_strength = 0.01
        if denoise < 0.01:
            return (latent_image,)
        start_at_step = 0
        input_latent = latent_image
        if refiner_prep_steps is not None:
            if refiner_prep_steps >= base_steps:
                refiner_prep_steps = base_steps - 1
            if refiner_prep_steps > 0:
                start_at_step = refiner_prep_steps
                precondition_result = nodes.common_ksampler(refiner_model, noise_seed + 2, steps, cfg, sampler_name, scheduler, refiner_positive, refiner_negative, latent_image, denoise=denoise, disable_noise=False, start_step=steps - refiner_prep_steps, last_step=steps, force_full_denoise=False)
                input_latent = precondition_result[0]
        if base_steps >= steps:
            return nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, input_latent, denoise=denoise, disable_noise=False, start_step=start_at_step, last_step=steps, force_full_denoise=True)
        base_result = nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, input_latent, denoise=denoise, disable_noise=False, start_step=start_at_step, last_step=base_steps, force_full_denoise=True)
        return nodes.common_ksampler(refiner_model, noise_seed + noise_offset, steps, cfg, sampler_name, scheduler, refiner_positive, refiner_negative, base_result[0], denoise=denoise * refiner_strength, disable_noise=False, start_step=base_steps, last_step=steps, force_full_denoise=True)
```