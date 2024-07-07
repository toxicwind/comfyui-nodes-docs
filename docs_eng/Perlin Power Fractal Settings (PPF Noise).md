# Documentation
- Class name: PPFNoiseSettings
- Category: Power Noise Suite/Sampling/Settings
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node is designed to configure and set up power fractal noise, which is a programmed noise type used in various applications, such as computer graphics and simulations. It covers parameters that affect noise properties and ensures a high degree of control over the noise generation process.

# Input types
## Required
- X
    - The X-coordinate input is essential to define the space position within the noise function. It affects how the noise mode is generated and evolved on the X axis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- Y
    - Y-coordinate input is essential to determine the vertical position within the noise function, affecting the generation and evolution of noise mode on the Y axis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- Z
    - Z-coordinate input is necessary to specify the depth position within the noise function, affecting the generation and evolution of noise mode on the Z axis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- evolution
    - Evolution parameters control the progress of noise patterns over time, making noise landscape dynamic and evolutive.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame
    - Frame input is used for initial noise generation to ensure that the noise mode starts at a given point and evolves consistently.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - Scale parameters adjust the overall size and frequency of the noise mode to affect the particle size and detail level at which the noise is generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- octaves
    - Eight degrees determine the number of frequency layers in noise, contributing to the complexity and richness of noise patterns.
    - Comfy dtype: INT
    - Python dtype: int
- persistence
    - Continuity affects the smoothness of noise transitions, with higher values leading to a smoother gradient and lower values leading to more sudden changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lacunarity
    - The interval adjusts the interval between continuous frequency layers, affecting the overall structure and appearance of noise patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- exponent
    - Index parameters modify the contrast and clarity of noise, higher values increase the margin and create a clearer margin.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - Brightness adjusts the overall intensity of noise to positive values that increase the visibility of noise and negative values reduce it.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - Contrast parameters control the difference between the brightest and darkest parts of the noise and enhance or reduce the overall visual impact.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- ppf_settings
    - The output provides an integrated set of power fractal noise settings that encapsulate all configured parameters that can be used to generate and manipulate noise patterns accordingly.
    - Comfy dtype: PPF_SETTINGS
    - Python dtype: Dict[str, float]

# Usage tips
- Infra type: CPU

# Source code
```
class PPFNoiseSettings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'X': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'Y': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'Z': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'evolution': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': 0.0, 'step': 0.01}), 'frame': ('INT', {'default': 0, 'max': 99999999, 'min': 0, 'step': 1}), 'scale': ('FLOAT', {'default': 5, 'max': 2048, 'min': 2, 'step': 0.01}), 'octaves': ('INT', {'default': 8, 'max': 8, 'min': 1, 'step': 1}), 'persistence': ('FLOAT', {'default': 1.5, 'max': 23.0, 'min': 0.01, 'step': 0.01}), 'lacunarity': ('FLOAT', {'default': 2.0, 'max': 99.0, 'min': 0.01, 'step': 0.01}), 'exponent': ('FLOAT', {'default': 4.0, 'max': 38.0, 'min': 0.01, 'step': 0.01}), 'brightness': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.01})}}
    RETURN_TYPES = ('PPF_SETTINGS',)
    RETURN_NAMES = ('ppf_settings',)
    FUNCTION = 'power_fractal_settings'
    CATEGORY = 'Power Noise Suite/Sampling/Settings'

    def power_fractal_settings(self, X, Y, Z, evolution, frame, scale, octaves, persistence, lacunarity, exponent, brightness, contrast):
        return ({'X': X, 'Y': Y, 'Z': Z, 'evolution': evolution, 'frame': frame, 'scale': scale, 'octaves': octaves, 'persistence': persistence, 'lacunarity': lacunarity, 'exponent': exponent, 'brightness': brightness, 'contrast': contrast},)
```