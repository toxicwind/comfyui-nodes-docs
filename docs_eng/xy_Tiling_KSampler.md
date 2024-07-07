# Documentation
- Class name: xy_Tiling_KSampler
- Category: Jags_vector/xy_tile_sampler
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

The node facilitates the implementation of the sampling process by applying a levelling strategy that enhances the ability of the model to generate high-resolution images. It manages the levelling configuration and integrates with the model to produce the output that reflects the required levelling mode.

# Input types
## Required
- model
    - Model parameters are essential because they define the neural network structure used in the sampling process. They are the basis for node operations and determine the quality and characteristics of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - The seed parameter initializes the random number generator to ensure that the sampling process is replicable and consistent. It plays a vital role in maintaining the reliability of the results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the number of turns that the sampling process will experience. It directly affects the condensation and detail of the final output, and more steps may lead to more finer details of the image.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the model during the sampling process to influence the style and structure of the image generation. It is an important aspect of controlling creative output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects a particular sampling method from a predefined set of options. It plays an important role in adjusting node behaviour to different requirements and expected outcomes.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - Scheduler parameters control the rhythm and progress of the sampling process and ensure that nodes run efficiently and effectively. It is key to balancing performance and quality.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - The positive parameter provides the condition data that guides the sampling process towards desired characteristics. It is essential to guide the generation of specific results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative parameters introduce condition data that should be avoided during the sampling process. It helps to extract and remove unwanted features.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- latent_image
    - The latent_image parameter provides an initial potential indication of the process to be constructed. It is essential for setting the basis for image generation.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- tileX
    - The tileX parameter specifies whether to apply a tile in a horizontal direction. It affects the distribution and sequencing of the image sheeting.
    - Comfy dtype: INT
    - Python dtype: int
- tileY
    - The tileY parameter determines whether to apply a tile in a vertical direction. It affects the stacking and grouping of the image sheet.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- denoise
    - Decoupling parameters control the level of noise reduction applied during the sampling process. By minimizing noise, it contributes to a clearer and more refined output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - Potential parameters represent the intermediate potentials generated during the sampling process. It is a key step in achieving the final image generation.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- progress_latent
    - The potential parameters of progress capture the potential signs of evolution as the sampling progresses. It reflects the iterative refinement of the image to its state of completion.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class xy_Tiling_KSampler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'tileX': ('INT', {'default': 1, 'min': 0, 'max': 2}), 'tileY': ('INT', {'default': 1, 'min': 0, 'max': 2})}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('latent', 'progress_latent')
    FUNCTION = 'sample'
    CATEGORY = 'Jags_vector/xy_tile_sampler'

    def apply_asymmetric_tiling(self, model, tileX, tileY):
        for layer in [layer for layer in model.modules() if isinstance(layer, torch.nn.Conv2d)]:
            layer.padding_modeX = 'circular' if tileX else 'constant'
            layer.padding_modeY = 'circular' if tileY else 'constant'
            layer.paddingX = (layer._reversed_padding_repeated_twice[0], layer._reversed_padding_repeated_twice[1], 0, 0)
            layer.paddingY = (0, 0, layer._reversed_padding_repeated_twice[2], layer._reversed_padding_repeated_twice[3])
            print(layer.paddingX, layer.paddingY)

    def __hijackConv2DMethods(self, model, tileX: bool, tileY: bool):
        for layer in [l for l in model.modules() if isinstance(l, torch.nn.Conv2d)]:
            layer.padding_modeX = 'circular' if tileX else 'constant'
            layer.padding_modeY = 'circular' if tileY else 'constant'
            layer.paddingX = (layer._reversed_padding_repeated_twice[0], layer._reversed_padding_repeated_twice[1], 0, 0)
            layer.paddingY = (0, 0, layer._reversed_padding_repeated_twice[2], layer._reversed_padding_repeated_twice[3])

            def make_bound_method(method, current_layer):

                def bound_method(self, *args, **kwargs):
                    return method(current_layer, *args, **kwargs)
                return bound_method
            bound_method = make_bound_method(self.__replacementConv2DConvForward, layer)
            layer._conv_forward = bound_method.__get__(layer, type(layer))

    def __replacementConv2DConvForward(self, layer, input: torch.Tensor, weight: torch.Tensor, bias: Optional[torch.Tensor]):
        working = torch.nn.functional.pad(input, layer.paddingX, mode=layer.padding_modeX)
        working = torch.nn.functional.pad(working, layer.paddingY, mode=layer.padding_modeY)
        return torch.nn.functional.conv2d(working, weight, bias, layer.stride, (0, 0), layer.dilation, layer.groups)

    def __restoreConv2DMethods(self, model):
        for layer in [l for l in model.modules() if isinstance(l, torch.nn.Conv2d)]:
            layer._conv_forward = torch.nn.Conv2d._conv_forward.__get__(layer, torch.nn.Conv2d)

    def sample(self, model, seed, tileX, tileY, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        self.__hijackConv2DMethods(model.model, tileX == 1, tileY == 1)
        result = nodes.common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)
        self.__restoreConv2DMethods(model.model)
        return result
```