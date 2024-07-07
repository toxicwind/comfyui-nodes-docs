# Documentation
- Class name: LatentBlend
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentBlend node is designed to integrate and mix two groups of potential samples seamlessly through the specified mix factor. It operates by adjusting the contribution of each sample set and allows for the creation of composite expressions that can be used for further processing or visualization.

# Input types
## Required
- samples1
    - The first group of potential samples will be mixed with another group. It plays a crucial role in determining the initial state of the mixed output.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- samples2
    - A potential sample of the second group, which will be commingled with the first group, is equally important in influencing the final mixed results.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- blend_factor
    - A floating number, which determines the extent to which the second group of samples blends with the first group of samples. It is essential for controlling the balance between the two groups of samples in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- blend_mode
    - Specifies the mix mode used for group samples. The only option currently supported is 'normal'.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- samples_out
    - The output is a mixture of potential samples that are combined with the specified mix factors.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBlend:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples1': ('LATENT',), 'samples2': ('LATENT',), 'blend_factor': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'blend'
    CATEGORY = '_for_testing'

    def blend(self, samples1, samples2, blend_factor: float, blend_mode: str='normal'):
        samples_out = samples1.copy()
        samples1 = samples1['samples']
        samples2 = samples2['samples']
        if samples1.shape != samples2.shape:
            samples2.permute(0, 3, 1, 2)
            samples2 = comfy.utils.common_upscale(samples2, samples1.shape[3], samples1.shape[2], 'bicubic', crop='center')
            samples2.permute(0, 2, 3, 1)
        samples_blended = self.blend_mode(samples1, samples2, blend_mode)
        samples_blended = samples1 * blend_factor + samples_blended * (1 - blend_factor)
        samples_out['samples'] = samples_blended
        return (samples_out,)

    def blend_mode(self, img1, img2, mode):
        if mode == 'normal':
            return img2
        else:
            raise ValueError(f'Unsupported blend mode: {mode}')
```