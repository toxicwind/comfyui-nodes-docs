# Documentation
- Class name: InstructPixToPixConditioning
- Category: conditioning/instructpix2pix
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

InstructPixToPixConditioning is designed to process image data by encoding image data into potential expressions for further manipulation or analysis. It plays a key role in converting raw pixel data into forms that are more conducive to the creation of images.

# Input types
## Required
- positive
    - The positive condition parameter is essential to the operation of the node because it provides a positive example or desired result that guides the coding process. It affects the direction of potential spatial transformation.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- negative
    - The adverse condition parameter, as the opposite of the positive condition, provides an example that should be avoided or minimized during the encoding process. It helps to fine-tune the output of the node to match the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- pixels
    - Pixels parameters are the core input of nodes, representing the original image data that you need to encode. Their quality and format directly influence the accuracy and validity of the coding process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The vae parameter is a key component of the node, which represents the variable coder model used to encode pixel data into potential space. The selection and configuration of the VAE model significantly influences the performance of the node.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Output types
- positive
    - Positive output represents the condition data that is coded on the basis of the positive examples provided. It is a key component of the follow-up image generation or operation process that relies on the positive guidance.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- negative
    - Negative output corresponds to the condition data that are coded on the basis of negative examples. It plays a crucial role in ensuring that images are generated to avoid undesirable features.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- latent
    - Potential output is the encoded expression for entering pixel data. It serves as the basis for further image-processing tasks and captures basic features in simplified form.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class InstructPixToPixConditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'vae': ('VAE',), 'pixels': ('IMAGE',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('positive', 'negative', 'latent')
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/instructpix2pix'

    def encode(self, positive, negative, pixels, vae):
        x = pixels.shape[1] // 8 * 8
        y = pixels.shape[2] // 8 * 8
        if pixels.shape[1] != x or pixels.shape[2] != y:
            x_offset = pixels.shape[1] % 8 // 2
            y_offset = pixels.shape[2] % 8 // 2
            pixels = pixels[:, x_offset:x + x_offset, y_offset:y + y_offset, :]
        concat_latent = vae.encode(pixels)
        out_latent = {}
        out_latent['samples'] = torch.zeros_like(concat_latent)
        out = []
        for conditioning in [positive, negative]:
            c = []
            for t in conditioning:
                d = t[1].copy()
                d['concat_latent_image'] = concat_latent
                n = [t[0], d]
                c.append(n)
            out.append(c)
        return (out[0], out[1], out_latent)
```