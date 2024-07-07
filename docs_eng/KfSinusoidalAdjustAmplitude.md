# Documentation
- Class name: KfSinusoidalAdjustAmplitude
- Category: ROOT_CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is designed to adjust the amplitude of the sine curve to allow fine-tuning of the shape without changing its underlying properties, such as wavelength and phase. It emphasizes the role of the node in fine-tuning the dynamics of the curve for various applications.

# Input types
## Required
- curve
    - A curve parameter is necessary because it defines the base sine curve that you want to adjust the amplitude. It directly influences the output and determines the shape and characteristics of the modified curve.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve
## Optional
- adjustment
    - Adjusts the parameters to modify the amplitude of the sine curve to allow for precise control of peaks and grains of the curve. It plays a crucial role in customizing the curves according to specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - An output curve is a modified sine curve with an adjusted amplitude that represents the result of a node operation. It is important because it conveys the final shape that can be used for further processing or analysis.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- sinusoidal_curve
    - This output is the same as the modified curve, emphasizing that the main function of the node is to adjust the amplitude while preserving the other properties of the curve. It is very useful for applications that require the final sine shape.
    - Comfy dtype: SINUSOIDAL_CURVE
    - Python dtype: kf.SinusoidalCurve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSinusoidalAdjustAmplitude:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE', 'SINUSOIDAL_CURVE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('SINUSOIDAL_CURVE', {'forceInput': True}), 'adjustment': ('FLOAT', {'default': 0, 'step': 0.01})}}

    def main(self, curve, adjustment):
        (wavelength, phase, amplitude) = (curve.wavelength, curve.phase, curve.amplitude)
        amplitude += adjustment
        curve = kf.SinusoidalCurve(wavelength=wavelength, phase=phase, amplitude=amplitude)
        return (curve, curve)
```