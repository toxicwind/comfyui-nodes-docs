# Documentation
- Class name: DetailerForEachPipe
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DetailerForEachPipe node is designed to enhance image details by applying a range of image-processing techniques. It focuses on refining the visual quality of various parts of the image through advanced algorithms to achieve higher levels of detail. The node plays a key role in the reprocessing process that emphasizes image content details.

# Input types
## Required
- image
    - Enter the image as the main data to be processed by the node. It is essential for the execution of the node, because it determines the object for which the details are enhanced. The characteristics of the image have a direct impact on the operation of the node and the quality of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - Splitting data provides an area of interest within the image. This is essential to understand which parts of the image need to be enhanced in detail. Spliting data guides the processing of nodes to ensure that only the relevant areas are enhanced.
    - Comfy dtype: SEGS
    - Python dtype: List[torch.Tensor]
- guide_size
    - The lead size parameter determines the scale of application of the enhanced detail. It is the key factor in determining the level of the visible detail in the final output. The lead size must be carefully selected to balance the detail with the calculation of the resource.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_size
    - The maximum size parameter sets a ceiling on the size of the image segment that is processed. It is important to control the load and to ensure that nodes run within available resources. This parameter helps to prevent overuse of memory during enhancement.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters are used to initialize random number generators to ensure repeatability of node operations. This is particularly important when you want to achieve consistent results in multiple node operations. Seeds provide some control for random elements in the enhancement process.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The step parameter specifies the number of turns that the enhancement algorithm will execute. It is the key determinant of the quality and detail of the final output. The greater the number of steps, the better the result, the longer the calculation time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configures the parameter enhancement algorithm settings to fine-tune output. It is a key factor in achieving the required level of detail and can significantly influence the visual results of the enhanced image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output image is the result of the detail enhancement process. It contains the original image, adds details and improves visual quality. This is the main output that users expect from node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - Output partition data provide information on the enhanced area in the image. This is useful for further processing or analysis of the area in which the image is divided.
    - Comfy dtype: SEGS
    - Python dtype: List[torch.Tensor]
- basic_pipe
    - Basic pipe output is a collection of models and parameters used in the enhancement process. It can be used for additional operations or for consistency at different stages of the image processing workflow.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
- cnet_images
    - Control network image output is a list of images processed by the control network during the enhancement process. These images can be used for review or further operation.
    - Comfy dtype: COMBO[IMAGE]
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class DetailerForEachPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'guide_size': ('FLOAT', {'default': 384, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'guide_size_for': ('BOOLEAN', {'default': True, 'label_on': 'bbox', 'label_off': 'crop_region'}), 'max_size': ('FLOAT', {'default': 1024, 'min': 64, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'noise_mask': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'force_inpaint': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'basic_pipe': ('BASIC_PIPE',), 'wildcard': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'refiner_ratio': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0}), 'cycle': ('INT', {'default': 1, 'min': 1, 'max': 10, 'step': 1})}, 'optional': {'detailer_hook': ('DETAILER_HOOK',), 'refiner_basic_pipe_opt': ('BASIC_PIPE',), 'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'SEGS', 'BASIC_PIPE', 'IMAGE')
    RETURN_NAMES = ('image', 'segs', 'basic_pipe', 'cnet_images')
    OUTPUT_IS_LIST = (False, False, False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, image, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, feather, noise_mask, force_inpaint, basic_pipe, wildcard, refiner_ratio=None, detailer_hook=None, refiner_basic_pipe_opt=None, cycle=1, inpaint_model=False, noise_mask_feather=0):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: DetailerForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        (model, clip, vae, positive, negative) = basic_pipe
        if refiner_basic_pipe_opt is None:
            (refiner_model, refiner_clip, refiner_positive, refiner_negative) = (None, None, None, None)
        else:
            (refiner_model, refiner_clip, _, refiner_positive, refiner_negative) = refiner_basic_pipe_opt
        (enhanced_img, cropped, cropped_enhanced, cropped_enhanced_alpha, cnet_pil_list, new_segs) = DetailerForEach.do_detail(image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, detailer_hook, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        if len(cnet_pil_list) == 0:
            cnet_pil_list = [empty_pil_tensor()]
        return (enhanced_img, new_segs, basic_pipe, cnet_pil_list)
```