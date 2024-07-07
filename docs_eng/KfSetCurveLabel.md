# Documentation
- Class name: KfSetCurveLabel
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node allows a descriptive label to be assigned to the curve, which enhances the retraceability and interpretability of the curve in the context in which the data can be visualized or analysed.

# Input types
## Required
- curve
    - Curve parameters are necessary because they represent the data structure to be assigned to labels and ensure that curves are recognized and referenced in the system.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
## Optional
- label
    - Tag parameters, as text identifiers for curves, help to organize and retrieve specific curves in larger data sets or workflows.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- curve
    - The output curve now contains assigned labels that provide more comprehensive data indications for further analysis or presentation.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfSetCurveLabel:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('KEYFRAMED_CURVE', {'forceInput': True}), 'label': ('STRING', {'multiline': False, 'default': '~curve~'})}}

    def main(self, curve, label):
        curve = deepcopy(curve)
        curve.label = label
        return (curve,)
```