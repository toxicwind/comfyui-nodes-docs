# Documentation
- Class name: MaskInvert
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Node for inverse treatment of Mask.

# Input types

## Required

- mask
    - Entered Mask
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- mask
    - Output Mask
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskInvert:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "mask": ("MASK", ),  #
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = 'mask_invert'
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_invert(self,mask):
        l_masks = []
        ret_masks = []

        if mask.dim() == 2:
            mask = torch.unsqueeze(mask, 0)

        for m in mask:
            l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))

        for i in range(len(l_masks)):
            _mask = l_masks[i]
            ret_masks.append(mask_invert(image2mask(_mask)))

        return (torch.cat(ret_masks, dim=0),)
```