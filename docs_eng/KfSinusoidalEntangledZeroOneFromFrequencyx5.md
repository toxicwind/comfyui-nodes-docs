# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx5
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is based on a given frequency to generate five entangled sine curves, representing a complex pattern of values from zero to one. It emphasizes the creation of complex wave shapes for applications that require cyclical, non-linear variations.

# Input types
## Required
- frequency
    - The frequency parameters determine the speed of oscillation of the sine curve and affect the overall rhythm and cyclicality of the waveform generation.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output contains five sine curves, each of which represents a unique change in the range of input frequencies from zero to one value.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx5(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 5

    def main(self, frequency):
        return super().main(n=5, frequency=frequency)
```