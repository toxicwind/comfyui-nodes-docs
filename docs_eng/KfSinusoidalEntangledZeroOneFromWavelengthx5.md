# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx5
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is based on the wavelength provided to generate five key frames of sine-forms, entangles zeros and one values in rhythm. It emphasizes the creation of cyclical, oscillating data structures that smooth the transition between specified high and low values.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the period of the sine curve, affecting the distance between the overall oscillation pattern and the successive peaks. It is essential to define the frequency and repetition of the curve.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- curves
    - The output consists of five key frame string curves, each representing a unique part of the sine pattern based on the input wavelength. These curves are essential to the function of the node and provide visual and numerical indications of oscillation.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx5(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 5

    def main(self, wavelength):
        return super().main(n=5, wavelength=wavelength)
```