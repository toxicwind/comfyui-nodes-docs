# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx6
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a set of six interlocking string curves with varying degrees of magnitude depending on the given wavelength. It emphasizes the creation of a complex, harmonious mode of transition to zero and one in the system, which allows for the analysis of oscillating behaviour.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the cycle of the sine curve, affecting the frequency and overall structure of the generation mode. It is critical in defining the interval between oscillating properties and peaks.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- curves
    - The output consists of six sine curves, each representing the only phase in the oscillation mode. These curves are essential for understanding the contribution of nodes to the dynamic behaviour of the system.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx6(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 6

    def main(self, wavelength):
        return super().main(n=6, wavelength=wavelength)
```