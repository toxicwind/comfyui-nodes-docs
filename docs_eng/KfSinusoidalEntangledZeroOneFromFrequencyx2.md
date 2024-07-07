# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx2
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a entangled sine curve based on the frequency provided, which moves from zero to zero again and again. It emphasizes that creating smooth, cyclical functions that demonstrate particular cyclical behaviour is very useful for applications that require oscillating patterns.

# Input types
## Required
- frequency
    - The frequency parameter determines the cyclicality of the sine curve, affecting the speed of its oscillation and the distance between peaks. It is critical to defining the overall rhythm and speed at which the curve is generated.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output consists of two entangled key frame string curves that show a zero-to-one oscillation pattern. These curves are the core of the node function and represent the main result of the treatment.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx2(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 2

    def main(self, frequency):
        return super().main(n=2, frequency=frequency)
```