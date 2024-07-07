# Documentation
- Class name: PPFNImageAsLatent
- Category: latent/util
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node facilitates the conversion of image data into potential expressions, which is very useful for various image processing tasks. It emphasizes the conversion of visual information into a format for subsequent models or algorithms, with a focus on the adaptability and efficiency of the conversion process.

# Input types
## Required
- images
    - Image parameters are essential because they provide the raw visual data needed to generate potential expressions. It affects the quality and accuracy of potential expressions and determines the validity of nodes in follow-up processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- resampling
    - The re-sampling parameter determines the method used to resize the image during the conversion process. It significantly influences the detail and clarity of the potential expression generated, thus affecting the overall performance of the node.
    - Comfy dtype: COMBO[nearest-exact, bilinear, area, bicubic, bislerp]
    - Python dtype: str

# Output types
- latents
    - Potential output represents the shape of converted image data in potential space, which is essential for further processing or analysis. It covers core visual information in compressed form and is prepared for downstream models or algorithms.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- images
    - Image output retains raw visual data, and an additional channel is now added to ensure compatibility. It serves as a reference for potential expressions and can be used for comparison or further visual analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNImageAsLatent:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'resampling': (['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp'],)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'images')
    FUNCTION = 'image_latent'
    CATEGORY = 'latent/util'

    def image_latent(self, images, resampling):
        if images.shape[-1] != 4:
            ones_channel = torch.ones(images.shape[:-1] + (1,), dtype=images.dtype, device=images.device)
            images = torch.cat((images, ones_channel), dim=-1)
        latents = images.permute(0, 3, 1, 2)
        latents = F.interpolate(latents, size=(images.shape[1] // 8, images.shape[2] // 8), mode=resampling)
        return ({'samples': latents}, images)
```