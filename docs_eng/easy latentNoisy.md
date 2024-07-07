# Documentation
- Class name: latentNoisy
- Category: EasyUse/Latent
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The latentnoisy class facilitates the generation of potential noise samples, which is essential for various models. It manages the process of creating noise and applying it to the potential space of the model, allowing the randomity of the output to be manipulated. It is designed to integrate seamlessly with existing pipes and to enhance the overall flexibility and control of the production process.

# Input types
## Required
- sampler_name
    - The sampler_name parameter is essential for defining the type of sampler to be used in a potential space sampling process. It determines the algorithm method and behaviour, thus affecting the quality and characteristics of the samples generated.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - Scheduler parameters are essential for controlling learning rates or other parameters during the sampling process. They help fine-tune model performance and achieve better results.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- steps
    - The Steps parameter defines the number or duration of the sampling process. It is a key factor in determining the condensability and stability of the sample.
    - Comfy dtype: INT
    - Python dtype: int
- start_at_step
    - The start_at_step parameter specifies the starting point of the sampling process. It is important to control the timing and sequencing of operations within the current line.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters mark the end of the sampling process. It works with start_at_step parameters and determines the range of steps for sampling.
    - Comfy dtype: INT
    - Python dtype: int
- source
    - The source parameter determines whether the calculation should be performed on CPU or GPU. It significantly affects the performance and efficiency of the sampling process.
    - Comfy dtype: COMBO[['CPU', 'GPU']]
    - Python dtype: str
- seed
    - Seed parameters are essential to ensure the repeatability and consistency of the sampling process. It initializes the random number generator and influences the generation of noise.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- pipe
    - The pipe parameter is an optional input that provides additional context and settings for the sampling process. It can include detailed information about models, loader settings and other waterlines specific to the flow line.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- optional_model
    - The optional_model parameter allows you to specify a model to be used in the sampling process. It is particularly useful when a custom model is needed to be integrated into the flow line.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- optional_latent
    - The optional_latet parameter provides a way of supplying pre-generated potential samples. This is very useful for further processing or analysis and does not need to regenerate samples from the beginning.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Output types
- pipe
    - Pipe output contains updated currentline information, including generated noise samples. It is a key part of the process because it allows the flow line to be continued or terminated as a result.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- latent
    - The latent output contains a potential sample of noise generated. These samples are essential for the further processing or analysis of model workflows.
    - Comfy dtype: LATENT
    - Python dtype: dict
- sigma
    - The sigma output indicates a difference in the noise level between the beginning and the end of the sampling process. This is an important value that can be used to adjust the noise level in subsequent operations.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: GPU

# Source code
```
class latentNoisy:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'steps': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 1, 'max': 10000}), 'source': (['CPU', 'GPU'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'optional': {'pipe': ('PIPE_LINE',), 'optional_model': ('MODEL',), 'optional_latent': ('LATENT',)}}
    RETURN_TYPES = ('PIPE_LINE', 'LATENT', 'FLOAT')
    RETURN_NAMES = ('pipe', 'latent', 'sigma')
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Latent'

    def run(self, sampler_name, scheduler, steps, start_at_step, end_at_step, source, seed, pipe=None, optional_model=None, optional_latent=None):
        model = optional_model if optional_model is not None else pipe['model']
        batch_size = pipe['loader_settings']['batch_size']
        empty_latent_height = pipe['loader_settings']['empty_latent_height']
        empty_latent_width = pipe['loader_settings']['empty_latent_width']
        if optional_latent is not None:
            samples = optional_latent
        else:
            torch.manual_seed(seed)
            if source == 'CPU':
                device = 'cpu'
            else:
                device = comfy.model_management.get_torch_device()
            noise = torch.randn((batch_size, 4, empty_latent_height // 8, empty_latent_width // 8), dtype=torch.float32, device=device).cpu()
            samples = {'samples': noise}
        device = comfy.model_management.get_torch_device()
        end_at_step = min(steps, end_at_step)
        start_at_step = min(start_at_step, end_at_step)
        comfy.model_management.load_model_gpu(model)
        model_patcher = comfy.model_patcher.ModelPatcher(model.model, load_device=device, offload_device=comfy.model_management.unet_offload_device())
        sampler = comfy.samplers.KSampler(model_patcher, steps=steps, device=device, sampler=sampler_name, scheduler=scheduler, denoise=1.0, model_options=model.model_options)
        sigmas = sampler.sigmas
        sigma = sigmas[start_at_step] - sigmas[end_at_step]
        sigma /= model.model.latent_format.scale_factor
        sigma = sigma.cpu().numpy()
        samples_out = samples.copy()
        s1 = samples['samples']
        samples_out['samples'] = s1 * sigma
        if pipe is None:
            pipe = {}
        new_pipe = {**pipe, 'samples': samples_out}
        del pipe
        return (new_pipe, samples_out, sigma)
```