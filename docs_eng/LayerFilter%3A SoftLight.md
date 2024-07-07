# Documentation
- Class name: SoftLight
- Category: 😺dzNodes/LayerFilter
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Soft light.

# Input types

## Required

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- soft
    - Fuzzy.
    - Comfy dtype: FLOAT
    - Python dtype: float

- threshold
    - High light threshold.
    - Comfy dtype: INT
    - Python dtype: int

- opacity
    - Transparency.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- image
    - Picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code

```python
class SoftLight:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "Soft": ("FLOAT", {Default" : 1, "min" : 0.2, "max" : 10, "step" : ), # Fuzzy
                "threshold":, # high light threshold
                "opacity": ("INT", {default": 100, "min" : 0, "max" : 100, "step" ), # Transparency
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'soft_light'
    CATEGORY = '😺dzNodes/LayerFilter'

    def soft_light(self, image, soft, threshold, opacity,):

        ret_images = []

        for i in image:
            i = torch.unsqueeze(i, 0)
            blend_mode = 'screen'
            _canvas = tensor2pil(i).convert('RGB')
            blur = int((_canvas.width + _canvas.height) / 200 * soft)
            _otsumask = gray_threshold(_canvas, otsu=True)
            _removebkgd = remove_background(_canvas, _otsumask, '#000000').convert('L')
            auto_threshold = get_image_bright_average(_removebkgd)
            light_mask = gray_threshold(_canvas, auto_threshold + threshold)
            highlight_mask = gray_threshold(_canvas, auto_threshold + (255 - auto_threshold) // 2 + threshold // 2)
            blurimage = gaussian_blur(_canvas, soft).convert('RGB')
            light = chop_image(_canvas, blurimage, blend_mode=blend_mode, opacity=opacity)
            highlight = chop_image(light, blurimage, blend_mode=blend_mode, opacity=opacity)
            _canvas.paste(highlight, mask=gaussian_blur(light_mask, blur * 2).convert('L'))
            _canvas.paste(highlight, mask=gaussian_blur(highlight_mask, blur).convert('L'))

            ret_images.append(pil2tensor(_canvas))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)