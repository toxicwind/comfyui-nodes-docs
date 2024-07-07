# Documentation
- Class name: LatentPixelScale
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The LatentPixelScale node is designed to sample the potential for images to a higher resolution. It enhances the detail and clarity of potential images by applying various scaling methods and factors. The node plays a key role in the image processing process, making it possible to create high-resolution images from a low-resolution potential state.

# Input types
## Required
- samples
    - The parameter'samples' is essential because it represents the potential expression of the image to be sampled. It is the main input that affects node operations and the quality of the output to be sampled.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- scale_method
    - The parameter's scale_method' determines the algorithm to be used for up-sampling potential images. This is a key option that affects the final appearance and performance of up-sampling images.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'lanczos', 'area']
    - Python dtype: str
- scale_factor
    - The parameter'sscape_factor' defines the extent to which a potential image is sampled. It is a key factor in controlling image magnification multiples and final resolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- vae
    - The parameter 'vae' is a variable encoder model used to decode and encode potential expressions. It is essential for the function of the node and ensures the integrity of the image during the sampling process.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- use_tiled_vae
    - The parameter 'use_tiled_vae' indicates whether the ply-down method should be used to decode and encode potential expressions. This improves the efficiency of large images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- upscale_model_opt
    - The optional parameter 'upscale_model_opt' allows the specification of a custom model to be used in the sampling process. It provides flexibility for advanced users wishing to apply specific sampling techniques.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: torch.nn.Module

# Output types
- latent
    - The output 'latet' represents a potential indication of the upper sampling of the input image. It is important because it retains the enhanced detail and resolution achieved through the upper sampling process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- image
    - The output 'image' is a visual expression of the potential image being sampled above. It is the final product of the node, showing the results of the sampling process in a human readable format.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class LatentPixelScale:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'scale_method': (s.upscale_methods,), 'scale_factor': ('FLOAT', {'default': 1.5, 'min': 0.1, 'max': 10000, 'step': 0.1}), 'vae': ('VAE',), 'use_tiled_vae': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'})}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, samples, scale_method, scale_factor, vae, use_tiled_vae, upscale_model_opt=None):
        if upscale_model_opt is None:
            latimg = core.latent_upscale_on_pixel_space2(samples, scale_method, scale_factor, vae, use_tile=use_tiled_vae)
        else:
            latimg = core.latent_upscale_on_pixel_space_with_model2(samples, scale_method, upscale_model_opt, scale_factor, vae, use_tile=use_tiled_vae)
        return latimg
```