# Documentation
- Class name: SEGSUpscalerPipe
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSUpscalerPipe is a node used to improve the resolution of images, which uses advanced up-sampling techniques. It uses the ability of deep learning models to magnify images while maintaining the integrity of semantic partitions (SEGS). This node is particularly suitable for applications requiring high-quality sampling of images, such as graphic design, photography and video processing.

# Input types
## Required
- image
    - The input image to be sampled. It is the main data source for the sampling process and is essential for achieving the required output resolution and quality.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - These are used to guide the sampling process to maintain the semantic integrity of the original image.
    - Comfy dtype: SEGS
    - Python dtype: torch.Tensor
- basic_pipe
    - Models and configurations that form the basis of the sampling process. It includes basic components such as models, clips, vae, and additional settings that influence the results of the sampling.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.nn.Module, torch.nn.Module, Any, Any]
- rescale_factor
    - Enter a multiple of the images that will be magnified. It directly affects the final resolution of the output image, and a higher number leads to a larger image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- resampling_method
    - The re-sampling method determines the algorithm to be used for uploading the image. Different methods may result in varying degrees of detail and image quality.
    - Comfy dtype: COMBO[lanczos, nearest, bilinear, bicubic]
    - Python dtype: str
- supersample
    - A sign that indicates whether to use ultra-sampling techniques for upsampling. Oversamping increases the sharpness and clarity of magnifying images.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- rounding_modulus
    - The number of molds used to magnify the image size. It ensures that the output image is consistent in size and suitable for further processing.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Random seeds to ensure that the sampling process is repeated. It is important to obtain consistent results when running multiple nodes.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Runs the number of steps of the sampling algorithm. More steps lead to better results, but may increase processing time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - A configuration parameter to adjust the balance between detail retention and noise reduction during the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The name of the sampler used in the sampling process. A different sampler can influence the distribution of the sample and the final image mass.
    - Comfy dtype: KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - A scheduler to control the learning rate during the sampling process. It can affect the collection and stability of sampling algorithms.
    - Comfy dtype: KSampler.SCHEDULERS
    - Python dtype: str
- denoise
    - The amount of noise to be applied during the sampling process. A higher value reduces the noise in the image, but it may also remove some details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- feather
    - A feather value for softening the edges of the image. It can create a smoother transition between different areas of the image.
    - Comfy dtype: INT
    - Python dtype: int
- inpaint_model
    - A boolean sign indicating whether to use repair models to fill missing or damaged areas in the image during the sampling period.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_mask_feather
    - The feather value applied to the noise mask to soften its edges. This helps to create a more natural look for magnified images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- upscaled_image
    - The output of the SEGSUppscalerPipe node is treated to achieve a larger image with a higher resolution, while maintaining semantic detail. It is the final result of the sampling process and can be further used or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SEGSUpscalerPipe:

    @classmethod
    def INPUT_TYPES(s):
        resampling_methods = ['lanczos', 'nearest', 'bilinear', 'bicubic']
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'basic_pipe': ('BASIC_PIPE',), 'rescale_factor': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 100.0, 'step': 0.01}), 'resampling_method': (resampling_methods,), 'supersample': (['true', 'false'],), 'rounding_modulus': ('INT', {'default': 8, 'min': 8, 'max': 1024, 'step': 8}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 0.5, 'min': 0.0001, 'max': 1.0, 'step': 0.01}), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'inpaint_model': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_mask_feather': ('INT', {'default': 20, 'min': 0, 'max': 100, 'step': 1})}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'upscaler_hook_opt': ('UPSCALER_HOOK',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    @staticmethod
    def doit(image, segs, basic_pipe, rescale_factor, resampling_method, supersample, rounding_modulus, seed, steps, cfg, sampler_name, scheduler, denoise, feather, inpaint_model, noise_mask_feather, upscale_model_opt=None, upscaler_hook_opt=None):
        (model, clip, vae, positive, negative) = basic_pipe
        return SEGSUpscaler.doit(image, segs, model, clip, vae, rescale_factor, resampling_method, supersample, rounding_modulus, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, feather, inpaint_model, noise_mask_feather, upscale_model_opt=upscale_model_opt, upscaler_hook_opt=upscaler_hook_opt)
```