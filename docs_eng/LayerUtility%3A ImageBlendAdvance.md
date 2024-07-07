# Documentation
- Class name: ImageBlendAdvance
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Allows you to synthesize a picture of a layer of different sizes on a background picture and to set the position and changes. A variety of hybrid models are available for selection, and transparency can be set.

Node provides a layer change method and an anti-sawing option. It helps to improve synthetic graphics.

Nodes provide mask output that can be used for follow-up streams.


# Input types
## Required

- background_image
    - Background image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- layer_image
    - Layer images for synthesis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- invert_mask
    - Whether to reverse the mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- blend_mode
    - Layer mix mode.
    - Comfy dtype: ENUM
    - Python dtype: str

- opacity
    - Opacity.
    - Comfy dtype: INT
    - Python dtype: int

- x_percent
    - The horizontal position of the layer on the background map is expressed in percentage terms as zero at the top left and 100 at the top right, which can be less than 0 or more, which means that part of the layer is outside the picture.
    - Comfy dtype: FLOAT
    - Python dtype: float

- y_percent
    - The vertical position of the layer on the background map is expressed as a percentage, with a top 0 and a bottom 100. For example, a 50 for the vertical center, 20 for the upper side and 80 for the lower side.
    - Comfy dtype: FLOAT
    - Python dtype: float

- mirror
    - Mirror flips. Provides two flip modes, flipped horizontally and flipped vertically.
    - Comfy dtype: ENUM
    - Python dtype: str

- scale
    - Layer magnification multiples, 1.0 means original size.
    - Comfy dtype: FLOAT
    - Python dtype: float

- aspect_ratio
    - The width ratio of the layer. 1.0 is the original scale, which is greater than the value, which is larger than the value, which is smaller than the value, which is flattening.
    - Comfy dtype: FLOAT
    - Python dtype: float

- rotate
    - Number of rotation degrees of the layer.
    - Comfy dtype: FLOAT
    - Python dtype: float

- transform_method
    - Sampling methods used to magnify and rotate formations, including lanczos, bicubic, hamming, bilinear, box, and nearest. Different sampling methods affect the composition and image processing time of synthesis.
    - Comfy dtype: ENUM
    - Python dtype: str

- anti_aliasing
    - The greater the value, the less visible it is. The higher the value will significantly reduce the processing speed of the nodes.
    - Comfy dtype: INT
    - Python dtype: int

## Optional

- layer_mask
    - Layer image mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor


# Output types

- image
    - Synthetic images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageBlendAdvance:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        mirror_mode = ['None', 'horizontal', 'vertical']
        method_mode = ['lanczos', 'bicubic', 'hamming', 'bilinear', 'box', 'nearest']
        return {
            "required": {
                "background_image": ("IMAGE", ),  #
                "layer_image": ("IMAGE",),  #
                "invert_mask": ("BOOLEAN", {"default": True}), # invert mask
                "blend_mode" (chop_mode, # mixed mode)
                "opacity": ("INT", {default": 100, "min" : 0, "max" : 100, "step" ), # Transparency
                "x_percent": ("FLOAT", {"default": 50, "min": -999, "max": 999, "step": 0.01}),
                "y_percent": ("FLOAT", {"default": 50, "min": -999, "max": 999, "step": 0.01}),
                "mirror": (mirror_mode, # mirror flipping)
                "scale": ("FLOAT", {"default": 1, "min": 0.01, "max": 100, "step": 0.01}),
                "aspect_ratio": ("FLOAT", {"default": 1, "min": 0.01, "max": 100, "step": 0.01}),
                "rotate": ("FLOAT", {"default": 0, "min": -999999, "max": 999999, "step": 0.01}),
                "transform_method": (method_mode,),
                "anti_aliasing": ("INT", {"default": 0, "min": 0, "max": 16, "step": 1}),
            },
            "optional": {
                "layer_mask": ("MASK",),  #
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = 'image_blend_advance'
    CATEGORY = '😺dzNodes/LayerUtility'

    def image_blend_advance(self, background_image, layer_image,
                            invert_mask, blend_mode, opacity,
                            x_percent, y_percent,
                            mirror, scale, aspect_ratio, rotate,
                            transform_method, anti_aliasing,
                            layer_mask=None
                            ):
        b_images = []
        l_images = []
        l_masks = []
        ret_images = []
        ret_masks = []
        for b in background_image:
            b_images.append(torch.unsqueeze(b, 0))
        for l in layer_image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
            else:
                l_masks.append(Image.new('L', m.size, 'white'))
        if layer_mask is not None:
            if layer_mask.dim() == 2:
                layer_mask = torch.unsqueeze(layer_mask, 0)
            l_masks = []
            for m in layer_mask:
                if invert_mask:
                    m = 1 - m
                l_masks.append(tensor2pil(torch.unsqueeze(m, 0)).convert('L'))

        max_batch = max(len(b_images), len(l_images), len(l_masks))
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

            orig_layer_width = _layer.width
            orig_layer_height = _layer.height
            _mask = _mask.convert("RGB")

            target_layer_width = int(orig_layer_width * scale)
            target_layer_height = int(orig_layer_height * scale * aspect_ratio)

            # mirror
            if mirror == 'horizontal':
                _layer = _layer.transpose(Image.FLIP_LEFT_RIGHT)
                _mask = _mask.transpose(Image.FLIP_LEFT_RIGHT)
            elif mirror == 'vertical':
                _layer = _layer.transpose(Image.FLIP_TOP_BOTTOM)
                _mask = _mask.transpose(Image.FLIP_TOP_BOTTOM)

            # scale
            _layer = _layer.resize((target_layer_width, target_layer_height))
            _mask = _mask.resize((target_layer_width, target_layer_height))
            # rotate
            _layer, _mask, _ = image_rotate_extend_with_alpha(_layer, rotate, _mask, transform_method, anti_aliasing)

            # Handle the position
            x = int(_canvas.width * x_percent / 100 - _layer.width / 2)
            y = int(_canvas.height * y_percent / 100 - _layer.height / 2)

            # composit layer
            _comp = copy.copy(_canvas)
            _compmask = Image.new("RGB", _comp.size, color='black')
            _comp.paste(_layer, (x, y))
            _compmask.paste(_mask, (x, y))
            _compmask = _compmask.convert('L')
            _comp = chop_image(_canvas, _comp, blend_mode, opacity)

            # composition background
            _canvas.paste(_comp, mask=_compmask)

            ret_images.append(pil2tensor(_canvas))
            ret_masks.append(image2mask(_compmask))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0), torch.cat(ret_masks, dim=0),)
```