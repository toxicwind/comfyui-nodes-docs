# Documentation
- Class name: KfSinusoidalGetAmplitude
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node extracts amplitude from a string curve and provides a measure of the peak deviation from the average. This is essential to understand the strength of the oscillation in the curve.

# Input types
## Required
- curve
    - The curve parameter entered represents the sine data structure from which the amplitude is extracted. It is essential for the running of the node, as it directly affects the output result.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: keyframed.SinusoidalCurve

# Output types
- amplitude
    - The output provides an amplitude to enter a sine curve, indicating the range of its oscillation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalGetAmplitude:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('FLOAT',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True})}}

    def main(self, curve):
        return (curve.amplitude,)
```