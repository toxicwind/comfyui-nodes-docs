# Documentation
- Class name: LatentMultiply
- Category: latent/advanced
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The node is intended to perform a multiplier operation for potential space samples. It receives a group of potential samples and a multiplier value, which is then applied to each sample in a pool, thereby scaling the potential spatial representation. In various production models, the size of the potential vector can significantly influence the output, so this operation is essential.

# Input types
## Required
- samples
    - The'samples' parameter represents the potential vector of a group multiplied by a given factor. This is essential for the operation of the node, as it determines the data that will be executed by multiplying operations.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- multiplier
    - The'multiplier' parameter is a floating point number used to zoom in potential samples. It plays an important role in the function of the node because it directly influences the size of the potential vectors obtained after the multiplication operation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- samples_out
    - The'samples_out 'parameter is an output of node containing a potential sample that has been multiplied by the specified multiplier. This output is important because it represents the converted potential space that can be used for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentMultiply:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'multiplier': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'op'
    CATEGORY = 'latent/advanced'

    def op(self, samples, multiplier):
        samples_out = samples.copy()
        s1 = samples['samples']
        samples_out['samples'] = s1 * multiplier
        return (samples_out,)
```