# Documentation
- Class name: LayerImageTransform
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

This node is used to change the gamer_image individually, to resize, rotate, change the width ratio and flip mirrors.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- x
    - Coordinates x values.
    - Comfy dtype: INT
    - Python dtype: int

- y
    - coordinates y.
    - Comfy dtype: INT
    - Python dtype: int

- mirror
    - Mirror flips. Provides two flip modes, flipped horizontally and flipped vertically.
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str
    - Options:
        - None
        - horizontal
        - vertical

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
    - Comfy dtype: STRING_ONEOF
    - Python dtype: str
    - Options:
        - lanczos
        - bicubic
        - hamming
        - bilinear
        - box
        - nearest

- anti_aliasing
    - The greater the value, the less visible it is. The higher the value will significantly reduce the processing speed of the nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- image
    - Change the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```python
class LayerImageTransform:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        mirror_mode = ['None', 'horizontal', 'vertical']
        method_mode = ['lanczos', 'bicubic', 'hamming', 'bilinear', 'box', 'nearest']
        return {
            "required": {
                "image": ("IMAGE",),  #
                "x": ("INT", {"default": 0, "min": -99999, "max": 99999, "step": 1}),
                "y": ("INT", {"default": 0, "min": -99999, "max": 99999, "step": 1}),
                "mirror": (mirror_mode, # mirror flipping)
                "scale": ("FLOAT", {"default": 1, "min": 0.01, "max": 100, "step": 0.01}),
                "aspect_ratio": ("FLOAT", {"default": 1, "min": 0.01, "max": 100, "step": 0.01}),
                "rotate": ("FLOAT", {"default": 0, "min": -999999, "max": 999999, "step": 0.01}),
                "transform_method": (method_mode,),
                "anti_aliasing": ("INT", {"default": 2, "min": 0, "max": 16, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'layer_image_transform'
    CATEGORY = '😺dzNodes/LayerUtility'

    def layer_image_transform(self, image, x, y, mirror, scale, aspect_ratio, rotate,
                            transform_method, anti_aliasing,
                  ):

        l_images = []
        l_masks = []
        ret_images = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])

        for i in range(len(l_images)):
            layer_image = l_images[i] if i < len(l_images) else l_images[-1]
            _image = tensor2pil(layer_image).convert('RGB')
            if i < len(l_masks):
                _mask = l_masks[i]
            else:
                _mask = Image.new('L', size=_image.size, color='white')
            _image_canvas = Image.new('RGB', size=_image.size, color='black')
            _mask_canvas = Image.new('L', size=_mask.size, color='black')
            orig_layer_width = _image.width
            orig_layer_height = _image.height
            target_layer_width = int(orig_layer_width * scale)
            target_layer_height = int(orig_layer_height * scale * aspect_ratio)
            # mirror
            if mirror == 'horizontal':
                _image = _image.transpose(Image.FLIP_LEFT_RIGHT)
                _mask = _mask.transpose(Image.FLIP_LEFT_RIGHT)
            elif mirror == 'vertical':
                _image = _image.transpose(Image.FLIP_TOP_BOTTOM)
                _mask = _mask.transpose(Image.FLIP_TOP_BOTTOM)
            # scale
            _image = _image.resize((target_layer_width, target_layer_height))
            _mask = _mask.resize((target_layer_width, target_layer_height))
            # rotate
            _image, _mask, _ = image_rotate_extend_with_alpha(_image, rotate, _mask, transform_method, anti_aliasing)
            # composit layer
            paste_x = (orig_layer_width - _image.width) // 2 + x
            paste_y = (orig_layer_height - _image.height) // 2 + y
            _image_canvas.paste(_image, (paste_x, paste_y))
            _mask_canvas.paste(_mask, (paste_x, paste_y))
            if tensor2pil(layer_image).mode == 'RGBA':
                _image_canvas = RGB2RGBA(_image_canvas, _mask_canvas)

            ret_images.append(pil2tensor(_image_canvas))

        log(f"{NODE_NAME} Processed {len(l_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)
```