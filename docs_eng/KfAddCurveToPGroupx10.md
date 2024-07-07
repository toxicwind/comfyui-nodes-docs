# Documentation
- Class name: KfAddCurveToPGroupx10
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node integrates multiple curves into a set of parameters and streamlines the management and application of key frame curves in the project. It emphasizes data integration to improve efficiency and workflow.

# Input types
## Required
- curve0
    - The initial curve is essential because it sets the basis for the parameter group. It is mandatory and directly affects the operation and output of the node.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- parameter_group
    - The parameter groups play a key role in organizing and constructing the data structure in the node workflow as containers of curves.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: kf.ParameterGroup
## Optional
- curve1
    - An additional curve, such as Curve1, increases the complexity and multifunctionality of the array of parameters and allows for the processing and operation of richer data sets.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve2
    - Further consolidation of curves, such as curve2, has helped nodes to process diversified and complex data and to improve overall functionality.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve3
    - Optional curves such as Curve3 provide additional dimensions to the array of parameters, enabling nodes to effectively manage more complex data structures.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve4
    - Curve4 includes the ability to further expand the parameters group to allow for more detailed control of the data being processed.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve5
    - Curve5 increased the ability of the parameter groups to integrate multiple data and increased the adaptability of nodes to various data inputs.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve6
    - By including curve6, nodes have gained the ability to manage more complex data sets, contributing to the overall robustness of the parameter group.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve7
    - Curve7 is another optional curve that includes data-processing capabilities that can further enrich the array of parameters and enhance nodes.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve8
    - The addition of curve8 allows for the processing of a wider range of data and enhances the multifunctionality of the array of parameters.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve
- curve9
    - Comprises the last alternative curve Curve9, which enables nodes to process the most complex data sets and maximizes the comprehensiveness of the array of parameters.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: kf.KeyframedCurve

# Output types
- parameter_group
    - The output parameter group is the collection of all input curves, representing a unified and structured data set that can be used downstream of the workflow.
    - Comfy dtype: PARAMETER_GROUP
    - Python dtype: kf.ParameterGroup

# Usage tips
- Infra type: CPU

# Source code
```
class KfAddCurveToPGroupx10:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('PARAMETER_GROUP',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve0': ('KEYFRAMED_CURVE', {'forceInput': True})}, 'optional': {'parameter_group': ('PARAMETER_GROUP', {'forceInput': True}), 'curve1': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve2': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve3': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve4': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve5': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve6': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve7': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve8': ('KEYFRAMED_CURVE', {'forceInput': True}), 'curve9': ('KEYFRAMED_CURVE', {'forceInput': True})}}

    def main(self, parameter_group=None, **kwargs):
        if parameter_group is None:
            parameter_group = kf.ParameterGroup(kwargs)
        else:
            parameter_group = deepcopy(parameter_group)
            for curve in parameter_group.values():
                parameter_group.parameters[curve.label] = curve
        return (parameter_group,)
```