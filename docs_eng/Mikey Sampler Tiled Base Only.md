# Documentation
- Class name: MikeySamplerTiledBaseOnly
- Category: Sampling
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The MikeySamplerTiledBaseOnly node is designed to generate high-quality images from the basic model through a two-stage sampling process. It uses a variety of techniques, such as potential spatial sampling, noise removal and on-sampling, to produce detailed and fine images. The node is focused on enhancing image quality and resolution through a complex combination of model-based and algorithmic methods.

# Input types
## Required
- base_model
    - Base_model parameters are essential for the operation of nodes, as they define the basic model that begins with the image generation process. They are the starting point for sampling and upsampling sequences and have a significant impact on the quality and properties of the final output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- samples
    - The samples parameter is essential for the node because it represents the point where the image is sampled from potential space. It plays a key role in determining the diversity and randomity of the image generation and influences the overall outcome of the sampling process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- positive_cond_base
    - The positionive_cond_base parameter is a conditional input that has a positive impact on the sampling process. It helps to guide the image towards desired properties and enhances the ability of nodes to produce the target output.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative_cond_base
    - The negative_cond_base parameter is entered as a condition that negatively affects the sampling process. It helps to remove unwanted features from the image generated and refines the output of nodes to meet the specified requirements.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- vae
    - The vae parameter is essential for the node because it represents a variable self-codifier used to decode potential expressions into pixel space. It is a key component in the process of converting sampling data into visual formats.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- model_name
    - The model_name parameter is specified as the upper sample model for the sampling process on the image. It is a determining factor in the selection of the model structure and its corresponding capabilities, directly affecting the quality of the sample.
    - Comfy dtype: folder_paths.get_filename_list('upscale_models')
    - Python dtype: str
## Optional
- seed
    - Seed parameters are used to initialize the random number generator to ensure repeatability of the sampling process. This is an important aspect when a consistent result is required for multiple implementations.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_by
    - Upscale_by parameters determine the number of times the original image size will increase. It directly affects the resolution and details of the sample image and plays an important role in the appearance of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_denoise
    - The tiler_denoise parameter controls the level of noise applied during the sheeting process. It is an important adjustment parameter that improves the visual quality of the sampled images by reducing the prostheses of noise.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The image output of the MikeySamplerTiledBaseOnly node represents the final sample and fine-processed image. It is the result of the node process and reflects the high resolution and detailed visual output that the node is intended to produce.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class MikeySamplerTiledBaseOnly(MikeySamplerTiled):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'samples': ('LATENT',), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'vae': ('VAE',), 'model_name': (folder_paths.get_filename_list('upscale_models'),), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1}), 'tiler_denoise': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)

    def phase_one(self, base_model, samples, positive_cond_base, negative_cond_base, upscale_by, model_name, seed, vae):
        image_scaler = ImageScale()
        vaedecoder = VAEDecode()
        uml = UpscaleModelLoader()
        upscale_model = uml.load_model(model_name)[0]
        iuwm = ImageUpscaleWithModel()
        sample1 = common_ksampler(base_model, seed, 30, 5, 'dpmpp_3m_sde_gpu', 'exponential', positive_cond_base, negative_cond_base, samples, start_step=0, last_step=14, force_full_denoise=False)[0]
        sample2 = common_ksampler(base_model, seed + 1, 32, 9.5, 'dpmpp_3m_sde_gpu', 'exponential', positive_cond_base, negative_cond_base, sample1, disable_noise=True, start_step=15, force_full_denoise=True)[0]
        pixels = vaedecoder.decode(vae, sample2)[0]
        (org_width, org_height) = (pixels.shape[2], pixels.shape[1])
        img = iuwm.upscale(upscale_model, image=pixels)[0]
        (upscaled_width, upscaled_height) = (int(org_width * upscale_by // 8 * 8), int(org_height * upscale_by // 8 * 8))
        img = image_scaler.upscale(img, 'nearest-exact', upscaled_width, upscaled_height, 'center')[0]
        return (img, upscaled_width, upscaled_height)

    def adjust_start_step(self, image_complexity, hires_strength=1.0):
        image_complexity /= 24
        if image_complexity > 1:
            image_complexity = 1
        image_complexity = min([0.55, image_complexity]) * hires_strength
        return min([32, 32 - int(round(image_complexity * 32, 0))])

    def run(self, seed, base_model, vae, samples, positive_cond_base, negative_cond_base, model_name, upscale_by=1.0, tiler_denoise=0.25, upscale_method='normal'):
        (img, upscaled_width, upscaled_height) = self.phase_one(base_model, samples, positive_cond_base, negative_cond_base, upscale_by, model_name, seed, vae)
        img = tensor2pil(img)
        tiled_image = run_tiler(img, base_model, vae, seed, positive_cond_base, negative_cond_base, tiler_denoise)
        return (tiled_image,)
```