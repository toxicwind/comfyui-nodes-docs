# Documentation
- Class name: KfSinusoidalGetPhase
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to extract phase information from the sine curve, which is essential for understanding the time position and position in oscillation patterns.

# Input types
## Required
- curve
    - Curve parameters are essential because they define the sine wave shape from which the phase will be extracted, directly impacting the output of the node.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: keyframed.SinusoidalCurve

# Output types
- phase
    - The output phase represents the temporal deviation of the sine wave, which is important for aligning or comparing oscillating patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalGetPhase:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('FLOAT',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True})}}

    def main(self, curve):
        return (curve.phase,)
```