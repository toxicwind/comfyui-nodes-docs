# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromFrequencyx7
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates a set of seven interlocking sine curves based on the basic frequency of input, each oscillating between zero and one. It emphasizes the creation of complex, synchronized waveforms for signal processing or visualization applications.

# Input types
## Required
- frequency
    - The frequency parameter determines the oscillation rate of the sine curve, influencing the overall pattern and cyclicality of the wave shape. It is essential to define the temporal properties of the output.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output consists of seven sine curves, each of which represents a unique phase shift and amplitude according to the input frequency. These curves are essential to the function of the node and provide a rich collection of data points for further analysis or operation.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromFrequencyx7(KfSinusoidalEntangledZeroOneFromFrequency):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 7

    def main(self, frequency):
        return super().main(n=7, frequency=frequency)
```