# Documentation
- Class name: ImageContrast
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The node is designed to enhance the visual attractiveness of the image by adjusting its contrast and brightness. It enhances the contrast of the image to improve the distinction between its luminous elements, thus generating more visible visual output. In addition, it adjusts the brightness to allow changes in the overall brightness or darkness of the image, which are essential for a variety of visual effects or for meeting certain aesthetic requirements.

# Input types
## Required
- IMAGE
    - An image parameter is necessary because it is the main input for node processing. It is a medium for applying its contrast and brightness adjustments, and the quality and resolution of the input directly influences the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- contrast
    - The contrast parameter plays an important role in node operations because it controls the increase in image contrast. By adjusting this parameter, the node can improve the overall visual impact by making the image more visible.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - Brightness parameters are essential for adjusting the overall brightness or darkness of the image. They can be used to create specific emotions or effects that directly affect the image's final appearance.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- IMAGE
    - The output image is the result of node processing, reflecting the adjustments made to the contrast and brightness of the input image. It is the crystallization of the node function and serves as the basis for further image processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class ImageContrast:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',), 'contrast': ('FLOAT', {'default': 1, 'min': 0, 'max': 10, 'step': 0.01}), 'brightness': ('FLOAT', {'default': 1, 'min': 0, 'max': 10, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE, contrast, brightness):
        cimg = conv_tensor_pil(IMAGE)
        (w, h) = cimg.size
        pbar = comfy.utils.ProgressBar(2)
        step = 0
        cnt = ImageEnhance.Contrast(cimg)
        cimg = cnt.enhance(contrast)
        step += 1
        pbar.update_absolute(step, h)
        brt = ImageEnhance.Brightness(cimg)
        cimg = brt.enhance(brightness)
        step += 1
        pbar.update_absolute(step, h)
        return conv_pil_tensor(cimg)
```