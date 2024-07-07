# Documentation
- Class name: JoinImageWithAlpha
- Category: mask/compositing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The JoinImageWith Alpha node is designed to integrate alpha masks into images seamlessly, enhancing visual combinations by mixing the two elements. By resizeing the alpha masks to match the size of the images entered, it combines them to produce individual output images with alpha channels, allowing for more sophisticated masking and synthesis techniques.

# Input types
## Required
- image
    - The image parameter is the main input of the node, which represents the basic visual content that will be combined with the alpha mask. It is essential for the operation of the node, as it determines the bottom structure of the final output image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- alpha
    - The alpha parameter defines the mask to be applied to the image. It is essential because it controls the transparency and visibility of different areas in the final synthetic image and allows for precise control of the mixing process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- output_image
    - Output_image is the result of node operations, a combination of images with alpha channels, reflecting the integration of input images and alpha masks. This output is important because it allows further processing or rendering with advanced mask features.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class JoinImageWithAlpha:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'alpha': ('MASK',)}}
    CATEGORY = 'mask/compositing'
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'join_image_with_alpha'

    def join_image_with_alpha(self, image: torch.Tensor, alpha: torch.Tensor):
        batch_size = min(len(image), len(alpha))
        out_images = []
        alpha = 1.0 - resize_mask(alpha, image.shape[1:])
        for i in range(batch_size):
            out_images.append(torch.cat((image[i][:, :, :3], alpha[i].unsqueeze(2)), dim=2))
        result = (torch.stack(out_images),)
        return result
```