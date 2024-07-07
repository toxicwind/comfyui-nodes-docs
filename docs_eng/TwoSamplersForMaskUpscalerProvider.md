# Documentation
- Class name: TwoSamplersForMaskUpscalerProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Two SamplersforMaskUpscalerProvider node is designed to facilitate image magnification using two different sampling methods. It allows selection of sampling methods and scheduling of sampling processes. The node plays a key role in enhancing image quality through complex sampling techniques and combinations of sampling algorithms.

# Input types
## Required
- scale_method
    - The scale_method parameter determines the algorithm to be used for image sampling. It is essential for the overall performance and quality of the sampling process, as it directly affects the resolution and clarity of the output.
    - Comfy dtype: str
    - Python dtype: str
- full_sample_schedule
    - Full_sample_schedule parameters determine when complete sampling will be performed during the top sampling process. It is important to control the timing and frequency of sampling, which in turn affects the details and texture of the final output.
    - Comfy dtype: str
    - Python dtype: str
- use_tiled_vae
    - This enhances the efficiency of the sampling process, especially for larger images.
    - Comfy dtype: bool
    - Python dtype: bool
- base_sampler
    - Base_sampler parameters are the main sampling method used to generate the initial sample set. It acts as a base during the sampling process, affecting the initial quality and characteristics of the output.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSampler
- mask_sampler
    - The mask_sampler parameter defines the sampling method to be applied to the mask. It is essential to determine how the mask affects the final sampling results, especially in the area where the mask is applied.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSampler
- mask
    - The mask parameter provides a mask to guide the sampling process. It is important to define the areas in the image that require special attention or treatment during the sampling.
    - Comfy dtype: MASK
    - Python dtype: np.ndarray
- vae
    - The vae parameter represents the variable-based encoder model used in the sampling process. It is a key component for generating high-quality potential expressions of the input image.
    - Comfy dtype: VAE
    - Python dtype: VAE
## Optional
- tile_size
    - The tile_size parameter sets the block size that is used to process the image when using a block method. It is important for optimizing the time of memory use and processing, especially for high-resolution images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- upscaler
    - Upscaler output provides the final top image or potential expression. It is the end result of the sampling process and represents an enhanced image quality and resolution achieved through complex sampling and upsampling methods at nodes.
    - Comfy dtype: UPSCALER
    - Python dtype: TwoSamplersForMaskUpscaler

# Usage tips
- Infra type: CPU

# Source code
```
class TwoSamplersForMaskUpscalerProvider:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'full_sample_schedule': (['none', 'interleave1', 'interleave2', 'interleave3', 'last1', 'last2', 'interleave1+last1', 'interleave2+last1', 'interleave3+last1'],), 'use_tiled_vae': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'base_sampler': ('KSAMPLER',), 'mask_sampler': ('KSAMPLER',), 'mask': ('MASK',), 'vae': ('VAE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}, 'optional': {'full_sampler_opt': ('KSAMPLER',), 'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_base_opt': ('PK_HOOK',), 'pk_hook_mask_opt': ('PK_HOOK',), 'pk_hook_full_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, scale_method, full_sample_schedule, use_tiled_vae, base_sampler, mask_sampler, mask, vae, full_sampler_opt=None, upscale_model_opt=None, pk_hook_base_opt=None, pk_hook_mask_opt=None, pk_hook_full_opt=None, tile_size=512):
        upscaler = core.TwoSamplersForMaskUpscaler(scale_method, full_sample_schedule, use_tiled_vae, base_sampler, mask_sampler, mask, vae, full_sampler_opt, upscale_model_opt, pk_hook_base_opt, pk_hook_mask_opt, pk_hook_full_opt, tile_size=tile_size)
        return (upscaler,)
```