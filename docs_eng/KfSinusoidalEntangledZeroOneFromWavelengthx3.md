# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx3
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a set of three interlocking sine curves based on the wavelength of the input, creating a complex pattern of oscillation between zero and one. It is designed to introduce highly cyclical changes appropriate to applications that require complex waveforms.

# Input types
## Required
- wavelength
    - The wavelength parameters determine the cycle of the sine curve, affecting the overall complexity and frequency of the generation mode. This is a key input, as it directly affects the spatial properties of the curve.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- curves
    - The output consists of three sine curves, each with its unique phase and amplitude, which are derived from input wavelengths. These curves are the core of the node function and represent the main result of the treatment.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx3(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 3

    def main(self, wavelength):
        return super().main(n=3, wavelength=wavelength)
```