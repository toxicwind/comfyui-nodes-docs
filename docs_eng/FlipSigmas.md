# Documentation
- Class name: FlipSigmas
- Category: sampling/custom_sampling/sigmas
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The FlipSigmas node is designed to operate the sigma value used in the sampling process. It can reverse the sigmas order and ensure that the sampling process follows a particular sequence. In a custom sampling strategy, the node has an important influence on the outcome, with the sigmas sequence being critical to the outcome.

# Input types
## Required
- sigmas
    - The `sigmas' parameter is a volume that contains the sigma values used in the sampling process. It is essential to define the order and scale of noise reductions during the sampling. Node directs the operation of this parameter to generate the quality and properties of the sample.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- SIGMAS
    - The output `SIGMAS' is a volume that represents the sigma value after a flip. This output is very important because it determines the sequence of subsequent sampling steps and may result in different results of the sample.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FlipSigmas:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sigmas': ('SIGMAS',)}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/sigmas'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, sigmas):
        if len(sigmas) == 0:
            return (sigmas,)
        sigmas = sigmas.flip(0)
        if sigmas[0] == 0:
            sigmas[0] = 0.0001
        return (sigmas,)
```