# Documentation
- Class name: TwoSamplersForMaskUpscalerProviderPipe
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Two Samplers For MaskUpscaler Provider Pipe node is designed to expand the image efficiently using two different sampling methods. It performs the magnification process using a combination of basic samplers and mask samplers, as well as mask and variable self-codifiers (VAE). The node can handle different magnification methods and plans, and can selectively use block VAE to improve performance. It is particularly suitable for applications requiring high-quality image magnification.

# Input types
## Required
- scale_method
    - Scale_method parameters determine the algorithm for image magnification. This is a key component because it directly affects the quality and efficiency of the magnification process.
    - Comfy dtype: str
    - Python dtype: str
- full_sample_schedule
    - The full_sample_schedule parameter determines when full sampling is performed during the magnification process. This parameter is essential for controlling the frequency of sampling and thus for balancing speed and quality.
    - Comfy dtype: str
    - Python dtype: str
- use_tiled_vae
    - This parameter is important for optimizing performance in the GPU structure.
    - Comfy dtype: bool
    - Python dtype: bool
- base_sampler
    - The basic sampler is a basic component of the magnification process and is responsible for producing the initial sample. Its selection can greatly influence the overall results of the magnification.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSampler
- mask_sampler
    - The mask sampler is used in conjunction with the base sampler to apply specific sampling techniques to the masked area of the image. It plays a key role in achieving the magnification effect.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSampler
- mask
    - The mask parameter defines the image range that will be processed by the mask sampler. It plays a vital role in the selective zooming of images in the selected area.
    - Comfy dtype: MASK
    - Python dtype: Mask
- basic_pipe
    - The basic pipe covers the basic elements required for the magnification process, including the VAE. It is essential for the function of the node.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: BasicPipe
## Optional
- tile_size
    - The tile_size parameter specifies the size of the tiles to be used when processing images using the fragment VAE. It is important for managing memory use and processing time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- upscaler
    - The output of the node is a magnifying object that contains the results of the magnification process. It is important because it represents the final output for further use or analysis.
    - Comfy dtype: UPSCALER
    - Python dtype: Upscaler

# Usage tips
- Infra type: GPU

# Source code
```
class TwoSamplersForMaskUpscalerProviderPipe:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'full_sample_schedule': (['none', 'interleave1', 'interleave2', 'interleave3', 'last1', 'last2', 'interleave1+last1', 'interleave2+last1', 'interleave3+last1'],), 'use_tiled_vae': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'base_sampler': ('KSAMPLER',), 'mask_sampler': ('KSAMPLER',), 'mask': ('MASK',), 'basic_pipe': ('BASIC_PIPE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}, 'optional': {'full_sampler_opt': ('KSAMPLER',), 'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_base_opt': ('PK_HOOK',), 'pk_hook_mask_opt': ('PK_HOOK',), 'pk_hook_full_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, scale_method, full_sample_schedule, use_tiled_vae, base_sampler, mask_sampler, mask, basic_pipe, full_sampler_opt=None, upscale_model_opt=None, pk_hook_base_opt=None, pk_hook_mask_opt=None, pk_hook_full_opt=None, tile_size=512):
        mask = make_2d_mask(mask)
        (_, _, vae, _, _) = basic_pipe
        upscaler = core.TwoSamplersForMaskUpscaler(scale_method, full_sample_schedule, use_tiled_vae, base_sampler, mask_sampler, mask, vae, full_sampler_opt, upscale_model_opt, pk_hook_base_opt, pk_hook_mask_opt, pk_hook_full_opt, tile_size=tile_size)
        return (upscaler,)
```