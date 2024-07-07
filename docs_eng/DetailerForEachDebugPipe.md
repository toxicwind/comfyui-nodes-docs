# Documentation
- Class name: DetailerForEachTestPipe
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the DetailerForEachTestPipe class is designed to perform detailed image processing tasks for individual image input. It enhances images by using various models and parameters, and produces processed images of many types, including original images, cropping and enhanced versions. The method is a central part of the image enhancement stream, focusing on improving the visual quality and detail of the input image.

# Input types
## Required
- image
    - The 'image'parameter is the main input of the node, which represents the image to be processed. It is essential for the implementation of the node, because it determines the enhanced object. The quality and content of the image significantly influences the output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - The'segs' parameter provides information on the partition of the image, which is essential for enhancing and processing the target within a given region. It affects how the nodes handle and fine-tune different parts of the image.
    - Comfy dtype: SEGS
    - Python dtype: List[Segmentation]
- guide_size
    - The 'guide_size' parameter specifies the guiding size of the enhancement process. It plays an important role in determining the size of the level of detail that will be the focus of attention during image enhancement.
    - Comfy dtype: INT
    - Python dtype: int
- max_size
    - The'max_size' parameter sets the maximum size of the image processing operation. It is important to control the resolution and calculation of the load performed by the node.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - The'seed' parameter is used to initialize the random number generator to ensure the repeatability of the random process of the nodes.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The'steps' parameter defines the number of turns or steps to be taken in the enhancement process. It directly affects the thoroughness of the enhancement.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The 'cfg'parameter contains configuration settings for node processing. It is essential for customizing node behaviour to meet specific enhancement requirements.
    - Comfy dtype: CONFIG
    - Python dtype: Configuration
- sampler_name
    - The sampling strategy to be used during the enhancement of the'sampler_name' parameter identification node is important for determining the method for processing image details.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The'scheduler' parameter is responsible for controlling the speed or tempo of implementation of enhancement steps. It affects the efficiency and results of node operations.
    - Comfy dtype: SCHEDULER
    - Python dtype: Scheduler
- denoise
    - The 'denoise' parameter indicates whether you should apply noise operations to images. It is important to improve image clarity and reduce noise prostheses.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- feather
    - The 'feather' parameter controls the softness of the edges of the processing image. It is important for the natural transition between different areas of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_mask
    - The 'noise_mask' parameter determines whether noise masks are used during enhancement. This may be important for some enhanced technologies that require noise management.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- force_inpaint
    - The 'force_inpaint' parameter determines whether to enforce restoration operations for images. This may be critical for filling missing or damaged areas in the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- basic_pipe
    - The 'basic_pipe' parameter covers the basic processing flow line for the image, including models and other components. It is essential for the initial phase of image enhancement.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, Any, Any]
## Optional
- wildcard
    - The 'wildcard' parameter allows for additional flexibility in processing by providing wildcard options. It can be used to introduce variability or special conditions into the operation of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- enhanced_img
    - The 'enhanced_img' output is the result of the image enhancement process, showing improved visual quality and detail. It is a key output because it represents the main objective of the node function.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- new_segs
    - The 'new_segs' output contains up-to-date split information after the enhancement process. This is important to understand the application of the post-enhanced area of the image.
    - Comfy dtype: SEGS
    - Python dtype: List[Segmentation]
- basic_pipe
    - The `basic_pipe' output reflects the basic treatment flow line used, which may be useful for further processing or analysis during the follow-up phase of the image processing workflow.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, Any, Any]
- cropped
    - The 'cropped' output consists of a list of cropped images derived from the original input. These images can be used for concentration enhancement or analysis in a given area.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]
- cropped_enhanced
    - The 'cropped_enhanced' output provides an enhanced list of cropping images highlighting the detailed improvements made to each subparagraph.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]
- cropped_enhanced_alpha
    - The `cropped_enhanced_alpha' output includes images with the alpha channel, which represents greater regional transparency and applies to stubbles or synthesizing in further image processing.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]
- cnet_images
    - The 'cnet_images' output is a list of images processed by the control network, which may be important for applications involving neurological network-based image control.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class DetailerForEachTestPipe(DetailerForEachPipe):
    RETURN_TYPES = ('IMAGE', 'SEGS', 'BASIC_PIPE', 'IMAGE', 'IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('image', 'segs', 'basic_pipe', 'cropped', 'cropped_refined', 'cropped_refined_alpha', 'cnet_images')
    OUTPUT_IS_LIST = (False, False, False, True, True, True, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, image, segs, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, denoise, feather, noise_mask, force_inpaint, basic_pipe, wildcard, cycle=1, refiner_ratio=None, detailer_hook=None, refiner_basic_pipe_opt=None, inpaint_model=False, noise_mask_feather=0):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: DetailerForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        (model, clip, vae, positive, negative) = basic_pipe
        if refiner_basic_pipe_opt is None:
            (refiner_model, refiner_clip, refiner_positive, refiner_negative) = (None, None, None, None)
        else:
            (refiner_model, refiner_clip, _, refiner_positive, refiner_negative) = refiner_basic_pipe_opt
        (enhanced_img, cropped, cropped_enhanced, cropped_enhanced_alpha, cnet_pil_list, new_segs) = DetailerForEach.do_detail(image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, detailer_hook, refiner_ratio=refiner_ratio, refiner_model=refiner_model, refiner_clip=refiner_clip, refiner_positive=refiner_positive, refiner_negative=refiner_negative, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        if len(cropped) == 0:
            cropped = [empty_pil_tensor()]
        if len(cropped_enhanced) == 0:
            cropped_enhanced = [empty_pil_tensor()]
        if len(cropped_enhanced_alpha) == 0:
            cropped_enhanced_alpha = [empty_pil_tensor()]
        if len(cnet_pil_list) == 0:
            cnet_pil_list = [empty_pil_tensor()]
        return (enhanced_img, new_segs, basic_pipe, cropped, cropped_enhanced, cropped_enhanced_alpha, cnet_pil_list)
```