# Documentation
- Class name: KfConditioningAddx10
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node accumulates a processing condition input that enhances the overall condition data through the input provided by the polymer.

# Input types
## Required
- cond_0
    - The initial condition data is essential to the operation of the node. It sets a baseline for subsequent polymerization.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
## Optional
- cond_1
    - An optional condition input that contributes to the cumulative effect of the output. It is combined with base condition data.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_2
    - Another additional optional condition input further facilitates the cumulative processing of node operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_3
    - Another optional condition input, which is integrated into the cumulative output, enhances the overall function of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_4
    - This optional condition input is part of a cumulative data stream that affects the final output of nodes.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_5
    - This condition input further refines the cumulative data and plays a role in the integrated treatment of nodes.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_6
    - An optional input that facilitates the cumulative data processing of nodes and influences the quality of the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_7
    - This option input is integrated into cumulative data, further enhancing the processing capacity of nodes.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_8
    - This condition input helps to accumulate the final output and influences the overall effect of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- cond_9
    - An additional optional condition input is part of the cumulative data that affects the final output of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]

# Output types
- cond_t_out
    - The cumulative results of the conditions entered represent the aggregate and post-processing data.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[Any, Dict[str, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class KfConditioningAddx10:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('CONDITIONING',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'cond_0': ('CONDITIONING', {'forceInput': True})}, 'optional': {'cond_1': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_2': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_3': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_4': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_5': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_6': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_7': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_8': ('CONDITIONING', {'forceInput': True, 'default': 0}), 'cond_9': ('CONDITIONING', {'forceInput': True, 'default': 0})}}

    def main(self, cond_0, **kwargs):
        ((cond_t_out, cond_d_out),) = deepcopy(cond_0)
        for ((cond_t, cond_d),) in kwargs.values():
            (cond_t, cond_d) = (deepcopy(cond_t), deepcopy(cond_d))
            cond_t_out = cond_t_out + cond_t
            cond_d_out['pooled_output'] = cond_d_out['pooled_output'] + cond_d['pooled_output']
        return [((cond_t_out, cond_d_out),)]
```