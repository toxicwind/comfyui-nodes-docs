# Documentation
- Class name: ConditioningConcat
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditionConcat node is designed to combine two conditions into a single output. It tactfully connects the source input to the target input along the specified dimensions to ensure that the output generated is well suited to the next steps in the neural network architecture.

# Input types
## Required
- conditioning_to
    - The 'conventioning_to' parameter indicates a target condition input that will be linked to another condition input. It plays a key role in determining the structure of the final output, as it determines the basis for additional condition information.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]
- conditioning_from
    - The 'conventioning_from' parameter provides a source-condition input that will be combined with 'convention_to'. It is important because it contributes additional context or features to the output of the final connection and may enhance the ability of the model to make informed predictions.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]

# Output types
- output
    - The output of the ConditionConcat node is a combined condition mass that integrates the elements entered in 'convention_to' and 'convention_from'. This output is strategically constructed to be compatible with downstream neural network operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningConcat:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning_to': ('CONDITIONING',), 'conditioning_from': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'concat'
    CATEGORY = 'conditioning'

    def concat(self, conditioning_to, conditioning_from):
        out = []
        if len(conditioning_from) > 1:
            logging.warning('Warning: ConditioningConcat conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.')
        cond_from = conditioning_from[0][0]
        for i in range(len(conditioning_to)):
            t1 = conditioning_to[i][0]
            tw = torch.cat((t1, cond_from), 1)
            n = [tw, conditioning_to[i][1].copy()]
            out.append(n)
        return (out,)
```