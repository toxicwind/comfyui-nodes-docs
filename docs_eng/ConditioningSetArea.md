# Documentation
- Class name: ConditioningSetArea
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditionSetArea nodes are designed to operate and add data to the condition set, which is essential for influencing behaviour in some models. It allows for the designation of an area and its associated strength, which can guide model output in the desired direction.

# Input types
## Required
- conditioning
    - Conditional parameters are essential because they define the initial state or context of the model's treatment. This is a key input that directly affects how the model interprets and responds to the data it processes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- width
    - Width parameters specify the width of the area for which conditions are to be treated. It plays an important role in determining the spatial range of conditions in model operations.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the area affected by the condition. It is important for controlling the interest of the model in a given area.
    - Comfy dtype: INT
    - Python dtype: int
- x
    - The x parameter determines the horizontal starting point of the area affected by the condition. It is essential for the precise location of the conditions for application in the precise positioning model input space.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y parameter determines the vertical starting point of the area for which conditions are to be processed. It works with x parameter to define the exact coordinates of the effect of the conditions.
    - Comfy dtype: INT
    - Python dtype: int
- strength
    - The strength parameters quantify the strength of the condition effect. It is a key factor in the extent to which model output is affected by the set of conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - The output set of conditions is the result of applying the specified parameters to the initial set of conditions. It reflects the updated state of the model to be used for further processing.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningSetArea:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'width': ('INT', {'default': 64, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 64, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'append'
    CATEGORY = 'conditioning'

    def append(self, conditioning, width, height, x, y, strength):
        c = node_helpers.conditioning_set_values(conditioning, {'area': (height // 8, width // 8, y // 8, x // 8), 'strength': strength, 'set_area_to_bounds': False})
        return (c,)
```