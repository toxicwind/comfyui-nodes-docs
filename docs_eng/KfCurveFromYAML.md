# Documentation
- Class name: KfCurveFromYAML
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is designed to interpret the YAML string to generate key frame curves, which are essential components in animation and simulation workflows. By allowing users to define complex motion paths through text-based formats, it streamlines the creation process, facilitates its use and enhances the modularization of the design process.

# Input types
## Required
- yaml
    - The `yaml' parameter is a string with a curve in the YAML format. It is essential because it directly defines the structure and characteristics of the curve to be created. It is essential for the running of the nodes, specifying the key frames and the plug-in method used in the curve.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- curve
    - Output 'curve' is a data structure that represents the key frame curve defined by the input YAML. It covers the motion path with key frames, plugs and other attributes and becomes an essential element of follow-up in animation or simulation processes.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurveFromYAML:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'yaml': ('STRING', {'multiline': True, 'default': 'curve:\n- - 0\n  - 0\n  - linear\n- - 1\n  - 1\nloop: false\nbounce: false\nduration: 1\nlabel: foo'})}}

    def main(self, yaml):
        curve = kf.serialization.from_yaml(yaml)
        return (curve,)
```