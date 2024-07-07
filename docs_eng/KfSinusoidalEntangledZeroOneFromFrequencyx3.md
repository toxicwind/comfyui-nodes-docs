# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx3
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a set of three sine curves based on a given frequency, which are interwoven in a zero-one mode. It emphasizes the creation of a cyclical wave shape that smooths the transition between zero and one, with a focus on the use of frequency parameters to control the periodicity and overall shape of the curve.

# Input types
## Required
- frequency
    - The frequency parameters determine the cyclicality of the sine curve, affecting the spacing and repetition of the peak valley of the wave. This is essential for defining the rhythm and rhythm of generating the curve.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output is three sine curves, each of which represents a unique phase shift in a zero interwoven. These curves are at the core of the node function as the main result of the treatment.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx3(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 3

    def main(self, frequency):
        return super().main(n=3, frequency=frequency)
```