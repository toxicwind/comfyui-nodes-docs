# Documentation
- Class name: LatentComposite
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentComposite node is designed to mix the potential expressions of two different sample sets. It performs synthesis operations, which can be performed in a normal or plume manner, by which one sample is integrated seamlessly into another according to the specified coordinates and mixing method.

# Input types
## Required
- samples_to
    - The parameter'samples_to' means the underlying potential sample that will be synthesized'samples_from'. It's vital because it determines the structure and dimensions of the final output.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- samples_from
    - The parameter'samples_from' defines the potential samples that will be synthesized on'samples_to'. Its selection significantly influences the final combination.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- x
    - Parameter'x' specifies the horizontal starting coordinates of the synthetic operation. Its value directly affects the location of'samples_from' in'samples_to'.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The parameter 'y' determines the vertical starting coordinates of the synthetic operation. It is essential for'samples_from' placement in'samples_to'.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- feather
    - Parameter'feather' controls the smoothness of the edges of the synthetic operation. Non-zero values create a plume or gradual transition between two groups of samples.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples_out
    - The parameter'samples_out' is the result of a synthetic operation, representing a potential sample that has been merged from'samples_to' and'samples_from'.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentComposite:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples_to': ('LATENT',), 'samples_from': ('LATENT',), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'feather': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'composite'
    CATEGORY = 'latent'

    def composite(self, samples_to, samples_from, x, y, composite_method='normal', feather=0):
        x = x // 8
        y = y // 8
        feather = feather // 8
        samples_out = samples_to.copy()
        s = samples_to['samples'].clone()
        samples_to = samples_to['samples']
        samples_from = samples_from['samples']
        if feather == 0:
            s[:, :, y:y + samples_from.shape[2], x:x + samples_from.shape[3]] = samples_from[:, :, :samples_to.shape[2] - y, :samples_to.shape[3] - x]
        else:
            samples_from = samples_from[:, :, :samples_to.shape[2] - y, :samples_to.shape[3] - x]
            mask = torch.ones_like(samples_from)
            for t in range(feather):
                if y != 0:
                    mask[:, :, t:1 + t, :] *= 1.0 / feather * (t + 1)
                if y + samples_from.shape[2] < samples_to.shape[2]:
                    mask[:, :, mask.shape[2] - 1 - t:mask.shape[2] - t, :] *= 1.0 / feather * (t + 1)
                if x != 0:
                    mask[:, :, :, t:1 + t] *= 1.0 / feather * (t + 1)
                if x + samples_from.shape[3] < samples_to.shape[3]:
                    mask[:, :, :, mask.shape[3] - 1 - t:mask.shape[3] - t] *= 1.0 / feather * (t + 1)
            rev_mask = torch.ones_like(mask) - mask
            s[:, :, y:y + samples_from.shape[2], x:x + samples_from.shape[3]] = samples_from[:, :, :samples_to.shape[2] - y, :samples_to.shape[3] - x] * mask + s[:, :, y:y + samples_from.shape[2], x:x + samples_from.shape[3]] * rev_mask
        samples_out['samples'] = s
        return (samples_out,)
```