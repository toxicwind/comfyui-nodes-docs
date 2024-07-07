# Documentation
- Class name: KfSinusoidalAdjustPhase
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to modify the phase of the sine curve to allow for timing of the wave to be adjusted without changing its basic characteristics, such as wavelength and amplitude.

# Input types
## Required
- curve
    - The input curve parameter is necessary because it defines the base sine curve that will be adjusted to the phase by the node operation.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve
## Optional
- adjustment
    - The adjustment parameter is a floating point value that affects the degree of phase shift applied to the input curve and the timing of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - The output represents a modified sine curve of the adjusted phase, which can be further used in applications that require dynamic wave adjustments.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- sinusoidal_curve
    - This output is the same as the modified sine curve and provides a consistent expression of the phase-adjusted wave for downstream processes.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalAdjustPhase:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE', 'SINUSOIDAL_CURVE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True}), 'adjustment': ('FLOAT', {'default': 0.0, 'step': 0.1308996939})}}

    def main(self, curve, adjustment):
        (wavelength, phase, amplitude) = (curve.wavelength, curve.phase, curve.amplitude)
        phase += adjustment
        curve = kf.SinusoidalCurve(wavelength=wavelength, phase=phase, amplitude=amplitude)
        return (curve, curve)
```