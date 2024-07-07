# Documentation
- Class name: AutoAdjust
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Automatically adjusts the brightness, contrast and white balance of the picture. Provides some manual adjustment options to compensate for the deficiencies of the automatic adjustment.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- strength
    - The strength of the adjustment. The greater the value, the greater the difference from the original figure.
    - Comfy dtype: INT
    - Python dtype: int

- brightness
    - Lightness adjusts manually.
    - Comfy dtype: INT
    - Python dtype: int

- contrast
    - Contrast adjusts manually.
    - Comfy dtype: INT
    - Python dtype: int

- saturation
    - Saturation adjusts manually.
    - Comfy dtype: INT
    - Python dtype: int

- red
    - Red channel manual adjustment.
    - Comfy dtype: INT
    - Python dtype: int

- green
    - Green Channel manual adjustment.
    - Comfy dtype: INT
    - Python dtype: int

- blue
    - Blue Channel manually adjusted.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class AutoAdjust:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "image": ("IMAGE", ),  #
                "strength": ("INT", {"default": 100, "min": 0, "max": 100, "step": 1}),
                "brightness": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "contrast": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "saturation": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "red": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "green": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "blue": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'auto_adjust'
    CATEGORY = '😺dzNodes/LayerColor'


    def auto_adjust(self, image, strength, brightness, contrast, saturation, red, green, blue):

        if brightness < 0:
            brightness_offset = brightness / 100 + 1
        else:
            brightness_offset = brightness / 50 + 1
        if contrast < 0:
            contrast_offset = contrast / 100 + 1
        else:
            contrast_offset = contrast / 50 + 1
        if saturation < 0:
            saturation_offset = saturation / 100 + 1
        else:
            saturation_offset = saturation / 50 + 1

        red_gamma = self.balance_to_gamma(red)
        green_gamma = self.balance_to_gamma(green)
        blue_gamma = self.balance_to_gamma(blue)


        l_images = []
        l_masks = []
        ret_images = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
            else:
                l_masks.append(Image.new('L', m.size, 'white'))

        max_batch = max(len(l_images), len(l_masks))
        for i in range(max_batch):
            _image = l_images[i] if i < len(l_images) else l_images[-1]
            _mask = l_masks[i] if i < len(l_masks) else l_masks[-1]
            orig_image = tensor2pil(_image)
            r, g, b, _  = image_channel_split(orig_image, mode = 'RGB')
            r = normalize_gray(r)
            g = normalize_gray(g)
            b = normalize_gray(b)
            if red:
                r = gamma_trans(r, red_gamma).convert('L')
            if green:
                g = gamma_trans(g, green_gamma).convert('L')
            if blue:
                b = gamma_trans(b, blue_gamma).convert('L')
            ret_image = image_channel_merge((r, g, b), 'RGB')

            if brightness:
                brightness_image = ImageEnhance.Brightness(ret_image)
                ret_image = brightness_image.enhance(factor=brightness_offset)
            if contrast:
                contrast_image = ImageEnhance.Contrast(ret_image)
                ret_image = contrast_image.enhance(factor=contrast_offset)
            if saturation:
                color_image = ImageEnhance.Color(ret_image)
                ret_image = color_image.enhance(factor=saturation_offset)

            ret_image = chop_image_v2(orig_image, ret_image, blend_mode="normal", opacity=strength)
            if orig_image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, orig_image.split()[-1])

            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)

    def balance_to_gamma(self, balance:int) -> float:
        return 0.00005 * balance * balance - 0.01 * balance + 1
```