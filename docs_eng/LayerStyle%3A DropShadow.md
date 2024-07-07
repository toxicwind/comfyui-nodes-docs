# Documentation
- Class name: DropShadow
- Category: 😺dzNodes/LayerStyle
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generates a shadow.

# Input types
## Required

- background_image
    - Background image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- layer_image
    - The mask of the layer image, the shadow of which is generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- invert_mask
    - Invert mask
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- blend_mode
    - Shade mixed mode.
    - Comfy dtype: STRING
    - Python dtype: str

- opacity
    - Transparency
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
    - The shadows are blurred.
    - Comfy dtype: INT
    - Python dtype: int

- shadow_color
    - The color of the shadow.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- layer_mask
    - A layer of mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Generates the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class DropShadow:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "background_image": ("IMAGE", ),  #
                "layer_image": ("IMAGE",),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # invert mask
                "blend_mode" (chop_mode, # mixed mode)
                "opacity": ("INT", {default": 50, "min" : 0, "max" : 100, "step" ), # Transparency
                "distance_x": ("INT", {default" : 25, "min" :-9999, "max" :9999, "step" ), #x_deverse
                "distance_y": ("INT", "default" : 25, "min" :-9999, "max" :9999, "step" ), # y_ offset
                "grow": ("INT", {default" : 6, "min" :-9999, "max" :9999, "step" ): # Expand
                "blur": ("INT", {default" : 18, "min" : 0, "max" : 100, "step" ): # Fuzzy
                "shadow_color": ("STRING", {"default": "#000000}), # Background colour
            },
            "optional": {
                "layer_mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'drop_shadow'
    CATEGORY = '😺dzNodes/LayerStyle'

    def drop_shadow(self, background_image, layer_image,
                  invert_mask, blend_mode, opacity, distance_x, distance_y,
                  grow, blur, shadow_color,
                  layer_mask=None
                  ):

        b_images = []
        l_images = []
        l_masks = []
        ret_images = []
        for b in background_image:
            b_images.append(torch.unsqueeze(b, 0))
        for l in layer_image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
        if layer_mask is not None:
            if layer_mask.dim() == 2:
                layer_mask = torch.unsqueeze(layer_mask, 0)
            l_masks = []
            for m in layer_mask:
                if invert_mask:
                    m = 1 - m
                l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))
        if len(l_masks) == 0:
            log(f"Error: {NODE_NAME} skipped, because the available mask is not found.", message_type='error')
            return (background_image,)

        max_batch = max(len(b_images), len(l_images), len(l_masks))
        distance_x = -distance_x
        distance_y = -distance_y
        shadow_color = Image.new("RGB", tensor2pil(l_images[0]).size, color=shadow_color)

        for i in range(max_batch):
            background_image = b_images[i] if i < len(b_images) else b_images[-1]
            layer_image = l_images[i] if i < len(l_images) else l_images[-1]
            _mask = l_masks[i] if i < len(l_masks) else l_masks[-1]

            # preprocess
            _canvas = tensor2pil(background_image).convert('RGB')
            _layer = tensor2pil(layer_image)

            if _mask.size != _layer.size:
                _mask = Image.new('L', _layer.size, 'white')
                log(f"Warning: {NODE_NAME} mask mismatch, dropped!", message_type='warning')

            if distance_x != 0 or distance_y != 0:
                _mask = shift_image_mask, list_x, list_y) #
            shadow_mask = expand_mask (image2mask), grow, blur #extension, blurry
            # Synthetic Shadows
            alpha = tensor2pil(shadow_mask).convert('L')
            _shadow = chop_image(_canvas, shadow_color, blend_mode, opacity)
            _canvas.paste(_shadow, mask=alpha)
            # Synthetic player
            _canvas.paste(_layer, mask=_mask)

            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```