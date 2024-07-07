# Documentation
- Class name: MikeySamplerTiled
- Category: Mikey/Sampling
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

MikeySamplerTiled is designed to implement a complex sampling process, including the generation and fine-tuning of potential samples, and then to magnify the images and magnify the peace sheet. It uses various models and conditions to produce high-quality, magnified images, which are detailed and consistent.

# Input types
## Required
- base_model
    - The underlying model is essential for the initial sampling process and provides the infrastructure for the image generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_model
    - The fine-tuning model is used to improve the quality of the sample image by applying further fine-tuning steps. It plays a key role in achieving greater detail and clarity in magnifying the image.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- samples
    - Samples represent potential spatial vectors that are used as input to the image generation process. The diversity and quality of these samples directly affect the diversity and accuracy of the images generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - VAE (distributive encoder) is essential for decoding potential samples into pixel space and for converting them into physical images that can be further processed and magnified.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive_cond_base
    - Guidance is being provided for the reconciliation of underlying models during sampling to ensure that the images generated are consistent with the required characteristics and attributes.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- negative_cond_base
    - Negative reconciliations are used to inhibit the generation of certain features or attributes in the image and allow for stricter control over the appearance of the final image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- positive_cond_refiner
    - The fine-tuning of models guides the process of fine-tuning, focusing on enhancing the exaggeration of specific features and details in the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- negative_cond_refiner
    - The negative adjustment of the fine-tuning model helps to contain unwanted elements during the fine-tuning process and preserves the integrity of the required image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- model_name
    - The model name is used to identify specific magnification models used in image magnification processes. It is a key factor in determining scaling techniques and generating image quality.
    - Comfy dtype: folder_paths.get_filename_list('upscale_models')
    - Python dtype: str
## Optional
- seed
    - Seeds provide a degree of replicability for the sampling process, ensuring that the same results can be obtained if the same seed values are used to repeat the process.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_by
    - The magnification factor determines the degree of magnification applied to the original image. It directly affects the resolution and detail of the magnification image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_denoise
    - The noise level is a parameter to control the amount of noise that is applied during the flattening process. It affects the clarity and smoothness of the flattening image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tiler_model
    - A sheeting model is assigned to a sheeting operation. It can be a base model or a fine-tuning model that affects the final appearance of the sheeting image.
    - Comfy dtype: COMBO['base', 'refiner']
    - Python dtype: str

# Output types
- tiled_image
    - Tiled images are the main output of nodes, representing a magnified and peaceful version of the images entered. They demonstrate the ability of nodes to produce detailed and structured final images.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- upscaled_image
    - Magnifying the image is an additional output that provides a non-plain version of the magnifying image. It is very useful for comparison and further processing.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class MikeySamplerTiled:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'refiner_model': ('MODEL',), 'samples': ('LATENT',), 'vae': ('VAE',), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'positive_cond_refiner': ('CONDITIONING',), 'negative_cond_refiner': ('CONDITIONING',), 'model_name': (folder_paths.get_filename_list('upscale_models'),), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1}), 'tiler_denoise': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'tiler_model': (['base', 'refiner'], {'default': 'base'})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE')
    RETURN_NAMES = ('tiled_image', 'upscaled_image')
    FUNCTION = 'run'
    CATEGORY = 'Mikey/Sampling'

    def phase_one(self, base_model, refiner_model, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, upscale_by, model_name, seed, vae):
        image_scaler = ImageScale()
        vaedecoder = VAEDecode()
        uml = UpscaleModelLoader()
        upscale_model = uml.load_model(model_name)[0]
        iuwm = ImageUpscaleWithModel()
        sample1 = common_ksampler(base_model, seed, 30, 6.5, 'dpmpp_3m_sde_gpu', 'exponential', positive_cond_base, negative_cond_base, samples, start_step=0, last_step=14, force_full_denoise=False)[0]
        sample2 = common_ksampler(refiner_model, seed, 32, 3.5, 'dpmpp_3m_sde_gpu', 'exponential', positive_cond_refiner, negative_cond_refiner, sample1, disable_noise=True, start_step=15, force_full_denoise=True)[0]
        pixels = vaedecoder.decode(vae, sample2)[0]
        (org_width, org_height) = (pixels.shape[2], pixels.shape[1])
        img = iuwm.upscale(upscale_model, image=pixels)[0]
        (upscaled_width, upscaled_height) = (int(org_width * upscale_by // 8 * 8), int(org_height * upscale_by // 8 * 8))
        img = image_scaler.upscale(img, 'nearest-exact', upscaled_width, upscaled_height, 'center')[0]
        return (img, upscaled_width, upscaled_height)

    def run(self, seed, base_model, refiner_model, vae, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, model_name, upscale_by=1.0, tiler_denoise=0.25, upscale_method='normal', tiler_model='base'):
        (img, upscaled_width, upscaled_height) = self.phase_one(base_model, refiner_model, samples, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, upscale_by, model_name, seed, vae)
        img = tensor2pil(img)
        if tiler_model == 'base':
            tiled_image = run_tiler(img, base_model, vae, seed, positive_cond_base, negative_cond_base, tiler_denoise)
        else:
            tiled_image = run_tiler(img, refiner_model, vae, seed, positive_cond_refiner, negative_cond_refiner, tiler_denoise)
        return (tiled_image, img)
```