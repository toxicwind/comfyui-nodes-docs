# Documentation
- Class name: MaskBoxDetect
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Explores the area in which mask is located and outputs its position and size.

# Input types

## Required

- mask
    - Mask image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

- detect
    - The detection method, the Min_bounding_rect is the smallest outer rectangle of large shapes, the max_inscribed_rect is the largest inner rectangle of large shapes, and the mask_area is the active area of mask pixels.
    - Optional value: ['min_buying_rect','max_inscribed_rect','mask_area']
    - Comfy dtype: STRING
    - Python dtype: str

- x_adjust
    - Amend the horizontal deviation after detection.
    - Comfy dtype: INT
    - Python dtype: int

- y_adjust
    - Fixes the vertical deviation after detection.
    - Comfy dtype: INT
    - Python dtype: int

- scale_adjust
    - Amends the scaling deviation after detection.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types

- box_preview
    - A preview of the detection results. Red represents the results detected, and green means the modified output results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- x_percent
    - The x-axis percentage position.
    - Comfy dtype: FLOAT
    - Python dtype: float

- y_percent
    - The y-axis percentage position.
    - Comfy dtype: FLOAT
    - Python dtype: float

- width
    - Box width.
    - Comfy dtype: INT
    - Python dtype: int

- height
    - Box height.
    - Comfy dtype: INT
    - Python dtype: int

- x
    - Top left corner position x coordinate output.
    - Comfy dtype: INT
    - Python dtype: int

- y
    - An output of the top left corner position y coordinates.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```python
class MaskBoxDetect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        detect_mode = ['min_bounding_rect', 'max_inscribed_rect', 'mask_area']
        return {
            "required": {
                "mask": ("MASK", ),
                "Detect": (detect_mode, # detection type: minimum external rectangle/maximum inner rectangle/mass mask area
                "x_adjust": ("INT", {default" :0, "min" :-9999, "max" :9999, "step" ), #xaxalfixes
                "y_adjust": ("INT", {default" :0, "min" :-9999, "max" :9999, "step" ), # y-axis fixation
                "scale_adjust": # Proportional fixation
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE", "FLOAT", "FLOAT", "INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("box_preview", "x_percent", "y_percent", "width", "height", "x", "y",)
    FUNCTION = 'mask_box_detect'
    CATEGORY = '😺dzNodes/LayerMask'

    def mask_box_detect(self, mask, detect, x_adjust, y_adjust, scale_adjust):

        if mask.dim() == 2:
            mask = torch.unsqueeze(mask, 0)

        if mask.shape[0] > 0:
            mask = torch.unsqueeze(mask[0], 0)

        _mask = mask2image(mask).convert('RGB')

        _mask = gaussian_blur(_mask, 20).convert('L')
        x = 0
        y = 0
        width = 0
        height = 0

        if detect == "min_bounding_rect":
            (x, y, width, height) = min_bounding_rect(_mask)
        elif detect == "max_inscribed_rect":
            (x, y, width, height) = max_inscribed_rect(_mask)
        else:
            (x, y, width, height) = mask_area(_mask)
        log(f"{NODE_NAME}: Box detected. x={x},y={y},width={width},height={height}")
        _width = width
        _height = height
        if scale_adjust != 1.0:
            _width = int(width * scale_adjust)
            _height = int(height * scale_adjust)
            x = x - int((_width - width) / 2)
            y = y - int((_height - height) / 2)
        x += x_adjust
        y += y_adjust
        x_percent = (x + _width / 2) / _mask.width * 100
        y_percent = (y + _height / 2) / _mask.height * 100
        preview_image = tensor2pil(mask).convert('RGB')
        preview_image = draw_rect(preview_image, x - x_adjust, y - y_adjust, width, height, line_color="#F00000", line_width=int(preview_image.height / 60))
        preview_image = draw_rect(preview_image, x, y, width, height, line_color="#00F000", line_width=int(preview_image.height / 40))
        log(f"{NODE_NAME} Processed.", message_type='finish')
        return ( pil2tensor(preview_image), round(x_percent, 2), round(y_percent, 2), _width, _height, x, y,)
```