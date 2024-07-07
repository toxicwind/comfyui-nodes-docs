# Documentation
- Class name: LayeredDiffusionDecodeRGBA
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionDecodeRGBA node is designed to decode RGBA images from given pixel values and contains the alpha channel for transparency.

# Input types
## Required
- samples
    - The “samples” parameter is essential to the decoding process because it contains pixel data and version information necessary for the proper operation of nodes.
    - Comfy dtype: dict
    - Python dtype: Dict[str, torch.Tensor]
- images
    - The “images” parameter is essential for the node to perform its decoding operation to preserve the image data that needs to be processed.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor
- sd_version
    - The " sd_version " parameter specifies the version of the Stable Diffusion model to be used, which affects the decoding process and the quality of the image generated.
    - Comfy dtype: str
    - Python dtype: str
- sub_batch_size
    - The “sub_batch_size” parameter determines the number of images to be processed at each rotation, which affects performance and memory use during decoding.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- image
    - The "image" output represents the RGBA image data decoded, in which the alpha channel represents the transparency of the image.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor
- alpha
    - The "alpha" output is the alpha channel for RGBA images and is essential for rendering transparency effects in the final image.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionDecodeRGBA(LayeredDiffusionDecode):
    """
    Decode alpha channel value from pixel value.
    [B, C=3, H, W] => [B, C=4, H, W]
    Outputs RGBA image.
    """
    RETURN_TYPES = ('IMAGE',)

    def decode(self, samples, images, sd_version: str, sub_batch_size: int):
        (image, mask) = super().decode(samples, images, sd_version, sub_batch_size)
        alpha = 1.0 - mask
        return JoinImageWithAlpha().join_image_with_alpha(image, alpha)
```