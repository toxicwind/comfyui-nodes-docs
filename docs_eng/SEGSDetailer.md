# Documentation
- Class name: SEGSDetailer
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSDetailer node is designed to enhance the details of the image based on split information. It enhances its visual quality by scaling and processing segments of the image, especially in applications where fine details are needed. The node uses advanced deep learning models to achieve this enhancement and thus obtains more sophisticated and detailed output images.

# Input types
## Required
- image
    - Enter the image, which will be processed by the SEGSDetailer node. As the main data source for the detail enhancement process, it is essential to achieve the desired results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - Separates data that provide image structure information. This input is essential to understand which parts of the image need to be focused on detail enhancement.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
## Optional
- guide_size
    - The lead size parameter determines the zoom factor for the detail enhancement process. It affects the extent to which the image snippets are magnified before the enhancement, and thus the level of detail for the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The number of steps to be implemented in the process of detail enhancement. More steps usually lead to more fine output, but they may also increase the calculation time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- segs
    - Splits the data based on the output when you enter the image and divide the information into more detail.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- cnet_images
    - A list of control network images generated during detail enhancement can be used for further analysis or visualization.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SEGSDetailer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'guide_size': ('FLOAT', {'default': 256, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 768, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'noise_mask': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'force_inpaint': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'basic_pipe': ('BASIC_PIPE',), 'refiner_ratio': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 100}), 'cycle': ('INT', {'default': 1, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'refiner_basic_pipe_opt': ('BASIC_PIPE',), 'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}}
    RETURN_TYPES = ('SEGS', 'IMAGE')
    RETURN_NAMES = ('segs', 'cnet_images')
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    @staticmethod
    def do_detail(image, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, noise_mask, force_inpaint, basic_pipe, refiner_ratio=None, batch_size=1, cycle=1, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        (model, clip, vae, positive, negative) = basic_pipe
        if refiner_basic_pipe_opt is None:
            (refiner_model, refiner_clip, refiner_positive, refiner_negative) = (None, None, None, None)
        else:
            (refiner_model, refiner_clip, _, refiner_positive, refiner_negative) = refiner_basic_pipe_opt
        segs = core.segs_scale_match(segs, image.shape)
        new_segs = []
        cnet_pil_list = []
        for i in range(batch_size):
            seed += 1
            for seg in segs[1]:
                cropped_image = seg.cropped_image if seg.cropped_image is not None else crop_ndarray4(image.numpy(), seg.crop_region)
                cropped_image = to_tensor(cropped_image)
                is_mask_all_zeros = (seg.cropped_mask == 0).all().item()
                if is_mask_all_zeros:
                    print(f'Detailer: segment skip [empty mask]')
                    new_segs.append(seg)
                    continue
                if noise_mask:
                    cropped_mask = seg.cropped_mask
                else:
                    cropped_mask = None
                cropped_positive = [[condition, {k: core.crop_condition_mask(v, image, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in positive]
                cropped_negative = [[condition, {k: core.crop_condition_mask(v, image, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in negative]
                (enhanced_image, cnet_pils) = core.enhance_detail(cropped_image, model, clip, vae, guide_size, guide_size_for, max_size, seg.bbox, seed, steps, cfg, sampler_name, scheduler, cropped_positive, cropped_negative, denoise, cropped_mask, force_inpaint, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, control_net_wrapper=seg.control_net_wrapper, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
                if cnet_pils is not None:
                    cnet_pil_list.extend(cnet_pils)
                if enhanced_image is None:
                    new_cropped_image = cropped_image
                else:
                    new_cropped_image = enhanced_image
                new_seg = SEG(to_numpy(new_cropped_image), seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, None)
                new_segs.append(new_seg)
        return ((segs[0], new_segs), cnet_pil_list)

    def doit(self, image, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, noise_mask, force_inpaint, basic_pipe, refiner_ratio=None, batch_size=1, cycle=1, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: SEGSDetailer does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        (segs, cnet_pil_list) = SEGSDetailer.do_detail(image, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, noise_mask, force_inpaint, basic_pipe, refiner_ratio, batch_size, cycle=cycle, refiner_basic_pipe_opt=refiner_basic_pipe_opt, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        if len(cnet_pil_list) == 0:
            cnet_pil_list = [empty_pil_tensor()]
        return (segs, cnet_pil_list)
```