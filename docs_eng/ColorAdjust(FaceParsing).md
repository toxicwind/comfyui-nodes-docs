# Documentation
- Class name: ColorAdjust
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The ColorAdjust node is designed to modify the visual features of the image by adjusting the contrast, brightness, saturation, colour phase and gamma values of the image. The node enhances the image's appearance and can be used to correct or stylish visual output for various applications.

# Input types
## Required
- image
    - The image parameter is essential for the ColorAdjust node, as it is the input that will be adjusted for colour. It influences the execution by determining the basic visual content that the node will process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- contrast
    - Contrast parameters allow users to increase or reduce differences between the darkest and brightest elements of the image. It plays an important role in enhancing the visual clarity and depth of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - Brightness adjustments can make the image look brighter or darker, which is controlled by brightness parameters. It is essential to change the overall brightness or darkness of the visual content.
    - Comfy dtype: FLOAT
    - Python dtype: float
- saturation
    - Saturation parameters control the intensity of the colour in the image. It is important for users who want to achieve a lighter or more soft palette.
    - Comfy dtype: FLOAT
    - Python dtype: float
- hue
    - Adjusting the colours changes the colours in the image to different parts of the chromatography. This parameter plays a key role in changing the overall tone of the visual content.
    - Comfy dtype: FLOAT
    - Python dtype: float
- gamma
    - The gamma parameter affects the overall brightness of the image. It is particularly suitable for adjusting the image's perceived brightness in a non-linear manner.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The result parameter represents the output of the ColorAdjust node, i.e., the colour-adjusted modified image. It is important because it reflects the final visual result of the node process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ColorAdjust:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'contrast': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 255, 'step': 0.01, 'round': 0.001, 'display': 'number'}), 'brightness': ('FLOAT', {'default': 1.0, 'min': -255, 'max': 255, 'step': 0.01, 'round': 0.001, 'display': 'number'}), 'saturation': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 255, 'step': 0.01, 'round': 0.001, 'display': 'number'}), 'hue': ('FLOAT', {'default': 0, 'min': -0.5, 'max': 0.5, 'step': 0.001, 'round': 0.001, 'display': 'number'}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 255, 'step': 0.01, 'round': 0.001, 'display': 'number'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, image: Tensor, contrast: float=1, brightness: float=1, saturation: float=1, hue: float=0, gamma: float=1):
        permutedImage = image.permute(0, 3, 1, 2)
        if contrast != 1:
            permutedImage = functional.adjust_contrast(permutedImage, contrast)
        if brightness != 1:
            permutedImage = functional.adjust_brightness(permutedImage, brightness)
        if saturation != 1:
            permutedImage = functional.adjust_saturation(permutedImage, saturation)
        if hue != 0:
            permutedImage = functional.adjust_hue(permutedImage, hue)
        if gamma != 1:
            permutedImage = functional.adjust_gamma(permutedImage, gamma)
        result = permutedImage.permute(0, 2, 3, 1)
        return (result,)
```