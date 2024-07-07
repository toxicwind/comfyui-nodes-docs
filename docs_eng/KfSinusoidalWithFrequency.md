# Documentation
- Class name: KfSinusoidalWithFrequency
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node generates sine curves with adjustable frequencies, phase and amplitude, simulates cyclical motion patterns. It is designed to provide multifunctional tools for users to create smooth, oscillating transitions in the project.

# Input types
## Required
- frequency
    - Frequency parameters determine the rate at which the sine curve oscillates, and higher values lead to faster and more frequent cycles. This is essential for setting animating rhythms and rhythms.
    - Comfy dtype: FLOAT
    - Python dtype: float
- phase
    - The phase parameter moves the sine curve along the time line, allowing for the control of the starting point of the oscillation. This is essential to align the action with the particular event or action in the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude parameters control the range of oscillations and determine the peak and grain of the sine curve. It affects the overall strength and magnitude of the action.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - The output is a key frame curve object with a sine pattern that can be used for various animations and simulations.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.SinusoidalCurve
- sinusoidal_curve
    - The output provides a sine curve in a format that is directly applicable to visual elements and provides a smooth and dynamic expression of oscillation.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: keyframed.SinusoidalCurve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalWithFrequency:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE', 'SINUSOIDAL_CURVE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'frequency': ('FLOAT', {'default': 1 / 12, 'step': 0.01}), 'phase': ('FLOAT', {'default': 0.0, 'step': 0.1308996939}), 'amplitude': ('FLOAT', {'default': 1, 'step': 0.01})}}

    def main(self, frequency, phase, amplitude):
        curve = kf.SinusoidalCurve(frequency=frequency, phase=phase, amplitude=amplitude)
        return (curve, curve)
```