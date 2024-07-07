# Documentation
- Class name: OuterGlowV2
- Category: 😺dzNodes/LayerStyle
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

External luminous effect V2.

# Input types

## Required

- background_image
    - Background pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- layer_image
    - Layer pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- invert_mask
    - Invert mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- blend_mode
    - Mixed mode.
    - Comfy dtype: ['screen', 'linear dodge', 'color dodge', 'lighten', 'hard light', 'linear light', 'other mode']
    - Python dtype: str

- opacity
    - Transparency.
    - Comfy dtype: INT
    - Python dtype: int

- brightness
    - Brightness.
    - Comfy dtype: INT
    - Python dtype: int

- glow_range
    - Glory range.
    - Comfy dtype: INT
    - Python dtype: int

- blur
    - Fuzzy.
    - Comfy dtype: INT
    - Python dtype: int

- light_color
    - The center color of the light source.
    - Comfy dtype: STRING
    - Python dtype: str

- glow_color
    - The color of the exterior of the glimmer.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- layer_mask
    - Layer mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class OuterGlowV2:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        modes = copy.copy(BLEND_MODES)
        chop_mode_list = ["screen", "linear dodge(add)", "color dodge", "lighten", "dodge", "hard light", "linear light"]
        for i in chop_mode_list:
            modes.pop(i)
        chop_mode_list.extend(list(modes.keys()))

        return {
            "required": {
                "background_image": ("IMAGE", ),  #
                "layer_image": ("IMAGE",),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # invert mask
                "blend_mode": (chop_mode_list), # mixed mode
                "opacity": ("INT", {default": 100, "min" : 0, "max" : 100, "step" ), # Transparency
                "brightness": ("INT", "default" : 5, "min" : 2, "max" : 20, "step" ), # iterative
                "glow_range": ("INT", {default" :48, "min" :-9999, "max" :9999, "step" ), # expansion
                "blur": ("INT", {default" : 25, "min" : 0, "max" : 9999, "step" ), # Expanding
                "light_color": ( "STRING", {default": #FFBF30}), # light center colour
                "glow_color": ("STRING", {"default": "#FE000000}), # Florious Outer Colors
            },
            "optional": {
                "layer_mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'outer_glow_v2'
    CATEGORY = '😺dzNodes/LayerStyle'

    def outer_glow_v2(self, background_image, layer_image,
                  invert_mask, blend_mode, opacity,
                  brightness, glow_range, blur, light_color, glow_color,
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
        blur_factor = blur / 20.0
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
            grow = glow_range
            for x in range(brightness):
                blur = int(grow * blur_factor)
                _color = step_color(glow_color, light_color, brightness, x)
                glow_mask = expand_mask (image2mask), grow, blur) #extension, blurry
                # Synthetic
                color_image = Image.new("RGB", _layer.size, color=_color)
                alpha = tensor2pil(glow_mask).convert('L')
                _glow = chop_image_v2(_canvas, color_image, blend_mode, int(step_value(1, opacity, brightness, x)))
                _canvas.paste(_glow.convert('RGB'), mask=alpha)
                grow = grow - int(glow_range/brightness)
            # Synthetic player
            _canvas.paste(_layer, mask=_mask)

            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```