# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx8
- Category: math
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

KfSinosoidalEntangled ZeroOneFromFrequencyx 8 node produces eight entangled sine curves based on the given frequency. Each curve is designed to shake between zero and one, with a relative deviation to ensure entanglement. The objective of the node is to create a complex oscillation model that can be used for applications that require synchronization but different wave shapes.

# Input types
## Required
- frequency
    - The frequency parameter determines the rate at which the sine curve oscillates. It is essential for setting the overall pattern of the curve and influences the cycle and amplitude of each oscillation. The higher the frequency, the faster the oscillation.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- KEYFRAMED_CURVE
    - The output of KfSinosoidalEntangled ZeroOneFromFrequencyx8 is eight key frame sine curves. Each curve represents a unique oscillation pattern, entangled with other curves, and provides a rich wavering set for further operations or analysis.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx8(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 8

    def main(self, frequency):
        return super().main(n=8, frequency=frequency)
```