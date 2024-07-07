# Documentation
- Class name: SD_4XUpscale_Conditioning
- Category: conditioning/upscale_diffusion
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SD_4XUpscale_Conditioning is designed to enhance image quality by applying four-fold magnification changes. It uses the ability of diffusion models to expand images in conditions that provide positive and negative adjustment input to guide the magnification process. This node is particularly suitable for generating high-resolution images from low-resolution input without compromising details.

# Input types
## Required
- images
    - The Images parameter is the input in which the node will be enlarged. It is essential for the operation of the node, because it defines the content to be converted. The quality and resolution of the input image directly influences the output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- positive
    - Enter the reconciliation to guide the magnification process in order to achieve the desired results. It helps nodes focus on enhancing the specific features or aspects of the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - Negative modifier input is used to suppress unwanted features or hypotheses during the magnification process. It plays a vital role in maintaining the integrity of the original image content.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
## Optional
- scale_ratio
    - The scale_ratio parameter determines the degree of magnification applied to the input image. It is an important factor in controlling the final resolution of the output image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_augmentation
    - Noise enhancement is an optional parameter that introduces random noise to the magnification process, which helps to generate more diverse outputs.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- positive
    - A zoom image is being provided to the output in accordance with the enhanced conditions for inputting into the reconciliation.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - Negative output contains conditions that are optimized on the basis of negative-direction reconciliations to inhibit negative-direction reconciliations from entering unwanted features.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- latent
    - The latent output represents the potential space for magnifying the image and can be used for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SD_4XUpscale_Conditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'scale_ratio': ('FLOAT', {'default': 4.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'noise_augmentation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('positive', 'negative', 'latent')
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/upscale_diffusion'

    def encode(self, images, positive, negative, scale_ratio, noise_augmentation):
        width = max(1, round(images.shape[-2] * scale_ratio))
        height = max(1, round(images.shape[-3] * scale_ratio))
        pixels = comfy.utils.common_upscale(images.movedim(-1, 1) * 2.0 - 1.0, width // 4, height // 4, 'bilinear', 'center')
        out_cp = []
        out_cn = []
        for t in positive:
            n = [t[0], t[1].copy()]
            n[1]['concat_image'] = pixels
            n[1]['noise_augmentation'] = noise_augmentation
            out_cp.append(n)
        for t in negative:
            n = [t[0], t[1].copy()]
            n[1]['concat_image'] = pixels
            n[1]['noise_augmentation'] = noise_augmentation
            out_cn.append(n)
        latent = torch.zeros([images.shape[0], 4, height // 4, width // 4])
        return (out_cp, out_cn, {'samples': latent})
```