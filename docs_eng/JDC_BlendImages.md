# Documentation
- Class name: BlendImages
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The BlendImages class achieved the seamless integration of two images and created a composite picture of smooth transition between the original elements by adjusting the transparency of one picture and covering it on another.

# Input types
## Required
- IMAGE_A
    - IMAGE_A is the first input image of the foundation of the integration process. Its visual elements play a vital role in determining the foundation of the final combination and overall aesthetics.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- IMAGE_B
    - IMAGE_B is intended to integrate the second input image on the base layer provided by IMAGE_A. It is essential to add depth and complexity to the final picture, helping to enrich the synthetic image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- blend
    - The blend parameter controls the level of transparency when IMAGE_B covers IMAGE_A. The parameter is essential in balancing two pictures and ensuring a pleasant integration of nature and vision.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- IMAGE
    - The output IMAGE represents the end result of the integration process, combining the visual elements of the two imported images into a single, coherent picture. This demonstrates the ability of the node to integrate the different elements into a harmonious whole.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class BlendImages:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE_A': ('IMAGE',), 'IMAGE_B': ('IMAGE',), 'blend': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.001})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE_A, IMAGE_B, blend):
        source_a = conv_tensor_pil(IMAGE_A)
        source_b = conv_tensor_pil(IMAGE_B)
        (aw, ah) = (source_a.width, source_a.height)
        (bw, bh) = (source_b.width, source_b.height)
        img_a = Image.new('RGB', (aw, ah))
        img_a.paste(source_a)
        img_b = Image.new('RGB', (bw, bh))
        img_b.paste(source_b)
        if aw != bw or ah != bh:
            img_b.resize((aw, ah), resample=get_pil_resampler('lanczos'))
        return conv_pil_tensor(Image.blend(img_a, img_b, blend))
```