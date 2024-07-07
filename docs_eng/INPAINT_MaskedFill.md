# Documentation
- Class name: MaskedFill
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

The node implements image restoration by filling the missing or hidden areas of the image with different algorithms and matching them to the surrounding context, so that the filled areas are seamlessly integrated with the original images.

# Input types
## Required
- image
    - The image parameter is necessary because it provides the basic input into the image restoration process. It is the primary data for node operations and is used to achieve the required image restoration effects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask parameter defines the image range that requires image restoration. It serves as a guide for nodes to determine where the image content needs to be filled or modified.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- fill
    - Fill parameters determine the method of image restoration to be used, which has a significant impact on the quality and style of content. It is essential to achieve the desired visual outcomes.
    - Comfy dtype: COMBO[('neutral', 'telea', 'navier-stokes')]
    - Python dtype: str
## Optional
- falloff
    - The decay parameters influence the smoothness of the image restoration transition by controlling erosion and blurring the radius of the operation, thus determining the way in which the filling area is integrated with the original image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output image is the result of an image restoration process in which the masked area is filled with content that matches the surrounding context and provides a seamless and visually consistent final image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MaskedFill:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'mask': ('MASK',), 'fill': (['neutral', 'telea', 'navier-stokes'],), 'falloff': ('INT', {'default': 0, 'min': 0, 'max': 8191, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'inpaint'
    FUNCTION = 'fill'

    def fill(self, image: Tensor, mask: Tensor, fill: str, falloff: int):
        alpha = mask.expand(1, *mask.shape[-2:]).floor()
        falloff = make_odd(falloff)
        if falloff > 0:
            erosion = binary_erosion(alpha, falloff)
            alpha = alpha * gaussian_blur(erosion, falloff)
        if fill == 'neutral':
            image = image.detach().clone()
            m = (1.0 - alpha).squeeze(1)
            for i in range(3):
                image[:, :, :, i] -= 0.5
                image[:, :, :, i] *= m
                image[:, :, :, i] += 0.5
        else:
            import cv2
            method = cv2.INPAINT_TELEA if fill == 'telea' else cv2.INPAINT_NS
            alpha_np = alpha.squeeze(0).cpu().numpy()
            alpha_bc = alpha_np.reshape(*alpha_np.shape, 1)
            for slice in image:
                image_np = slice.cpu().numpy()
                filled_np = cv2.inpaint((255.0 * image_np).astype(np.uint8), (255.0 * alpha_np).astype(np.uint8), 3, method)
                filled_np = filled_np.astype(np.float32) / 255.0
                filled_np = image_np * (1.0 - alpha_bc) + filled_np * alpha_bc
                slice.copy_(torch.from_numpy(filled_np))
        return (image,)
```