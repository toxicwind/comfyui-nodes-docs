# Documentation
- Class name: KfSinusoidalGetWavelength
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfSinosoidalGetWavelength node is designed to extract characteristic wavelengths from a sine curve. It plays a key role in analysing and understanding the cyclical nature of the curve, providing a basic parameter for applications such as signal processing and wave-shaped analysis, which is critical in various applications.

# Input types
## Required
- curve
    - The `curve' parameter is essential to the operation of the node because it represents the sine curve from which the wavelengths are derived. It is a necessary input that directly influences the output of the node and determines the accuracy and relevance of the wavelength values obtained.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: Keyframed sinusoidal curve object

# Output types
- wavelength
    - The 'waterength'output parameter represents the length of a whole cycle of a sine curve. This is a key information segment that can be used for further analysis or for informed decision-making in the context of applications for which nodes are used.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalGetWavelength:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('FLOAT',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True})}}

    def main(self, curve):
        return (curve.wavelength,)
```