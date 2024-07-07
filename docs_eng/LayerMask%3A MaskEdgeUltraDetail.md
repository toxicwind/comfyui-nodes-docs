# Documentation
- Class name: MaskEdgeUltraDetail
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

This node combines the functions of the Spacepxl [ComfyUI-Image-Filters] (https://github.com/spacepxl/ComfyUI-Image-Filters) of Alpha Matte and Guided Filter Alpha, thanking the original author.

# Input types

## Required

- image
    - Enter the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Enter the mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- method
    - Provides both PyMatting and OpenCV-GuidedFilter approaches to the edges. PyMatting processes slowly, but for video, it is recommended that this method be used to obtain a smoother mask sequence.
    - Comfy dtype: LIST
    - Python dtype: str

- mask_grow
    - Mask expansion. Positive value is outward expansion, negative value is internal contraction. For rougher masks, negative values are usually used to shrink their edges to achieve better results.
    - Comfy dtype: INT
    - Python dtype: int

- fix_gap
    - Fixes the gap in the mask. If there is a more visible gap in the mask, the value is adjusted higher.
    - Comfy dtype: INT
    - Python dtype: int

- fix_threshold
    - The threshold to repair the mask.
    - Comfy dtype: FLOAT
    - Python dtype: float

- detail_range
    - Edge Details Range.
    - Comfy dtype: INT
    - Python dtype: int

- black_point
    - Marginal black sampling threshold value.
    - Comfy dtype: FLOAT
    - Python dtype: float

- white_point
    - Marginal black sampling threshold value.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types

- image
    - Output images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Output mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskEdgeUltraDetail:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        method_list = ['PyMatting', 'OpenCV-GuidedFilter']
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "method": (method_list,),
                "mask_grow": ("INT", {"default": 0, "min": -999, "max": 999, "step": 1}),
                "fix_gap": ("INT", {"default": 0, "min": 0, "max": 32, "step": 1}),
                "fix_threshold": ("FLOAT", {"default": 0.75, "min": 0.01, "max": 0.99, "step": 0.01}),
                "detail_range": ("INT", {"default": 12, "min": 1, "max": 256, "step": 1}),
                "black_point": ("FLOAT", {"default": 0.01, "min": 0.01, "max": 0.98, "step": 0.01}),
                "white_point": ("FLOAT", {"default": 0.99, "min": 0.02, "max": 0.99, "step": 0.01}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK", )
    RETURN_NAMES = ("image", "mask", )
    FUNCTION = "mask_edge_ultra_detail"
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_edge_ultra_detail(self, image, mask, method, mask_grow, fix_gap, fix_threshold,
                               detail_range, black_point, white_point,):
        ret_images = []
        ret_masks = []
        l_images = []
        l_masks = []
        if mask.dim() == 2:
            mask = torch.unsqueeze(mask, 0)
        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
        for m in mask:
            l_masks.append(torch.unsqueeze(m, 0))
        if len(l_images) != len(l_masks) or tensor2pil(l_images[0]).size != tensor2pil(l_masks[0]).size:
            log(f"Error: {NODE_NAME} skipped, because mask does'nt match image.", message_type='error')
            return (image, mask,)

        for i in range(len(l_images)):
            _image = l_images[i]
            orig_image = tensor2pil(_image).convert('RGB')
            _image = pil2tensor(orig_image)
            _mask = l_masks[i]
            if mask_grow != 0:
                _mask = expand_mask(_mask, mask_grow, mask_grow//2)
            if fix_gap:
                _mask = mask_fix(_mask, 1, fix_gap, fix_threshold, fix_threshold)
            if method == 'OpenCV-GuidedFilter':
                _mask = guided_filter_alpha(_image, _mask, detail_range)
                _mask = tensor2pil(histogram_remap(_mask, black_point, white_point))
            else:
                _mask = tensor2pil(mask_edge_detail(_image, _mask, detail_range, black_point, white_point))

            ret_image = RGB2RGBA(orig_image, _mask.convert('L'))
            ret_images.append(pil2tensor(ret_image))
            ret_masks.append(image2mask(_mask))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), torch.cat(ret_masks, dim=0),)
```