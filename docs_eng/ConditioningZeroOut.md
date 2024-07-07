# Documentation
- Class name: ConditioningZeroOut
- Category: advanced/conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Conditioning ZeroOut nodes is designed to operate condition data by zeroing specific elements in condition data (e.g. 'pooled_output'). This process is essential for controlling the flow of information in neural networks and allows targeted changes to model predictions without changing the underlying structure of the data.

# Input types
## Required
- conditioning
    - The 'conventioning' parameter is essential to the operation of the node because it provides the input data that will be processed. This input significantly influences the execution of the node and the outcome of the zeroing exercise, determining which of the condition data is positioned as a modified target.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]

# Output types
- conditioning
    - The output 'convention' parameter represents the condition data modified by the Zero_out operation. It is important because it carries up-to-date information that directly affects the next steps in the neural network processing process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningZeroOut:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'zero_out'
    CATEGORY = 'advanced/conditioning'

    def zero_out(self, conditioning):
        c = []
        for t in conditioning:
            d = t[1].copy()
            if 'pooled_output' in d:
                d['pooled_output'] = torch.zeros_like(d['pooled_output'])
            n = [torch.zeros_like(t[0]), d]
            c.append(n)
        return (c,)
```