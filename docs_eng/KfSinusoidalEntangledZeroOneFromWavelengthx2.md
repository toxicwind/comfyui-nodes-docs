# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx2
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a entangled sine curve based on the given wavelength, designed to create a complex and synchronized pattern. It emphasizes the interaction between wavelength and the generation of waveforms, focusing on the harmony and rhythm of the curve.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the cycle of the sine curve, influencing the overall pattern and frequency of the wave shape. It is critical in determining the aesthetic and functional quality of the output.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- KEYFRAMED_CURVE
    - The output contains two entangled and synchronized sine curves that provide a rich display of the properties of the input wavelength. These curves can be used in applications that require rhythm and cyclical patterns.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx2(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 2

    def main(self, wavelength):
        return super().main(n=2, wavelength=wavelength)
```