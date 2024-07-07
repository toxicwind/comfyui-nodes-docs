# Documentation
- Class name: SEGSUpscaler
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSUpscaler node is designed to enhance the resolution of images by using split data and upscaling models. It takes images while maintaining the integrity of partitioned areas and ensures that the details of these areas are preserved and enhanced in the scaling process. This node is particularly suitable for applications of critical importance for high-resolution partitioning, such as medical imaging or satellite image analysis.

# Input types
## Required
- image
    - The input image to be sampled is the basic parameter of the SEGSUpscaler node. It is used as the basis for node operations to produce higher-resolution output. The quality and content of the input image directly influences the final sampling results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - Splitting data or'segs' is essential for SEGSUpscaler nodes, as it provides the information needed to separate and process different areas within the image. These data ensure that the details of the partitions are kept on the sample, which is essential for relying on applications that are accurately split.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
## Optional
- rescale_factor
    - Recalculating factors are an important parameter that determines the degree of sampling to be applied to input images. Higher values can lead to a much larger resolution and can enhance detail, but if not carefully managed, they can also introduce hypotheses.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- enhanced_image
    - The output of the SEGSUpscaler node is an enhanced image that has been sampled up to a higher resolution. The image retains partitioned areas with improved detail and clarity that are suitable for further analysis or for display in high resolution formats.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SEGSUpscaler:

    @classmethod
    def INPUT_TYPES(s):
        resampling_methods = ['lanczos', 'nearest', 'bilinear', 'bicubic']
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'rescale_factor': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 100.0, 'step': 0.01}), 'resampling_method': (resampling_methods,), 'supersample': (['true', 'false'],), 'rounding_modulus': ('INT', {'default': 8, 'min': 8, 'max': 1024, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'upscaler_hook_opt': ('UPSCALER_HOOK',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    @staticmethod
    def doit(image, segs, model, clip, vae, rescale_factor, resampling_method, supersample, rounding_modulus, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, inpaint_model, noise_mask_feather, upscale_model_opt=None, upscaler_hook_opt=None):
        new_image = segs_upscaler.upscaler(image, upscale_model_opt, rescale_factor, resampling_method, supersample, rounding_modulus)
        segs = core.segs_scale_match(segs, new_image.shape)
        ordered_segs = segs[1]
        for (i, seg) in enumerate(ordered_segs):
            cropped_image = crop_ndarray4(new_image.numpy(), seg.crop_region)
            cropped_image = to_tensor(cropped_image)
            mask = to_tensor(seg.cropped_mask)
            mask = tensor_gaussian_blur_mask(mask, feather)
            is_mask_all_zeros = (seg.cropped_mask == 0).all().item()
            if is_mask_all_zeros:
                print(f'SEGSUpscaler: segment skip [empty mask]')
                continue
            cropped_mask = seg.cropped_mask
            seg_seed = seed + i
            enhanced_image = segs_upscaler.img2img_segs(cropped_image, model, clip, vae, seg_seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, noise_mask=cropped_mask, control_net_wrapper=seg.control_net_wrapper, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
            if not enhanced_image is None:
                new_image = new_image.cpu()
                enhanced_image = enhanced_image.cpu()
                left = seg.crop_region[0]
                top = seg.crop_region[1]
                tensor_paste(new_image, enhanced_image, (left, top), mask)
                if upscaler_hook_opt is not None:
                    upscaler_hook_opt.post_paste(new_image)
        enhanced_img = tensor_convert_rgb(new_image)
        return (enhanced_img,)
```