# Documentation
- Class name: SUPIR_decode
- Category: SUPIR
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-SUPIR.git

The SUPIR_decode node is designed to convert potential variables into visual data, playing a key role in the creation of the SUPIR system. As an interface between abstract representations of data and tangible results, it can create images from encoded information. The node emphasizes the reconstruction aspects of the SUPIR framework, focusing on the authenticity and quality of generating visual content.

# Input types
## Required
- SUPIR_VAE
    - The SUPIR_VAE parameter represents the change-of-codator model used in the SUPIR framework. It is essential for the decoding process because it contains the information and structure needed to convert potential codes to images. This parameter plays a key role in ensuring the accuracy and consistency of the visual data generated.
    - Comfy dtype: SUPIRVAE
    - Python dtype: torch.nn.Module
- latents
    - The flatts parameter is a set of coding variables that form the basis of the image generation process. It is the key input because it provides the SUPIR_decode node that will be used to rebuild the infrastructure and content of the image. The quality of the flatts directly influences the final output, making it an important component in the process of generation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- use_tiled_vae
    - The use_tiled_vae parameter is a boolean symbol used to determine whether the node should be decoded by a block method. This method can improve the efficiency and management of the decoding process, especially for larger images, by processing smaller parts at once. This is an important option for optimizing the SUPIR_decode node performance.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- decoder_tile_size
    - The decoder_tile_size parameter specifies the size of the tile to be used to activate the fragmentation method. It plays a crucial role in balancing load and memory use, ensuring that the decoding process optimizes the hardware resources available. The appropriate tile size can lead to more efficient and faster image reconstruction.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The image output is the result of the decoding process, and SUPIR_decode node has successfully converted potential variables into visual expressions. This output is a high-resolution image that reflects the input lotts and reflects the generation capacity of the SUPIR system.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SUPIR_decode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'SUPIR_VAE': ('SUPIRVAE',), 'latents': ('LATENT',), 'use_tiled_vae': ('BOOLEAN', {'default': True}), 'decoder_tile_size': ('INT', {'default': 512, 'min': 64, 'max': 8192, 'step': 64})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'decode'
    CATEGORY = 'SUPIR'

    def decode(self, SUPIR_VAE, latents, use_tiled_vae, decoder_tile_size):
        device = mm.get_torch_device()
        mm.unload_all_models()
        samples = latents['samples']
        dtype = SUPIR_VAE.dtype
        (orig_H, orig_W) = latents['original_size']
        (B, H, W, C) = samples.shape
        pbar = comfy.utils.ProgressBar(B)
        SUPIR_VAE.to(device)
        if use_tiled_vae:
            from .SUPIR.utils.tilevae import VAEHook
            if not hasattr(SUPIR_VAE.decoder, 'original_forward'):
                SUPIR_VAE.decoder.original_forward = SUPIR_VAE.decoder.forward
            SUPIR_VAE.decoder.forward = VAEHook(SUPIR_VAE.decoder, decoder_tile_size // 8, is_decoder=True, fast_decoder=False, fast_encoder=False, color_fix=False, to_gpu=True)
        elif hasattr(SUPIR_VAE.decoder, 'original_forward'):
            SUPIR_VAE.decoder.forward = SUPIR_VAE.decoder.original_forward
        out = []
        for sample in samples:
            autocast_condition = dtype != torch.float32 and (not comfy.model_management.is_device_mps(device))
            with torch.autocast(comfy.model_management.get_autocast_device(device), dtype=dtype) if autocast_condition else nullcontext():
                sample = 1.0 / 0.13025 * sample
                decoded_image = SUPIR_VAE.decode(sample.unsqueeze(0)).float()
                out.append(decoded_image)
                pbar.update(1)
        decoded_out = torch.cat(out, dim=0)
        if decoded_out.shape[2] != orig_H or decoded_out.shape[3] != orig_W:
            print('Restoring original dimensions: ', orig_W, 'x', orig_H)
            decoded_out = F.interpolate(decoded_out, size=(orig_H, orig_W), mode='bicubic')
        decoded_out = decoded_out.cpu().to(torch.float32).permute(0, 2, 3, 1)
        decoded_out = torch.clip(decoded_out, 0, 1)
        return (decoded_out,)
```