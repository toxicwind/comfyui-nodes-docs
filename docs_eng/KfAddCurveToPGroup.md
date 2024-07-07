# Documentation
- Class name: KfAddCurveToPGroup
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node integrates the curves into the parameters group to facilitate the management and organization of the key frame curves in the project. It enhances workflows by allowing seamless additions to ensure that they become part of the structured group so that they can be easily accessed and operated.

# Input types
## Required
- curve
    - A curve parameter is essential because it defines the particular curve to be added to the parameter group. It is the main input parameter, and the data and properties of which curves are to be managed within the group.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.Curve
## Optional
- parameter_group
    - Parameter groups, as containers of curves, allow the collective management of multiple parameters. Their existence or non-existence affects the structure and organization of the data in the node operation.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: kf.ParameterGroup

# Output types
- parameter_group
    - The output parameter group is now enhanced by the addition of curves to become a more comprehensive parameter management entity. It is important because it represents the outcome of node operations and contains organized data processing for further use.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: kf.ParameterGroup

# Usage tips
- Infra type: CPU

# Source code
```
class KfAddCurveToPGroup:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('PARAMETER_GROUP',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('KEYFRAMED_CURVE', {'forceInput': True})}, 'optional': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True})}}

    def main(self, curve, parameter_group=None):
        curve = deepcopy(curve)
        if parameter_group is None:
            parameter_group = kf.ParameterGroup([curve])
        else:
            parameter_group = deepcopy(parameter_group)
            parameter_group.parameters[curve.label] = curve
        return (parameter_group,)
```