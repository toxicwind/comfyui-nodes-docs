# Documentation
- Class name: ReferencePreprocessorNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/Reference/preprocess
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

ReferencePreprocessorNode aims to convert input images to potential spatial expressions using a variable self-encoder (VAE). It plays a key role in preparing images for the operation of the advanced control network by encoding visual content into a format that can be further processed by downstream nodes.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node because it is the original visual input that needs to be preprocessed. It is the primary data that the node will convert to potential expression.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The VAE parameter specifies the node that will be used to encode the image to potential space as a variable-incoder model. This model is the core of the node function because it defines how the image is converted.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE
- latent_size
    - The latent_size parameter defines the dimensions of the potential space that the image will be encoded. It is a key component because it determines the size and structure of the code expression.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]

# Output types
- proc_IMAGE
    - Proc_IMAGE output is an image processed in the form of a potential expression. It is important because it is used as an input to a follow-on node in the control network, allowing for more advanced processing.
    - Comfy dtype: IMAGE
    - Python dtype: comfy.utils.ReferencePreprocWrapper

# Usage tips
- Infra type: GPU

# Source code
```
class ReferencePreprocessorNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'vae': ('VAE',), 'latent_size': ('LATENT',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('proc_IMAGE',)
    FUNCTION = 'preprocess_images'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/Reference/preprocess'

    def preprocess_images(self, vae: VAE, image: Tensor, latent_size: Tensor):
        image = image.movedim(-1, 1)
        image = comfy.utils.common_upscale(image, latent_size['samples'].shape[3] * 8, latent_size['samples'].shape[2] * 8, 'nearest-exact', 'center')
        image = image.movedim(1, -1)
        try:
            image = vae.vae_encode_crop_pixels(image)
        except Exception:
            image = VAEEncode.vae_encode_crop_pixels(image)
        encoded = vae.encode(image[:, :, :, :3])
        return (ReferencePreprocWrapper(condhint=encoded),)
```