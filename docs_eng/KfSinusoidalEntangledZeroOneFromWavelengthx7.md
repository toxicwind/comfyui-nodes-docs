# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx7
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node produces a set of seven unique sine curves based on the wavelength of the input, with the phase deviation of each curve being used to represent the binary sequence derived from the wavelength. It emphasizes the creation of a structured model that adjusts the frequency based on wavelength parameters, depending on the frequency, between zero and one.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the frequency of the sine curve and influences the overall mode of producing the sequence. It is essential for the operation of the node, as it determines the particle size and cyclicality of binary expressions.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- KEYFRAMED_CURVE
    - The output is a collection of seven sine curves, each representing the only phase in the binary sequence. The combination of these curves provides a visual and numerical expression of the entangled zero pattern based on the input wavelength.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx7(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 7

    def main(self, wavelength):
        return super().main(n=7, wavelength=wavelength)
```