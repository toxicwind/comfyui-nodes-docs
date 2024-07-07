# Documentation
- Class name: KfEvaluateCurveAtT
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfEvaluateCurveAtt node is designed to assess and retrieve the value of the key frame curve at a given time 't'. It operates by accepting a key frame curve and a time parameter, and returns the floating point and integer value of the time point curve, which gives a full insight into the state of the curve at that time.

# Input types
## Required
- curve
    - The `curve' parameter is essential because it defines the key frame curves to be assessed by the node. It is the key component that directly affects node output by determining the shape and value of the curve to be analysed at the specified time 't'.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- t
    - The `t' parameter specifies the time at which the curve value is to be assessed. Although it has a default value of 0, it is essential to determine the exact output of the node, as it indicates the exact location of the value extracted along the curve.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- curve_value_float
    - The floating point at the time 't' curve value represents the key output of the node. It captures the precise continuous nature of the specified time curve and provides a detailed insight into its behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- curve_value_int
    - The integer value of the curve value at the time 't'indicates that it provides a discrete version of the curve value. This output may be particularly useful in the context where integer values are needed or preferred, such as for some types of data analysis or visualization.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class KfEvaluateCurveAtT:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('FLOAT', 'INT')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('KEYFRAMED_CURVE', {'forceInput': True}), 't': ('INT', {'default': 0})}}

    def main(self, curve, t):
        return (curve[t], int(curve[t]))
```