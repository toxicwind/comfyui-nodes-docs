# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx9
- Category: core
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

KfSinosoidalEntangledZeroOneFromWavelengthx9 produces a set of nine string curves based on the given wavelength, which entangle between zero and one. This node is particularly suitable for creating complex patterns that require multiple interwoven frequencies.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the period of the sine oscillation, which is essential for setting the frequency of the curve. It directly affects the overall shape and cyclicality of the output mode.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- KEYFRAMED_CURVE
    - The output of this node is a cluster of nine key frame sine curves. Each curve is designed to provide a unique contribution to the composite wave shape, providing a rich confluence.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: Tuple[kf.SinusoidalCurve, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx9(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 9

    def main(self, wavelength):
        return super().main(n=9, wavelength=wavelength)
```