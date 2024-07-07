# Documentation
- Class name: RgbSparseCtrlPreprocessor
- Category: Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl/preprocess
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The RgbSparseCtrlPreprocessor node is designed to prepare image data for advanced control network processing involving dilution control mechanisms. It will enter image magnification to match potential size, encode images as potential space, and package code data in pre-processing formats specific to downstream control network applications.

# Input types
## Required
- image
    - The image parameter is essential for the pre-processing stage, as it represents the original input that will be magnified and coded. It is the basic element that affects the output of nodes and the follow-up in the control network.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The vae parameter assigns the VAE model, which will be used to encode the image as a potential expression. This model is essential for the node to convert the input image to a format suitable for the operation of the advanced control network.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE
- latent_size
    - The latent_size parameter defines the dimensions of the potential space that the image will be encoded. It is the key determinant of the quality of node output and the subsequent applicability of the coded data within the framework of the control network.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- proc_IMAGE
    - Proc_IMAGE output is a pre-processing version of the input image, coded as a potential space expression. This output is designed to be compatible with the advanced control network node and is not intended for use in other types of image input.
    - Comfy dtype: IMAGE
    - Python dtype: PreprocSparseRGBWrapper

# Usage tips
- Infra type: GPU

# Source code
```
class RgbSparseCtrlPreprocessor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'vae': ('VAE',), 'latent_size': ('LATENT',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('proc_IMAGE',)
    FUNCTION = 'preprocess_images'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl/preprocess'

    def preprocess_images(self, vae: VAE, image: Tensor, latent_size: Tensor):
        image = image.movedim(-1, 1)
        image = comfy.utils.common_upscale(image, latent_size['samples'].shape[3] * 8, latent_size['samples'].shape[2] * 8, 'nearest-exact', 'center')
        image = image.movedim(1, -1)
        try:
            image = vae.vae_encode_crop_pixels(image)
        except Exception:
            image = VAEEncode.vae_encode_crop_pixels(image)
        encoded = vae.encode(image[:, :, :, :3])
        return (PreprocSparseRGBWrapper(condhint=encoded),)
```