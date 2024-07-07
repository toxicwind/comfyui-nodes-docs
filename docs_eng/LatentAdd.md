# Documentation
- Class name: LatentAdd
- Category: latent/advanced
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The “LatentAdd” node is designed to implement element-by-element additions for two groups of potential samples. It ensures that samples are appropriately recast to match dimensions before additions, thus allowing seamless combinations of potential expressions from different sources or scales.

# Input types
## Required
- samples1
    - The “samples1” parameter represents the first group of potential samples to be added. It plays a key role in the operation of the node, as it provides one of the number of add-on operations. The quality and format of these samples directly influence the results of the node implementation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- samples2
    - The samples2 parameter saves a second group of potential samples to be added to samples1. Its compatibility with samples1 in shape and type is essential for the successful implementation of the node function.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- samples_out
    - The " samples_out " parameter is the result of an addition exercise performed by the node. It contains a potential sample that is added up and that is important because it represents the output of the node's main function.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentAdd:

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
        samples_out['samples'] = s1 + s2
        return (samples_out,)
```