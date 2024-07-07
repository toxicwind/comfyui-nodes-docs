# Documentation
- Class name: GetSigma
- Category: latent/noise
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_Noise.git

The node is designed to calculate the sigma value, which is an indicator of the noise or letter ratio in the context of the generation model. It processes the output of the model within the specified step range to determine the sigma changes and provides insight into model behaviour and noise properties.

# Input types
## Required
- model
    - Model parameters are essential because they define the generation models to be analysed. They affect the entire process by identifying the data sources used to calculate the sigma values.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- sampler_name
    - The sampler name determines the method of sampling from the model, which in turn affects the sigma calculation as it affects the quality and distribution of sampling data.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - The scheduler parameter is essential because it controls the sampling process, including the noise removal process, which directly affects the sigma calculation by changing the noise level in the sample data.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- steps
    - The step parameters define the heterogeneity of the calculation of the sigma value and affect the comprehensiveness of noise analysis.
    - Comfy dtype: INT
    - Python dtype: int
- start_at_step
    - The parameter specifies the starting point for the sigma calculation, determines the initial state of noise analysis and its evolution in the specified step.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - The end-step parameters set the endpoint for the sigma calculation, affecting the final state of noise analysis and the overall change in sigma within the step.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- sigma
    - The output sigma values represent changes in noise properties within the specified step range and provide performance measures for models in terms of noise reduction and signal clarity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: GPU

# Source code
```
class GetSigma:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'steps': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'calc_sigma'
    CATEGORY = 'latent/noise'

    def calc_sigma(self, model, sampler_name, scheduler, steps, start_at_step, end_at_step):
        device = comfy.model_management.get_torch_device()
        end_at_step = min(steps, end_at_step)
        start_at_step = min(start_at_step, end_at_step)
        real_model = None
        comfy.model_management.load_model_gpu(model)
        real_model = model.model
        sampler = comfy.samplers.KSampler(real_model, steps=steps, device=device, sampler=sampler_name, scheduler=scheduler, denoise=1.0, model_options=model.model_options)
        sigmas = sampler.sigmas
        sigma = sigmas[start_at_step] - sigmas[end_at_step]
        sigma /= model.model.latent_format.scale_factor
        return (sigma.cpu().numpy(),)
```