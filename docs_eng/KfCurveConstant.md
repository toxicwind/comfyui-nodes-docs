# Documentation
- Class name: KfCurveConstant
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfCurveConstant node is designed to produce a constant curve in the frame of the key frame. It encapsifies a single value provided as input and expresses it as a constant curve that does not change over time. The node is useful in creating a stable state or fixed point in the dynamic system, where a constant value is required for a period of time.

# Input types
## Required
- value
    - The `value' parameter is essential because it defines the constant value of the curve. It is the only input into the node and directly influences the output to ensure that the curve remains constant for the duration of its duration. This parameter is essential for establishing a steady state in the simulation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- curve
    - Output 'curve' represents a constant curve in the frame of the key frame. It is generated from input values and then used to create a curve that does not fluctuate over time. This output is important because it provides a visual and computational representation of the constant state of the system.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurveConstant:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('FLOAT', {'forceInput': True})}}

    def main(self, value):
        curve = kf.Curve(value)
        return (curve,)
```