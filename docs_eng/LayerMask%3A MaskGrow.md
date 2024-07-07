# Documentation
- Class name: MaskGrow
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

An expansionary contraction edge and fuzzy treatment of mask

# Input types

## Required

- mask
    - Enter the mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- invert_mask
    - Reverse mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- grow
    - Extensions.
    - Comfy dtype: INT
    - Python dtype: int

- blur
    - Fuzzy amount.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- mask
    - Output mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskGrow:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "mask": ("MASK", ),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # invert mask
                "grow": ("INT", {"default": 4, "min": -999, "max": 999, "step": 1}),
                "blur": ("INT", {"default": 4, "min": 0, "max": 999, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = 'mask_grow'
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_grow(self, mask, invert_mask, grow, blur,):

        l_masks = []
        ret_masks = []

        if mask.dim() == 2:
            mask = torch.unsqueeze(mask, 0)

        for m in mask:
            if invert_mask:
                m = 1 - m
            l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))

        for i in range(len(l_masks)):

            _mask = l_masks[i]
            ret_masks.append(expand_mask(image2mask(_mask), grow, blur) )

        log(f"{NODE_NAME} Processed {len(ret_masks)} mask(s).", message_type='finish')
        return (torch.cat(ret_masks, dim=0),)
```