# Documentation
- Class name: Asymmetric_Tiled_KSampler
- Category: Sampling/Tiled
- Output node: False
- Repo Ref: https://github.com/FlyingFireCo/tiled_ksampler.git

The Asymmetric_Tiled_KSampler node is designed to perform efficient and customized sampling of potential space. It does so by applying asymmetric tiles to models, thus allowing the creation of images with seamless textures. This node is particularly suitable for creating large, high-resolution images by levelling smaller segments of images. It emphasizes flexibility and control in the sampling process, meeting a variety of creative and technological needs, rather than addressing the specifics of the bottom approach.

# Input types
## Required
- model
    - Model parameters are essential because they define the neural network structure used in the sampling process. They directly affect the ability of nodes to generate images and the quality of the results produced.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- seed
    - Seed parameters are important for the repeatability of the sampling process. They ensure that the same initial conditions lead to the same results, which are very valuable for debugging and coherent output generation.
    - Comfy dtype: INT
    - Python dtype: int
- tileX
    - The tileX parameter determines the horizontal behaviour along the X axis. It is essential to control how the image is divided into segments for the generation of seamless textures.
    - Comfy dtype: INT
    - Python dtype: int
- tileY
    - The tileY parameter controls the floors along the y axis, similar to the tileX, but used in a vertical direction. It plays an important role in the overall image map.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The step parameter specifies the number of turns that the sampling process will experience. It is a key factor in determining the level of detail and the shape of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameter, which represents the size of the configuration, is used to adjust the sensitivity of the sampling process to the input of conditions. It is a key factor in fine-tuning the output to meet specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter focuses on the sampling method to be used from the predefined options. It is essential to customize the sampling technology to the specific needs of the task at hand.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - Scheduler parameters determine the dispatch algorithm that will guide the sampling process. It is a significant factor in the efficiency and effectiveness of sampling operations.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positionive parameter provides the model with information on positive conditions to guide the sampling process towards the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- negative
    - Negative parameters provide negative conditions that help to avoid unnecessary features or hypotheses in the images generated.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- latent_image
    - The latent_image parameter is an input into the sampling process, representing the initial state or encoding of the image to be generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- denoise
    - The denoise parameter adjusts the level of noise reduction applied during the sampling process. It is an important control to balance image details with noise.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The output represents the final state of the image in potential space after the sampling process. It is important because it can be further processed or used to generate the final image.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Asymmetric_Tiled_KSampler:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tileX': ('INT', {'default': 1, 'min': 0, 'max': 1}), 'tileY': ('INT', {'default': 1, 'min': 0, 'max': 1}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'Sampling/Tiled'

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