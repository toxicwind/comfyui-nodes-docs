# Documentation
- Class name: KSampler_inspire_pipe
- Category: InspirePack/a1111_compat
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The KSampler_inspire_pipe node is designed to facilitate the generation of sampling processes within the model and to guide the generation of new potential expressions by integrating multiple parameters. It refines output by integrating random seeds, the number of steps specified, and the configuration settings. The main purpose of the node is to explore the potential space of the model by providing a structured but flexible framework that enhances the creative process.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is essential for the sampling process and provides the basic components required for the sampling process, including models and other relevant elements. It is the backbone of node operations and allows potential samples to be generated.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, ...]
- seed
    - Seed parameters are essential for introducing randomity in the sampling process, ensuring diversity and non-repetition of the samples generated. They serve as a starting point for random numbers, thus significantly influencing the soleness of the output.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameters specify the number of turns that the sampling process will experience, directly affecting the depth of potential space exploration. It is a key factor in determining the diversity and quality of samples to be generated.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter, as a configuration setting, fine-tunes the sampling process to allow adjustments to the behaviour and characteristics that produce the sample. It plays a key role in shaping the output of the node as a whole.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter plays an important role in selecting a suitable sampling strategy, which in turn affects the distribution and nature of the samples generated. It is a key decision point in the node function.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - The Scheduler parameter determines the dispatch strategy of the sampling process and manages the progress and rhythm of the generation process. It is essential to maintain a structured approach to sample generation.
    - Comfy dtype: ENUM
    - Python dtype: str
- latent_image
    - The latent_image parameter is the input of the sampling process, representing the initial state or context that the new sample will generate. It is part of the node operation as the basis for creating a new potential expression.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- denoise
    - The denoise parameter adjusts the level of noise reduction applied during the sampling process, affecting the clarity and quality of the samples generated. It is a key control for balancing noise and detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_mode
    - Noise_mode parameters specify the calculation mode for noise generation, either using GPU for accelerated processing or selecting CPUs. It affects the efficiency and performance of the sampling process.
    - Comfy dtype: ENUM
    - Python dtype: str
- batch_seed_mode
    - Match_seed_mode parameters to manage randomity between batches are essential to ensure diversity in the generation of samples. It affects the overall variability and consistency of the output.
    - Comfy dtype: ENUM
    - Python dtype: str
## Optional
- variation_seed
    - The variation_seed parameter introduces additional randomity in the sampling process and contributes to the diversity of output. It allows subtle changes in the samples produced and increases the scope of node creation.
    - Comfy dtype: INT
    - Python dtype: int
- variation_strength
    - The variation_strength parameter controls the intensity of changes in the generation of the sample, balancing the level of novelty with the original input. It is a key factor for diversification and an attractive set of outputs.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The latent parameter represents the output of the sampling process and contains the newly generated potential expression. It is a direct reflection of the main function of the node and covers the creation of the sampling process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- vae
    - The vae parameter, which consists of output-based variations from the encoder component, is essential for generating high-quality, structured expressions. It marks the internal integration of node functions into an advanced generation model.
    - Comfy dtype: VAE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class KSampler_inspire_pipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'batch_seed_mode': (['incremental', 'comfy', 'variation str inc:0.01', 'variation str inc:0.05'],), 'variation_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'variation_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT', 'VAE')
    FUNCTION = 'sample'
    CATEGORY = 'InspirePack/a1111_compat'

    def sample(self, basic_pipe, seed, steps, cfg, sampler_name, scheduler, latent_image, denoise, noise_mode, batch_seed_mode='comfy', variation_seed=None, variation_strength=None):
        (model, clip, vae, positive, negative) = basic_pipe
        latent = common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, noise_mode, incremental_seed_mode=batch_seed_mode, variation_seed=variation_seed, variation_strength=variation_strength)[0]
        return (latent, vae)
```