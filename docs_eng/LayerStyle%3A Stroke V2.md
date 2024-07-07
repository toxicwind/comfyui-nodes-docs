# Documentation
- Class name: StrokeV2
- Category: 😺dzNodes/LayerStyle
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Generate the side of the picture.

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
    - Comfy dtype: ENUM
    - Python dtype: str

- opacity
    - Transparency.
    - Comfy dtype: INT
    - Python dtype: int

- stroke_grow
    - The margin of expansion/constriction is described as expansion and negative as contraction.
    - Comfy dtype: INT
    - Python dtype: int

- stroke_width
    - Diagram Width
    - Comfy dtype: INT
    - Python dtype: int

- blur
    - Fuzzy.
    - Comfy dtype: INT
    - Python dtype: int

- stroke_color
    - Draw side colours.
    - Comfy dtype: STRING
    - Python dtype: str

## Optional

- layer_mask
    - The mask of the layer image, where the side of the picture is created.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- mask
    - Mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class StrokeV2:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "background_image": ("IMAGE", ),  #
                "layer_image": ("IMAGE",),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # invert mask
                "blend_mode": (chop_mode_v2), # mixed mode
                "opacity": ("INT", {default": 100, "min" : 0, "max" : 100, "step" ), # Transparency
                "stroke_grow": ("INT", {default" 0, "min" :-999, "max" 999, "step" ), # shrink value
                "stoke_width": ("INT", {default" : 8, "min" : 0, "max" : 999, "step" ), #extended value
                "blur": ("INT", {default" : 0, "min" : 0, "max" : 100, "step" ), # fuzzy
                "stroke_color": ("STRING", {"default": #FF000}, #side colour
            },
            "optional": {
                "layer_mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'stroke_v2'
    CATEGORY = '😺dzNodes/LayerStyle'

    def stroke_v2(self, background_image, layer_image,
                  invert_mask, blend_mode, opacity,
                  stroke_grow, stroke_width, blur, stroke_color,
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

        grow_offset = int(stroke_width / 2)
        inner_stroke = stroke_grow - grow_offset
        outer_stroke = inner_stroke + stroke_width
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

            inner_mask = expand_mask(image2mask(_mask), inner_stroke, blur)
            outer_mask = expand_mask(image2mask(_mask), outer_stroke, blur)
            stroke_mask = subtract_mask(outer_mask, inner_mask)
            color_image = Image.new('RGB', size=_layer.size, color=stroke_color)
            blend_image = chop_image_v2(_layer, color_image, blend_mode, opacity)
            _canvas.paste(_layer, mask=_mask)
            _canvas.paste(blend_image, mask=tensor2pil(stroke_mask))

            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```