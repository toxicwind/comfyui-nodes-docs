# Documentation
- Class name: SUPIR_encode
- Category: SUPIR
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-SUPIR.git

The SUPIR_encode node is designed to efficiently process and encode images to potential space using the variable-based encoder model. It optimizes the encoding process by adjusting the forward transmission of the model according to the size of the input image and the size of the given tiles, ensuring that the computational efficiency and memory are kept within reasonable limits.

# Input types
## Required
- SUPIR_VAE
    - SUPIR_VAE parameters represent the variable coder model used to encode the image. It is essential for the operation of nodes, as it defines the structure and parameters to be applied in the encoding process.
    - Comfy dtype: SUPIRVAE
    - Python dtype: torch.nn.Module
- image
    - The image parameter is the input data for the SUPIR_encode node. It is vital because it is the object of the encoded process and the quality and size of the image directly influences the ultimate potential expression.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- encoder_dtype
    - The encoder_dtype parameter specifies the type of data to be used for internal encoder calculations. It plays an important role in balancing the performance and accuracy of nodes, affecting the speed and quality of codes.
    - Comfy dtype: STR
    - Python dtype: str
- use_tiled_vae
    - The use_tiled_vae parameters determine whether nodes should be encoded using a block approach. This is useful for processing larger images and may improve memory use and coding efficiency by decomposing them into smaller, more manageable parts.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- encoder_tile_size
    - The encoder_tile_size parameter defines the tile size to be used to enable the coding method. It is important to optimize the coding process, especially for high-resolution images, by controlling the particle size divided by the tiles.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The latent parameter represents the output of the SUPIR_encode node, i.e. an encoded version of the image, in the form of a potential vector. This compression is essential for further analysis or generation tasks in the pipeline.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SUPIR_encode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'SUPIR_VAE': ('SUPIRVAE',), 'image': ('IMAGE',), 'use_tiled_vae': ('BOOLEAN', {'default': True}), 'encoder_tile_size': ('INT', {'default': 512, 'min': 64, 'max': 8192, 'step': 64}), 'encoder_dtype': (['bf16', 'fp32', 'auto'], {'default': 'auto'})}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latent',)
    FUNCTION = 'encode'
    CATEGORY = 'SUPIR'

    def encode(self, SUPIR_VAE, image, encoder_dtype, use_tiled_vae, encoder_tile_size):
        device = mm.get_torch_device()
        mm.unload_all_models()
        if encoder_dtype == 'auto':
            try:
                if mm.should_use_bf16():
                    print('Encoder using bf16')
                    vae_dtype = 'bf16'
                else:
                    print('Encoder using using fp32')
                    vae_dtype = 'fp32'
            except:
                raise AttributeError("ComfyUI version too old, can't autodetect properly. Set your dtypes manually.")
        else:
            vae_dtype = encoder_dtype
            print(f'Encoder using using {vae_dtype}')
        dtype = convert_dtype(vae_dtype)
        image = image.permute(0, 3, 1, 2)
        (B, C, H, W) = image.shape
        downscale_ratio = 32
        (orig_H, orig_W) = (H, W)
        if W % downscale_ratio != 0:
            W = W - W % downscale_ratio
        if H % downscale_ratio != 0:
            H = H - H % downscale_ratio
        if orig_H % downscale_ratio != 0 or orig_W % downscale_ratio != 0:
            image = F.interpolate(image, size=(H, W), mode='bicubic')
        resized_image = image.to(device)
        if use_tiled_vae:
            from .SUPIR.utils.tilevae import VAEHook
            if not hasattr(SUPIR_VAE.encoder, 'original_forward'):
                SUPIR_VAE.encoder.original_forward = SUPIR_VAE.encoder.forward
            SUPIR_VAE.encoder.forward = VAEHook(SUPIR_VAE.encoder, encoder_tile_size, is_decoder=False, fast_decoder=False, fast_encoder=False, color_fix=False, to_gpu=True)
        elif hasattr(SUPIR_VAE.encoder, 'original_forward'):
            SUPIR_VAE.encoder.forward = SUPIR_VAE.encoder.original_forward
        pbar = comfy.utils.ProgressBar(B)
        out = []
        for img in resized_image:
            SUPIR_VAE.to(dtype).to(device)
            autocast_condition = dtype != torch.float32 and (not comfy.model_management.is_device_mps(device))
            with torch.autocast(comfy.model_management.get_autocast_device(device), dtype=dtype) if autocast_condition else nullcontext():
                z = SUPIR_VAE.encode(img.unsqueeze(0))
                z = z * 0.13025
                out.append(z)
                pbar.update(1)
        if len(out[0].shape) == 4:
            samples_out_stacked = torch.cat(out, dim=0)
        else:
            samples_out_stacked = torch.stack(out, dim=0)
        return ({'samples': samples_out_stacked, 'original_size': [orig_H, orig_W]},)
```