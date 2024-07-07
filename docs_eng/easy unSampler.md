# Documentation
- Class name: unsampler
- Category: EasyUse/Sampler
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The unsampler class generates high-quality images from potential vectors through a sampling process. It is designed to be user-friendly and efficient, allowing the customization of parameters to achieve the desired results.

# Input types
## Required
- steps
    - The number of steps determines the progress of the sampling process, and more steps usually lead to an improvement in the quality of the image. This is a key parameter because it directly affects the output results.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - The parameter specifies the steps at which the sampling process should be terminated. It is important to control the duration of the sampling process and to calculate the cost.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters `cfg' that affect the behaviour of the sampling process, such as the level of detail and noise reduction levels in the generation of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter determines the sampling method used, which significantly alters the properties that generate the image.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - Scheduler parameters define sampling strategies to be adjusted over time, affecting the quality and consistency of the final output.
    - Comfy dtype: COMBO
    - Python dtype: str
- normalize
    - Harmonization is a pre-treatment step that enhances the stability and performance of the sampling process by ensuring standardization of input data.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- pipe
    - The “pipe” parameter is an optional input that contains the additional context and resources required for the sampling process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- optional_model
    - The 'optional_model'parameter allows the user to specify a custom model for the sampling process, thereby generating images with unique characteristics.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- optional_positive
    - The “optional_positionive” parameter provides the reconciliation data that can guide the sampling process towards the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- optional_negative
    - The 'optional_negative'parameter provides negative rebalancing data and helps to avoid creating features that do not want to appear in the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- optional_latent
    - The “optional_latet” parameters are used to provide initial potential vectors that can be improved during the sampling process.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Output types
- pipe
    - The "pipe" output includes the results of the sampling process, including the images generated and any additional context or resources used in the process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- latent
    - The "latet" output provides the ultimate potential vector that represents the generation of the image and can be further analysed or used as input for other processes.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Usage tips
- Infra type: GPU

# Source code
```
class unsampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'end_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'cfg': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'normalize': (['disable', 'enable'],)}, 'optional': {'pipe': ('PIPE_LINE',), 'optional_model': ('MODEL',), 'optional_positive': ('CONDITIONING',), 'optional_negative': ('CONDITIONING',), 'optional_latent': ('LATENT',)}}
    RETURN_TYPES = ('PIPE_LINE', 'LATENT')
    RETURN_NAMES = ('pipe', 'latent')
    FUNCTION = 'unsampler'
    CATEGORY = 'EasyUse/Sampler'

    def unsampler(self, cfg, sampler_name, steps, end_at_step, scheduler, normalize, pipe=None, optional_model=None, optional_positive=None, optional_negative=None, optional_latent=None):
        model = optional_model if optional_model is not None else pipe['model']
        positive = optional_positive if optional_positive is not None else pipe['positive']
        negative = optional_negative if optional_negative is not None else pipe['negative']
        latent_image = optional_latent if optional_latent is not None else pipe['samples']
        normalize = normalize == 'enable'
        device = comfy.model_management.get_torch_device()
        latent = latent_image
        latent_image = latent['samples']
        end_at_step = min(end_at_step, steps - 1)
        end_at_step = steps - end_at_step
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device='cpu')
        noise_mask = None
        if 'noise_mask' in latent:
            noise_mask = comfy.sample.prepare_mask(latent['noise_mask'], noise.shape, device)
        noise = noise.to(device)
        latent_image = latent_image.to(device)
        _positive = comfy.sampler_helpers.convert_cond(positive)
        _negative = comfy.sampler_helpers.convert_cond(negative)
        (models, inference_memory) = comfy.sampler_helpers.get_additional_models({'positive': _positive, 'negative': _negative}, model.model_dtype())
        comfy.model_management.load_models_gpu([model] + models, model.memory_required(noise.shape) + inference_memory)
        model_patcher = comfy.model_patcher.ModelPatcher(model.model, load_device=device, offload_device=comfy.model_management.unet_offload_device())
        sampler = comfy.samplers.KSampler(model_patcher, steps=steps, device=device, sampler=sampler_name, scheduler=scheduler, denoise=1.0, model_options=model.model_options)
        sigmas = sampler.sigmas.flip(0) + 0.0001
        pbar = comfy.utils.ProgressBar(steps)

        def callback(step, x0, x, total_steps):
            pbar.update_absolute(step + 1, total_steps)
        samples = sampler.sample(noise, positive, negative, cfg=cfg, latent_image=latent_image, force_full_denoise=False, denoise_mask=noise_mask, sigmas=sigmas, start_step=0, last_step=end_at_step, callback=callback)
        if normalize:
            samples -= samples.mean()
            samples /= samples.std()
        samples = samples.cpu()
        comfy.sample.cleanup_additional_models(models)
        out = latent.copy()
        out['samples'] = samples
        if pipe is None:
            pipe = {}
        new_pipe = {**pipe, 'samples': out}
        return (new_pipe, out)
```