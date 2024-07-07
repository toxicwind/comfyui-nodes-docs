# Documentation
- Class name: ConditioningSetMask
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Conditioning Setmask node is designed to modify the given set of conditions by applying a mask and adjusting its strength. It allows customization of the condition area and enhances the flexibility of the model to respond to different inputs.

# Input types
## Required
- conditioning
    - Conditional parameters are necessary because it defines the basic set of conditions that the nodes will operate. It directly affects the manner in which the mask and strength parameters are applied and the end result.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- mask
    - The mask parameter is essential to determine the elements that are to be modified by the concentration of conditions. It works in conjunction with the strength parameter to control the scope of the change.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- strength
    - The strength parameter determines the intensity of the mask's impact on the set of conditions. It is particularly important because it adjusts the scope of the mask's impact and allows fine-tuning of node output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - Set_cond_area parameters specify whether to use the default condition area or the application of the mask boundary. This option significantly changes the set of behavioural and result conditions of the node.
    - Comfy dtype: COMBO['default', 'mask bounds']
    - Python dtype: str

# Output types
- conditioning
    - The output set of conditions is the result of applying the input mask and strength to the original set of conditions. It represents the ultimate contribution of the node to the model processing process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningSetMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'mask': ('MASK',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'set_cond_area': (['default', 'mask bounds'],)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'append'
    CATEGORY = 'conditioning'

    def append(self, conditioning, mask, set_cond_area, strength):
        set_area_to_bounds = False
        if set_cond_area != 'default':
            set_area_to_bounds = True
        if len(mask.shape) < 3:
            mask = mask.unsqueeze(0)
        c = node_helpers.conditioning_set_values(conditioning, {'mask': mask, 'set_area_to_bounds': set_area_to_bounds, 'mask_strength': strength})
        return (c,)
```