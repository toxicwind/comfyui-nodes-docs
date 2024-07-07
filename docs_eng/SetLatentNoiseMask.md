# Documentation
- Class name: SetLatentNoiseMask
- Category: latent/inpaint
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SetLatentnoisemask node is designed to apply noise masks to a group of potential samples. It plays a key role in the restoration process, by allowing selective handling of potential space expressions. The node is essential for generating consistent and accurate visual output by ensuring that the hidden areas are appropriately modified according to the available mask.

# Input types
## Required
- samples
    - The "samples" parameter is a collection of potential expressions that will be modified by the noise mask. It is essential for the operation of the node, as it determines the data that will experience the masking process. It directly influences the execution of the node and the ultimate visual effect.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- mask
    - The " mask " parameter defines the area of the potential sample that needs to be hidden. It is essential for the node, because it determines the part of the potential space that will be changed. The mask shape must be compatible with the potential sample so that the node works correctly.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- modified_samples
    - The "modified_samples" output consists of a potential sample of the noise mask that has been applied. This output is important because it represents the main result of the node and will be used for the subsequent repair workflow phase.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class SetLatentNoiseMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'set_mask'
    CATEGORY = 'latent/inpaint'

    def set_mask(self, samples, mask):
        s = samples.copy()
        s['noise_mask'] = mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1]))
        return (s,)
```