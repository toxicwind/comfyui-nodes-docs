# Documentation
- Class name: MikeySamplerTiledAdvancedBaseOnly
- Category: Mikey/Sampling
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The MikeySamplerTiledAdvancedBaseOnly node is designed to perform advanced image sampling and upsampling operations. It combines basic models, variable coders (VAE) and block techniques to enhance image quality and detail. The main objective of the node is to generate high-resolution images from potential samples, using sophisticated algorithms and noise techniques to obtain excellent results.

# Input types
## Required
- base_model
    - The basic model parameter is essential to the operation of the node because it defines the bottom model used for sampling. It directly affects the quality and properties of the samples generated, which are essential for achieving the required upsampling and image enhancement.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- samples
    - Sample input is a key element of the node function and provides a potential expression that will be converted to a high-resolution image. The quality of the sample directly influences the final output, making it a key parameter for achieving the node objective.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - VAE parameters play an important role in decoding nodes and encoding potentials. They play a key role in converting sampling data into formats suitable for sampling and further processing.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive_cond_base
    - The positionive_cond_base parameter is essential to guide the sampling process to produce images with the required properties. It is used as a positive adjustment factor to influence the ability of nodes to produce images that meet specific criteria.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative_cond_base
    - The negative_cond_base parameter is a key factor in guiding the sampling process to avoid undesirable outcomes. It helps to optimize the image generation process by providing negative reconciliations, which are essential to ensure that node output is consistent with expected results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- model_name
    - The model_name parameter is essential in determining which sampling models will be used to enhance the image. It determines the specific configuration and capabilities of the model, which are essential for achieving the required upsampling and image quality improvements.
    - Comfy dtype: folder_paths.get_filename_list('upscale_models')
    - Python dtype: str
- seed
    - Seed parameters are important to ensure the repeatability and consistency of the sampling process. It initializes the random number generator, which affects the generation of the sample and, in turn, the final image output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- denoise_image
    - The denoise_image parameter allows control of the noise level applied to the image during the top sampling process. It is an optional setting that can be adjusted as necessary to achieve a balance between image detail and noise reduction.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The Steps parameter defines the number of turns to be used in the sampling process. It is an optional input that can be fine-tuned to control the complexity and detail in which the image is generated.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameter, Abbreviation, is used to adjust the settings of the sampling process. It is an optional parameter that can be modified to affect the behaviour of nodes and the image properties generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used. It is an optional input that allows for the selection of different sampling techniques, which can significantly affect the performance of the node and the quality of the output image.
    - Comfy dtype: comfy.samplers.KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - Scheduler parameters determine the dispatch strategy for the sampling process. It is an optional set-up that can be customized to optimize the efficiency of nodes and generate high-quality images.
    - Comfy dtype: comfy.samplers.KSampler.SCHEDULERS
    - Python dtype: str
- upscale_by
    - Upscale_by parameters set the zoom factor for the sampling process. It is an optional input that allows users to control the degree of sampling applied to the image, which influences the final resolution and details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_denoise
    - The tiler_denoise parameter is used to control the noise level of each small square during the flattening process. It is an optional parameter that can be adjusted to improve the visual quality of the final image by reducing the noise in individual small squares.
    - Comfy dtype: FLOAT
    - Python dtype: float
- image_optional
    - The image_optional parameter allows optional input of an image that can be encoded into potential space for further processing. This allows nodes to use existing image work and provides flexibility for input data processing.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Output types
- output_image
    - The output_image parameter represents the final, upsampling and enhanced images generated by nodes. It is the result of node processing and reflects the combined effects of applied sampling, upsampling and noise technology.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: GPU

# Source code
```
class MikeySamplerTiledAdvancedBaseOnly:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'samples': ('LATENT',), 'vae': ('VAE',), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'model_name': (folder_paths.get_filename_list('upscale_models'),), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'denoise_image': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'steps': ('INT', {'default': 30, 'min': 1, 'max': 1000}), 'cfg': ('FLOAT', {'default': 6.5, 'min': 0.0, 'max': 1000.0, 'step': 0.1}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1}), 'tiler_denoise': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'image_optional': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('output_image',)
    FUNCTION = 'run'
    CATEGORY = 'Mikey/Sampling'

    def phase_one(self, base_model, samples, positive_cond_base, negative_cond_base, upscale_by, model_name, seed, vae, denoise_image, steps, cfg, sampler_name, scheduler):
        image_scaler = ImageScale()
        vaedecoder = VAEDecode()
        uml = UpscaleModelLoader()
        upscale_model = uml.load_model(model_name)[0]
        iuwm = ImageUpscaleWithModel()
        start_step = int(steps - steps * denoise_image)
        sample1 = common_ksampler(base_model, seed, steps, cfg, sampler_name, scheduler, positive_cond_base, negative_cond_base, samples, start_step=start_step, last_step=steps, force_full_denoise=False)[0]
        pixels = vaedecoder.decode(vae, sample1)[0]
        (org_width, org_height) = (pixels.shape[2], pixels.shape[1])
        img = iuwm.upscale(upscale_model, image=pixels)[0]
        (upscaled_width, upscaled_height) = (int(org_width * upscale_by // 8 * 8), int(org_height * upscale_by // 8 * 8))
        img = image_scaler.upscale(img, 'nearest-exact', upscaled_width, upscaled_height, 'center')[0]
        return (img, upscaled_width, upscaled_height)

    def upscale_image(self, samples, vae, upscale_by, model_name):
        image_scaler = ImageScale()
        vaedecoder = VAEDecode()
        uml = UpscaleModelLoader()
        upscale_model = uml.load_model(model_name)[0]
        iuwm = ImageUpscaleWithModel()
        pixels = vaedecoder.decode(vae, samples)[0]
        (org_width, org_height) = (pixels.shape[2], pixels.shape[1])
        img = iuwm.upscale(upscale_model, image=pixels)[0]
        (upscaled_width, upscaled_height) = (int(org_width * upscale_by // 8 * 8), int(org_height * upscale_by // 8 * 8))
        img = image_scaler.upscale(img, 'nearest-exact', upscaled_width, upscaled_height, 'center')[0]
        return (img, upscaled_width, upscaled_height)

    def run(self, seed, base_model, vae, samples, positive_cond_base, negative_cond_base, model_name, upscale_by=2.0, tiler_denoise=0.4, upscale_method='normal', denoise_image=1.0, steps=30, cfg=6.5, sampler_name='dpmpp_sde_gpu', scheduler='karras', image_optional=None):
        if image_optional is not None:
            vaeencoder = VAEEncode()
            samples = vaeencoder.encode(vae, image_optional)[0]
        if denoise_image > 0:
            (img, upscaled_width, upscaled_height) = self.phase_one(base_model, samples, positive_cond_base, negative_cond_base, upscale_by, model_name, seed, vae, denoise_image, steps, cfg, sampler_name, scheduler)
            img = tensor2pil(img)
        else:
            img = self.upscale_image(samples, vae, upscale_by, model_name)
            img = tensor2pil(img)
        tiled_image = run_tiler_for_steps(img, base_model, vae, seed, cfg, sampler_name, scheduler, positive_cond_base, negative_cond_base, steps, tiler_denoise)
        return (tiled_image,)
```