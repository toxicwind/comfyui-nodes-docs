# Documentation
- Class name: KfSinusoidalWithWavelength
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates sine curves with customable wavelength, phase and amplitude that allow for the creation of cyclical wave shapes for various applications.

# Input types
## Required
- wavelength
    - The wavelength determines the period of the sine curve and affects the distance between its overall length and its peak.
    - Comfy dtype: FLOAT
    - Python dtype: float
- phase
    - The phase moves the sine curve along the time line, changing its peak and the time of the valley relative to the starting point.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude controls the peak of the sine curve and the size of the valley, affecting the extent of its oscillation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - Output is a key frame curve object that represents the sine wave type and can be further operated or visualized.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.KfCurve
- sinusoidal_curve
    - This is a string curve derived from the input parameters, which encapsulates the waveforms generated for use in various contexts.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: keyframed.SinusoidalCurve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalWithWavelength:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE', 'SINUSOIDAL_CURVE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'wavelength': ('FLOAT', {'default': 12, 'step': 0.5}), 'phase': ('FLOAT', {'default': 0.0, 'step': 0.1308996939}), 'amplitude': ('FLOAT', {'default': 1, 'step': 0.01})}}

    def main(self, wavelength, phase, amplitude):
        curve = kf.SinusoidalCurve(wavelength=wavelength, phase=phase, amplitude=amplitude)
        return (curve, curve)
```