# Documentation
- Class name: SeargeSDXLImage2ImageSampler2
- Category: Searge/_deprecated_/Sampling
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates an advanced sampling process for image generation, bringing together multiple models and fine-tuning techniques to improve the quality and detail of the output images. It produces high-resolution, consistent-style images by using the capabilities of the underlying models and fine-tuning models, as well as the input of conditions.

# Input types
## Required
- base_model
    - The base model is essential for building the infrastructure needed for the sampling process. It determines the initial state of image generation and sets the tone for subsequent improvements.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- base_positive
    - This input, as a positive adjustment element, influences the direction and quality of the image generation. It provides an important guide to the desired aesthetic and subject matter elements of the model.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- base_negative
    - Negative adjustment is essential to improve the image generation process by avoiding unnecessary features or styles. It helps to fine-tune the output and align it with the desired creative vision.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- refiner_model
    - The fine-tuning model plays a key role in the final phase of image generation, focusing on enhancing detail and improving overall visual quality. It ensures that output meets higher aesthetic standards.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_positive
    - This input plays an important role in guiding the positive aspects of modelling retention and highlighting images to ensure that the final output is in line with the desired creative direction.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- refiner_negative
    - The fine-tuning of negative inputs helps to identify and mitigate any unwanted elements in the image and to produce a more refined and perfect end product.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- image
    - Image input is the starting point of the sampling process and provides a visual context that is converted and enhanced by node operations. It is essential for generating a coherent and informative output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- vae
    - The VAE component is essential to the sampling process, which makes it possible to encode and decode image data in order to achieve a shift in style and aesthetics. It is the key to the ability of nodes to produce diverse and fine outputs.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- noise_seed
    - Noise seeds are a key parameter that introduces variability and ensures diversity of output in the sampling process. It is essential to prevent duplication of models and to promote creative diversity.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps in the sampling process determines the complexity and detail of generating the image. It is a key factor in achieving a balance between computational efficiency and visual quality.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configuration parameters are essential for fine-tuning the sampling process and allow for adjustments in the level of detail and overall visual style of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The name of the sampler is a key input that determines the particular sampling method to be used at the node. It affects the efficiency and effectiveness of the image generation process.
    - Comfy dtype: SAMPLER_NAME
    - Python dtype: str
- scheduler
    - The scheduler determines the rhythm and progress of the sampling process, ensuring a smooth transition from the initial to the final state. This is essential for a consistent and seemingly natural output.
    - Comfy dtype: SCHEDULER_NAME
    - Python dtype: str
- base_ratio
    - The base scale parameter is very important in determining the proportion of the steps dedicated to the initial sampling phase. It affects the balance between the base detail and the fine-tuning stage.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Noise parameters are essential to control noise reduction levels in the generation of images. They directly affect the clarity and visual attractiveness of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- softness
    - Soft and parameter effects amplification and mixing of the original images contribute to the smoothness and natural transition of the visual elements in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- upscale_model
    - The magnification model is used to improve the resolution of images and to provide better-quality canvas for further refinement and enhancement.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: torch.nn.Module
- scaled_width
    - The target width of the image magnifies, setting the size of the canvas of the fine image and influencing the level of detail in the output.
    - Comfy dtype: INT
    - Python dtype: int
- scaled_height
    - The object height of the image magnification, together with the width of the magnification, determines the ultimate size of the magnification image.
    - Comfy dtype: INT
    - Python dtype: int
- noise_offset
    - Noise offset parameters introduce additional variability in the sampling process, further enhancing the sample of the image generated.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_strength
    - The fine-tuning parameters adjust the intensity of the fine-tuning process, affecting the detail and clarity of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output of the image is the final result of the sampling process, representing the high-resolution, aestheticly fine-tuned manifestations of the input image, enhanced by the complex operation of nodes.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class SeargeSDXLImage2ImageSampler2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'base_positive': ('CONDITIONING',), 'base_negative': ('CONDITIONING',), 'refiner_model': ('MODEL',), 'refiner_positive': ('CONDITIONING',), 'refiner_negative': ('CONDITIONING',), 'image': ('IMAGE',), 'vae': ('VAE',), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551600}), 'steps': ('INT', {'default': 20, 'min': 0, 'max': 200}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 30.0, 'step': 0.5}), 'sampler_name': ('SAMPLER_NAME', {'default': 'ddim'}), 'scheduler': ('SCHEDULER_NAME', {'default': 'ddim_uniform'}), 'base_ratio': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'denoise': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'upscale_model': ('UPSCALE_MODEL',), 'scaled_width': ('INT', {'default': 1536, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'scaled_height': ('INT', {'default': 1536, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'noise_offset': ('INT', {'default': 1, 'min': 0, 'max': 1}), 'refiner_strength': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 1.0, 'step': 0.05}), 'softness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sample'
    CATEGORY = 'Searge/_deprecated_/Sampling'

    def sample(self, base_model, base_positive, base_negative, refiner_model, refiner_positive, refiner_negative, image, vae, noise_seed, steps, cfg, sampler_name, scheduler, base_ratio, denoise, softness, upscale_model=None, scaled_width=None, scaled_height=None, noise_offset=None, refiner_strength=None):
        base_steps = int(steps * (base_ratio + 0.0001))
        if noise_offset is None:
            noise_offset = 1
        if refiner_strength is None:
            refiner_strength = 1.0
        if refiner_strength < 0.01:
            refiner_strength = 0.01
        if steps < 1:
            return (image,)
        scaled_image = image
        use_upscale_model = upscale_model is not None and softness < 0.9999
        if use_upscale_model:
            upscale_result = comfy_extras.nodes_upscale_model.ImageUpscaleWithModel().upscale(upscale_model, image)
            scaled_image = upscale_result[0]
        if scaled_width is not None and scaled_height is not None:
            upscale_result = nodes.ImageScale().upscale(scaled_image, 'bicubic', scaled_width, scaled_height, 'center')
            scaled_image = upscale_result[0]
        if use_upscale_model and softness > 0.0001:
            upscale_result = nodes.ImageScale().upscale(image, 'bicubic', scaled_width, scaled_height, 'center')
            scaled_original = upscale_result[0]
            blend_result = comfy_extras.nodes_post_processing.Blend().blend_images(scaled_image, scaled_original, softness, 'normal')
            scaled_image = blend_result[0]
        if denoise < 0.01:
            return (scaled_image,)
        vae_encode_result = nodes.VAEEncode().encode(vae, scaled_image)
        input_latent = vae_encode_result[0]
        if base_steps >= steps:
            result_latent = nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, input_latent, denoise=denoise, disable_noise=False, start_step=0, last_step=steps, force_full_denoise=True)
        else:
            base_result = nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, input_latent, denoise=denoise, disable_noise=False, start_step=0, last_step=base_steps, force_full_denoise=True)
            result_latent = nodes.common_ksampler(refiner_model, noise_seed + noise_offset, steps, cfg, sampler_name, scheduler, refiner_positive, refiner_negative, base_result[0], denoise=denoise * refiner_strength, disable_noise=False, start_step=base_steps, last_step=steps, force_full_denoise=True)
        vae_decode_result = nodes.VAEDecode().decode(vae, result_latent[0])
        output_image = vae_decode_result[0]
        return (output_image,)
```