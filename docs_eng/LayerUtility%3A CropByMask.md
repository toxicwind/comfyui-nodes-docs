# Documentation
- Class name: CropByMask
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Customizes the picture according to mask's scope. This node is used in conjunction with RestoreCropBox and ImageScaleRestore to tailor the local parts of the picture, zoom in and put them back in place.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask_for_crop
    - The mask of the image will automatically be cut according to the mask range.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- invert_mask
    - Whether to reverse mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- detect
    - The detection method, the Min_bounding_rect is the smallest outer rectangle of large shapes, the max_inscribed_rect is the largest inner rectangle of large shapes, and the mask_area is the active area of mask pixels.
    - Comfy dtype: STRING
    - Python dtype: str

- top_reserve
    - Keeps the size of the top of the cut.
    - Comfy dtype: INT
    - Python dtype: int

- bottom_reserve
    - Keeps the size at the bottom of the cut.
    - Comfy dtype: INT
    - Python dtype: int

- left_reserve
    - Adjusts the size of the left side.
    - Comfy dtype: INT
    - Python dtype: int

- right_reserve
    - Adjusts the size of the right side.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- croped_image
    - Cut the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- croped_mask
    - Post-cut mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- crop_box
    - Custom box data, used when RestoreCropBox nodes are restored.
    - Comfy dtype: BOX
    - Python dtype: list

- box_preview
    - A preview of the cut-off position, with red being the detectable range, and green being the scope of the cut-off after the border has been retained.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class CropByMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        detect_mode = ['min_bounding_rect', 'max_inscribed_rect', 'mask_area']
        return {
            "required": {
                "image": ("IMAGE", ),  #
                "mask_for_crop": ("MASK",),
                "invert_mask": ("BOOLEAN", {"default": False}), #invert mask#
                "detect": (detect_mode,),
                "top_reserve": ("INT", {"default": 20, "min": -9999, "max": 9999, "step": 1}),
                "bottom_reserve": ("INT", {"default": 20, "min": -9999, "max": 9999, "step": 1}),
                "left_reserve": ("INT", {"default": 20, "min": -9999, "max": 9999, "step": 1}),
                "right_reserve": ("INT", {"default": 20, "min": -9999, "max": 9999, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK", "BOX", "IMAGE",)
    RETURN_NAMES = ("croped_image", "croped_mask", "crop_box", "box_preview")
    FUNCTION = 'crop_by_mask'
    CATEGORY = '😺dzNodes/LayerUtility'

    def crop_by_mask(self, image, mask_for_crop, invert_mask, detect,
                  top_reserve, bottom_reserve, left_reserve, right_reserve
                  ):

        ret_images = []
        ret_masks = []
        l_images = []
        l_masks = []


        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
        if mask_for_crop.dim() == 2:
            mask_for_crop = torch.unsqueeze(mask_for_crop, 0)
        # Use the first card if there's more mask
        if mask_for_crop.shape[0] > 1:
            log(f"Warning: Multiple mask inputs, using the first.", message_type='warning')
            mask_for_crop = torch.unsqueeze(mask_for_crop[0], 0)
        if invert_mask:
            mask_for_crop = 1 - mask_for_crop
        l_masks.append(tensor2pil(torch.unsqueeze(mask_for_crop, 0)).convert('L'))

        _mask = mask2image(mask_for_crop)
        bluredmask = gaussian_blur(_mask, 20).convert('L')
        x = 0
        y = 0
        width = 0
        height = 0
        if detect == "min_bounding_rect":
            (x, y, width, height) = min_bounding_rect(bluredmask)
        elif detect == "max_inscribed_rect":
            (x, y, width, height) = max_inscribed_rect(bluredmask)
        else:
            (x, y, width, height) = mask_area(_mask)

        width = num_round_to_multiple(width, 8)
        height = num_round_to_multiple(height, 8)
        log(f"{NODE_NAME}: Box detected. x={x},y={y},width={width},height={height}")
        canvas_width, canvas_height = tensor2pil(torch.unsqueeze(image[0], 0)).convert('RGB').size
        x1 = x - left_reserve if x - left_reserve > 0 else 0
        y1 = y - top_reserve if y - top_reserve > 0 else 0
        x2 = x + width + right_reserve if x + width + right_reserve < canvas_width else canvas_width
        y2 = y + height + bottom_reserve if y + height + bottom_reserve < canvas_height else canvas_height
        preview_image = tensor2pil(mask_for_crop).convert('RGB')
        preview_image = draw_rect(preview_image, x, y, width, height, line_color="#F00000", line_width=(width+height)//100)
        preview_image = draw_rect(preview_image, x1, y1, x2 - x1, y2 - y1,
                                  line_color="#00F000", line_width=(width+height)//200)
        crop_box = (x1, y1, x2, y2)
        for i in range(len(l_images)):
            _canvas = tensor2pil(l_images[i]).convert('RGB')
            _mask = l_masks[0]
            ret_images.append(pil2tensor(_canvas.crop(crop_box)))
            ret_masks.append(image2mask(_mask.crop(crop_box)))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), torch.cat(ret_masks, dim=0), list(crop_box), pil2tensor(preview_image),)

```