# Documentation
- Class name: KfPGroupCurveMultiply
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node achieves the application of a set of parameters to curves and adjusts the parameter values over time to the dynamics of the key frame data.

# Input types
## Required
- parameter_group
    - argument group, the value of which is multiplied by the curve. This is essential to define the set of parameters to be adjusted by the node.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, Any]
- curve
    - The curve defines the multiplier factors for the parameter groups at different points in time. It is essential for controlling dynamic adjustment.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.Curve

# Output types
- result
    - Output is a modified array of parameters whose values are adjusted by the curve multiplied.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class KfPGroupCurveMultiply:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('PARAMETER_GROUP',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True}), 'curve': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, parameter_group, curve):
        parameter_group = deepcopy(parameter_group)
        curve = deepcopy(curve)
        return (parameter_group * curve,)
```