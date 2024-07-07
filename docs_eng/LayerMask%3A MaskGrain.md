# Documentation
- Class name: MaskGrain
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Add noise to the mask.

# Input types

## Required

- mask
    - Mask
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- grain
    - Noise intensity.
    - Comfy dtype: INT
    - Python dtype: int

- invert_mask
    - Invert Mask
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types

- mask
    - Mask
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskGrain:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "mask": ("MASK", ),  #
                "grain": ("INT", {"default": 6, "min": 0, "max": 127, "step": 1}),
                "invert_mask": ("BOOLEAN", {"default": False}), # Invert mask
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = 'mask_grain'
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_grain(self, mask, grain, invert_mask):

        l_masks = []
        ret_masks = []

        if mask.dim() == 2:
            mask = torch.unsqueeze(mask, 0)
        for m in mask:
            if invert_mask:
                m = 1 - m
            l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))

        for mask in l_masks:
            if grain:
                white_mask = Image.new('L', mask.size, color="white")
                inner_mask = tensor2pil(expand_mask(image2mask(mask), 0 - grain, int(grain))).convert('L')
                outter_mask = tensor2pil(expand_mask(image2mask(mask), grain, int(grain * 2))).convert('L')
                ret_mask = Image.new('L', mask.size, color="black")
                ret_mask = chop_image_v2(ret_mask, outter_mask, blend_mode="dissolve", opacity=50).convert('L')
                ret_mask.paste(white_mask, mask=inner_mask)
                ret_masks.append(image2mask(ret_mask))
            else:
                ret_masks.append(image2mask(mask))

        log(f"{NODE_NAME} Processed {len(ret_masks)} mask(s).", message_type='finish')
        return (torch.cat(ret_masks, dim=0),)
```