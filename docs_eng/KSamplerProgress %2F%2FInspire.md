# Documentation
- Class name: KSampler_progress
- Category: InspirePack/analysis
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The KSampler_progress node is designed to facilitate the sampling process by gradually introducing noise and fine-tuning potential indications within the specified number of steps. It enhances the exploration of the potential space of the model and provides insight into the behaviour of the model under different noise conditions.

# Input types
## Required
- model
    - Model parameters are essential because they define the sources of potential space to be explored. They are the basis for node operations and determine the types of samples that can be generated and analysed.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seeds are used for initialization of random number generators to ensure that sampling processes are replicable and consistent and play a key role in maintaining the integrity of the test results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the number of turns that the sampling process will experience. It directly affects the depth of potential space exploration and the particle size of the result.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters, usually referred to as 'cfg', to adjust the settings of the sampling process. It plays an important role in the operation of the micro-regulating point to achieve the desired results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used in the sampling process. It determines the strategy to be used over the potential space and has a significant impact on the quality of the sample.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - The scheduler parameters define the dispatch strategy for the sampling process. It is critical in managing the progress of noise introduction and the pace of sampling.
    - Comfy dtype: ENUM
    - Python dtype: str
- positive
    - The positionive parameter is used to provide the model with positive reconciliation data that can guide the sampling process towards the desired outcome. This is essential for directing the output to a particular result.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - The negative parameter is used to provide negative-conforming data, which helps to avoid characteristics that are not desired during the sampling process. It is essential to improve the quality of the samples generated.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - The latent_image parameter is the input that contains the initial sample or seed of the sampling process. It sets the starting point for the exploration and is essential for the generation of subsequent potential samples.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- denoise
    - The denoise parameter controls the level of noise reduction applied in the sampling process. It plays a key role in balancing potential space exploration against the clarity of the results sample.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_mode
    - The noise_mode parameter determines the mode of calculation for noise processing, whether GPU or CPU. It is important for optimizing the performance and efficiency of the sampling process.
    - Comfy dtype: ENUM
    - Python dtype: str
- interval
    - The spacing parameters specify the frequency of the intermediate samples collected during the sampling process. It affects the density of the data points captured and the details of progress tracking.
    - Comfy dtype: INT
    - Python dtype: int
- omit_start_latent
    - The omit_start_latet parameter decides whether to include an initial potential sample in the final output. It helps to manage the range of results, focusing on the evolution of the sample over time.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latent
    - The potential output represents a potential sample that is eventually refined after the sampling process. It encapsifies the results of the exploration and serves as a basis for further analysis or the generation of images.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any
- progress_latent
    - Progress_latet output provides an intermediate indication of the potential sample at the specified intervals of the sampling process. It provides insight into the sample over time and over time.
    - Comfy dtype: LATENT
    - Python dtype: List[Dict[str, Any]]

# Usage tips
- Infra type: GPU

# Source code
```
class KSampler_progress(a1111_compat.KSampler_inspire):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'interval': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'omit_start_latent': ('BOOLEAN', {'default': True, 'label_on': 'True', 'label_off': 'False'})}}
    CATEGORY = 'InspirePack/analysis'
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('latent', 'progress_latent')

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, noise_mode, interval, omit_start_latent):
        adv_steps = int(steps / denoise)
        sampler = a1111_compat.KSamplerAdvanced_inspire()
        if omit_start_latent:
            result = []
        else:
            result = [latent_image['samples']]
        for i in range(0, adv_steps + 1):
            add_noise = i == 0
            return_with_leftover_noise = i != adv_steps
            latent_image = sampler.sample(model, add_noise, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, i, i + 1, noise_mode, return_with_leftover_noise)[0]
            if i % interval == 0 or i == adv_steps:
                result.append(latent_image['samples'])
        if len(result) > 0:
            result = torch.cat(result)
            result = {'samples': result}
        else:
            result = latent_image
        return (latent_image, result)
```