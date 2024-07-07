# Documentation
- Class name: IterativeMixingKSamplerSimple
- Category: test
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The node simplifies the iterative mix and sampling process, making it possible to add and remove noise efficiently in a single framework. It is designed to provide simplified workflows for users who want to try iterative sampling techniques but do not want to face multiple node complexities.

# Input types
## Required
- model
    - Model parameters are essential because they define the basis of the sampling process. They affect the quality and properties of the samples generated and are a core component of the node function.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- positive
    - Entering into the reconciliation is essential to guide the sampling process towards the desired result. It affects the direction and nature of the sample generation and makes it subject to the specified conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative adjustment input helps improve the sampling process by avoiding undesirable outcomes. It plays a key role in guiding the creation of properties far from being needed.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- latent_image
    - Potential image parameters are essential for the iterative mixing process, as they represent the starting point for adding and removing noise. They significantly influence the initial state and evolution of the sample.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- seed
    - Seed parameters are important to ensure the repeatability and consistency of the sampling process. It initializes random numbers generation, which in turn affects the variability and diversity of the output samples.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The step parameters determine the number of turns during the sampling process, directly affecting the complexity and accuracy of the samples generated.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters (or cfg) are essential for adjusting the internal set-up of the sampling process. It affects the overall behaviour and performance of the nodes so that they can fine-tune the best results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sample name parameter is essential for selecting the appropriate sampling method. It determines the strategy to be used to generate the sample, which can significantly change the final output.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - The scheduler parameter is essential to manage the progress of the sampling process. It controls the pace and timing of the succession and affects the efficiency and quality of the results.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- denoise
    - Noise parameters play an important role in the refining of the sample. It adjusts the level of noise loss and improves the clarity and quality of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha_1
    - The alpha_1 parameter is essential in controlling the mixing progress during the sampling process. It affects the way the sample is mixed and integrated and affects the final appearance and characteristics of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blending_schedule
    - Mixed progress parameters are key to defining the transition between samples. It determines the mix strategy, which can significantly influence the smoothness and consistency of the generation sequence.
    - Comfy dtype: COMBO[list(BLENDING_SCHEDULE_MAP.keys())]
    - Python dtype: str
- blending_function
    - The hybrid function parameter is essential to determine how the samples are combined during the iterative process. It influences the final result by controlling the sample to merge.
    - Comfy dtype: COMBO[list(BLENDING_FUNCTION_MAP.keys())]
    - Python dtype: str
- normalize_on_mean
    - The homogenization parameter is important for adjusting the pre-processing steps of the data. It affects the standardization of the input data and affects the sampling process and the characteristics of the samples generated.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- samples
    - The output samples represent the end result of an iterative mix and sampling process. They contain the essence of input parameters and node functions, demonstrating the ability of nodes to generate complex and sophisticated data patterns.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IterativeMixingKSamplerSimple:
    """
    A simplified version of IterativeMixingKSamplerAdv, this node
    does the noising (unsampling) and de-noising (sampling) all within
    one node with easy settings.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 40, 'min': 0, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'alpha_1': ('FLOAT', {'default': 2.4, 'min': 0.05, 'max': 100.0, 'step': 0.05}), 'blending_schedule': (list(BLENDING_SCHEDULE_MAP.keys()), {'default': 'cosine'}), 'blending_function': (list(BLENDING_FUNCTION_MAP.keys()), {'default': 'addition'}), 'normalize_on_mean': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'test'

    def __init__(self):
        self.batch_unsampler = BatchUnsampler()

    def sample(self, model, positive, negative, latent_image, seed, steps, cfg, sampler_name, scheduler, denoise, alpha_1, blending_schedule, blending_function, normalize_on_mean):
        (z_primes,) = self.batch_unsampler.unsampler(model, sampler_name, scheduler, steps, 0, steps, latent_image, normalize=normalize_on_mean)
        sampler = IterativeMixingKSampler()
        (z_out, _, _, _) = sampler(model, seed, cfg, sampler_name, scheduler, positive, negative, z_primes, denoise=denoise, alpha_1=alpha_1, reverse_input_batch=True, blending_schedule=blending_schedule, blending_function=blending_function, stop_blending_at_pct=1.0)
        return ({'samples': z_out['samples'][-1:]},)
```