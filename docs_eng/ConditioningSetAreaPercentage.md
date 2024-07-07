# Documentation
- Class name: ConditioningSetAreaPercentage
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Conditioning SetAreaPercentage node is designed to modify the properties of the condition set by adding a new set of parameters that define area percentages. It operates by adjusting the 'area' attribute to a percentage value based on the width and altitude provided, without affecting existing limits. The node plays a key role in fine-tuning the conditions of the model, allowing for more sophisticated control of the condition process.

# Input types
## Required
- conditioning
    - Conditional parameters are essential for the node because they represent the initial set of conditions that will be modified. This is the starting point for node operations and determines the context of the percentage of the area to be applied.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- width
    - The width parameter defines the percentage of the area width relative to the total width. It is a key factor in determining the size of the area in which the conditions are concentrated, and therefore has a significant impact on the output of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- height
    - The height parameter specifies a percentage of the area height relative to the total height. It works with the width to determine the size of the area in which the conditions are concentrated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x
    - The x parameter indicates the horizontal position of the upper left corner of the condensed area. It is essential for the precise location of the percentage of the area of application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y
    - y parameter indicates the vertical position of the upper left corner of the condensed area. It is essential for the precise location of the area in the concentrated area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength
    - The intensity parameters determine the intensity of the impact of the concentration of conditions within the region. It allows fine-tuning of the regional characteristics to strongly influence overall conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - The output set of conditions is the modified version of the input, applying the area percentage and strength parameters. It represents the updated state of the node after processing.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningSetAreaPercentage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'width': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 1.0, 'step': 0.01}), 'height': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 1.0, 'step': 0.01}), 'x': ('FLOAT', {'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01}), 'y': ('FLOAT', {'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'append'
    CATEGORY = 'conditioning'

    def append(self, conditioning, width, height, x, y, strength):
        c = node_helpers.conditioning_set_values(conditioning, {'area': ('percentage', height, width, y, x), 'strength': strength, 'set_area_to_bounds': False})
        return (c,)
```