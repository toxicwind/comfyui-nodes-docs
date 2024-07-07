# Documentation
- Class name: LatentInterpolate
- Category: latent/advanced
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentInterpolate node is designed to interpolate two groups of potential samples. It achieves this by calculating the weighting and weighting of the input sample, which is determined by the assigned scale. This node is particularly useful in generating smooth transitions between different potential expressions, which is critical in applications such as image deformation or style migration.

# Input types
## Required
- samples1
    - The first group of potential samples that will be plugged in values. These samples are the starting point of the plug-in process and are essential for defining the initial state of transition.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- samples2
    - These samples represent the end of the plug value and are essential for determining the end state of the transition.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- ratio
    - Scale parameters control the degree of interpolation between two groups of samples. A value close to 0 produces an output closer to samples1, while a value close to 1 produces an output closer to samples2.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The output of the LatentInterpolate node is a potential sample after a set of plug-in values. These samples provide a seamless transition between the two based on a specified mass input sample.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentInterpolate:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples1': ('LATENT',), 'samples2': ('LATENT',), 'ratio': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'op'
    CATEGORY = 'latent/advanced'

    def op(self, samples1, samples2, ratio):
        samples_out = samples1.copy()
        s1 = samples1['samples']
        s2 = samples2['samples']
        s2 = reshape_latent_to(s1.shape, s2)
        m1 = torch.linalg.vector_norm(s1, dim=1)
        m2 = torch.linalg.vector_norm(s2, dim=1)
        s1 = torch.nan_to_num(s1 / m1)
        s2 = torch.nan_to_num(s2 / m2)
        t = s1 * ratio + s2 * (1.0 - ratio)
        mt = torch.linalg.vector_norm(t, dim=1)
        st = torch.nan_to_num(t / mt)
        samples_out['samples'] = st * (m1 * ratio + m2 * (1.0 - ratio))
        return (samples_out,)
```