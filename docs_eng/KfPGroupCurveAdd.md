# Documentation
- Class name: KfPGroupCurveAdd
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node facilitates the integration of curves into the parameters group and enhances the overall structure and functionality of the data model. It aims to simplify the process of combining key frame animation elements with parameter settings, thereby increasing the efficiency of data operations within the system.

# Input types
## Required
- parameter_group
    - The argument group is necessary because it forms the basis for the consolidation of the curve. It is the key component that influences the behaviour and output of the node as a whole and determines the structural context of the curve operation.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, Any]
- curve
    - Curve input is essential for introducing dynamic change into the parameter group. It carries animated data that will be merged with static parameters, thereby adding complexity and fluidity to the end result.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve

# Output types
- result
    - The combined output of the result parameter groups and curves represents a successful integration. It represents the crystal of node operations and covers two input combination properties and behaviors.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class KfPGroupCurveAdd:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('PARAMETER_GROUP',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True}), 'curve': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, parameter_group, curve):
        parameter_group = deepcopy(parameter_group)
        curve = deepcopy(curve)
        return (parameter_group + curve,)
```