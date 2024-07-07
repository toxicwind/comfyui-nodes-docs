# Documentation
- Class name: ImagePadForOutpaintMasked
- Category: image
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The ImagePadForOutpaintMaked node is designed to expand the boundaries of the image, a process called expansive. It does this by adding additional pixels, which are intelligently calculated to fit seamlessly with the original content. The function of the node is particularly useful in contexts that are important beyond the edge of the image, such as image editing or data enhancement tasks.

# Input types
## Required
- image
    - The image parameter is the main input of the node, which means the image that will be expanded. It is essential for the operation of the node, because the entire process is surrounded by the filling of the image. The quality of the final output depends heavily on the content of the original image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- left
    - The left parameter specifies the number of pixels that are filled on the left side of the image. It plays an important role in determining the final size of the extended image and the overall appearance of the extended area.
    - Comfy dtype: INT
    - Python dtype: int
- top
    - The top parameter determines the number of pixels that are filled at the top of the image. It is an important input that controls vertical filling and directly affects the height of the result image.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - The right parameter is set to the number of pixels that are filled on the right side of the image. It is essential to achieve the width required for the extended image and affects the visual consistency of the expansive area.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The bottom parameter determines the number of pixels that are filled at the bottom of the image. It is a key factor in creating the final height of the extended image and influencing the overall appearance of the filled area.
    - Comfy dtype: INT
    - Python dtype: int
- feathering
    - Feathering parameters control the smoothness of the transition between the original image and the filling area. It is particularly important to create a natural and seamless mix and enhances the visual effect of the extended image.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- mask
    - The mask parameter is optional input to define the mask of the image. It is used to specify the image range that should be retained during the image extension to ensure that the area remains unchanged.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- new_image
    - New_image output parameters represent extended images with filled additions. It is the main result of node operations and contains seamless integration of the original image with the newly filled area.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- new_mask
    - The new_mask output parameter is the updated mask that should be used to extend the image. It is important to maintain the integrity of a given area during the extension process and is particularly useful when further image operations are required.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImagePadForOutpaintMasked:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'top': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'right': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'bottom': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'feathering': ('INT', {'default': 40, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1})}, 'optional': {'mask': ('MASK',)}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'expand_image'
    CATEGORY = 'image'

    def expand_image(self, image, left, top, right, bottom, feathering, mask=None):
        (B, H, W, C) = image.size()
        new_image = torch.ones((B, H + top + bottom, W + left + right, C), dtype=torch.float32) * 0.5
        new_image[:, top:top + H, left:left + W, :] = image
        if mask is None:
            new_mask = torch.ones((H + top + bottom, W + left + right), dtype=torch.float32)
            t = torch.zeros((H, W), dtype=torch.float32)
        else:
            mask = F.pad(mask, (left, right, top, bottom), mode='constant', value=0)
            mask = 1 - mask
            t = torch.zeros_like(mask)
        if feathering > 0 and feathering * 2 < H and (feathering * 2 < W):
            for i in range(H):
                for j in range(W):
                    dt = i if top != 0 else H
                    db = H - i if bottom != 0 else H
                    dl = j if left != 0 else W
                    dr = W - j if right != 0 else W
                    d = min(dt, db, dl, dr)
                    if d >= feathering:
                        continue
                    v = (feathering - d) / feathering
                    if mask is None:
                        t[i, j] = v * v
                    else:
                        t[:, top + i, left + j] = v * v
        if mask is None:
            mask = new_mask.squeeze(0)
            mask[top:top + H, left:left + W] = t
            mask = mask.unsqueeze(0)
        return (new_image, mask)
```