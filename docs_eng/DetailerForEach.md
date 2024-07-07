# Documentation
- Class name: DetailerForEach
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DetailerForEach node is designed to enhance the details of the various parts of the image. It works by applying a detailed enhancement process to each part, including magnifying, denobbling, and pasting the enhanced parts back to the original image. This node is particularly suitable for improving the visual quality of images with different areas that require more detail.

# Input types
## Required
- image
    - To apply the input image of the detailed enhancement process. It serves as the basis for all subsequent operations in the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - In a series of segments defined in the image, each paragraph represents an enhanced area. These paragraphs are essential for identifying which parts of the image need to be dealt with in detail.
    - Comfy dtype: SEGS
    - Python dtype: List[Segment]
- model
    - Models for enhancement processes are usually an in-depth learning model capable of understanding and generating detailed images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The CLIP model or similar model, by providing text descriptions of the image content, assists in the generation of image enhancement with contextual sensitivity.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - Distribute from encoder to encode and decode image data, which is essential to the process of detail enhancement.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- guide_size
    - The lead size parameter determines the detail that increases the level of concern. It is a key factor in controlling the level of detail applied in each segment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The number of steps to be carried out during the sampling process has a direct impact on the quality and detail of the image that ultimately enhances.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- enhanced_image
    - The output is an enhanced image with improved detail, each of which is treated separately to obtain a higher resolution and clarity.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class DetailerForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'guide_size': ('FLOAT', {'default': 384, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 1024, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'noise_mask': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'force_inpaint': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'cycle': ('INT', {'default': 1, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'detailer_hook': ('DETAILER_HOOK',), 'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    @staticmethod
    def do_detail(image, segs, model, clip, vae, guide_size, guide_size_for_bbox, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard_opt=None, detailer_hook=None, refiner_ratio=None, refiner_model=None, refiner_clip=None, refiner_positive=None, refiner_negative=None, cycle=1, inpaint_model=False, noise_mask_feather=0):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: DetailerForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        image = image.clone()
        enhanced_alpha_list = []
        enhanced_list = []
        cropped_list = []
        cnet_pil_list = []
        segs = core.segs_scale_match(segs, image.shape)
        new_segs = []
        wildcard_concat_mode = None
        if wildcard_opt is not None:
            if wildcard_opt.startswith('[CONCAT]'):
                wildcard_concat_mode = 'concat'
                wildcard_opt = wildcard_opt[8:]
            (wmode, wildcard_chooser) = wildcards.process_wildcard_for_segs(wildcard_opt)
        else:
            (wmode, wildcard_chooser) = (None, None)
        if wmode in ['ASC', 'DSC']:
            if wmode == 'ASC':
                ordered_segs = sorted(segs[1], key=lambda x: (x.bbox[0], x.bbox[1]))
            else:
                ordered_segs = sorted(segs[1], key=lambda x: (x.bbox[0], x.bbox[1]), reverse=True)
        else:
            ordered_segs = segs[1]
        for (i, seg) in enumerate(ordered_segs):
            cropped_image = crop_ndarray4(image.numpy(), seg.crop_region)
            cropped_image = to_tensor(cropped_image)
            mask = to_tensor(seg.cropped_mask)
            mask = tensor_gaussian_blur_mask(mask, feather)
            is_mask_all_zeros = (seg.cropped_mask == 0).all().item()
            if is_mask_all_zeros:
                print(f'Detailer: segment skip [empty mask]')
                continue
            if noise_mask:
                cropped_mask = seg.cropped_mask
            else:
                cropped_mask = None
            if wildcard_chooser is not None and wmode != 'LAB':
                (seg_seed, wildcard_item) = wildcard_chooser.get(seg)
            elif wildcard_chooser is not None and wmode == 'LAB':
                (seg_seed, wildcard_item) = (None, wildcard_chooser.get(seg))
            else:
                (seg_seed, wildcard_item) = (None, None)
            seg_seed = seed + i if seg_seed is None else seg_seed
            cropped_positive = [[condition, {k: core.crop_condition_mask(v, image, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in positive]
            cropped_negative = [[condition, {k: core.crop_condition_mask(v, image, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in negative]
            (enhanced_image, cnet_pils) = core.enhance_detail(cropped_image, model, clip, vae, guide_size, guide_size_for_bbox, max_size, seg.bbox, seg_seed, steps, cfg, sampler_name, scheduler, cropped_positive, cropped_negative, denoise, cropped_mask, force_inpaint, wildcard_opt=wildcard_item, wildcard_opt_concat_mode=wildcard_concat_mode, detailer_hook=detailer_hook, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, control_net_wrapper=seg.control_net_wrapper, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
            if cnet_pils is not None:
                cnet_pil_list.extend(cnet_pils)
            if not enhanced_image is None:
                image = image.cpu()
                enhanced_image = enhanced_image.cpu()
                tensor_paste(image, enhanced_image, (seg.crop_region[0], seg.crop_region[1]), mask)
                enhanced_list.append(enhanced_image)
                if detailer_hook is not None:
                    detailer_hook.post_paste(image)
            if not enhanced_image is None:
                enhanced_image_alpha = tensor_convert_rgba(enhanced_image)
                new_seg_image = enhanced_image.numpy()
                mask = tensor_resize(mask, *tensor_get_size(enhanced_image))
                tensor_putalpha(enhanced_image_alpha, mask)
                enhanced_alpha_list.append(enhanced_image_alpha)
            else:
                new_seg_image = None
            cropped_list.append(cropped_image)
            new_seg = SEG(new_seg_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
            new_segs.append(new_seg)
        image_tensor = tensor_convert_rgb(image)
        cropped_list.sort(key=lambda x: x.shape, reverse=True)
        enhanced_list.sort(key=lambda x: x.shape, reverse=True)
        enhanced_alpha_list.sort(key=lambda x: x.shape, reverse=True)
        return (image_tensor, cropped_list, enhanced_list, enhanced_alpha_list, cnet_pil_list, (segs[0], new_segs))

    def doit(self, image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, cycle=1, detailer_hook=None, inpaint_model=False, noise_mask_feather=0):
        (enhanced_img, *_) = DetailerForEach.do_detail(image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, detailer_hook, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        return (enhanced_img,)
```