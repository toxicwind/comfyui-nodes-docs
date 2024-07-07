# Documentation
- Class name: KfCurveFromString
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to explain and convert a mathematical curve string to a format that can be used for further processing. It encapsulates the logic of parsing Chigozie strings, which is a compact way to describe the key frame curve and to produce a curve object that can be visualized or used in various mathematical and graphic applications.

# Input types
## Required
- chigozie_string
    - The input parameter is a string that defines the curve using the Chigozie expression, which is essential for the node to generate the corresponding curve object. It directly affects the shape and characteristics of the output curve.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- curve
    - Output is a curve object that represents the mathematical curve defined by the input string. It is the main result of the node operation and can be used to render, analyse, or further processed in the key frame-based workflow.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurveFromString:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'chigozie_string': ('STRING', {'multiline': True, 'default': '0:(1)'})}}

    def main(self, chigozie_string):
        curve = curve_from_cn_string(chigozie_string)
        return (curve,)
```