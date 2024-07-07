# Documentation
- Class name: preDetailerFix
- Category: EasyUse/Fix
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The preDetailerFix node is intended to enhance the pre-processing phase of the image data pipeline and to ensure that the input image is properly prepared for further analysis and operation. The node focuses on restoring common problems during the initial phase of image processing, thereby improving the quality and reliability of subsequent operations.

# Input types
## Required
- pipe
    - The pipe parameter is necessary because it carries the core data and settings needed to run the node. It includes models, clip and wae components, as well as images and other relevant information, which determines the process of processing the node.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- guide_size
    - The guide_size parameter is essential to define the resolution of node processing images, directly affecting the level of detail and computational efficiency.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guide_size_for
    - The guide_size_for parameters determine the method of applying the guiding dimensions, whether through boundary frames or by cropping areas, which significantly influences the results of image processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- max_size
    - The max_size parameter sets a ceiling on image size to ensure that processing remains within manageable limits and to prevent excessive resource consumption.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters are important to ensure the repeatability of node operations and allow consistent results to be obtained in different operations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameters define the number of overlaps that nodes will implement, which is directly related to the thoroughness of image processing and the potential for improved results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of nodes to affect their behaviour and the quality of image processing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter is critical in selecting appropriate sampling methods for nodes, which will greatly affect the efficiency and effectiveness of image processing.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - Scheduler parameters are critical to managing the speed of implementation of nodes, ensuring optimal performance and resource utilization.
    - Comfy dtype: COMBO
    - Python dtype: str
- denoise
    - The denoise parameters help to control noise reduction processes and improve the clarity and quality of image processing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- feather
    - Feather parameters are important for softening the edges of image processing, leading to a smoother transition and more attractive visual outcomes.
    - Comfy dtype: INT
    - Python dtype: int
- noise_mask
    - Noise_mask parameters enable or disable noise masking functions, which are essential for managing false images that are not required in image processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- force_inpaint
    - The force_inpaint parameter is important in guiding nodes to fill missing or damaged parts of the image to ensure the integrity and consistency of the final output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- drop_size
    - The drop_size parameter determines the size of the area to be removed from the image, which is essential to remove unwanted elements and improve the overall image quality.
    - Comfy dtype: INT
    - Python dtype: int
- wildcard
    - The wildcard parameters allow dynamic adjustment and customization of node operations and provide flexibility to process various image-processing scenarios.
    - Comfy dtype: STRING
    - Python dtype: str
- cycle
    - The cycle parameters determine the number of nodes being duplicated, which enhances the stability and reliability of image-processing results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - Output Pipe is an integrated structure that covers processed images and related data and provides the basis for follow-up operations in the pipeline.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class preDetailerFix:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'guide_size': ('FLOAT', {'default': 256, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 768, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'noise_mask': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'force_inpaint': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'cycle': ('INT', {'default': 1, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'bbox_segm_pipe': ('PIPE_LINE',), 'sam_pipe': ('PIPE_LINE',), 'optional_image': ('IMAGE',)}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_IS_LIST = (False,)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Fix'

    def doit(self, pipe, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, feather, noise_mask, force_inpaint, drop_size, wildcard, cycle, bbox_segm_pipe=None, sam_pipe=None, optional_image=None):
        model = pipe['model'] if 'model' in pipe else None
        if model is None:
            raise Exception(f"[ERROR] pipe['model'] is missing")
        clip = pipe['clip'] if 'clip' in pipe else None
        if clip is None:
            raise Exception(f"[ERROR] pipe['clip'] is missing")
        vae = pipe['vae'] if 'vae' in pipe else None
        if vae is None:
            raise Exception(f"[ERROR] pipe['vae'] is missing")
        if optional_image is not None:
            images = optional_image
        else:
            images = pipe['images'] if 'images' in pipe else None
            if images is None:
                raise Exception(f"[ERROR] pipe['image'] is missing")
        positive = pipe['positive'] if 'positive' in pipe else None
        if positive is None:
            raise Exception(f"[ERROR] pipe['positive'] is missing")
        negative = pipe['negative'] if 'negative' in pipe else None
        if negative is None:
            raise Exception(f"[ERROR] pipe['negative'] is missing")
        bbox_segm_pipe = bbox_segm_pipe or (pipe['bbox_segm_pipe'] if pipe and 'bbox_segm_pipe' in pipe else None)
        if bbox_segm_pipe is None:
            raise Exception(f"[ERROR] bbox_segm_pipe or pipe['bbox_segm_pipe'] is missing")
        sam_pipe = sam_pipe or (pipe['sam_pipe'] if pipe and 'sam_pipe' in pipe else None)
        if sam_pipe is None:
            raise Exception(f"[ERROR] sam_pipe or pipe['sam_pipe'] is missing")
        loader_settings = pipe['loader_settings'] if 'loader_settings' in pipe else {}
        new_pipe = {'images': images, 'model': model, 'clip': clip, 'vae': vae, 'positive': positive, 'negative': negative, 'seed': seed, 'bbox_segm_pipe': bbox_segm_pipe, 'sam_pipe': sam_pipe, 'loader_settings': loader_settings, 'detail_fix_settings': {'guide_size': guide_size, 'guide_size_for': guide_size_for, 'max_size': max_size, 'seed': seed, 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'denoise': denoise, 'feather': feather, 'noise_mask': noise_mask, 'force_inpaint': force_inpaint, 'drop_size': drop_size, 'wildcard': wildcard, 'cycle': cycle}}
        del bbox_segm_pipe
        del sam_pipe
        return (new_pipe,)
```