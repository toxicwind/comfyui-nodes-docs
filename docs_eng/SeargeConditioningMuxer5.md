# Documentation
- Class name: SeargeConditioningMuxer5
- Category: Searge/_deprecated_/FlowControl
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

This node serves as a condition multi-routine reuser that selects a particular reconciliation input according to the value of the selector. It helps the data to pass through the network's route and ensures that appropriate reconciliation signals are passed to subsequent operations.

# Input types
## Required
- input0
    - The first reconciliation input is a key component of the node operation. It represents one of the potential data streams that the input selector can select.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input1
    - The second adjustment input, another important part of the node function. When the input selection is set to 1, it will be the selected data stream.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input2
    - The third reconciliation input helps the node to flow different data streams according to the value route of the selector.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input3
    - The fourth reconciliation input is part of the node diversification selection mechanism. When the input selection is 3, it becomes the active input.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input4
    - The fifth reconciliation input completes the selection set of nodes. When the value of the input selection is 4 it will be the selected input.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input_selector
    - Select the parameter to determine which of the reconciliations are entered through the node. It is essential to determine the output according to the range of values set.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the node is based on the reconciliation input selected by the input selector. It represents the result of the node operation, i.e. the appropriate reconciliation signal for the downstream process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeConditioningMuxer5:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input0': ('CONDITIONING',), 'input1': ('CONDITIONING',), 'input2': ('CONDITIONING',), 'input3': ('CONDITIONING',), 'input4': ('CONDITIONING',), 'input_selector': ('INT', {'default': 0, 'min': 0, 'max': 4})}}
    RETURN_TYPES = ('CONDITIONING',)
    RETURN_NAMES = ('output',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/FlowControl'

    def mux(self, input0, input1, input2, input3, input4, input_selector):
        if input_selector == 1:
            return (input1,)
        elif input_selector == 2:
            return (input2,)
        elif input_selector == 3:
            return (input3,)
        elif input_selector == 4:
            return (input4,)
        else:
            return (input0,)
```