# Documentation
- Class name: PorterDuffImageComposite
- Category: mask/compositing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

PorterDuffImageComposite is designed to perform image synthesis using the Porter-Duff synthetic operator. It receives source and target images, as well as their respective alpha masks and synthetic models, to generate synthetic images and masks. This node is essential for mixing images in a way that simulates the visual effects of various hybrid models.

# Input types
## Required
- source
    - The source image is the key input in the synthesis process because it represents the main visual content that will mix with the target image. It is essential to determine the final appearance of the synthesis results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- source_alpha
    - The source alpha mask defines the transparency of the source image and plays an important role in the way the source image interacts with the target image during the synthesis process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- destination
    - The target image will be synthesized as the background for the source image. It is an important component for determining the final appearance of the composite image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- destination_alpha
    - The target alpha mask specifies the level of transparency of the target image and affects how the source image is blended with it during synthesis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mode
    - Synthetic mode determines the algorithm to be used for hybrid source and target images. It is a key parameter that determines the visual results of synthetic operations.
    - Comfy dtype: COMBO[PorterDuffMode]
    - Python dtype: PorterDuffMode

# Output types
- composited_image
    - Synthetic images are the result of a mix of source and target images based on the specified synthetic mode. It represents the final visual output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- composited_alpha
    - Synthetic alpha represents the transparency mask generated during the synthesis process. It is used to define the level of transparency of synthetic images.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PorterDuffImageComposite:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'source': ('IMAGE',), 'source_alpha': ('MASK',), 'destination': ('IMAGE',), 'destination_alpha': ('MASK',), 'mode': ([mode.name for mode in PorterDuffMode], {'default': PorterDuffMode.DST.name})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'composite'
    CATEGORY = 'mask/compositing'

    def composite(self, source: torch.Tensor, source_alpha: torch.Tensor, destination: torch.Tensor, destination_alpha: torch.Tensor, mode):
        batch_size = min(len(source), len(source_alpha), len(destination), len(destination_alpha))
        out_images = []
        out_alphas = []
        for i in range(batch_size):
            src_image = source[i]
            dst_image = destination[i]
            assert src_image.shape[2] == dst_image.shape[2]
            src_alpha = source_alpha[i].unsqueeze(2)
            dst_alpha = destination_alpha[i].unsqueeze(2)
            if dst_alpha.shape[:2] != dst_image.shape[:2]:
                upscale_input = dst_alpha.unsqueeze(0).permute(0, 3, 1, 2)
                upscale_output = comfy.utils.common_upscale(upscale_input, dst_image.shape[1], dst_image.shape[0], upscale_method='bicubic', crop='center')
                dst_alpha = upscale_output.permute(0, 2, 3, 1).squeeze(0)
            if src_image.shape != dst_image.shape:
                upscale_input = src_image.unsqueeze(0).permute(0, 3, 1, 2)
                upscale_output = comfy.utils.common_upscale(upscale_input, dst_image.shape[1], dst_image.shape[0], upscale_method='bicubic', crop='center')
                src_image = upscale_output.permute(0, 2, 3, 1).squeeze(0)
            if src_alpha.shape != dst_alpha.shape:
                upscale_input = src_alpha.unsqueeze(0).permute(0, 3, 1, 2)
                upscale_output = comfy.utils.common_upscale(upscale_input, dst_alpha.shape[1], dst_alpha.shape[0], upscale_method='bicubic', crop='center')
                src_alpha = upscale_output.permute(0, 2, 3, 1).squeeze(0)
            (out_image, out_alpha) = porter_duff_composite(src_image, src_alpha, dst_image, dst_alpha, PorterDuffMode[mode])
            out_images.append(out_image)
            out_alphas.append(out_alpha.squeeze(2))
        result = (torch.stack(out_images), torch.stack(out_alphas))
        return result
```