# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx4
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a set of four sine curves based on the wavelength of the input, entangled together, creating a pattern of oscillation between zero and one. It is designed to generate complex wave shapes for applications that require cyclical but complex wave shapes.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the period of the sine curve, influencing the frequency and overall shape of the wave shape. This is a key input, because it directly affects the pattern and regularity of oscillations.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output consists of four entangled sine curves, each representing a unique part of the input wavelength oscillation mode. This output is important because it provides the basis for further analysis or operation in various applications.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx4(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 4

    def main(self, wavelength):
        return super().main(n=4, wavelength=wavelength)
```