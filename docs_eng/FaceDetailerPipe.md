# Documentation
- Class name: FaceDetailerPipe
- Category: ImpactPack/Simple
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The FaceDetailer Pipe node is designed to enhance the profile of the face in the image. It processes the input image to fine-tune facial features and improves overall quality, using a range of advanced image-processing techniques and models. The main objective is to provide more detailed and refined visual output, especially for applications requiring high-quality facial expressions.

# Input types
## Required
- image
    - The input image is the primary data needed to execute facial detail at the node. It is the basis for all follow-up and enhancement activities. The quality and resolution of the input image directly influences the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- detailer_pipe
    - Detailer_pipe is the set of models and parameters that guide the process of facial fine-tuning. It includes such important components as models, clips and vae, which are essential for achieving the required level of detail enhancement.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]
- guide_size
    - Theguide_size parameter determines the size of the lead image for facial detail. This is a key factor that affects the level of detail that can be achieved in the final output. A larger guide size usually allows for more detailed enhancements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_size
    - The max_size parameter sets the maximum size of the input image. This is an important consideration, as larger images can significantly increase processing time and resource requirements and have an impact on performance and memory use.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - An enhanced image output is the main result of the FaceDetailer Pipe node. It contains facial details that are refined and improved from the original input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- cropped_refined
    - Cropped_refined output contains a series of detailed facial images that are made from enhanced images. They can be used for further processing or as stand-alone detailed images.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]
- mask
    - The mask output is a binary image that depicts an enhanced facial area. This is very useful for segregating detailed areas for additional processing or analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class FaceDetailerPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'detailer_pipe': ('DETAILER_PIPE',), 'guide_size': ('FLOAT', {'default': 384, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 1024, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'noise_mask': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'force_inpaint': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'bbox_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1}), 'bbox_crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 10, 'step': 0.1}), 'sam_detection_hint': (['center-1', 'horizontal-2', 'vertical-2', 'rect-4', 'diamond-4', 'mask-area', 'mask-points', 'mask-point-bbox', 'none'],), 'sam_dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'sam_threshold': ('FLOAT', {'default': 0.93, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'sam_bbox_expansion': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1}), 'sam_mask_hint_threshold': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'sam_mask_hint_use_negative': (['False', 'Small', 'Outter'],), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'refiner_ratio': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0}), 'cycle': ('INT', {'default': 1, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'IMAGE', 'MASK', 'DETAILER_PIPE', 'IMAGE')
    RETURN_NAMES = ('image', 'cropped_refined', 'cropped_enhanced_alpha', 'mask', 'detailer_pipe', 'cnet_images')
    OUTPUT_IS_LIST = (False, True, True, False, False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Simple'

    def doit(self, image, detailer_pipe, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, feather, noise_mask, force_inpaint, bbox_threshold, bbox_dilation, bbox_crop_factor, sam_detection_hint, sam_dilation, sam_threshold, sam_bbox_expansion, sam_mask_hint_threshold, sam_mask_hint_use_negative, drop_size, refiner_ratio=None, cycle=1, inpaint_model=False, noise_mask_feather=0):
        result_img = None
        result_mask = None
        result_cropped_enhanced = []
        result_cropped_enhanced_alpha = []
        result_cnet_images = []
        if len(image) > 1:
            print(f'[Impact Pack] WARN: FaceDetailer is not a node designed for video detailing. If you intend to perform video detailing, please use Detailer For AnimateDiff.')
        (model, clip, vae, positive, negative, wildcard, bbox_detector, segm_detector, sam_model_opt, detailer_hook, refiner_model, refiner_clip, refiner_positive, refiner_negative) = detailer_pipe
        for (i, single_image) in enumerate(image):
            (enhanced_img, cropped_enhanced, cropped_enhanced_alpha, mask, cnet_pil_list) = FaceDetailer.enhance_face(single_image.unsqueeze(0), model, clip, vae, guide_size, guide_size_for, max_size, seed + i, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, bbox_threshold, bbox_dilation, bbox_crop_factor, sam_detection_hint, sam_dilation, sam_threshold, sam_bbox_expansion, sam_mask_hint_threshold, sam_mask_hint_use_negative, drop_size, bbox_detector, segm_detector, sam_model_opt, wildcard, detailer_hook, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
            result_img = torch.cat((result_img, enhanced_img), dim=0) if result_img is not None else enhanced_img
            result_mask = torch.cat((result_mask, mask), dim=0) if result_mask is not None else mask
            result_cropped_enhanced.extend(cropped_enhanced)
            result_cropped_enhanced_alpha.extend(cropped_enhanced_alpha)
            result_cnet_images.extend(cnet_pil_list)
        if len(result_cropped_enhanced) == 0:
            result_cropped_enhanced = [empty_pil_tensor()]
        if len(result_cropped_enhanced_alpha) == 0:
            result_cropped_enhanced_alpha = [empty_pil_tensor()]
        if len(result_cnet_images) == 0:
            result_cnet_images = [empty_pil_tensor()]
        return (result_img, result_cropped_enhanced, result_cropped_enhanced_alpha, result_mask, detailer_pipe, result_cnet_images)
```