# Documentation
- Class name: KfCurvesMultiply
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfCurvesMulliply node is designed to multiply the given two key frames by elements, effectively combining their respective values in the corresponding key frames. This operation is essential for non-linear adjustment and operation of the intensity or magnitude of animated curves and enhances creative control in animation and simulation processes.

# Input types
## Required
- curve_1
    - The first key frame curve input is essential because it defines the initial key frame that will be multiplied by the second curve and its associated values. This parameter is essential for creating a baseline animation or effect that will be modified by the second curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - The second key frame curve is entered as a multiplier for the first curve, allowing an animation or effect defined by the first curve to be adjusted. This parameter is essential for changing the dynamics of the animation in a controlled way or applying complex effects.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- result
    - The output of the KfCurvesMulliply node is a new key frame curve representing an element-by-element multiplier of two input curves. This result curve can be used to further fine-tune animations or to introduce new levels of complexity and detail in the animation sequence.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesMultiply:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, curve_1, curve_2):
        curve_1 = deepcopy(curve_1)
        curve_2 = deepcopy(curve_2)
        return (curve_1 * curve_2,)
```