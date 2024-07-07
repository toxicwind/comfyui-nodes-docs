# Documentation
- Class name: ColorCorrect
- Category: postprocessing/Color Adjustments
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The ColorCorrect node is designed to adjust the colour properties of the image, enhance its visual attractiveness and correct colour imbalances. It achieves expectations by adjusting different aspects of temperature, tone, brightness, contrast, saturation and gamma, improving image quality and ensuring consistency between a set of images.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input into the node color correction process. It is the basis for all adjustments and its characteristics directly affect the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- temperature
    - Temperature parameters are used to adjust the color tone of the image and to simulate warmer or colder colour effects. It plays an important role in setting the emotional and overall appearance of the image and helps the visual narrative of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- hue
    - Colour parameters change the colour spectrum of the image, allowing the dominant colour to change without changing brightness or saturation. It affects the overall colour balance of the image and can be used to match desired aesthetics.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - The brightness parameter controls the overall brightness level of the image. By adjusting the parameter, the node corrects the problem of under- or over-exposure and ensures that the details of the image are clearly visible and well balanced.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - The contrast parameter adjusts the difference between the brightest and darkest parts of the image to enhance visual impact and depth. It is essential to make the image more visible and visible.
    - Comfy dtype: FLOAT
    - Python dtype: float
- saturation
    - The saturation parameter enhances or reduces the energy of the colour in the image. It is important to reach the desired colour abundance level and can significantly change the image's mood.
    - Comfy dtype: FLOAT
    - Python dtype: float
- gamma
    - The gamma parameter adjusts the overall colour range of the image to influence the middle tone and shadow rendering. It is essential to achieve natural and visual pleasures in color correction.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output image is the result of a color correction process that reflects all the adjustments made to the input image. It represents the end product and shows an enhanced visual appeal and a corrected colour balance.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ColorCorrect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'temperature': ('FLOAT', {'default': 0, 'min': -100, 'max': 100, 'step': 5}), 'hue': ('FLOAT', {'default': 0, 'min': -90, 'max': 90, 'step': 5}), 'brightness': ('FLOAT', {'default': 0, 'min': -100, 'max': 100, 'step': 5}), 'contrast': ('FLOAT', {'default': 0, 'min': -100, 'max': 100, 'step': 5}), 'saturation': ('FLOAT', {'default': 0, 'min': -100, 'max': 100, 'step': 5}), 'gamma': ('FLOAT', {'default': 1, 'min': 0.2, 'max': 2.2, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'color_correct'
    CATEGORY = 'postprocessing/Color Adjustments'

    def color_correct(self, image: torch.Tensor, temperature: float, hue: float, brightness: float, contrast: float, saturation: float, gamma: float):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros_like(image)
        brightness /= 100
        contrast /= 100
        saturation /= 100
        temperature /= 100
        brightness = 1 + brightness
        contrast = 1 + contrast
        saturation = 1 + saturation
        for b in range(batch_size):
            tensor_image = image[b].numpy()
            modified_image = Image.fromarray((tensor_image * 255).astype(np.uint8))
            modified_image = ImageEnhance.Brightness(modified_image).enhance(brightness)
            modified_image = ImageEnhance.Contrast(modified_image).enhance(contrast)
            modified_image = np.array(modified_image).astype(np.float32)
            if temperature > 0:
                modified_image[:, :, 0] *= 1 + temperature
                modified_image[:, :, 1] *= 1 + temperature * 0.4
            elif temperature < 0:
                modified_image[:, :, 2] *= 1 - temperature
            modified_image = np.clip(modified_image, 0, 255) / 255
            modified_image = np.clip(np.power(modified_image, gamma), 0, 1)
            hls_img = cv2.cvtColor(modified_image, cv2.COLOR_RGB2HLS)
            hls_img[:, :, 2] = np.clip(saturation * hls_img[:, :, 2], 0, 1)
            modified_image = cv2.cvtColor(hls_img, cv2.COLOR_HLS2RGB) * 255
            hsv_img = cv2.cvtColor(modified_image, cv2.COLOR_RGB2HSV)
            hsv_img[:, :, 0] = (hsv_img[:, :, 0] + hue) % 360
            modified_image = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
            modified_image = modified_image.astype(np.uint8)
            modified_image = modified_image / 255
            modified_image = torch.from_numpy(modified_image).unsqueeze(0)
            result[b] = modified_image
        return (result,)
```