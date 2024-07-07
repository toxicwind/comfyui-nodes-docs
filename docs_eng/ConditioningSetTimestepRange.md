# Documentation
- Class name: ConditioningSetTimestepRange
- Category: advanced/conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditionSetTimestepRange node is intended to modify the time frame of the set of conditions. It allows the percentage to be specified for start and end, and then the node applies the percentage to condition data to set the required range. This node plays a key role in controlling the time frame of condition information, which can significantly influence the behaviour of subsequent model operations.

# Input types
## Required
- conditioning
    - Conditional parameters are essential because they represent data sets to be operated by nodes. This is the core input, which determines the operation of nodes and subsequent modifications to the time frame of the concentration of conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- start
    - The starting parameter defines the beginning of the time range to be set within the condition data. It is essential to determine where the node will start changing the time range of the set of conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end
    - End parameters represent the end point of the time range to be set within the condition data. It is essential to create nodes that modify the end point of the time range of the condition set.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - Output parameters represent the set of conditions that are modified after the application of the specified time frame. It is important because it contains the latest time information to be used in the next step of the model operation.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningSetTimestepRange:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'start': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'set_range'
    CATEGORY = 'advanced/conditioning'

    def set_range(self, conditioning, start, end):
        c = node_helpers.conditioning_set_values(conditioning, {'start_percent': start, 'end_percent': end})
        return (c,)
```