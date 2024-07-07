# Documentation
- Class name: KSampler_inspire
- Category: InspirePack/a1111_compat
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to facilitate the sampling process from the given model, using parameters to control the generation of new potential samples. It emphasizes the flexibility and adaptability of the sampling process and allows for the exploration of diversified results within the defined configuration.

# Input types
## Required
- model
    - Model parameters are essential because they define the source of the data and the basis of the sampling process. Nodes cannot perform their intended functions without a model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seeds play an important role in ensuring the repeatability and randomity of the sampling process. They are a key factor in controlling the generation of the only sample.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The steps define the progress of the sampling process and determine the number of turns that the algorithm will implement. This directly affects the diversity and quantity of the output samples.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters are essential to fine-tune the behaviour of the sampling process. It affects the balance of exploration and use in the search space.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter determines the sampling strategy to be used, which is essential for the characterization of the results sample.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - The scheduler parameter is responsible for controlling the rhythm and adjustment of the sampling process. It plays a key role in optimizing the efficiency and effectiveness of the sampling.
    - Comfy dtype: ENUM
    - Python dtype: str
- positive
    - Reconciliation is being provided with an important background to guide the sampling process towards desired results. This is a key element in achieving the results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative adjustment as a filtering condition to remove unwanted features from the sampling process and to ensure that the output meets the specified constraints.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - Potential image parameters are essential for the sampling process, as they represent the starting point for generating a new sample. It sets the basis for subsequent conversions.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_mode
    - The noise mode determines the computational resources used for noise generation, which is essential for the sampling process. It affects the performance and efficiency of nodes.
    - Comfy dtype: ENUM
    - Python dtype: str
## Optional
- denoise
    - Noise parameters are important in improving the quality of the output samples by reducing noise. They contribute to a clearer and more consistent performance of the data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_seed_mode
    - The batch treatment model affects how seeds are managed in the batch, which may affect the diversity and uniqueness of the samples generated.
    - Comfy dtype: ENUM
    - Python dtype: str
- variation_seed
    - Variable seeds introduce variability in noise generation and contribute to the output of diversity of samples without changing core characteristics.
    - Comfy dtype: INT
    - Python dtype: int
- variation_strength
    - The intensity of variability regulates the extent to which noise is introduced and affects the subtle differences in the results sample.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- samples
    - Samples represent the output of the sampling process and contain new potential indications. They are the direct result of node execution and are valuable for further analysis or application.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class KSampler_inspire:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'batch_seed_mode': (['incremental', 'comfy', 'variation str inc:0.01', 'variation str inc:0.05'],), 'variation_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'variation_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'InspirePack/a1111_compat'

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, noise_mode, batch_seed_mode='comfy', variation_seed=None, variation_strength=None):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, noise_mode, incremental_seed_mode=batch_seed_mode, variation_seed=variation_seed, variation_strength=variation_strength)
```