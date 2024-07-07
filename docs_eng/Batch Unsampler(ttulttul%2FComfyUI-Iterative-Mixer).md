# Documentation
- Class name: BatchUnsampler
- Category: tests
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The BatchUnsampler class aims to apply reverse engineering to a range of potential variables, starting with a given potential image, and working gradually backwards. It uses the model's noise plan to generate a range of potential variables that can be very useful in understanding the internal expressions and noise dynamics of the model.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic structure and noise plan used to remove sampling operations. They are the basis for generating a sequence of oblivion potential variables and are essential to the function of the node.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- sampler_name
    - The sampler_name parameter is important because it determines the type of sampling method to be used in the de-sampling process. It affects the quality and properties of the potential variables generated, and thus the overall outcome of the de-noise sequence.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - Scheduler parameters are essential because they determine the tone-level dispatch strategy to be applied in the decoupling of sampling operations. It affects the smoothness and consistency of potential noise sequences, which is essential for accurate representation.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- steps
    - The Steps parameter is important because it defines the number of intermediate steps that can be used to remove potential variables from sampling. It directly affects the resolution and particle size of the noise potential sequence and affects the ability of the nodes to capture the details of the noise plan.
    - Comfy dtype: INT
    - Python dtype: int
- start_at_step
    - The start_at_step parameter specifies the initial steps to cancel the sample start. It sets the starting point for the noise sequence, which is essential to control the range of potential variables generated.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters mark the final step towards the end of the sample. It establishes the end point of the denoise sequence and affects the extent to which the potential variables are dissipated.
    - Comfy dtype: INT
    - Python dtype: int
- latent_image
    - The latent_image parameter is essential because it provides a potential image of the source from which the sample starts. It is the basis for generating the entire series of potential variables and is indispensable for the operation of the node.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
## Optional
- normalize
    - When the normalize parameter is enabled, the potential variables generated are adjusted to an average value of zero, which may be useful for some downstream applications. It modifys the output of the unsampled sample, which may enhance the comparability of the denominable variables.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latent_batch
    - The latent_batch output contains a potential variable sequence for noise removal, representing reverse engineering of the noise plan applied to the original potential image. It is an important result of the CatchUnsampler operation and provides valuable insights into the noise dynamics within the model.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchUnsampler:
    """
    Unsample a latent step by step back to the start of the noise schedule.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'steps': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 1, 'max': 10000}), 'latent_image': ('LATENT',), 'normalize': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latent_batch',)
    FUNCTION = 'unsampler'
    CATEGORY = 'tests'

    @torch.no_grad()
    def unsampler(self, model, sampler_name, scheduler, steps, start_at_step, end_at_step, latent_image, normalize=False):
        """
        Generate a batch of latents representing each z[i] in the
        progressively noised sequence of latents stemming from the
        source latent_image, using the model's noising schedule (sigma)
        in reverse and applying normal noise at each step in the manner
        prescribed by the original latent diffusion paper.
        """
        latent = latent_image
        latent_image = latent['samples']
        sigmas = calc_sigmas(model, sampler_name, scheduler, steps, start_at_step, end_at_step)
        sigmas = sigmas.flip(0)
        z = generate_noised_latents(latent_image, sigmas, normalize=normalize)
        out = {'samples': z}
        return (out,)
```