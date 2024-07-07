# Documentation
- Class name: KfConditioningAdd
- Category: CATEGORY
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is used to generate a combined reconciliation output from the two reconciliations. It emphasizes data integration to enhance the overall reconciliation impact without changing the respective data structures.

# Input types
## Required
- conditioning_1
    - The first reconciliation input is essential for the operation of the node, providing the initial data set to be combined with the second input. It provides the basis for the integration process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, Any]]
- conditioning_2
    - The second reconciliation input supplements the first input and allows for the addition of another data set to the mix. This is essential for achieving full reconciliation results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, Any]]

# Output types
- CONDITIONING
    - Output is the combined reconciliation set of two input additions. It represents an enhanced reconciliation effect that can be used further in the process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class KfConditioningAdd:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('CONDITIONING',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning_1': ('CONDITIONING',), 'conditioning_2': ('CONDITIONING',)}}

    def main(self, conditioning_1, conditioning_2):
        conditioning_1 = deepcopy(conditioning_1)
        conditioning_2 = deepcopy(conditioning_2)
        assert len(conditioning_1) == len(conditioning_2)
        outv = []
        for (i, ((c1_tensor, c1_dict), (c2_tensor, c2_dict))) in enumerate(zip(conditioning_1, conditioning_2)):
            c1_tensor += c2_tensor
            if 'pooled_output' in c1_dict and 'pooled_output' in c2_dict:
                c1_dict['pooled_output'] += c2_dict['pooled_output']
            outv.append((c1_tensor, c1_dict))
        return (outv,)
```