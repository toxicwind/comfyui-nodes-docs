# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx6
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is based on the frequency provided to generate a set of six interlocking sine curves, each oscillating between zero and one. It emphasizes the creation of interconnected waveforms of consistent intricacies to facilitate the generation and analysis of complex models.

# Input types
## Required
- frequency
    - The frequency parameter determines the speed of oscillation of the sine curve, affecting the overall rhythm and cyclicality of the wave shape. It is essential to define the temporal characteristics of the output.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output consists of six sine curves, each representing a unique phase shift explanation of the input frequency. These curves are at the core of the node function and provide a rich data set for further analysis or visualization.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx6(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 6

    def main(self, frequency):
        return super().main(n=6, frequency=frequency)
```