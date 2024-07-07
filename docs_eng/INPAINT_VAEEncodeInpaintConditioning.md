# Documentation
- Class name: VAEEncodeInpaintConditioning
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

Use the variable from the encoder (VAE) to encode the input image as a potential sign, especially for the restoration task. This node plays a key role in the generation process, enabling the model to learn more detail in the data by conditioning the code on the positive and negative samples.

# Input types
## Required
- positive
    - Positive samples are essential to guide the coding process towards the desired results. They provide a reference for the model as to what is a “right” or correct state in the context of the restoration mission.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- negative
    - Negative samples contrast with positive samples to help the model distinguish between correct and incorrect expressions. This is essential to improve the understanding of the model and to improve the quality of the restoration results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The VAE model is the core component responsible for encoding the input image into potential space. It is a key input, as it directly affects the quality and accuracy of the coding process.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- pixels
    - The pixel data form the input of the VAE model and are essential to the encoded process. It is through these pixels that model learning represents and recreates visual information.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask parameter is used to identify the area in the image that needs to be repaired. It is a key component that guides the model in the encoding process to focus on the particular area of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- positive
    - The active output represents a potential indication of the conditions of the positive sample and is used for further processing or as a reference for restoration tasks.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- negative
    - Negative output corresponds to the potential expression of the conditions of the negative sample, contrasts with the positive output and helps to distinguish the correct expression.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- latent_inpaint
    - Potential restoration output is a particular type of potential expression, including image samples and noise masks, which are essential to the restoration process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- latent_samples
    - Potential sample output provides a collection of random samples from potential space that can be used to generate new examples or to further analyse the coding capabilities of models.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncodeInpaintConditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'vae': ('VAE',), 'pixels': ('IMAGE',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT', 'LATENT')
    RETURN_NAMES = ('positive', 'negative', 'latent_inpaint', 'latent_samples')
    FUNCTION = 'encode'
    CATEGORY = 'inpaint'

    def encode(self, positive, negative, vae, pixels, mask):
        (positive, negative, latent) = nodes.InpaintModelConditioning().encode(positive, negative, pixels, vae, mask)
        latent_inpaint = dict(samples=positive[0][1]['concat_latent_image'], noise_mask=latent['noise_mask'].round())
        return (positive, negative, latent_inpaint, latent)
```