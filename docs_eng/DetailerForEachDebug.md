# Documentation
- Class name: DetailerForEachTest
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DetailerForEachTest node is designed to enhance image details by treating each image segment separately. It uses advanced models and techniques to fine-tune and enhance image quality, focusing on areas of interest within the image. The node aims to increase visual clarity and detail without compromising the integrity of the original image.

# Input types
## Required
- image
    - Enter the load of the image, and the node is processed to enhance its details. This is a basic parameter, because all operations of the node are organized around this image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- segs
    - Splits the data and defines the areas of interest in the image. For nodes, it is important to determine which parts of the image need to be consolidated in detail.
    - Comfy dtype: List[seg]
    - Python dtype: List[Any]
- model
    - Model for detail enhancement. It plays an important role in the ability of nodes to fine-tune and enhance image details according to input parameters.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- guide_size
    - The lead size parameter determines the scale of the enhanced detail. It is essential to control the level of detail that the node will apply to the image.
    - Comfy dtype: int
    - Python dtype: int
- guide_size_for
    - The guide size is used for parameters, specifying the reference dimensions for the detail enhancement process. This is important to align the enhancement to the desired output dimensions.
    - Comfy dtype: int
    - Python dtype: int
- max_size
    - The maximum size parameter limits the resolution of the enhanced image. It ensures that the enhanced image does not exceed a certain size, which may be important for performance or storage considerations.
    - Comfy dtype: int
    - Python dtype: int
- seed
    - A random torrent used to initialize a random process within a node. It ensures that the result is repeated when the node runs with the same parameter.
    - Comfy dtype: int
    - Python dtype: int
- steps
    - Runs the steps of the enhancement process. It affects the thoroughness of the enhancement and the time it takes to complete the operation.
    - Comfy dtype: int
    - Python dtype: int
- cfg
    - Controls the configuration of all aspects of the enhancement process. This is a key parameter that allows micro-reconciliation point behaviour to achieve the desired results.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- sampler_name
    - The name of the sampler used to select the sample during the enhancement process. It affects the sampling strategy and may affect the quality of the enhanced image.
    - Comfy dtype: str
    - Python dtype: str
- scheduler
    - A learning rate scheduler is used during model training. It is important for adjusting learning rates over time to improve training efficiency and model performance.
    - Comfy dtype: torch.optim.lr_scheduler
    - Python dtype: torch.optim.lr_scheduler
- positive
    - Guides the enhancement process to a list of positive conditions for the desired outcome and their associated details. This is a key parameter to guide node behaviour.
    - Comfy dtype: List[condition_details]
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- negative
    - This is essential to control the behaviour of nodes in order to avoid undesirable outcomes.
    - Comfy dtype: List[condition_details]
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
## Optional
- clip
    - CLIP volume, which provides context information to guide the enhancement process. This is an optional parameter that can be used to influence the style and content of the enhanced image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- vae
    - A variable coder (VAE) for generating or fine-tuning image details. This is an optional component that can be used to introduce or improve specific features in the image.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- denoise
    - Go to the noise switch and decide whether to apply the noise step to the enhanced image. It improves visual quality by reducing the noise.
    - Comfy dtype: bool
    - Python dtype: bool
- feather
    - Featuring parameters to control the smoothness of the edge of the enhanced image. It is important to create a natural transition between the enhanced and original regions of the image.
    - Comfy dtype: float
    - Python dtype: float
- noise_mask
    - Noise mask loads define the image range to be used for noise reduction. This is an optional parameter that can be used to selectively reduce the noise of parts of the image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- force_inpaint
    - It can be used to fill missing or damaged areas in the image.
    - Comfy dtype: bool
    - Python dtype: bool
- wildcard
    - The wildcard parameter allows for the dynamic selection of enhancement options based on certain conditions. It provides flexibility on how to apply enhancements to different segments of the image at the node.
    - Comfy dtype: str
    - Python dtype: str
- detailer_hook
    - An optional hook function can be used to perform custom operations after the detail enhancement process. It allows additional processing of images.
    - Comfy dtype: Callable
    - Python dtype: Callable[..., Any]
- cycle
    - Repeats the number of cycles of the enhancement process. It can be used to apply multiple enhancements to obtain more refined results.
    - Comfy dtype: int
    - Python dtype: int
- inpaint_model
    - An optional repair model that can be used to fill missing or damaged areas in the image during the enhancement process.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- noise_mask_feather
    - The feather value of the noise mask controls noise to reduce the smoothness of the edges. It helps to create a smoother transition between noise reduction and the original area.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- enhanced_img
    - Details increase the amount of enhanced images generated. It represents the main output of the nodes, showing increased visual clarity and detail.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- cropped
    - A list of clipping image lengths has been processed for detail enhancement. These numbers represent the enhanced parts of the image that are focused on.
    - Comfy dtype: List[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- cropped_enhanced
    - An enhanced list of clippings of images. Each volume corresponds to an enhanced part of the original image, showing improved details.
    - Comfy dtype: List[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- cropped_enhanced_alpha
    - A list of enhanced clipping image lengths with a alpha channel. These volumes contain transparency information that can be used for further processing or stacking.
    - Comfy dtype: List[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- cnet_images
    - The list of PIL images generated by the control network during the enhancement process provides visual feedback or additional analysis.
    - Comfy dtype: List[PIL.Image]
    - Python dtype: List[PIL.Image]

# Usage tips
- Infra type: GPU

# Source code
```
class DetailerForEachTest(DetailerForEach):
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('image', 'cropped', 'cropped_refined', 'cropped_refined_alpha', 'cnet_images')
    OUTPUT_IS_LIST = (False, True, True, True, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, detailer_hook=None, cycle=1, inpaint_model=False, noise_mask_feather=0):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: DetailerForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        (enhanced_img, cropped, cropped_enhanced, cropped_enhanced_alpha, cnet_pil_list, new_segs) = DetailerForEach.do_detail(image, segs, model, clip, vae, guide_size, guide_size_for, max_size, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, noise_mask, force_inpaint, wildcard, detailer_hook, cycle=cycle, inpaint_model=inpaint_model, noise_mask_feather=noise_mask_feather)
        if len(cropped) == 0:
            cropped = [empty_pil_tensor()]
        if len(cropped_enhanced) == 0:
            cropped_enhanced = [empty_pil_tensor()]
        if len(cropped_enhanced_alpha) == 0:
            cropped_enhanced_alpha = [empty_pil_tensor()]
        if len(cnet_pil_list) == 0:
            cnet_pil_list = [empty_pil_tensor()]
        return (enhanced_img, cropped, cropped_enhanced, cropped_enhanced_alpha, cnet_pil_list)
```