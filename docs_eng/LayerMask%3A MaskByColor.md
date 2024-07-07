# Documentation
- Class name: MaskByColor
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Create Mask nodes according to colour.

# Input types

## Required

- image
    - Enter the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- color
    - Colour Selector. Click on the color block to select the colour. You can pick up the screen colour using the straw on the colours panel. Note: When using the straws, maximize the browser window.
    - Comfy dtype: COLOR
    - Python dtype: str
    - Default value: #FF

- color_in_HEX
    - Enter the colour value. If you enter this entry, use it first, ignoring the color selected by color.
    - Comfy dtype: STRING
    - Python dtype: str
    - Default value: ""

- threshold
    - The greater the value of the mask range, the greater the mask range.
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

- invert_mask
    - Whether to reverse the mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

## Optional

- mask
    - Mask input. This input is optional. If you have a mask, only the colour within the mask is included in the range.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- mask
    - Output Mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskByColor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", ),
                "color": ("COLOR", {"default": "#FFFFFF"},),
                "color_in_HEX": ("STRING", {"default": ""}),
                "threshold": ("INT", { "default": 0, "min": 0, "max": 100, "step": 1, }),
                "fix_gap": ("INT", {"default": 2, "min": 0, "max": 32, "step": 1}),
                "fix_threshold": ("FLOAT", {"default": 0.75, "min": 0.01, "max": 0.99, "step": 0.01}),
                "invert_mask": ("BOOLEAN", {"default": False}), # Invert mask
            },
            "optional": {
                "mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "mask_by_color"
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_by_color(self, image, color, color_in_HEX, threshold,
                      fix_gap, fix_threshold, invert_mask, mask=None):

        if color_in_HEX != "" and color_in_HEX.startswith('#') and len(color_in_HEX) == 7:
            color = color_in_HEX

        ret_masks = []
        l_images = []
        l_masks = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
            else:
                l_masks.append(Image.new('L', m.size, 'white'))
        if mask is not None:
            if mask.dim() == 2:
                mask = torch.unsqueeze(mask, 0)
            l_masks = []
            for m in mask:
                if invert_mask:
                    m = 1 - m
                l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))

        for i in range(len(l_images)):
            img = l_images[i] if i < len(l_images) else l_images[-1]
            img = tensor2pil(img)
            _mask = l_masks[i] if i < len(l_masks) else l_masks[-1]

            mask = Image.new('L', _mask.size, 'black')
            mask.paste(create_mask_from_color_tensor(img, color, threshold), mask=_mask)
            mask = image2mask(mask)
            if invert_mask:
                mask = 1 - mask
            if fix_gap:
                mask = mask_fix(mask, 1, fix_gap, fix_threshold, fix_threshold)
            ret_masks.append(mask)

        return (torch.cat(ret_masks, dim=0), )
```