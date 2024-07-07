# Documentation
- Class name: WAS_KSampler
- Category: WAS Suite/Sampling
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_KSampler node is designed to perform sampling operations in the SAS package, using advanced sampling techniques to generate potential expressions. It plays a key role in creating new images or enhancing existing ones, making an important contribution to the entire image synthesis process.

# Input types
## Required
- model
    - Model parameters are essential for nodes because they define the underlying neural network structure used for sampling. They directly affect the quality and properties of the potential expression generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seed parameters are essential for determining the sexual outcome to initiate the sampling process. It ensures the recoupability of the result, which is critical for consistent image generation in different operations.
    - Comfy dtype: SEED
    - Python dtype: Union[int, str]
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used, which is essential for the operation of the nodes. Different samplers can produce different results, so this option is essential for achieving the desired result.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The scheduler parameters determine the learning rate plan for the sampling process, which is essential for the efficiency and effectiveness of the sampling algorithm. It may significantly affect the quality of the potential images generated.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - This is an important factor guiding the output in the desired direction.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, List[str]]
- negative
    - Negative parameters provide negative condition information to prevent sampling images from containing unwanted features. It is essential to ensure that the output is consistent with the specified constraints.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, List[str]]
- latent_image
    - The flatt_image parameter is the input of the sampling process, representing the initial state of the image to be refined. It is a basic component that sets the starting point for the creation or enhancement of the image.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- steps
    - The number of steps determines the number of turns during the sampling process, affecting the collection and detail of the ultimate potential images. More steps usually lead to more fine output.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter, which represents the ratio of non-classifier guides, adjusts the balance between content and randomity in the sample. It plays an important role in controlling the authenticity of the image generation and input conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Decord parameters control the level of noise reduction applied during the sampling process. This is a fine-tuning option that increases the clarity of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The images of potential output representatives sampled in coded form can be further processed or used as input for subsequent image generation tasks.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_KSampler:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'seed': ('SEED',), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'WAS Suite/Sampling'

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return nodes.common_ksampler(model, seed['seed'], steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)
```