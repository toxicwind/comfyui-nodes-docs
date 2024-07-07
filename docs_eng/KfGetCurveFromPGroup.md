# Documentation
- Class name: KfGetCurveFromPGroup
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node facilitates the extraction of specific curves from the parameters group, enabling users to isolate and analyse individual data trends in complex data sets.

# Input types
## Required
- curve_label
    - The identifier of the curve to be extracted is essential to accurately locate the exact data trends to be analysed.
    - Comfy dtype: STRING
    - Python dtype: str
- parameter_group
    - The contours of the parameters that form the data sets from which curves will be extracted play a crucial role in the overall data analysis process.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: kf.ParameterGroup

# Output types
- curve
    - The curves extracted represent isolated data trends and provide a clear and focused view of specific patterns of larger data concentration.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfGetCurveFromPGroup:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_label': ('STRING', {'default': 'My Curve'}), 'parameter_group': ('PARAMETER_GROUP', {'forceInput': True})}}

    def main(self, curve_label, parameter_group):
        curve = parameter_group.parameters[curve_label]
        return (deepcopy(curve),)
```