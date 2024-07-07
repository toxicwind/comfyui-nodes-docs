# Documentation
- Class name: KfCurvesMultiplyx10
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node facilitates the multiplicity of curves by multiplying them and enhances the ability to operate and combine key frame data to achieve complex animations or simulations. It aims to simplify the process of scaling and integrating various curve inputes, thus enabling the creation of complex motion sequences.

# Input types
## Required
- curve_0
    - The main curve input is essential for the multiplying process, and it serves as the basis for other curve factors. Its existence ensures that nodes can start complex operations.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
## Optional
- curve_1
    - The subsequent curve input is used as a multiplier to enhance the overall scaling effect of the main curve. Each curve enriches the complexity and detail of the final output.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - Additional curve input further refines the scaling process and allows for careful control of the sequence of movements generated.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_3
    - The inclusion of more curve input increases the multifunctionality of nodes, allowing a wide range of effects to be achieved by combining multiple curve values.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_4
    - More curve input provides fine particle size control and allows complex operations of the final output according to the specific characteristics of each curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_5
    - Combined with additional curves, a more complex level of detail can be achieved in the final animation, as each curve contributes a unique scaling factor.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_6
    - More curves are multiplied to provide a higher degree of accuracy and customization in the resulting motion sequence.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_7
    - By including more curve input, nodes generate highly complex and nuanced animations to meet specific creative needs.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_8
    - Further consolidation of the curve has enhanced the ability of nodes to generate complex and detailed animations, responding to the demands of advanced campaign design.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_9
    - The last set of curve input gives nodes the ability to achieve excellent detail and precision in the final animation, driving the boundary of likelihood.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- curve_out
    - The output represents the cumulative result of all input curves, provides a single, unified curve and encapsulates the combined effects.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesMultiplyx10:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_0': ('KEYFRAMED_CURVE', {'forceInput': True})}, 'optional': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_3': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_4': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_5': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_6': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_7': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_8': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1}), 'curve_9': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 1})}}

    def main(self, curve_0, curve_1, curve_2, curve_3, curve_4, curve_5, curve_6, curve_7, curve_8, curve_9):
        curve_out = curve_0 * curve_1 * curve_2 * curve_3 * curve_4 * curve_5 * curve_6 * curve_7 * curve_8 * curve_9
        return (curve_out,)
```