# Documentation
- Class name: KSamplerAdvanced_progress
- Category: InspirePack/analysis
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

KSamplerAdvanced_progress nodes are designed to improve the generation process by promoting advanced sampling procedures within the model and incorporating noise and scheduling mechanisms. It aims to improve the quality and diversity of the output by gradually adjusting the sampling parameters.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basic structure and learning outcomes that nodes will be used in the sampling process. It is the basis for node operations and determines the potential scope and nature of output generation.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- add_noise
    - The add_noise parameter is crucial, and it determines whether noise is introduced in the sampling process. This may lead to a more diversified and even more creative outcome, adding randomity to the output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - The noise_seed parameter is important because it provides the basis for randomity in noise generation. It ensures that noise patterns are recreated, which is important for consistent experiments and comparison of results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameter specifies the number of turns that the sampling process will experience. It directly affects the complexity and detail of the output, and more steps may lead to more refined results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a configuration value used to adjust the behaviour of the sampling process. It is a key factor in controlling the balance between exploration and utilization in output generation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used. It affects the strategy used to generate the output, which significantly changes the characteristics and distribution of the results.
    - Comfy dtype: SAMPLER
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the scheduling strategy for the sampling process over time. It plays an important role in achieving a dynamic balance between different aspects of generation, such as noise levels and sampling frequency.
    - Comfy dtype: SCHEDULER
    - Python dtype: str
- positive
    - The positionive parameter provides data that are being reconciled to guide the sampling process towards the desired results. It is essential to guide the generation in a particular direction, ensuring that the results meet certain criteria or expectations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative parameters provide negative-contribution data that help the sampling process avoid undesirable outcomes. They play a key role in refining output by preventing the generation of certain models or features.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - The latent_image parameter is the underlying potential expression of the sampling process. It is a key element because it directly affects the initial state and potential trajectory in which the output is generated.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- start_at_step
    - The start_at_step parameter specifies the starting point of the sampling process. It is important to define the iterative scope to be implemented, thus affecting the overall progress and timing of the generation.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters mark the end of the sampling process. Together with start_at_step, it determines the total number of steps that the process will cover, which directly affects the comprehensiveness of the results.
    - Comfy dtype: INT
    - Python dtype: int
- noise_mode
    - The noise_mode parameter sets out the calculation model for noise generation and processing. This is a key option that affects the performance and efficiency of nodes, and the GPU is better suited for intensive calculations, while the CPU applies to tasks with less resource consumption.
    - Comfy dtype: GPU(=A1111),CPU
    - Python dtype: str
- return_with_leftover_noise
    - Return_with_leftover_noise parameters determine whether the node returns the remaining noise with the potential sample. This may be useful for further analysis or for additional processing phases.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- interval
    - The interval parameter sets the frequency for the node to save a potential intermediate sample during the sampling process. It affects the particle size of the output and allows capture of the progress generated.
    - Comfy dtype: INT
    - Python dtype: int
- omit_start_latent
    - The omit_start_latet parameter determines whether to omit the initial potential sample from the output. This is useful in some workflows, such as starting points that are not interested or to reduce redundancy in the result.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_progress_latent_opt
    - The prev_progress_latet_opt parameter allows continuation of the previous sampling process and provides a way to attach new results to existing potential samples. This helps to create an expanded or iterative output.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- latent
    - The latent output represents the final potential sample produced by the node and contains the final results of the sampling process. It is a key component, as it provides the basis for further analysis or downstream treatment.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- progress_latent
    - Progress_latet output provides a range of potential intermediate samples captured at specific intervals during the sampling process. This feature is valuable for monitoring the evolution of production and understanding the dynamics of model behaviour.
    - Comfy dtype: LATENT
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvanced_progress(a1111_compat.KSamplerAdvanced_inspire):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.5, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'return_with_leftover_noise': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'}), 'interval': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'omit_start_latent': ('BOOLEAN', {'default': False, 'label_on': 'True', 'label_off': 'False'})}, 'optional': {'prev_progress_latent_opt': ('LATENT',)}}
    FUNCTION = 'sample'
    CATEGORY = 'InspirePack/analysis'
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('latent', 'progress_latent')

    def sample(self, model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, noise_mode, return_with_leftover_noise, interval, omit_start_latent, prev_progress_latent_opt=None):
        sampler = a1111_compat.KSamplerAdvanced_inspire()
        if omit_start_latent:
            result = []
        else:
            result = [latent_image['samples']]
        for i in range(start_at_step, end_at_step + 1):
            cur_add_noise = i == start_at_step and add_noise
            cur_return_with_leftover_noise = i != steps or return_with_leftover_noise
            latent_image = sampler.sample(model, cur_add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, i, i + 1, noise_mode, cur_return_with_leftover_noise)[0]
            print(f'{i}, {i + 1}')
            if i % interval == 0 or i == steps:
                result.append(latent_image['samples'])
        if len(result) > 0:
            result = torch.cat(result)
            result = {'samples': result}
        else:
            result = latent_image
        if prev_progress_latent_opt is not None:
            result['samples'] = torch.cat((prev_progress_latent_opt['samples'], result['samples']), dim=0)
        return (latent_image, result)
```