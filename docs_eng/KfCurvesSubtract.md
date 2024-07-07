# Documentation
- Class name: KfCurvesSubtract
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node achieves the function of subtracting another curve from one curve and achieving the desired results in the area of animation and data visualization by combining key frame operations and mathematical calculations.

# Input types
## Required
- curve_1
    - The first curve input is essential because it sets a baseline for the subtraction process. It is the centre of the process because it determines the form and structure of the post-operational result curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - The second curve is an element to be subtracted from the first curve. Its role is crucial because it directly affects the final result of the subtraction and determines the shape and characteristics of the result curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- result_curve
    - The output represents the result of a subtraction operation that combines the essence of the two input curves into a single, refined curve, reflecting the difference between the original two curves.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesSubtract:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, curve_1, curve_2):
        curve_1 = deepcopy(curve_1)
        curve_2 = deepcopy(curve_2)
        return (curve_1 - curve_2,)
```