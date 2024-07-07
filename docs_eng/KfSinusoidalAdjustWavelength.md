# Documentation
- Class name: KfSinusoidalAdjustWavelength
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

Such nodes provide a method of adjusting the wavelength of the string curve, effectively changing its cycle without affecting other features, such as phase or amplitude. Adjustments are applied in a way that maintains the overall shape of the curve to ensure smooth and continuous transformations that apply to the various applications that require fine-tuning the temporal characteristics of the curve.

# Input types
## Required
- curve
    - The input curve parameter is necessary to define the base string curve that you want to adjust the wavelength. This parameter directly affects the input of node processing and determines the starting properties of the curve before any adjustment is made.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve
## Optional
- adjustment
    - Adjusts the parameter as a multiplier for wavelength adjustment, allowing precise control to be applied to the extent of the change in the curve. It plays a vital role in fine-tuning the temporal properties of the sine curve.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - The output represents an adjusted sine curve, reflecting the results of node processing. It is important because it provides an updated curve that can be used for follow-up or visualization.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- sinusoidal_curve
    - This output is the same as the 'curve' output and provides a further-used adjusted sine curve. It ensures that users can access the modified curve in its new form and fit into various workflows.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalAdjustWavelength:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE', 'SINUSOIDAL_CURVE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True}), 'adjustment': ('FLOAT', {'default': 0.0, 'step': 0.5})}}

    def main(self, curve, adjustment):
        (wavelength, phase, amplitude) = (curve.wavelength, curve.phase, curve.amplitude)
        wavelength += adjustment
        curve = kf.SinusoidalCurve(wavelength=wavelength, phase=phase, amplitude=amplitude)
        return (curve, curve)
```