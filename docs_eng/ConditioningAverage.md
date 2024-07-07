# Documentation
- Class name: ConditioningAverage
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditionAverage nodes are designed to mix different conditions by applying weighted averages. It combines `convention_from' with `convention_to' based on specified strength intelligence and allows fine control of condition processes in the generation model.

# Input types
## Required
- conditioning_to
    - The `conventioning_to' parameter is essential because it defines the target condition data that will be applied with a weighted average. It plays an important role in determining the final output of nodes, influencing the outcome by influencing the method of implementation of the mixed conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- conditioning_from
    - The `conventioning_from' parameter is essential because it provides data on the source conditions that will be averaged with `conventioning_to'. It is important because it determines the initial conditions that will be mixed, thus affecting the execution of nodes and the output of results.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- conditioning_to_strength
    - The `conventioning_to_prength' parameter is critical in determining the extent to which `convention_to' affects the weighted average. It directly affects the operation of nodes by controlling the extent to which `convention_to' covers `convention_from' in the mix.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - The output of the ConditionAverage node is a list of groups of words containing the modified lengths and possibly the 'pooled_output' dictionary. This output represents the results of the weighted average mixing process and is important for further processing in the generation model.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningAverage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning_to': ('CONDITIONING',), 'conditioning_from': ('CONDITIONING',), 'conditioning_to_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'addWeighted'
    CATEGORY = 'conditioning'

    def addWeighted(self, conditioning_to, conditioning_from, conditioning_to_strength):
        out = []
        if len(conditioning_from) > 1:
            logging.warning('Warning: ConditioningAverage conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.')
        cond_from = conditioning_from[0][0]
        pooled_output_from = conditioning_from[0][1].get('pooled_output', None)
        for i in range(len(conditioning_to)):
            t1 = conditioning_to[i][0]
            pooled_output_to = conditioning_to[i][1].get('pooled_output', pooled_output_from)
            t0 = cond_from[:, :t1.shape[1]]
            if t0.shape[1] < t1.shape[1]:
                t0 = torch.cat([t0] + [torch.zeros((1, t1.shape[1] - t0.shape[1], t1.shape[2]))], dim=1)
            tw = torch.mul(t1, conditioning_to_strength) + torch.mul(t0, 1.0 - conditioning_to_strength)
            t_to = conditioning_to[i][1].copy()
            if pooled_output_from is not None and pooled_output_to is not None:
                t_to['pooled_output'] = torch.mul(pooled_output_to, conditioning_to_strength) + torch.mul(pooled_output_from, 1.0 - conditioning_to_strength)
            elif pooled_output_from is not None:
                t_to['pooled_output'] = pooled_output_from
            n = [tw, t_to]
            out.append(n)
        return (out,)
```