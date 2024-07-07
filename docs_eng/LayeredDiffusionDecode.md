# Documentation
- Class name: LayeredDiffusionDecode
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionDecode class is designed to perform a pixel decoding process to reconstruct images with alpha channels and effectively separate the transparency information from the RGB component. It can process different versions of the diffusion model and integrate with the system to provide seamless image generation experiences.

# Input types
## Required
- samples
    - The “samples” parameter is essential to provide the potential expression required for the decoding process. It serves as the basis for image reconstruction and ensures that the output is consistent with the expected generation model.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- images
    - The “images” parameter is essential because it provides raw pixel data that need to be decoded. These data are the main input for extracting the alpha channel and reconstructing the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- sd_version
    - The " sd_version" parameter indicates a version of a stable diffusion model for decoding processes. It is important because it determines the specific characteristics and capabilities of the model that will be applied to decoding.
    - Comfy dtype: StableDiffusionVersion
    - Python dtype: Enum
- sub_batch_size
    - The “sub_batch_size” parameter defines the number of images processed in each decoding process and optimizes the trade-off between computational efficiency and memory use. It affects the throughput and resource allocation of the decoding process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The "image" output represents the reconstructed RGB image data, which is the main result of the decoding process. It reflects the ability to generate the diffusion models applied.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The "mask" output provides alpha channel information, which is essential for defining transparency in rebuilding images. It is an important component for further image processing and operation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionDecode:
    """
    Decode alpha channel value from pixel value.
    [B, C=3, H, W] => [B, C=4, H, W]
    Outputs RGB image + Alpha mask.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'images': ('IMAGE',), 'sd_version': ([StableDiffusionVersion.SD1x.value, StableDiffusionVersion.SDXL.value], {'default': StableDiffusionVersion.SDXL.value}), 'sub_batch_size': ('INT', {'default': 16, 'min': 1, 'max': 4096, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'decode'
    CATEGORY = 'layer_diffuse'

    def __init__(self) -> None:
        self.vae_transparent_decoder = {}

    def decode(self, samples, images, sd_version: str, sub_batch_size: int):
        """
        sub_batch_size: How many images to decode in a single pass.
        See https://github.com/huchenlei/ComfyUI-layerdiffuse/pull/4 for more
        context.
        """
        sd_version = StableDiffusionVersion(sd_version)
        if sd_version == StableDiffusionVersion.SD1x:
            url = 'https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_sd15_vae_transparent_decoder.safetensors'
            file_name = 'layer_sd15_vae_transparent_decoder.safetensors'
        elif sd_version == StableDiffusionVersion.SDXL:
            url = 'https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/vae_transparent_decoder.safetensors'
            file_name = 'vae_transparent_decoder.safetensors'
        if not self.vae_transparent_decoder.get(sd_version):
            model_path = load_file_from_url(url=url, model_dir=layer_model_root, file_name=file_name)
            self.vae_transparent_decoder[sd_version] = TransparentVAEDecoder(load_torch_file(model_path), device=comfy.model_management.get_torch_device(), dtype=torch.float16 if comfy.model_management.should_use_fp16() else torch.float32)
        pixel = images.movedim(-1, 1)
        (B, C, H, W) = pixel.shape
        assert H % 64 == 0, f'Height({H}) is not multiple of 64.'
        assert W % 64 == 0, f'Height({W}) is not multiple of 64.'
        decoded = []
        for start_idx in range(0, samples['samples'].shape[0], sub_batch_size):
            decoded.append(self.vae_transparent_decoder[sd_version].decode_pixel(pixel[start_idx:start_idx + sub_batch_size], samples['samples'][start_idx:start_idx + sub_batch_size]))
        pixel_with_alpha = torch.cat(decoded, dim=0)
        pixel_with_alpha = pixel_with_alpha.movedim(1, -1)
        image = pixel_with_alpha[..., 1:]
        alpha = pixel_with_alpha[..., 0]
        return (image, alpha)
```