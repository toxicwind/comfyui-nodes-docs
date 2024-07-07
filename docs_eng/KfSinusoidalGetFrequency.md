# Documentation
- Class name: KfSinusoidalGetFrequency
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node extracts the basic frequency from the sine curve and provides a measure of its oscillation rate.

# Input types
## Required
- curve
    - The input curve parameter is necessary because it is the source of the data for the extraction frequency.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.Keyframed

# Output types
- frequency
    - Output represents the basic frequency of input string curves.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalGetFrequency:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('FLOAT',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True})}}

    def main(self, curve):
        return (1 / curve.wavelength,)
```