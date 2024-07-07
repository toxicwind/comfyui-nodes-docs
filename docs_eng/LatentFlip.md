# Documentation
- Class name: LatentFlip
- Category: latent/transform
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentFlip node is designed to convert potential spatial expressions by reversing them along a specified axis application. This node plays a key role in manipulation of potential features, which is essential for tasks such as data enhancement or exploration of potential space structures.

# Input types
## Required
- samples
    - The “samples” parameter is essential because it contains potential indications that nodes will be dealt with. It directly influences the ability of nodes to do flip operations and, in turn, their output.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- flip_method
    - The flip_method parameter determines which axis the potential sample will be flipped along. It is a key component because it determines the nature of the change applied to the potential space.
    - Comfy dtype: COMBO['x-axis: vertically', 'y-axis: horizontally']
    - Python dtype: str

# Output types
- samples
    - The'samples' output contains the potential indication of a reversal, which is the result of node operations. This output is important because it represents conversion data that can be used for downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class LatentFlip:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'flip_method': (['x-axis: vertically', 'y-axis: horizontally'],)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'flip'
    CATEGORY = 'latent/transform'

    def flip(self, samples, flip_method):
        s = samples.copy()
        if flip_method.startswith('x'):
            s['samples'] = torch.flip(samples['samples'], dims=[2])
        elif flip_method.startswith('y'):
            s['samples'] = torch.flip(samples['samples'], dims=[3])
        return (s,)
```