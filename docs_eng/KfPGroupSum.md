# Documentation
- Class name: KfPGroupSum
- Category: keyframed/experimental
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfPGroupSum node is designed to aggregate the key frame curves into a single composite curve. It operates by adding the curves associated with the given parameter group, thereby generating a uniform expression that contains the collective behaviour of the input curve.

# Input types
## Required
- parameter_group
    - The argument group is the key input for the KfPGroupSum node because it contains the key frame curves that you want to add to. This input directly influences the output curve by determining which curves contribute to the final composite curve.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, kf.Curve]

# Output types
- composite_curve
    - The output of the KfPGroupSum node is a composite key frame curve, which is the sum of all input curves in the parameter group. This curve is important because it provides a simplified view of the combined motion or effect that the input curve represents.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfPGroupSum:
    CATEGORY = 'keyframed/experimental'
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True})}}

    def main(self, parameter_group):
        parameter_group = deepcopy(parameter_group)
        outv = kf.Curve(0)
        for curve in parameter_group.parameters.values():
            outv += curve
        return (outv,)
```