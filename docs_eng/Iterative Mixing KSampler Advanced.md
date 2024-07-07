# Documentation
- Class name: IterativeMixingKSamplerAdv
- Category: test
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The node improves the potential expression of noise by gradually introducing a predefined set of potential vectors, with the aim of improving the quality and consistency of the samples generated.

# Input types
## Required
- model
    - Model parameters are essential because they define the generation network used to denoise and refine potential expressions.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- seed
    - Seeds are essential to the random processes involved in the denocture and sampling steps, ensuring the replicability and diversity of outputs.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration parameter is important because it adjusts the behaviour of the sampling process to affect the quality and characteristics of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name determines the sampling method used, which is essential for the iterative mix and final output.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameters are the key to the noise removal process and control the rate of noise reduction in the succession.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - Reconciliation is providing an important context for the generation process, leading to the generation of the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative reconciliations are essential to limit sampling space, prevent undesirable hypotheses and ensure consistency of results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image_batch
    - Potential image batches are the starting point of an iterative mixing process, and each element affects the refined trajectory.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- denoise
    - Noise parameters are essential for controlling the level of noise reduction at each step, balancing refinements and preventing hypotheses.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha_1
    - The Alpha-1 impact mixed plan determines how potential vectors can be mixed into noise processes to achieve the best results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- reverse_input_batch
    - Reverse input batch parameters alter the order of potential vectors and affect the progress and consistency of the iterative mix.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- blending_schedule
    - Mixed schemes play an important role in determining the rate of guiding potential vector consolidation, affecting the quality of the final samples.
    - Comfy dtype: COMBO
    - Python dtype: str
- stop_blending_at_pct
    - This parameter determines the percentage of mixed cessation, balances the impact of guiding potential vectors and ensures the desired level of detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_blending_at_pct
    - The condensed percentage parameters limit the impact of mixing, prevent over-mixing and maintain the integrity of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blending_function
    - The mixed function defines the mathematical calculations that are used to group the potential vectors and the noise samples to influence the final appearance of the output.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- mixed_latents
    - Combining potential vectors represents potential indications of iterative refining, which is the core of the node output.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noised_latents
    - The initial noise state of the batch is captured by the potential vector of noise to inform the noise removal process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- intermediate_latents
    - These intermediate potential vectors document the progress of the iterative blending process and provide insights into refining the trajectories.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- plot_image
    - The drawing image visualization mix plan provides a graphical representation of the iterative mix process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class IterativeMixingKSamplerAdv:
    """
    Take a batch of latents, z_prime, and progressively de-noise them
    step by step from z_prime[0] to z_prime[steps], mixing in a weighted
    fraction of z_prime[i] at each step so that de-noising is guided by
    the z_prime latents. This batch sampler assumes that the number of steps
    is just the length of z_prime, so there is no steps parameter. The parameter
    latent_image_batch should come from the Batch Unsampler node. The parameter
    alpha_1 controls an exponential cosine function that schedules how much
    of the noised latents to mix with the de-noised latents at each step.
    Small values cause more of the noised latents to be mixed in at each step,
    which provides more guidance to the diffusion, but which may result in more
    artifacts. Large values (i.e. >1.0) can cause output to be grainy. Your
    mileage may vary.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image_batch': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'alpha_1': ('FLOAT', {'default': 2.4, 'min': 0.05, 'max': 100.0, 'step': 0.05}), 'reverse_input_batch': ('BOOLEAN', {'default': True}), 'blending_schedule': (list(BLENDING_SCHEDULE_MAP.keys()), {'default': 'cosine'}), 'stop_blending_at_pct': ('FLOAT', {'default': 1.0}), 'clamp_blending_at_pct': ('FLOAT', {'default': 1.0}), 'blending_function': (list(BLENDING_FUNCTION_MAP.keys()), {'default': 'addition'})}}
    RETURN_TYPES = ('LATENT', 'LATENT', 'LATENT', 'IMAGE')
    RETURN_NAMES = ('mixed_latents', 'noised_latents', 'intermediate_latents', 'plot_image')
    FUNCTION = 'sample'
    CATEGORY = 'test'

    def sample(self, model, seed, cfg, sampler_name, scheduler, positive, negative, latent_image_batch, denoise=1.0, alpha_1=0.1, reverse_input_batch=True, blending_schedule='cosine', stop_blending_at_pct=1.0, clamp_blending_at_pct=1.0, blending_function=list(BLENDING_FUNCTION_MAP.keys())[0]):
        sampler = IterativeMixingKSampler()
        return sampler(model, seed, cfg, sampler_name, scheduler, positive, negative, latent_image_batch, denoise=denoise, alpha_1=alpha_1, reverse_input_batch=True, blending_schedule=blending_schedule, stop_blending_at_pct=stop_blending_at_pct, clamp_blending_at_pct=clamp_blending_at_pct, blending_function=blending_function)
```