# Documentation
- Class name: SEGSDetailerForAnimateDiff
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSDetailer ForAnimateDiff node is designed to enhance the detail of the partitions in the frame, especially the quality of the animated differences. It improves their clarity and detail by scaling and processing the various parts of the image, using advanced models and sampling techniques.

# Input types
## Required
- image_frames
    - The image_frames parameter is necessary because it provides the original image data that the node will process. It directly affects the quality of the output and the ability of the node to enhance the detail in the frame.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - The segs parameter defines the partitions within the node that will focus on the image_frames, which are essential for the identification and processing of specific areas of interest in the image data.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- guide_size
    - guide_size parameters set the zoom factor for the detail enhancement process. It is important because it determines the level of detail that will be introduced into the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guide_size_for
    - guide_size_for parameters indicate whether theguide_size should be applied to the border or to the crop area. This option enhances the focus in the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- max_size
    - The max_size parameter sets the maximum size for a magnified frame. It ensures that the enhanced image does not exceed a certain resolution, maintaining performance and memory efficiency.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The Seed parameter is used to generate random numbers during the sampling process. It ensures the replicability of results when running nodes using the same feed values.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters determine the number of turns to be used in the sampling process. More steps can lead to more refined results, but may increase processing time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the sampling process to allow fine-tuning of details to enhance algorithm behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used for nodes. Different samplers can provide different results in terms of detail and noise properties.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the dispatch strategy for the sampling process. It affects how the sampling process evolves over time.
    - Comfy dtype: STRING
    - Python dtype: str
- denoise
    - The denoise parameter controls the level of noise that should be used to enhance the image. It is an important factor in achieving the balance of detail and noise in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- basic_pipe
    - The basic_pipe parameter covers the core components required for the detail enhancement process, including models, clips and vae. It is the basis for the node function.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
## Optional
- refiner_ratio
    - When providing the parameter refiner_ratio, it determines the effect of the alternative refiner model on detail enhancement. It allows further fine-tuning of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: Optional[float]
- refiner_basic_pipe_opt
    - The optional Refiner_basic_pipe_opt parameters expand the capacity of nodes by providing an additional set of components for use in the sub-definition process.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Optional[Tuple[Any, ...]]

# Output types
- segs
    - The segs output contains the enhanced partition details for input frames. It marks the completion of node processing and represents the main result of the detail enhancement operation.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[Tuple[int, int], List[SEG]]
- cnet_images
    - The cnet_images output provides a visual indication of the effect of the control network on the detail enhancement process. These images can be used for further analysis or as a reference for the validity of nodes.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SEGSDetailerForAnimateDiff:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_frames': ('IMAGE',), 'segs': ('SEGS',), 'guide_size': ('FLOAT', {'default': 256, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 768, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'basic_pipe': ('BASIC_PIPE',), 'refiner_ratio': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0})}, 'optional': {'refiner_basic_pipe_opt': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('SEGS', 'IMAGE')
    RETURN_NAMES = ('segs', 'cnet_images')
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    @staticmethod
    def do_detail(image_frames, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, basic_pipe, refiner_ratio=None, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        (model, clip, vae, positive, negative) = basic_pipe
        if refiner_basic_pipe_opt is None:
            (refiner_model, refiner_clip, refiner_positive, refiner_negative) = (None, None, None, None)
        else:
            (refiner_model, refiner_clip, _, refiner_positive, refiner_negative) = refiner_basic_pipe_opt
        segs = core.segs_scale_match(segs, image_frames.shape)
        new_segs = []
        cnet_image_list = []
        for seg in segs[1]:
            cropped_image_frames = None
            for image in image_frames:
                image = image.unsqueeze(0)
                cropped_image = seg.cropped_image if seg.cropped_image is not None else crop_tensor4(image, seg.crop_region)
                cropped_image = to_tensor(cropped_image)
                if cropped_image_frames is None:
                    cropped_image_frames = cropped_image
                else:
                    cropped_image_frames = torch.concat((cropped_image_frames, cropped_image), dim=0)
            cropped_image_frames = cropped_image_frames.cpu().numpy()
            cropped_positive = [[condition, {k: core.crop_condition_mask(v, cropped_image_frames, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in positive]
            cropped_negative = [[condition, {k: core.crop_condition_mask(v, cropped_image_frames, seg.crop_region) if k == 'mask' else v for (k, v) in details.items()}] for (condition, details) in negative]
            (enhanced_image_tensor, cnet_images) = core.enhance_detail_for_animatediff(cropped_image_frames, model, clip, vae, guide_size, guide_size_for, max_size, seg.bbox, seed, steps, cfg, sampler_name, scheduler, cropped_positive, cropped_negative, denoise, seg.cropped_mask, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, control_net_wrapper=seg.control_net_wrapper, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
            if cnet_images is not None:
                cnet_image_list.extend(cnet_images)
            if enhanced_image_tensor is None:
                new_cropped_image = cropped_image_frames
            else:
                new_cropped_image = enhanced_image_tensor.cpu().numpy()
            new_seg = SEG(new_cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, None)
            new_segs.append(new_seg)
        return ((segs[0], new_segs), cnet_image_list)

    def doit(self, image_frames, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, basic_pipe, refiner_ratio=None, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        (segs, cnet_images) = SEGSDetailerForAnimateDiff.do_detail(image_frames, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, basic_pipe, refiner_ratio, refiner_basic_pipe_opt, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        if len(cnet_images) == 0:
            cnet_images = [empty_pil_tensor()]
        return (segs, cnet_images)
```