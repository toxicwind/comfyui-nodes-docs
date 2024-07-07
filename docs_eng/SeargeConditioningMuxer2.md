# Documentation
- Class name: SeargeConditioningMuxer2
- Category: Searge/_deprecated_/FlowControl
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node, as a multi-routine repeater, selects one of the two conditions for input according to the value of the selector. It is designed to allow data processing to be carried out conditionally by proper input to the output from the middle of the data stream.

# Input types
## Required
- input0
    - The first condition is entered and the selection will be considered by the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input1
    - The second condition input is the first input alternative option.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- input_selector
    - Select the parameter to determine which condition input will be routed to the output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - Enter the conditions based on the input_selector value.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeConditioningMuxer2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input0': ('CONDITIONING',), 'input1': ('CONDITIONING',), 'input_selector': ('INT', {'default': 0, 'min': 0, 'max': 1})}}
    RETURN_TYPES = ('CONDITIONING',)
    RETURN_NAMES = ('output',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/FlowControl'

    def mux(self, input0, input1, input_selector):
        if input_selector == 1:
            return (input1,)
        else:
            return (input0,)
```