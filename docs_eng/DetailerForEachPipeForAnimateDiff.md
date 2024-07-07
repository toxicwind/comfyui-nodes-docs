# Documentation
- Class name: DetailerForEachPipeForAnimateDiff
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DetailerForEachPipeForAnimateDiff node is designed to enhance the details of the frame by using split information. It handles each section separately to improve the visual quality of animation differences, focusing on areas defined by boundary frames or by cropping areas. The node achieves a higher level of detail in the output, using advanced sampling techniques and noise mitigation strategies.

# Input types
## Required
- image_frames
    - The image_frames parameter is essential because it provides the original image data that nodes will process. It is the basis for applying enhanced detail, the quality of which directly affects the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - The segs parameter defines the split information that the node uses to identify different areas of the image for processing. It is essential for the node to understand which parts of the image require further detail.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[torch.Tensor, List[SEG]]
- guide_size
    - Theguide_size parameter determines the size of the lead image used to enhance details. It is a key factor in controlling the level of detail added to the frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_size
    - The max_size parameter sets the maximum size of the frame to ensure that the enhanced detail does not exceed a resolution. It plays a role in optimizing the balance between processing the details and performance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters are used to generate random numbers within nodes to ensure repeatability of results. This is an important aspect when you want to achieve consistent results in multiple operations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters specify the number of details to be executed. More steps usually lead to higher-quality output, but may increase processing time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameter adjusts the configuration settings for the detail enhancement process. It is a key parameter that affects the overall behaviour of the node and the final appearance of the enhancement detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the sampling method to be used during the detail enhancement. Different sampling methods produce different results in terms of detail quality and processing speed.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - Scheduler parameters determine the schedule algorithm to be used in the detail enhancement process. It influences how the node manages the enhancement steps to achieve the best results.
    - Comfy dtype: STRING
    - Python dtype: str
- denoise
    - The denoise parameter controls the level of noise reduction applied to the frame. This is an important setting for achieving clean and clear output without compromising the enhanced detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- feather
    - Feather parameters are used to soften the edges of the enhancement segment and provide a smoother transition between the detailed area and the rest of the image.
    - Comfy dtype: INT
    - Python dtype: int
- basic_pipe
    - The basic_pipe parameter provides the basic models and components necessary for the detailed enhancement process. It is a key input that allows nodes to perform their functions.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, Any, Any, Any, Any]
- refiner_ratio
    - The refiner_ratio parameter specifies the proportion of the fine-tuning model contribution to detail enhancement. It allows fine-tuning of the enhancement process to reach the required level of detail.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output parameter is the ultimate enhancement frame with improved detail. It is the main result of node processing and reflects the effectiveness of the application details enhancement technology.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - The segs output parameter provides updated split information after the detail enhancement process. It includes a new paragraph that integrates the enhanced detail into the original split data.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[torch.Tensor, List[SEG]]
- basic_pipe
    - The basic_pipe output parameter returns the base model and components used during the detail enhancement period. It may be useful for further processing or analysis purposes.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, Any, Any, Any, Any]
- cnet_images
    - cnet_images output parameters include a list of control network images generated during the detail enhancement process. These images provide insight into the intermediate enhancement phase and help with debugging and quality assessment.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class DetailerForEachPipeForAnimateDiff:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_frames': ('IMAGE',), 'segs': ('SEGS',), 'guide_size': ('FLOAT', {'default': 384, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 1024, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'basic_pipe': ('BASIC_PIPE',), 'refiner_ratio': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0})}, 'optional': {'detailer_hook': ('DETAILER_HOOK',), 'refiner_basic_pipe_opt': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('IMAGE', 'SEGS', 'BASIC_PIPE', 'IMAGE')
    RETURN_NAMES = ('image', 'segs', 'basic_pipe', 'cnet_images')
    OUTPUT_IS_LIST = (False, False, False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    @staticmethod
    def doit(image_frames, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, feather, basic_pipe, refiner_ratio=None, detailer_hook=None, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        enhanced_segs = []
        cnet_image_list = []
        for sub_seg in segs[1]:
            single_seg = (segs[0], [sub_seg])
            (enhanced_seg, cnet_images) = SEGSDetailerForAnimateDiff().do_detail(image_frames, single_seg, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, basic_pipe, refiner_ratio, refiner_basic_pipe_opt, inpaint_model, noise_mask_feather)
            image_frames = SEGSPaste.doit(image_frames, enhanced_seg, feather, alpha=255)[0]
            if cnet_images is not None:
                cnet_image_list.extend(cnet_images)
            if detailer_hook is not None:
                detailer_hook.post_paste(image_frames)
            enhanced_segs += enhanced_seg[1]
        new_segs = (segs[0], enhanced_segs)
        return (image_frames, new_segs, basic_pipe, cnet_image_list)
```