# Documentation
- Class name: PasteByMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The PasteByMask node is designed to use a mask to determine the position and paste an image to another image. It is intelligently resizes the image to be pasted to suit the size of the mask, with options to maintain the original vertical ratio or to fill the mask area completely. This node plays a key role in the image processing task, providing flexibility and precision in placing and adjusting the image elements when multiple images are required to be incorporated seamlessly.

# Input types
## Required
- image_base
    - A base image of another image will be pasted on it. It is an operating canvas whose properties influence the final combination.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_to_paste
    - The image that will be pasted to the base image. Its visual content and size play a key role in determining the results of the paste operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Determines the mask where the image_to_paste will be placed on the image_base. It serves as a template to control the visibility and location of the pasted image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- resize_behavior
    - Determines how to adjust the size of the image_to_paste to the mask. This is a key parameter that affects the zoom-out ratio of the pasted image.
    - Comfy dtype: COMBO['resize', 'keep_ratio_fill', 'keep_ratio_fit', 'source_size', 'source_size_unmasked']
    - Python dtype: str
## Optional
- mask_mapping_optional
    - An optional parameter, if available, specifies which base image should be pasted. It adds an additional layer of control to the complex operation involving multiple images.
    - Comfy dtype: MASK_MAPPING
    - Python dtype: torch.Tensor

# Output types
- result
    - The final output image is applied to the image_to_paste based on the mask and resize_behavior parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PasteByMask:
    """
    Pastes `image_to_paste` onto `image_base` using `mask` to determine the location. The `resize_behavior` parameter determines how the image to paste is resized to fit the mask. If `mask_mapping_optional` obtained from a 'Separate Mask Components' node is used, it will control which image gets pasted onto which base image.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_base': ('IMAGE',), 'image_to_paste': ('IMAGE',), 'mask': ('IMAGE',), 'resize_behavior': (['resize', 'keep_ratio_fill', 'keep_ratio_fit', 'source_size', 'source_size_unmasked'],)}, 'optional': {'mask_mapping_optional': ('MASK_MAPPING',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'paste'
    CATEGORY = 'Masquerade Nodes'

    def paste(self, image_base, image_to_paste, mask, resize_behavior, mask_mapping_optional=None):
        image_base = tensor2rgba(image_base)
        image_to_paste = tensor2rgba(image_to_paste)
        mask = tensor2mask(mask)
        (B, H, W, C) = image_base.shape
        MB = mask.shape[0]
        PB = image_to_paste.shape[0]
        if mask_mapping_optional is None:
            if B < PB:
                assert PB % B == 0
                image_base = image_base.repeat(PB // B, 1, 1, 1)
            (B, H, W, C) = image_base.shape
            if MB < B:
                assert B % MB == 0
                mask = mask.repeat(B // MB, 1, 1)
            elif B < MB:
                assert MB % B == 0
                image_base = image_base.repeat(MB // B, 1, 1, 1)
            if PB < B:
                assert B % PB == 0
                image_to_paste = image_to_paste.repeat(B // PB, 1, 1, 1)
        mask = torch.nn.functional.interpolate(mask.unsqueeze(1), size=(H, W), mode='nearest')[:, 0, :, :]
        (MB, MH, MW) = mask.shape
        is_empty = ~torch.gt(torch.max(torch.reshape(mask, [MB, MH * MW]), dim=1).values, 0.0)
        mask[is_empty, 0, 0] = 1.0
        boxes = masks_to_boxes(mask)
        mask[is_empty, 0, 0] = 0.0
        min_x = boxes[:, 0]
        min_y = boxes[:, 1]
        max_x = boxes[:, 2]
        max_y = boxes[:, 3]
        mid_x = (min_x + max_x) / 2
        mid_y = (min_y + max_y) / 2
        target_width = max_x - min_x + 1
        target_height = max_y - min_y + 1
        result = image_base.detach().clone()
        for i in range(0, MB):
            if is_empty[i]:
                continue
            else:
                image_index = i
                if mask_mapping_optional is not None:
                    image_index = mask_mapping_optional[i].item()
                source_size = image_to_paste.size()
                (SB, SH, SW, _) = image_to_paste.shape
                width = int(target_width[i].item())
                height = int(target_height[i].item())
                if resize_behavior == 'keep_ratio_fill':
                    target_ratio = width / height
                    actual_ratio = SW / SH
                    if actual_ratio > target_ratio:
                        width = int(height * actual_ratio)
                    elif actual_ratio < target_ratio:
                        height = int(width / actual_ratio)
                elif resize_behavior == 'keep_ratio_fit':
                    target_ratio = width / height
                    actual_ratio = SW / SH
                    if actual_ratio > target_ratio:
                        height = int(width / actual_ratio)
                    elif actual_ratio < target_ratio:
                        width = int(height * actual_ratio)
                elif resize_behavior == 'source_size' or resize_behavior == 'source_size_unmasked':
                    width = SW
                    height = SH
                resized_image = image_to_paste[i].unsqueeze(0)
                if SH != height or SW != width:
                    resized_image = torch.nn.functional.interpolate(resized_image.permute(0, 3, 1, 2), size=(height, width), mode='bicubic').permute(0, 2, 3, 1)
                pasting = torch.ones([H, W, C])
                ymid = float(mid_y[i].item())
                ymin = int(math.floor(ymid - height / 2)) + 1
                ymax = int(math.floor(ymid + height / 2)) + 1
                xmid = float(mid_x[i].item())
                xmin = int(math.floor(xmid - width / 2)) + 1
                xmax = int(math.floor(xmid + width / 2)) + 1
                (_, source_ymax, source_xmax, _) = resized_image.shape
                (source_ymin, source_xmin) = (0, 0)
                if xmin < 0:
                    source_xmin = abs(xmin)
                    xmin = 0
                if ymin < 0:
                    source_ymin = abs(ymin)
                    ymin = 0
                if xmax > W:
                    source_xmax -= xmax - W
                    xmax = W
                if ymax > H:
                    source_ymax -= ymax - H
                    ymax = H
                pasting[ymin:ymax, xmin:xmax, :] = resized_image[0, source_ymin:source_ymax, source_xmin:source_xmax, :]
                pasting[:, :, 3] = 1.0
                pasting_alpha = torch.zeros([H, W])
                pasting_alpha[ymin:ymax, xmin:xmax] = resized_image[0, source_ymin:source_ymax, source_xmin:source_xmax, 3]
                if resize_behavior == 'keep_ratio_fill' or resize_behavior == 'source_size_unmasked':
                    paste_mask = pasting_alpha.unsqueeze(2).repeat(1, 1, 4)
                else:
                    paste_mask = torch.min(pasting_alpha, mask[i]).unsqueeze(2).repeat(1, 1, 4)
                result[image_index] = pasting * paste_mask + result[image_index] * (1.0 - paste_mask)
        return (result,)
```