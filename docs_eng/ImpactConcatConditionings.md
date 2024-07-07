# Documentation
- Class name: ConcatConditionings
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The node is intended to combine multiple conditions into individual output. It effectively combines their effects by connecting the first element of each condition to the main input. The node plays a key role in consolidating different conditions signals to guide subsequent model behaviour.

# Input types
## Required
- conditioning1
    - The main conditions are entered, which will be combined with other conditions. It is essential because it forms the basis for the combined output and affects the final conditions applied to the model.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]
## Optional
- conditioning_from
    - Enter the additional condition that will be linked to the main condition input. Each input is expected to contribute to the overall condition effect, but if multiple conditions exist, a warning is given that only the first one will be applied.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]

# Output types
- out
    - The output of the node is a consolidated list of condition-to-conditions, consisting of each pair that is connected by the main and additional condition-strength, and a copy of the original condition to the secondary element.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConcatConditionings:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning1': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, **kwargs):
        conditioning_to = list(kwargs.values())[0]
        for (k, conditioning_from) in list(kwargs.items())[1:]:
            out = []
            if len(conditioning_from) > 1:
                print('Warning: ConcatConditionings {k} contains more than 1 cond, only the first one will actually be applied to conditioning1.')
            cond_from = conditioning_from[0][0]
            for i in range(len(conditioning_to)):
                t1 = conditioning_to[i][0]
                tw = torch.cat((t1, cond_from), 1)
                n = [tw, conditioning_to[i][1].copy()]
                out.append(n)
            conditioning_to = out
        return (out,)
```