# Documentation
- Class name: UltimateSDUpscale
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/ssitu/ComfyUI_UltimateSDUpscale

UltimeSDUPSCale nodes are designed to use advanced technology to enhance the resolution of images. It uses the powerful function of a stable diffusion model to magnify images and provide users with high-quality, detailed results. The main objective of this node is to enhance visual authenticity while maintaining the nature of the original images, making them applicable to applications ranging from photo enhancement to art conversion.

# Input types
## Required
- image
    - The image parameter is essential because it is the basis for the magnification process. It determines the content and structure to be enhanced and its quality directly influences the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- model
    - Model parameters are essential for the operation of nodes because they define the AI models used to magnify the process. The selection of models significantly influences the style and quality of the magnification results.
    - Comfy dtype: MODEL
    - Python dtype: str
- positive
    - The reconciliations are being provided with the required characterization guidance for the AI model during the magnification process to ensure that the final image meets the user's expectations.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative reconciliation helps AI models avoid unnecessary features or hypotheses in magnifying images, improve overall quality and ensure more accurate presentation of desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- vae
    - The VAE parameter is essential to the magnification process, as it makes it possible to encode and decode the image, maintaining the nature of the original image and increasing its resolution.
    - Comfy dtype: VAE
    - Python dtype: str
- upscale_by
    - The upscale_by parameter determines the magnification multiplier of the image, directly affecting the size and level of detail of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - It is important that the Seed parameters generate replicable results during the magnification process, ensuring consistency in multiple operations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters affect the number of overlaps in which the AI model is implemented during the magnification process, which may affect the quality and detail of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the AI model to affect the overall style and consistency of the magnifying image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter determines the sampling method used by the AI model, which may change the style features and quality of the magnified image.
    - Comfy dtype: ENUM
    - Python dtype: comfy.samplers.KSampler.SAMPLERS
- scheduler
    - The Scheduler parameter affects the learning rate schedule of the AI model and influences condensation and final output quality.
    - Comfy dtype: ENUM
    - Python dtype: comfy.samplers.KSampler.SCHEDULERS
- denoise
    - The denoise parameter is used to control noise reduction levels applied during the magnification process and to increase the clarity and sharpness of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- upscale_model
    - The magnification models that are assigned to be used for the upscale_model parameters are essential for achieving the desired resolution and quality enhancement.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: str
- mode_type
    - The mode_type parameter determines the magnified processing pattern, which may affect the visual features and overall appearance of the final image.
    - Comfy dtype: ENUM
    - Python dtype: list
- tile_width
    - The tile_width parameter sets the tile width to be used for processing, which may affect the efficiency and quality of the magnification process.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile_height parameter defines the height of the tiles and influences how the images are separated and treated, thus influencing the results of the magnification.
    - Comfy dtype: INT
    - Python dtype: int
- mask_blur
    - The mask_blur parameter adjustment should be applied to the fuzzy level of the image mask, which could improve the seamless integration of the magnification area with the original image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_padding
    - The tile_padding parameter specifies the filling around each tile, which is important for maintaining the integrity of the image structure during the magnification process.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_mode
    - The seam_fix_mode parameters determine the method used to repair the seams between tiles, which enhances the visual continuity and overall quality of the magnified images.
    - Comfy dtype: ENUM
    - Python dtype: list
- seam_fix_denoise
    - The seam_fix_denoise parameter controls applied to the level of noise reduction in the seams help to reduce prostheses and increase the smoothness of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seam_fix_width
    - The seam_fix_width parameter sets the regional width around the seams for noise reduction and smoothing, affecting the seamless appearance of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_mask_blur
    - The seam_fix_mask_blur parameter adjustment should be applied to the level of ambiguity around the seams, which would help to increase the more natural transition between tiles.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_padding
    - The seam_fix_padding parameter defines the filling around the seams, which is essential to ensure that most of the smooth and consistent integration into the final image takes place.
    - Comfy dtype: INT
    - Python dtype: int
- force_uniform_tiles
    - Force_uniform_tiles parameters ensure that all tiles have the same size, which can simplify processing and increase the homogeneity of the magnified images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tiled_decode
    - The tiled_decode parameter indicates whether the image should be decoded by tiles, which can increase efficiency and quality in the magnification process for large images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - The output image is the result of a magnification process, showing higher resolution and enhanced detail, while preserving the nature of the original image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class UltimateSDUpscale:

    @classmethod
    def INPUT_TYPES(s):
        return prepare_inputs(USDU_base_inputs())
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, image, model, positive, negative, vae, upscale_by, seed, steps, cfg, sampler_name, scheduler, denoise, upscale_model, mode_type, tile_width, tile_height, mask_blur, tile_padding, seam_fix_mode, seam_fix_denoise, seam_fix_mask_blur, seam_fix_width, seam_fix_padding, force_uniform_tiles, tiled_decode):
        shared.sd_upscalers[0] = UpscalerData()
        shared.actual_upscaler = upscale_model
        shared.batch = [tensor_to_pil(image, i) for i in range(len(image))]
        sdprocessing = StableDiffusionProcessing(tensor_to_pil(image), model, positive, negative, vae, seed, steps, cfg, sampler_name, scheduler, denoise, upscale_by, force_uniform_tiles, tiled_decode)
        script = usdu.Script()
        processed = script.run(p=sdprocessing, _=None, tile_width=tile_width, tile_height=tile_height, mask_blur=mask_blur, padding=tile_padding, seams_fix_width=seam_fix_width, seams_fix_denoise=seam_fix_denoise, seams_fix_padding=seam_fix_padding, upscaler_index=0, save_upscaled_image=False, redraw_mode=MODES[mode_type], save_seams_fix_image=False, seams_fix_mask_blur=seam_fix_mask_blur, seams_fix_type=SEAM_FIX_MODES[seam_fix_mode], target_size_type=2, custom_width=None, custom_height=None, custom_scale=upscale_by)
        images = [pil_to_tensor(img) for img in shared.batch]
        tensor = torch.cat(images, dim=0)
        return (tensor,)
```