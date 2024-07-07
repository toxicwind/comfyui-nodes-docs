# Documentation
- Class name: KfCurvesDivide
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node performs the division of the two curves and provides the means to analyse their relationship. It is essential for the operation of the need to standardize or compare the curve data and provides a direct way to obtain a new curve with the division result.

# Input types
## Required
- curve_1
    - The first curve is the basic input that defines the number of operations in the division operation. Its value is essential for determining the number of outcomes of the division, as it directly affects the shape and characteristics of the result curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - The second curve is another important input, which is used as a division in the division operation. Its importance is that it influences the scaling of the result curve vis-à-vis the first curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- result_curve
    - The output of the node is a new curve, which represents the result of the first input curve divided by the second curve. This result curve is important because it contains a homogenization relationship between the two original curves.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesDivide:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, curve_1, curve_2):
        curve_1 = deepcopy(curve_1)
        curve_2 = deepcopy(curve_2)
        return (curve_1 / curve_2,)
```