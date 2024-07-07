# Documentation
- Class name: ColorCorrectShadowAndHighlight
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Adjusts the colour of the image dark and bright.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- shadow_brightness
    - Darkness adjusts to brightness.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 1, "min": 0.0, "max": 3, "step": 0.01}

- shadow_saturation
    - Darkness saturation adjustment value.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 1, "min": 0.0, "max": 3, "step": 0.01}

- shadow_hue
    - Dark colour adjustment value.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -255, "max": 255, "step": 1}

- shadow_level_offset
    - The offset of the dark taker value, with a larger value that allows more areas close to brightness to be included in the dark.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -99, "max": 99, "step": 1}

- shadow_range
    - The extent of the darkness.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 0.25, "min": 0.01, "max": 0.99, "step": 0.01}

- highlight_brightness
    - Brightness adjusts to the brightness of the brightness.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 1, "min": 0.0, "max": 3, "step": 0.01}

- highlight_saturation
    - The saturation adjustment value of the bright spot.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 1, "min": 0.0, "max": 3, "step": 0.01}

- highlight_hue
    - The colour of the bright spot adjusts the value.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -255, "max": 255, "step": 1}

- highlight_level_offset
    - The deflection of brightness extraction values, with larger values, allowing more areas close to the dark to be added to the brightness.
    - Comfy dtype: INT
    - Python dtype: int
    - Options: {"default": 0, "min": -99, "max": 99, "step": 1}

- highlight_range
    - The range of brightness.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Options: {"default": 0.25, "min": 0.01, "max": 0.99, "step": 0.01}

## Optional

- mask
    - Enter the mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorCorrectShadowAndHighlight:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),
                "shadow_brightness": ("FLOAT", {"default": 1, "min": 0.0, "max": 3, "step": 0.01}),
                "shadow_saturation": ("FLOAT", {"default": 1, "min": 0.0, "max": 3, "step": 0.01}),
                "shadow_hue": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "shadow_level_offset": ("INT", {"default": 0, "min": -99, "max": 99, "step": 1}),
                "shadow_range": ("FLOAT", {"default": 0.25, "min": 0.01, "max": 0.99, "step": 0.01}),
                "highlight_brightness": ("FLOAT", {"default": 1, "min": 0.0, "max": 3, "step": 0.01}),
                "highlight_saturation": ("FLOAT", {"default": 1, "min": 0.0, "max": 3, "step": 0.01}),
                "highlight_hue": ("INT", {"default": 0, "min": -255, "max": 255, "step": 1}),
                "highlight_level_offset": ("INT", {"default": 0, "min": -99, "max": 99, "step": 1}),
                "highlight_range": ("FLOAT", {"default": 0.25, "min": 0.01, "max": 0.99, "step": 0.01}),
            },
            "optional": {
                "mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'color_shadow_and_highlight'
    CATEGORY = '😺dzNodes/LayerColor'

    def color_shadow_and_highlight(self, image,
                               shadow_brightness, shadow_saturation,
                               shadow_level_offset, shadow_range, shadow_hue,
                               highlight_brightness, highlight_saturation, highlight_hue,
                               highlight_level_offset, highlight_range,
                               mask=None
                               ):

        ret_images = []
        input_images = []
        input_masks = []

        for i in image:
            input_images.append(torch.unsqueeze(i, 0))
            m = tensor2pil(i)
            if m.mode == 'RGBA':
                input_masks.append(m.split()[-1])
            else:
                input_masks.append(Image.new('L', size=m.size, color='white'))
        if mask is not None:
            if mask.dim() == 2:
                mask = torch.unsqueeze(mask, 0)
            input_masks = []
            for m in mask:
                input_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))
        max_batch = max(len(input_images), len(input_masks))

        for i in range(max_batch):
            _image = input_images[i] if i < len(input_images) else input_images[-1]
            _image = tensor2pil(_image).convert('RGB')
            _mask = input_masks[i] if i < len(input_masks) else input_masks[-1]

            avg_gray = get_gray_average(_image, _mask)
            shadow_level, highlight_level = calculate_shadow_highlight_level(avg_gray)
            _canvas = _image.copy()
            if shadow_saturation !=1 or shadow_brightness !=1 or shadow_hue:
                shadow_low_threshold = (shadow_level + shadow_level_offset) / 100 + shadow_range / 2
                shadow_low_threshold = norm_value(shadow_low_threshold)
                shadow_high_threshold = (shadow_level + shadow_level_offset) / 100 - shadow_range / 2
                shadow_high_threshold = norm_value(shadow_high_threshold)
                _shadow_mask = luminance_keyer(_image, shadow_low_threshold, shadow_high_threshold)
                _shadow = _image.copy()
                if shadow_brightness != 1:
                    brightness_image = ImageEnhance.Brightness(_shadow)
                    _shadow = brightness_image.enhance(factor=shadow_brightness)
                if shadow_saturation != 1:
                    color_image = ImageEnhance.Color(_shadow)
                    _shadow = color_image.enhance(factor=shadow_saturation)
                if shadow_hue:
                    _h, _s, _v = _shadow.convert('HSV').split()
                    _h = image_hue_offset(_h, shadow_hue)
                    _shadow = image_channel_merge((_h, _s, _v), 'HSV')
                _canvas.paste(_shadow, mask=gaussian_blur(_shadow_mask,(_shadow_mask.width + _shadow_mask.height)//800))
                _canvas.paste(_image, mask=ImageChops.invert(_mask))
            if highlight_saturation != 1 or highlight_brightness != 1 or highlight_hue:
                highlight_low_threshold = (highlight_level + highlight_level_offset) / 100 - highlight_range / 2
                highlight_low_threshold = norm_value(highlight_low_threshold)
                highlight_high_threshold = (highlight_level + highlight_level_offset) / 100 + highlight_range / 2
                highlight_high_threshold = norm_value(highlight_high_threshold)
                _highlight_mask = luminance_keyer(_image, highlight_low_threshold, highlight_high_threshold)
                _highlight = _image.copy()
                if highlight_brightness != 1:
                    brightness_image = ImageEnhance.Brightness(_highlight)
                    _highlight = brightness_image.enhance(factor=highlight_brightness)
                if highlight_saturation != 1:
                    color_image = ImageEnhance.Color(_highlight)
                    _highlight = color_image.enhance(factor=highlight_saturation)
                if highlight_hue:
                    _h, _s, _v = _highlight.convert('HSV').split()
                    _h = image_hue_offset(_h, highlight_hue)
                    _highlight = image_channel_merge((_h, _s, _v), 'HSV')
                _canvas.paste(_highlight, mask=gaussian_blur(_highlight_mask, (_highlight_mask.width + _highlight_mask.height)//800))
                _canvas.paste(_image, mask=ImageChops.invert(_mask))
            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```