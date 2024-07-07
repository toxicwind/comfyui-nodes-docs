# Documentation
- Class name: WAS_Image_Perlin_Noise
- Category: WAS Suite/Image/Generate/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Perlin_Noise node is designed to generate Perlin noise patterns that can be used in graphic applications to create natural textures. It generates procedural noises using the Python image library based on specified parameters (e.g. width, height, scaling, eight degrees, continuity, and optional random seeds). This node is very useful for users seeking to introduce organic and diversified textures into the project, without the need for external image assets.

# Input types
## Required
- width
    - The `width' parameter determines the horizontal resolution of the noise image generated. This is a key factor in defining the output size and influencing the way noise patterns are displayed and used in graphic applications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The " height " parameter sets the vertical resolution of the noise image. Together with the " width", it creates a canvas of the image that Perlin noise will be rendered to influence the proportion of viewing noise details.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - The `scaling' parameter adjusts the size of the Perlin noise unit. It changes the density of the noise mode, with higher values leading to more complex and smaller noise units, while lower values produce more thinner and larger units.
    - Comfy dtype: INT
    - Python dtype: int
- octaves
    - The '8 degrees' parameter controls the number of frequency levels used to construct noise patterns. More eight degrees add complexity and detail to noise and create more natural and diverse textures.
    - Comfy dtype: INT
    - Python dtype: int
- persistence
    - The `continuity' parameter defines the rate of reduction of the amplitude between eight degrees consecutively. It affects the contrast between different noise layers and contributes to the formation of overall texture features.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- seed
    - The'seed' parameter is the optional integer used to initialize the random number generator to ensure repeatable noise patterns. When using the same seed value, it allows for consistent results.
    - Comfy dtype: INT
    - Python dtype: Optional[int]

# Output types
- image
    - The 'Image' output provides the generated Perlin noise as an image. It can be used further or directly for texture purposes in graphic applications.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Perlin_Noise:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'width': ('INT', {'default': 512, 'max': 2048, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 2048, 'min': 64, 'step': 1}), 'scale': ('INT', {'default': 100, 'max': 2048, 'min': 2, 'step': 1}), 'octaves': ('INT', {'default': 4, 'max': 8, 'min': 0, 'step': 1}), 'persistence': ('FLOAT', {'default': 0.5, 'max': 100.0, 'min': 0.01, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'perlin_noise'
    CATEGORY = 'WAS Suite/Image/Generate/Noise'

    def perlin_noise(self, width, height, scale, octaves, persistence, seed):
        WTools = WAS_Tools_Class()
        image = WTools.perlin_noise(width, height, octaves, persistence, scale, seed)
        return (pil2tensor(image),)
```