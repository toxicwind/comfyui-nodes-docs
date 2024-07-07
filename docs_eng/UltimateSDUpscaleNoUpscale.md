# Documentation
- Class name: UltimateSDUpscaleNoUpscale
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/ssitu/ComfyUI_UltimateSDUpscale

The node class is designed to improve image quality by using complex image magnification algorithms, which take advantage of the powerful function of stabilizing diffuse processing. It is designed to improve visual authenticity while maintaining the original content and detail of the image. The node's primary function is to magnify the image and provide users with a clear and visually attractive high-resolution output.

# Input types
## Required
- upscaled_image
    - Magnified image parameters are essential because they form the basis of the node magnification process. This is an image that has been magnified and will be further optimized by nodes to improve its quality and resolution.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- model
    - Model parameters are essential for nodes, which determine the bottom AI model used to magnify the process. It ensures that the AI model is used to achieve the desired magnification results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Positive parameters play an important role in guiding the magnification process by providing positive conditional data. These data help the AI model to understand the desired results and improve the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative parameters are essential because they provide negative conditional data to help the AI model avoid undesirable results during the magnification process. It helps to improve image quality.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- vae
    - The vae parameter is important because it represents the variable-based encoder used in the magnification process. It helps to generate higher quality images by encoded and decoded visual information.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- seed
    - Seed parameters are essential for the node because it initializes the random number generator to ensure that the results are replicable and consistent in different operations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The step parameter defines the number of turns that the AI model will perform during the magnification process. It directly affects the quality of the calculation time and final output.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a floating point value that affects the configuration of the AI model during the magnification process. It helps fine-tune the behaviour of the model to obtain the best results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter is essential for selecting the appropriate sampling method during the magnification process. It influences how the AI model produces the magnified image and contributes to overall quality and appearance.
    - Comfy dtype: ENUM
    - Python dtype: Enum
- scheduler
    - The scheduler parameter is essential to manage the AI model learning rate during the magnification process. It helps to control training dynamics and achieve better magnification results.
    - Comfy dtype: ENUM
    - Python dtype: Enum
- denoise
    - The noise parameter is a floating point value that controls the level of noise reduction applied during the magnification process. It is important to increase the clarity and sharpness of the magnifying image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tile_width
    - The tile_width parameter is specified as the width of the tile that is used to flatten the image. It affects the particle size of the magnification process and affects the quality of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile_height parameter defines the height of the tile that is used to level magnify the image. It works with the tile_width to determine the levelling strategy and its impact on image quality.
    - Comfy dtype: INT
    - Python dtype: int
- mask_blur
    - The mask_blur parameter controls the degree of ambiguity applied to the image mask during the magnification process. It is important to smooth the edges and increase the visual consistency of the magnified image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_padding
    - The tile_padding parameter specifies the fill that should be applied to the edge of each tile. It is essential to ensure that the gap between tiles in the image is eventually magnified.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_mode
    - The seam_fix_mode parameter determines the method to repair the sutures in the magnified image. It is essential to ensure seamless and visual pleasure in the final output by minimizing the visibility of the tile boundary.
    - Comfy dtype: ENUM
    - Python dtype: Enum
- seam_fix_denoise
    - The seam_fix_denoise parameter adjustment should be used to magnify the level of noise reduction in the image seams. It helps to reduce hypotheses and achieve a smoother and more natural appearance in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seam_fix_width
    - Seem_fix_width parameters set the width of the area around the seam to be processed. It affects the effectiveness of the seam repair process and helps to increase the overall visual quality of the image.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_mask_blur
    - Seem_fix_mask_blur parameter controls the degree of ambiguity of the mask used for seam repair. It is important for smooth transition between tiles and for enhancing visual continuity of magnified images.
    - Comfy dtype: INT
    - Python dtype: int
- seam_fix_padding
    - Seem_fix_padding parameters specify the amount of filling that should be used on the edges of the image during a seam repair. It is essential to ensure that the edges of the image are magnified with clarity and impropriety.
    - Comfy dtype: INT
    - Python dtype: int
- force_uniform_tiles
    - Force_uniform_tiles parameters ensure that all tiles are of the same size during the magnification process. This helps ultimately to magnify the consistent and uniform appearance of the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tiled_decode
    - Tiled_decode parameters indicate whether you should decode the magnified images by tiles. This increases processing efficiency during the magnification process and manages memory use.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - The output image is the result of the magnification process, showing improved resolution and quality. It represents the main output of the node and provides users with a visual improvement version of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class UltimateSDUpscaleNoUpscale:

    @classmethod
    def INPUT_TYPES(s):
        required = USDU_base_inputs()
        remove_input(required, 'upscale_model')
        remove_input(required, 'upscale_by')
        rename_input(required, 'image', 'upscaled_image')
        return prepare_inputs(required)
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, upscaled_image, model, positive, negative, vae, seed, steps, cfg, sampler_name, scheduler, denoise, mode_type, tile_width, tile_height, mask_blur, tile_padding, seam_fix_mode, seam_fix_denoise, seam_fix_mask_blur, seam_fix_width, seam_fix_padding, force_uniform_tiles, tiled_decode):
        shared.sd_upscalers[0] = UpscalerData()
        shared.actual_upscaler = None
        shared.batch = [tensor_to_pil(upscaled_image, i) for i in range(len(upscaled_image))]
        sdprocessing = StableDiffusionProcessing(tensor_to_pil(upscaled_image), model, positive, negative, vae, seed, steps, cfg, sampler_name, scheduler, denoise, 1, force_uniform_tiles, tiled_decode)
        script = usdu.Script()
        processed = script.run(p=sdprocessing, _=None, tile_width=tile_width, tile_height=tile_height, mask_blur=mask_blur, padding=tile_padding, seams_fix_width=seam_fix_width, seams_fix_denoise=seam_fix_denoise, seams_fix_padding=seam_fix_padding, upscaler_index=0, save_upscaled_image=False, redraw_mode=MODES[mode_type], save_seams_fix_image=False, seams_fix_mask_blur=seam_fix_mask_blur, seams_fix_type=SEAM_FIX_MODES[seam_fix_mode], target_size_type=2, custom_width=None, custom_height=None, custom_scale=1)
        images = [pil_to_tensor(img) for img in shared.batch]
        tensor = torch.cat(images, dim=0)
        return (tensor,)
```