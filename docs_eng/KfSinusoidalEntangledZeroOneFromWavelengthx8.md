# Documentation
- Class name: KfSinusoidalEntangledZeroOneFromWavelengthx8
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node produces a set of eight sine curves based on the given wavelength, each with a different phase deviation. The main aim is to create a zero- and one-value entanglement mode for oscillating within the specified wavelength to facilitate the generation of complex waveforms for various applications.

# Input types
## Required
- wavelength
    - The wavelength parameter determines the length of a whole cycle of the sine curve. It is very important because it directly affects the frequency and periodicity of the waveform generation, thus influencing the overall pattern and behaviour of the curve.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output consists of eight sine curves, each of which represents a unique phase deviation within the specified wavelength. These curves are essential to the function of the nodes, as they provide the basis for further analysis or operation in the downstream process.
    - Comfy dtype: COMBO[kf.SinusoidalCurve]
    - Python dtype: List[kf.SinusoidalCurve]

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalEntangledZeroOneFromWavelengthx8(KfSinusoidalEntangledZeroOneFromWavelength):
    RETURN_TYPES = ('KEYFRAMED_CURVE',) * 8

    def main(self, wavelength):
        return super().main(n=8, wavelength=wavelength)
```