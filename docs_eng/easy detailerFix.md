# Documentation
- Class name: detailerFix
- Category: EasyUse/Fix
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The main objective of the detailerFix node is to enhance image details by using advanced models and algorithms. It focuses on refining the visual elements of the image and improving its overall quality and clarity. The main objective of the node is to provide a simple and effective detail that enhances the solution without the need for extensive image processing knowledge.

# Input types
## Required
- pipe
    - The pipe parameter is necessary because it carries all the necessary information and settings necessary for the DetailerFix node to perform its functions. It includes models, images and other settings that determine how the details are enhanced.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image_output
    - The image_output parameter determines how the post-processing result image is handled. It allows the user to select previews, saves or combinations of the two, thereby controlling the output process.
    - Comfy dtype: COMBO
    - Python dtype: str
- link_id
    - When the image_output is set as 'Sender' or 'Sender/Save', the link_id is essential to the operation of the node. It creates a connection to the image transfer to ensure that the processed image is delivered to the right destination.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- save_prefix
    - Save_prefix parameters are used to define common prefixes for saved image files. This helps to organize output and makes it easier for users to locate and manage enhanced images.
    - Comfy dtype: STRING
    - Python dtype: str
- model
    - Model parameters provide the models needed to enhance the process in detail. This is particularly important when the pipe parameters do not contain models, ensuring that nodes are able to access the models needed for processing.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- prompt
    - The prompt parameter is used to provide additional information or instructions that can guide the detail enhancement process. It may include specific details or preferences that the user wishes to consider during the execution.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The extra_pnginfo parameter contains supplementary data that can be used to refine the detail enhancement process. It provides additional context or options to improve the quality of the output image.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]
- my_unique_id
    - My_unique_id parameter is used to track and manage the processing of individual image details. It helps to link the output to a specific request and ensures the accuracy and organization of the results.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: int

# Output types
- pipe
    - Pipe output is an integrated structure that contains enhanced images and inputs of all relevant information in Pipe. It serves as a conduit for processing data, ensuring that the results are correctly transmitted along the pipeline.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The Image output is the main result of the detailerFix node, the enhanced image. It is the end result of the process of detail enhancement and is intended to be the end product of the user.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- cropped_refined
    - Cropped_refined output is an enhanced crop version of the image to obtain better focus and clarity. It highlights areas that have been refined and improved in the image and clearly shows the validity of nodes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- cropped_enhanced_alpha
    - Cropped_enhanced_alpha output is a special version of the enhanced image, containing the alpha channel representing transparency. This output is particularly useful for applications that require image stacking or synthesis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class detailerFix:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'], {'default': 'Preview'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'optional': {'model': ('MODEL',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('pipe', 'image', 'cropped_refined', 'cropped_enhanced_alpha')
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False, False, True, True)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Fix'

    def doit(self, pipe, image_output, link_id, save_prefix, model=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        easyCache.update_loaded_objects(prompt)
        my_unique_id = int(my_unique_id)
        model = model or (pipe['model'] if 'model' in pipe else None)
        if model is None:
            raise Exception(f"[ERROR] model or pipe['model'] is missing")
        detail_fix_settings = pipe['detail_fix_settings'] if 'detail_fix_settings' in pipe else None
        if detail_fix_settings is None:
            raise Exception(f"[ERROR] detail_fix_settings or pipe['detail_fix_settings'] is missing")
        mask = pipe['mask'] if 'mask' in pipe else None
        image = pipe['images']
        clip = pipe['clip']
        vae = pipe['vae']
        seed = pipe['seed']
        positive = pipe['positive']
        negative = pipe['negative']
        loader_settings = pipe['loader_settings'] if 'loader_settings' in pipe else {}
        guide_size = pipe['detail_fix_settings']['guide_size'] if 'guide_size' in pipe['detail_fix_settings'] else 256
        guide_size_for = pipe['detail_fix_settings']['guide_size_for'] if 'guide_size_for' in pipe['detail_fix_settings'] else True
        max_size = pipe['detail_fix_settings']['max_size'] if 'max_size' in pipe['detail_fix_settings'] else 768
        steps = pipe['detail_fix_settings']['steps'] if 'steps' in pipe['detail_fix_settings'] else 20
        cfg = pipe['detail_fix_settings']['cfg'] if 'cfg' in pipe['detail_fix_settings'] else 1.0
        sampler_name = pipe['detail_fix_settings']['sampler_name'] if 'sampler_name' in pipe['detail_fix_settings'] else None
        scheduler = pipe['detail_fix_settings']['scheduler'] if 'scheduler' in pipe['detail_fix_settings'] else None
        denoise = pipe['detail_fix_settings']['denoise'] if 'denoise' in pipe['detail_fix_settings'] else 0.5
        feather = pipe['detail_fix_settings']['feather'] if 'feather' in pipe['detail_fix_settings'] else 5
        crop_factor = pipe['detail_fix_settings']['crop_factor'] if 'crop_factor' in pipe['detail_fix_settings'] else 3.0
        drop_size = pipe['detail_fix_settings']['drop_size'] if 'drop_size' in pipe['detail_fix_settings'] else 10
        refiner_ratio = pipe['detail_fix_settings']['refiner_ratio'] if 'refiner_ratio' in pipe else 0.2
        batch_size = pipe['detail_fix_settings']['batch_size'] if 'batch_size' in pipe['detail_fix_settings'] else 1
        noise_mask = pipe['detail_fix_settings']['noise_mask'] if 'noise_mask' in pipe['detail_fix_settings'] else None
        force_inpaint = pipe['detail_fix_settings']['force_inpaint'] if 'force_inpaint' in pipe['detail_fix_settings'] else False
        wildcard = pipe['detail_fix_settings']['wildcard'] if 'wildcard' in pipe['detail_fix_settings'] else ''
        cycle = pipe['detail_fix_settings']['cycle'] if 'cycle' in pipe['detail_fix_settings'] else 1
        bbox_segm_pipe = pipe['bbox_segm_pipe'] if pipe and 'bbox_segm_pipe' in pipe else None
        sam_pipe = pipe['sam_pipe'] if 'sam_pipe' in pipe else None
        start_time = int(time.time() * 1000)
        if 'mask_settings' in pipe:
            mask_mode = pipe['mask_settings']['mask_mode'] if 'inpaint_model' in pipe['mask_settings'] else True
            inpaint_model = pipe['mask_settings']['inpaint_model'] if 'inpaint_model' in pipe['mask_settings'] else False
            noise_mask_feather = pipe['mask_settings']['noise_mask_feather'] if 'noise_mask_feather' in pipe['mask_settings'] else 20
            cls = ALL_NODE_CLASS_MAPPINGS['MaskDetailerPipe']
            if 'MaskDetailerPipe' not in ALL_NODE_CLASS_MAPPINGS:
                raise Exception(f"[ERROR] To use MaskDetailerPipe, you need to install 'Impact Pack'")
            basic_pipe = (model, clip, vae, positive, negative)
            (result_img, result_cropped_enhanced, result_cropped_enhanced_alpha, basic_pipe, refiner_basic_pipe_opt) = cls().doit(image, mask, basic_pipe, guide_size, guide_size_for, max_size, mask_mode, seed, steps, cfg, sampler_name, scheduler, denoise, feather, crop_factor, drop_size, refiner_ratio, batch_size, cycle=1, refiner_basic_pipe_opt=None, detailer_hook=None, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
            result_mask = mask
            result_cnet_images = ()
        else:
            if bbox_segm_pipe is None:
                raise Exception(f"[ERROR] bbox_segm_pipe or pipe['bbox_segm_pipe'] is missing")
            if sam_pipe is None:
                raise Exception(f"[ERROR] sam_pipe or pipe['sam_pipe'] is missing")
            (bbox_detector_opt, bbox_threshold, bbox_dilation, bbox_crop_factor, segm_detector_opt) = bbox_segm_pipe
            (sam_model_opt, sam_detection_hint, sam_dilation, sam_threshold, sam_bbox_expansion, sam_mask_hint_threshold, sam_mask_hint_use_negative) = sam_pipe
            if 'FaceDetailer' not in ALL_NODE_CLASS_MAPPINGS:
                raise Exception(f"[ERROR] To use FaceDetailer, you need to install 'Impact Pack'")
            cls = ALL_NODE_CLASS_MAPPINGS['FaceDetailer']
            (result_img, result_cropped_enhanced, result_cropped_enhanced_alpha, result_mask, pipe, result_cnet_images) = cls().doit(image, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, bbox_threshold, bbox_dilation, bbox_crop_factor, sam_detection_hint, sam_dilation, sam_threshold, sam_bbox_expansion, sam_mask_hint_threshold, sam_mask_hint_use_negative, drop_size, bbox_detector_opt, wildcard, cycle, sam_model_opt, segm_detector_opt, detailer_hook=None)
        end_time = int(time.time() * 1000)
        Step_time = 'Details fix:'+str (end_time - start_time) +'second'
        results = easySave(result_img, save_prefix, image_output, prompt, extra_pnginfo)
        sampler.update_value_by_id('results', my_unique_id, results)
        easyCache.update_loaded_objects(prompt)
        new_pipe = {'samples': None, 'images': result_img, 'model': model, 'clip': clip, 'vae': vae, 'seed': seed, 'positive': positive, 'negative': negative, 'wildcard': wildcard, 'bbox_segm_pipe': bbox_segm_pipe, 'sam_pipe': sam_pipe, 'loader_settings': {**loader_settings, 'spent_time': spent_time}, 'detail_fix_settings': detail_fix_settings}
        if 'mask_settings' in pipe:
            new_pipe['mask_settings'] = pipe['mask_settings']
        sampler.update_value_by_id('pipe_line', my_unique_id, new_pipe)
        del bbox_segm_pipe
        del sam_pipe
        del pipe
        if image_output in ('Hide', 'Hide/Save'):
            return {'ui': {}, 'result': (new_pipe, result_img, result_cropped_enhanced, result_cropped_enhanced_alpha, result_mask, result_cnet_images)}
        if image_output in ('Sender', 'Sender/Save'):
            PromptServer.instance.send_sync('img-send', {'link_id': link_id, 'images': results})
        return {'ui': {'images': results}, 'result': (new_pipe, result_img, result_cropped_enhanced, result_cropped_enhanced_alpha, result_mask, result_cnet_images)}
```