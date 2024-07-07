# Documentation
- Class name: Tiled_KSampler
- Category: Sampling/Tiled
- Output node: False
- Repo Ref: https://github.com/FlyingFireCo/tiled_ksampler.git

The Tiled_KSampler node is designed to perform efficient sampling by dividing the sampling process into smaller, easier-to-manage levelled areas. It uses the smoothing concept to enhance the sampling process, thus enabling the processing of larger models and data sets. The node is designed to provide a powerful and scalable solution for sampling tasks in the categories within which it belongs.

# Input types
## Required
- model
    - Model parameters are essential for the Tiled_KSampler node, as they define the bottom model architecture for sampling. This parameter directly affects the execution of the node and the quality of the sample results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seed parameters initialize the random number generator to ensure the repeatability of the sampling process. It plays a key role in determining the starting point of the sampling overlap.
    - Comfy dtype: INT
    - Python dtype: int
- tiling
    - Tiled parameters specify whether the sampling should be carried out using a sheeting method. It is important to control the mode of operation of nodes and to influence the efficiency of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Step parameters determine the number of turns of the sampling process. It is a key factor in controlling the duration and thoroughness of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameter, which represents the configuration value, is used to control the parameters of the sampling process. It is an important factor in fine-tuning the performance of different sampling task nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the specific sampling method to be used within the node. It is essential to adjust the function of the node to the required sampling technology.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The scheduler parameters define the modem algorithm to be applied during the sampling process. It is a key component for managing the sampling steps and achieving the desired results.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positionive parameter provides information on the positive conditions that guide the sampling process towards the desired result. It is important to influence the direction of the sampling.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- negative
    - The negativ parameter provides information on negative conditions to prevent some of the results of the sampling process. It plays an important role in shaping the results of the sampling.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- latent_image
    - The latent_image parameter is a key input that represents the initial potential state of the sampling process. It lays the foundation for subsequent sampling overlaps.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- denoise
    - The denoise parameter adjusts the noise intensity during the sampling process and allows the noise reduction level to be controlled. This is an optional but useful setting to fine-tune the sample output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The potential output represents the potential state of the final sampling resulting from the sampling process. It is important because it contains the results of node operations and is used as an input for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Tiled_KSampler:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tiling': ('INT', {'default': 1, 'min': 0, 'max': 1}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'Sampling/Tiled'

    def apply_circular(self, model, enable):
        for layer in [layer for layer in model.modules() if isinstance(layer, torch.nn.Conv2d)]:
            layer.padding_mode = 'circular' if enable else 'zeros'

    def sample(self, model, seed, tiling, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        self.apply_circular(model.model, tiling == 1)
        return nodes.common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)
```