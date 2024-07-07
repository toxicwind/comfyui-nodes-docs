# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx4
- Category: core
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

KfSinosoidalEntangled ZeroOneFromFrequencyx 4 is designed to generate multiple interlocking sine curves based on the given frequency. It operates by creating four different sine curves, each of which has a unique dichotomy and amplitude derived from the input frequency. This node is particularly suitable for applications that require complex, interconnected waveforms.

# Input types
## Required
- frequency
    - The frequency parameter is essential for determining the basic speed of a sine curve oscillation. It directly influences the output of nodes and influences the shape and cyclicality of the curve.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- KEYFRAMED_CURVE
    - The output of the nodes is a set of four key frame sine curves. Each curve represents a unique oscillation pattern, entangles with other curves, forming a complex wave structure.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx4(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 4

    def main(self, frequency):
        return super().main(n=4, frequency=frequency)
```