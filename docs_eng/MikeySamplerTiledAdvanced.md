# Documentation
- Class name: MikeySamplerTiledAdvanced
- Category: Mikey/Sampling
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The MikeySamplerTiledAdvanced node is a complex component designed to perform advanced sampling techniques for image sampling. It uses two phases involving basic and fine-tuning models to gradually improve the quality of sampled images. The main function of the node is to generate high-resolution images from potential expressions by using complex noise modelling and iterative refinement strategies.

# Input types
## Required
- base_model
    - The base model is essential for the initial phase of image sampling and provides the basis for the process of generation. It is essential for nodes to be able to generate consistent and structured images at a lower resolution.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_model
    - The fine-tuning model plays a key role in the second phase of the sampling process by fine-tuning image details based on the output of the underlying model. Its effects directly affect the quality of the final image.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- samples
    - Samples represent potential spatial vectors that are used as input to the image generation process. They are essential for creating a diverse and unique image output at nodes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - VAE (variate self-encoder) is used to decode potential expressions to pixel space. It is a key component for converting sample data into visual formats.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive_cond_base
    - Guidance is being provided to the underlying model during the sampling period to ensure that the images generated meet specific characteristics or attributes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[torch.Tensor]
- negative_cond_base
    - Negative conditions are used to limit the sampling process of the underlying model and to prevent undesirable features from being included in the images generated.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[torch.Tensor]
- positive_cond_refiner
    - The positive conditions of the fine-tuning model guide the enhancement process and focus on highlighting the required features in the fine-tuning image.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[torch.Tensor]
- negative_cond_refiner
    - Negative conditions of the fine-tuning model ensure that the fine-tuning process avoids introducing undesirable elements into the final image.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[torch.Tensor]
- model_name
    - The specific up-sampling model to be used in the node of the model name is essential for determining the upsampling capacity and performance of the node.
    - Comfy dtype: folder_paths.get_filename_list('upscale_models')
    - Python dtype: str
- seed
    - Seed parameters are essential to ensure the repeatability of the sampling process and allow consistent results to be obtained in different operations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- denoise_image
    - Noise parameters control the level of noise reduction applied during the sampling process, which can significantly affect the clarity and detail of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - Step parameters define the number of turns during the sampling process, which has a direct impact on the computational complexity of nodes and the quality of the images generated.
    - Comfy dtype: INT
    - Python dtype: int
- smooth_step
    - Smoothing steps are used to control the transition between different stages of the sampling process, with the aim of generating more smoother and natural progress in image details.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the sampling process to allow micro-reconciliation point behaviour to achieve optimal results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name specifies the sampling method to be used, which is a key factor in determining the method for generating an image sample at the node.
    - Comfy dtype: comfy.samplers.KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - The scheduler determines the rate of progress in the sampling process, which can affect the efficiency and results of image generation.
    - Comfy dtype: comfy.samplers.KSampler.SCHEDULERS
    - Python dtype: str
- upscale_by
    - The " zoom in " parameter sets the zoom factor of the sampling process on the image, directly affecting the resolution of the final output image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_denoise
    - This enhances the overall visual consistency of the sampled images.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_model
    - Tiled models determine which models to use in the roll-out process, allowing for the selection of base models or fine-tuning models to achieve different levels of detail in the final image.
    - Comfy dtype: COMBO['base', 'refiner']
    - Python dtype: str
- use_complexity_score
    - The use of the complexity fraction parameters indicates whether to include the complexity fractions in the flattening process, which helps to establish the priority order of the flattening process.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str
- image_optional
    - The optional image parameters allow for the inclusion of an additional image that can be used to influence the sampling process and introduce new visual elements into the image generated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- tiled_image
    - Tiled images are the main output of nodes, representing the final upsampling and sheeting version of the input. They demonstrate the ability of nodes to enhance image details through multi-stage sampling processes.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- upscaled_image
    - The above sampled image is an additional output that provides a view of the image after the initial up-sampling phase before the laying process. It highlights the intermediate results of the node during the top sample.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class MikeySamplerTiledAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'refiner_model': ('MODEL',), 'samples': ('LATENT',), 'vae': ('VAE',), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'positive_cond_refiner': ('CONDITIONING',), 'negative_cond_refiner': ('CONDITIONING',), 'model_name': (folder_paths.get_filename_list('upscale_models'),), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'denoise_image': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'steps': ('INT', {'default': 30, 'min': 1, 'max': 1000}), 'smooth_step': ('INT', {'default': 1, 'min': -1, 'max': 100}), 'cfg': ('FLOAT', {'default': 6.5, 'min': 0.0, 'max': 1000.0, 'step': 0.1}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1}), 'tiler_denoise': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'tiler_model': (['base', 'refiner'], {'default': 'base'}), 'use_complexity_score': (['true', 'false'], {'default': 'true'})}, 'optional': {'image_optional': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE')
    RETURN_NAMES = ('tiled_image', 'upscaled_image')
    FUNCTION = 'run'
    CATEGORY = 'Mikey/Sampling'

    def phase_one(self, base_model, refiner_model, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, upscale_by, model_name, seed, vae, denoise_image, steps, smooth_step, cfg, sampler_name, scheduler):
        image_scaler = ImageScale()
        vaedecoder = VAEDecode()
        uml = UpscaleModelLoader()
        upscale_model = uml.load_model(model_name)[0]
        iuwm = ImageUpscaleWithModel()
        start_step = int(steps - steps * denoise_image)
        if start_step > steps // 2:
            last_step = steps - 1
        elif start_step % 2 == 0:
            last_step = steps // 2 - 1
        else:
            last_step = steps // 2
        sample1 = common_ksampler(base_model, seed, steps, cfg, sampler_name, scheduler, positive_cond_base, negative_cond_base, samples, start_step=start_step, last_step=last_step, force_full_denoise=False)[0]
        start_step = last_step + 1
        total_steps = steps + smooth_step
        sample2 = common_ksampler(refiner_model, seed, total_steps, cfg, sampler_name, scheduler, positive_cond_refiner, negative_cond_refiner, sample1, disable_noise=True, start_step=start_step, force_full_denoise=True)[0]
        pixels = vaedecoder.decode(vae, sample2)[0]
        (org_width, org_height) = (pixels.shape[2], pixels.shape[1])
        img = iuwm.upscale(upscale_model, image=pixels)[0]
        (upscaled_width, upscaled_height) = (int(org_width * upscale_by // 8 * 8), int(org_height * upscale_by // 8 * 8))
        img = image_scaler.upscale(img, 'nearest-exact', upscaled_width, upscaled_height, 'center')[0]
        return (img, upscaled_width, upscaled_height)

    def run(self, seed, base_model, refiner_model, vae, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, model_name, upscale_by=1.0, tiler_denoise=0.25, upscale_method='normal', tiler_model='base', denoise_image=0.25, steps=30, smooth_step=0, cfg=6.5, sampler_name='dpmpp_3m_sde_gpu', scheduler='exponential', use_complexity_score='true', image_optional=None):
        if image_optional is not None:
            vaeencoder = VAEEncode()
            samples = vaeencoder.encode(vae, image_optional)[0]
        (img, upscaled_width, upscaled_height) = self.phase_one(base_model, refiner_model, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, upscale_by, model_name, seed, vae, denoise_image, steps, smooth_step, cfg, sampler_name, scheduler)
        img = tensor2pil(img)
        if tiler_model == 'base':
            tiled_image = run_tiler(img, base_model, vae, seed, positive_cond_base, negative_cond_base, tiler_denoise, use_complexity_score)
        else:
            tiled_image = run_tiler(img, refiner_model, vae, seed, positive_cond_refiner, negative_cond_refiner, tiler_denoise, use_complexity_score)
        return (tiled_image, img)
```