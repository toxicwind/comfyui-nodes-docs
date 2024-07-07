# Documentation
- Class name: WAS_Image_High_Pass_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_High_Pass_Filter node is designed to enhance the high-frequency detail of the image, effectively removing low-frequency noise or ambiguity. It applies high-access filters to input images, making the details more visible. Node can adjust the intensity and radius to control the intensity and scale of the filtering effect.

# Input types
## Required
- images
    - Input images that are to be processed by high-speed filters. This parameter is essential because it defines node operations to enhance the HF fractions of data.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
## Optional
- radius
    - Radius parameters determine the degree of ambiguity to be removed by the high-access filter. It affects the scale of the details retained in the output image.
    - Comfy dtype: INT
    - Python dtype: int
- strength
    - Strength parameters control the strength of the high-speed filter effect. Higher values will lead to a more visible increase in the high-frequency detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- color_output
    - color_output parameters specify whether the output should be colour (RGB) or greyscale (L). This affects the visual appearance of the filtering image.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: Union[str, Literal['true', 'false']]
- neutral_background
    - The neutral_background parameter determines whether a neutral colour background should be added to the image. This may help if a neutral background sheet is needed to obtain a better visual contrast.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: Union[str, Literal['true', 'false']]

# Output types
- images
    - Contains output parameters for processing images that enhance high-frequency details. These images are filtered out of low-frequency fractions and the details are highlighted.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_High_Pass_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'radius': ('INT', {'default': 10, 'min': 1, 'max': 500, 'step': 1}), 'strength': ('FLOAT', {'default': 1.5, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'color_output': (['true', 'false'],), 'neutral_background': (['true', 'false'],)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'high_pass'
    CATEGORY = 'WAS Suite/Image/Filter'

    def high_pass(self, images, radius=10, strength=1.5, color_output='true', neutral_background='true'):
        batch_tensor = []
        for image in images:
            transformed_image = self.apply_hpf(tensor2pil(image), radius, strength, color_output, neutral_background)
            batch_tensor.append(pil2tensor(transformed_image))
        batch_tensor = torch.cat(batch_tensor, dim=0)
        return (batch_tensor,)

    def apply_hpf(self, img, radius=10, strength=1.5, color_output='true', neutral_background='true'):
        img_arr = np.array(img).astype('float')
        blurred_arr = np.array(img.filter(ImageFilter.GaussianBlur(radius=radius))).astype('float')
        hpf_arr = img_arr - blurred_arr
        hpf_arr = np.clip(hpf_arr * strength, 0, 255).astype('uint8')
        if color_output == 'true':
            high_pass = Image.fromarray(hpf_arr, mode='RGB')
        else:
            grayscale_arr = np.mean(hpf_arr, axis=2).astype('uint8')
            high_pass = Image.fromarray(grayscale_arr, mode='L')
        if neutral_background == 'true':
            neutral_color = (128, 128, 128) if high_pass.mode == 'RGB' else 128
            neutral_bg = Image.new(high_pass.mode, high_pass.size, neutral_color)
            high_pass = ImageChops.screen(neutral_bg, high_pass)
        return high_pass.convert('RGB')
```