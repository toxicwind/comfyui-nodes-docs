# Documentation
- Class name: SeargeSDXLImage2ImageSampler
- Category: Searge/_deprecated_/Sampling
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeSDXLIMAGE2ImageSampler node is designed to improve image quality through a complex sampling enhancement process that uses multiple models and parameters to fine-tune output results. It aims to improve the quality and beauty of image creation by combining various conditions and refinement steps.

# Input types
## Required
- base_model
    - The basic model is essential to the image sampling process and forms the basis for image generation. It is the main model used to generate initial image data, which will be further refined and regulated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- base_positive
    - This parameter, as a positive adjustment input, influences the style and content of the image generated. It is critical in guiding the sampling process towards the desired aesthetic and thematic outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- base_negative
    - Negative adjustment input is used to exclude certain elements or features from the creation of the image and to ensure that the final output meets the intended specifications.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- refiner_model
    - The fine-tuning model plays a key role in the reprocessing phase and is used to fine-tune images to achieve a higher level of authenticity and a better aesthetic quality that meets expectations.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_positive
    - This input provides positive guidance for the process of fine-tuning, ensures that enhanced images retain desired properties and improves the output of the underlying model.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- refiner_negative
    - Negative adjustments to fine-tuning models help to avoid undesirable features in the final image and contribute to more controlled and accurate image enhancement.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- image
    - The image parameter is the target that the node will process and refine. It is the core element of the whole sampling operation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- vae
    - VAE (distributive encoder) is used to encode and decode image data, enabling nodes to manipulate the potential space of the image and produce high-quality visual effects.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- noise_seed
    - Noise seeds play an important role in introducing change in the sampling process, ensuring diversity of outputs and preventing duplication or predictability of results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the complexity and duration of the sampling process, directly affecting the details and fineness of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration parameter or 'cfg' is a floating point value used to adjust the sampling configuration to affect the overall behaviour and performance of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name identifies the specific sampling methods to be used, which are essential for determining the quality and characteristics of the images generated.
    - Comfy dtype: SAMPLER_NAME
    - Python dtype: str
- scheduler
    - The scheduler determines the rhythm and pace of the sampling process, ensuring that the fine-tuning phase is carried out efficiently and in an orderly manner.
    - Comfy dtype: SCHEDULER_NAME
    - Python dtype: str
- base_ratio
    - The base scale is a floating point value, which affects the ratio of steps assigned to the base model to the fine model, and the balance of rough and fine details in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Noise parameters control the level of noise reduction applied during the sampling process, directly affecting the clarity and smoothness of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- softness
    - The softness adjusts the blending intensity in combining magnification and original images, contributing to the seamless integration of overall visual harmony and detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- upscale_model
    - When a magnification model is provided, it is used to improve the resolution of the image, thereby obtaining higher quality and more detailed results.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: torch.nn.Module
- scaled_width
    - The diagnosis defines the expected width of the magnification image, which is important for setting the size of the canvas for fine-tuning the output of the image.
    - Comfy dtype: INT
    - Python dtype: int
- scaled_height
    - Scaled height corresponds to the expected height of the magnification image and works with the contraction to determine the final size of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- noise_offset
    - Noise offsets introduce a variable element to noise seeds, adding additional diversity to the sampling process and ensuring unique results.
    - Comfy dtype: INT
    - Python dtype: int
- refiner_strength
    - The intensity of fine-tuning is a floating point value that regulates the intensity of the fine-tuning process and allows control of the level of detail and clarity in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output images are the result of the sampling process, representing a high-quality, fine vision with input parameters and conditions, and showing the ability of nodes.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class SeargeSDXLImage2ImageSampler:

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