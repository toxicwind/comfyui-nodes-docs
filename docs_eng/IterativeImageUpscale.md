# Documentation
- Class name: IterativeImageUpscale
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the IterativeImageUpscale node is designed to implement an iterative image magnification. It receives an image and gradually improves its resolution through a series of fine-tuning steps. The node uses potential space models to encode and decode images, apply magnification factors and overlap with the number of steps specified to achieve the required level of detail.

# Input types
## Required
- pixels
    - The 'pixels' parameter indicates an input image that needs to be magnified. This is a key element, because the whole operation revolves around increasing the resolution of the image through iterative processing.
    - Comfy dtype: IMAGE
    - Python dtype: np.ndarray
- upscale_factor
    - The 'upscape_factor' parameter defines the magnification level during the magnification process. It determines how much of the input image will be magnified after processing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The'steps' parameter indicates the number of iterative steps to be performed during the magnification process. More steps usually lead to more smoother and more detailed magnification images.
    - Comfy dtype: INT
    - Python dtype: int
- upscaler
    - The 'upscaler' parameter refers to a magnification method or model that will be applied to increase the resolution of the image. It is an important part of the magnification process.
    - Comfy dtype: UPSCALER
    - Python dtype: Any
- vae
    - The 'vae' parameter is an example of the VAE that is used to encode and decode image data during magnification.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- temp_prefix
    - The 'temp_prefix' parameter is used to specify a temporary prefix for storing intermediate results during the magnification process. You can leave empty to use default behaviour.
    - Comfy dtype: STRING
    - Python dtype: str
- step_mode
    - The'step_mode' parameter determines the method used to scale the image in each step. It can be'simple' for linear scaling, or 'geometric' for index scaling.
    - Comfy dtype: COMBO[simple, geometric]
    - Python dtype: str
- unique_id
    - The 'unique_id'parameter is used internally to track the progress and state of the magnification operation. It is usually hidden from the user and distributed automatically.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- image
    - The 'image'output parameter represents a magnified image obtained through an iterative magnification process. It is the final product of the node function.
    - Comfy dtype: IMAGE
    - Python dtype: np.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class IterativeImageUpscale:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'upscale_factor': ('FLOAT', {'default': 1.5, 'min': 1, 'max': 10000, 'step': 0.1}), 'steps': ('INT', {'default': 3, 'min': 1, 'max': 10000, 'step': 1}), 'temp_prefix': ('STRING', {'default': ''}), 'upscaler': ('UPSCALER',), 'vae': ('VAE',), 'step_mode': (['simple', 'geometric'], {'default': 'simple'})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, pixels, upscale_factor, steps, temp_prefix, upscaler, vae, step_mode='simple', unique_id=None):
        if temp_prefix == '':
            temp_prefix = None
        core.update_node_status(unique_id, 'VAEEncode (first)', 0)
        if upscaler.is_tiled:
            latent = nodes.VAEEncodeTiled().encode(vae, pixels, upscaler.tile_size)[0]
        else:
            latent = nodes.VAEEncode().encode(vae, pixels)[0]
        refined_latent = IterativeLatentUpscale().doit(latent, upscale_factor, steps, temp_prefix, upscaler, step_mode, unique_id)
        core.update_node_status(unique_id, 'VAEDecode (final)', 1.0)
        if upscaler.is_tiled:
            pixels = nodes.VAEDecodeTiled().decode(vae, refined_latent[0], upscaler.tile_size)[0]
        else:
            pixels = nodes.VAEDecode().decode(vae, refined_latent[0])[0]
        core.update_node_status(unique_id, '', None)
        return (pixels,)
```