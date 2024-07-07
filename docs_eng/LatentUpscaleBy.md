# Documentation
- Class name: LatentUpscaleBy
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `LatentUpscaleby' node is designed to improve the resolution of potential expressions by using a variety of sampling methods. It plays a key role in the pre-processing process, particularly with regard to the application of potential vectors that require a higher level of certainty. The objective of the node is to improve the quality of potential data without changing the intrinsic properties of potential data.

# Input types
## Required
- samples
    - The `samples' parameter is essential because it contains potential indications of the need for sampling. It significantly influences the operation and final output of nodes and determines the underlying data for the implementation of sampling.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- upscale_method
    - The `upscale_method' parameter determines the algorithm to be used for sampling potential samples. It is a key factor in determining the quality and style of sampling output and provides a variety of options to meet different needs.
    - Comfy dtype: STRING
    - Python dtype: str
- scale_by
    - The `scale_by' parameter specifies the zoom factor during the sampling process. It is essential to control the level of sampling applied to potential samples and therefore directly affects the resolution of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- upscaled_samples
    - The `upscaled_samples' output represents potential indications after the sampling process. It is important because it contains the main function of the node and provides an enhanced potential vector ready for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentUpscaleBy:
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'upscale_method': (s.upscale_methods,), 'scale_by': ('FLOAT', {'default': 1.5, 'min': 0.01, 'max': 8.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'upscale'
    CATEGORY = 'latent'

    def upscale(self, samples, upscale_method, scale_by):
        s = samples.copy()
        width = round(samples['samples'].shape[3] * scale_by)
        height = round(samples['samples'].shape[2] * scale_by)
        s['samples'] = comfy.utils.common_upscale(samples['samples'], width, height, upscale_method, 'disabled')
        return (s,)
```