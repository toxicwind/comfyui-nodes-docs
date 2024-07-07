# Documentation
- Class name: KfCurvesAddx10
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is designed to aggregate multiple input curves and enhance the overall expression of the data by adding their value levels. It is used as a tool to simplify the analysis and visualization of key frame curves by seeking peace.

# Input types
## Required
- curve_0
    - Initial curve input is essential because it establishes a baseline for subsequent additions to other curves. It is mandatory and directly affects the results of node operations.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
## Optional
- curve_1
    - Additional curve input is essential for the function of the node, which helps increase the cumulative effect. They enhance the comprehensiveness of the final output.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_2
    - More curve input plays an important role in the process of aggregation, affecting the ultimate summation and the validity of nodes in terms of aggregate data.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_3
    - Subsequent curve input is essential for achieving full aggregation of nodes, affecting the depth and breadth of synthetic data.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_4
    - The inclusion of more curve input enriches the ability of nodes to aggregate and process data and helps to produce more finer final output.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_5
    - Additional curve input is essential to enhance the ability of nodes to synthesize a wider range of data, contributing to a more comprehensive understanding of aggregate information.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_6
    - The integration of more curve input into nodes allows for more detailed and complex aggregations and enriches the final expression of the data.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_7
    - The presence of extra curve input enhances the function of nodes to enable them to process and integrate a wider data point to the final sum.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_8
    - By including more curve input, nodes can effectively aggregate diversified data sets, which is essential for achieving the overall view of the composite curve.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve
- curve_9
    - The final curve input adds the last layer of data to the aggregation process to ensure that the output of the nodes is the full expression of all the combo curves.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Output types
- curve_out
    - The output represents the sum of all input curves and provides a comprehensive and integrated view of the aggregate data.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: keyframed.Curve

# Usage tips
- Infra type: CPU

# Source code
```
class KfCurvesAddx10:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CURVE',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve_0': ('KEYFRAMED_CURVE', {'forceInput': True})}, 'optional': {'curve_1': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_2': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_3': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_4': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_5': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_6': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_7': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_8': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0}), 'curve_9': ('KEYFRAMED_CURVE', {'forceInput': True, 'default': 0})}}

    def main(self, curve_0=0, curve_1=0, curve_2=0, curve_3=0, curve_4=0, curve_5=0, curve_6=0, curve_7=0, curve_8=0, curve_9=0):
        curve_out = curve_0 + curve_1 + curve_2 + curve_3 + curve_4 + curve_5 + curve_6 + curve_7 + curve_8 + curve_9
        return (curve_out,)
```