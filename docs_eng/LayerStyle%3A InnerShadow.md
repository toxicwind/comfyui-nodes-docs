# Documentation
- Class name: InnerShadow
- Category: 😺dzNodes/LayerStyle
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates an internal shadow effect.

# Input types

## Required

- background_image1
    - Background image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- layer_image1
    - Layer images for synthesis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- invert_mask
    - Whether to reverse the mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- blend_mode3
    - Shade mixed mode.
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str
    - Options:
        - screen
        - add
        - lighter
        - normal
        - multply
        - subtract
        - difference
        - darker
        - color_burn
        - color_dodge
        - linear_burn
        - linear_dodge
        - overlay
        - soft_light
        - hard_light
        - vivid_light
        - pin_light
        - linear_light
        - hard_mix

- opacity
    - The shadow of opacity.
    - Comfy dtype: INT
    - Python dtype: int

- distance_x
    - The horizontal shift of the shadow.
    - Comfy dtype: INT
    - Python dtype: int

- distance_y
    - The vertical deflection of the shadow.
    - Comfy dtype: INT
    - Python dtype: int

- grow
    - The shadow expands.
    - Comfy dtype: INT
    - Python dtype: int

- blur
    - The extent of the shadow blurring.
    - Comfy dtype: INT
    - Python dtype: int

- shadow_color4
    - Shadow colour.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- layer_mask1,2
    - The mask of the layer image, the shadow of which is generated.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Finally processed pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class InnerShadow:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        chop_mode = [
            'screen', 'add', 'lighter', 'normal', 'multply', 'subtract', 'difference',
            'darker', 'color_burn', 'color_dodge', 'linear_burn', 'linear_dodge', 'overlay',
            'soft_light', 'hard_light', 'vivid_light', 'pin_light', 'linear_light', 'hard_mix'
        ]

        return {
            "required": {
                "background_image1": ("IMAGE", ),  #
                "layer_image1": ("IMAGE",),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # Whether to reverse mask
                "blend_mode3" (chop_mode, #shaded mix mode)
                "opacity": # ("INT" {"default" : 50, "min" : 0, "max" : 100, "step" ):
                "distance_x": ("INT", {default" : 5, "min" :-9999, "max" :9999, "step" ), # the horizontal deviation of the shadow
                "distance_y": # ("INT" {default" : 5, "min" :-9999, "max" :9999, "step" ):
                "grow": # ("INT" {"default" : 2, "min" :-9999, "max" :9999, "step" ):
                "blur": ("INT", {default" 15, "min" : 0, "max" : 100, "step" ), # shadow level of blurry
                "shadow_color4": ("STRING", {"default": "#000000}), #shad colour
            },
            "optional": {
                "layer_mask1,2": ("MASK",),  #
            }
        }


    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'inner_shadow'
    CATEGORY = '😺dzNodes/LayerStyle'

    def inner_shadow(self, background_image1, layer_image1,
                     invert_mask, blend_mode3, opacity, distance_x, distance_y,
                     grow, blur, shadow_color4,
                     layer_mask1=None, layer_mask2=None
                     ):

        b_images = []
        l_images = []
        l_masks = []
        ret_images = []
        for b in background_image1:
            b_images.append(torch.unsqueeze(b, 0))
        for l in layer_image1:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
        if layer_mask1 is not None or layer_mask2 is not None:
            masks = [layer_mask1, layer_mask2]
            l_masks = []
            for m in masks:
                if m is not None:
                    if m.dim() == 2:
                        m = torch.unsqueeze(m, 0)
                    if invert_mask:
                        m = 1 - m
                    l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))
        if len(l_masks) == 0:
            log(f"Error: {NODE_NAME} skipped, because the available mask is not found.", message_type='error')
            return (background_image1,)
        max_batch = max(len(b_images), len(l_images), len(l_masks))
        distance_x = -distance_x
        distance_y = -distance_y
        shadow_color = Image.new("RGB", tensor2pil(l_images[0]).size, color=shadow_color4)
        for i in range(max_batch):
            background_image = b_images[i] if i < len(b_images) else b_images[-1]
            layer_image = l_images[i] if i < len(l_images) else l_images[-1]
            _mask = l_masks[i] if i < len(l_masks) else l_masks[-1]
            # preprocess
            _canvas = tensor2pil(background_image).convert('RGB')
            _layer = tensor2pil(layer_image).convert('RGB')
            if _mask.size != _layer.size:
                _mask = Image.new('L', _layer.size, 'white')
                log(f"Warning: {NODE_NAME} mask mismatch, dropped!", message_type='warning')

            if distance_x != 0 or distance_y != 0:
                _mask = shift_image_mask, list_x, list_y) #
            shadow_mask = expand_mask (image2mask), grow, blur #extension, blurry
            # Synthetic Shadows
            alpha = tensor2pil(shadow_mask).convert('L')
            _shadow = chop_image(_layer, shadow_color, blend_mode3, opacity)
            _layer.paste(_shadow, mask=ImageChops.invert(alpha))
            # Synthetic player
            _canvas.paste(_layer, mask=_mask)

            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```