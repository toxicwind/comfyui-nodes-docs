# Documentation
- Class name: LatentSubtract
- Category: latent/advanced
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentSubtract node is designed to deflate two groups of potential samples. It receives two potential indications as input and exports their differences, which are very useful for various applications, such as feature extraction or unusual detection in potential space.

# Input types
## Required
- samples1
    - The first group of potential samples for subtraction operations. These samples are critical because they form the basis of the operation and their quality directly influences the results of node execution.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- samples2
    - The second group of potential samples will be subtracted from the first group. The alignment and compatibility of these samples with the first group is essential for the relevance of the subtraction operation.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Output types
- samples_out
    - The output of the subtraction operation is a potential sample of differences between input sets. This output can be used for further analysis or as input to nodes in the follow-up processing process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentSubtract:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples1': ('LATENT',), 'samples2': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'op'
    CATEGORY = 'latent/advanced'

    def op(self, samples1, samples2):
        samples_out = samples1.copy()
        s1 = samples1['samples']
        s2 = samples2['samples']
        s2 = reshape_latent_to(s1.shape, s2)
        samples_out['samples'] = s1 - s2
        return (samples_out,)
```