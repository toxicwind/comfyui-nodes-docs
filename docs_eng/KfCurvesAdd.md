# Documentation
- Class name: KfCurvesAdd
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfCurvesAdd node is designed to combine two key frame curves into a composite curve. When the consolidation curve is critical to creating complex animations or data expressions, the node plays a key role in the workflow. It increases the overall functionality and diversity of the animation or graphic process by receiving two input curves and integrating them seamlessly.

# Input types
## Required
- curve_1
    - The first key frame curve to be merged is the basic input of the KfCurvesAdd node. It is essential for the formation of the final composite curve and directly affects the results of animated or graphical expressions. The node relies heavily on the structure and properties of the curve to perform its functions effectively.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - The second key frame curve, like the first curve, is the necessary input for the node. It is essential for the process of combining the curve, which significantly influences the shape and properties of the final composite curve. The node combines this curve with the first curve to achieve the desired animation or graphic effect.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- combined_curve
    - The output of the KfCurvesAdd node is a key frame curve representing the sum of the two input curves. This output is important because it contains the combined effect of the input curve and provides a single, coherent curve for further use in animation or data visualization processes.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesAdd:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, curve_1, curve_2):
        curve_1 = deepcopy(curve_1)
        curve_2 = deepcopy(curve_2)
        return (curve_1 + curve_2,)
```