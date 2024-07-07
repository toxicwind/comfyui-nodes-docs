# Documentation
- Class name: WAS_Latent_Upscale
- Category: WAS Suite/Latent/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `latent_upscale'method is designed to enhance the resolution of potential expressions by applying the specified plug-in mode and zoom factor. It plays a key role in the conversion of the WAS package, ensuring that potential features are accurately and efficiently magnified, thus contributing to the overall quality of the output generated.

# Input types
## Required
- samples
    - The samples parameter is essential because it preserves the potential expression to magnify. It directly influences the operation of the nodes by identifying the input data to be magnified.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- mode
    - The "mode" parameter defines the plug-in method used to magnify. It is essential because it determines the algorithm for raising the resolution, thus affecting the quality of the final output.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- factor
    - The “factor” parameter specifies the zoom factor for the magnification operation. It is the key determinant in the conversion process, as it controls the extent of magnification applied to potential samples.
    - Comfy dtype: FLOAT
    - Python dtype: float
- align
    - The “align” parameter is important because it decides whether to use an angular scaling. This option can have a subtle but observable effect on the expression of eventual magnification.
    - Comfy dtype: COMBO[bool]
    - Python dtype: bool

# Output types
- upscaled_samples
    - The "upscaled_samples" output contains the potential for magnification by conversion. It is important because it represents the direct result of node operations and contains the characteristics of the magnification.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_Latent_Upscale:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'samples': ('LATENT',), 'mode': (['area', 'bicubic', 'bilinear', 'nearest'],), 'factor': ('FLOAT', {'default': 2.0, 'min': 0.1, 'max': 8.0, 'step': 0.01}), 'align': (['true', 'false'],)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'latent_upscale'
    CATEGORY = 'WAS Suite/Latent/Transform'

    def latent_upscale(self, samples, mode, factor, align):
        valid_modes = ['area', 'bicubic', 'bilinear', 'nearest']
        if mode not in valid_modes:
            cstr(f"Invalid interpolation mode `{mode}` selected. Valid modes are: {', '.join(valid_modes)}").error.print()
            return (s,)
        align = True if align == 'true' else False
        if not isinstance(factor, float) or factor <= 0:
            cstr(f'The input `factor` is `{factor}`, but should be a positive or negative float.').error.print()
            return (s,)
        s = samples.copy()
        shape = s['samples'].shape
        size = tuple((int(round(dim * factor)) for dim in shape[-2:]))
        if mode in ['linear', 'bilinear', 'bicubic', 'trilinear']:
            s['samples'] = torch.nn.functional.interpolate(s['samples'], size=size, mode=mode, align_corners=align)
        else:
            s['samples'] = torch.nn.functional.interpolate(s['samples'], size=size, mode=mode)
        return (s,)
```