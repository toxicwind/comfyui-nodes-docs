# Documentation
- Class name: WAS_Dragon_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Dragon_Filter node is designed to use a range of image-processing techniques to simulate the shape of a stymied dragon. It enhances the visual appeal of the image by adjusting saturation, contrast, sharpness and brightness, while using high-access filters to add texture details. The node can color the final output and provide a rich and visible look for the processed image.

# Input types
## Required
- image
    - Enter the image, which will be processed by the node. It will serve as the basis for all subsequent image operations and enhancements performed by the node.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- saturation
    - The saturation adjustment factor of the image. It controls the strength of the colour inside the image, the higher the saturation, the lower the saturation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - The contrast adjustment factor for the image. It affects the difference between the darkest and brightest areas of the image, creating more or less visible colour ranges.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sharpness
    - The sharpness adjustment factor of the image. It controls the clarity and definition of the edge of the image, and the higher the value produces a sharper image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - The brightness of the image adjusts the factor. It controls the overall brightness or brightness of the image, making it brighter or darker as necessary.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highpass_radius
    - The radius parameters of the high-speed filter. It determines the range of texture details that are retained in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highpass_samples
    - The number of times a high-access filter is applied to the image. You can add texture details by applying multiple filters.
    - Comfy dtype: INT
    - Python dtype: int
- highpass_strength
    - The strength of the filter effect is high. It controls the strength of the texture details in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- colorize
    - A boolean sign determines whether the final image should be colored. When set to true, it uses colour blending to enhance visual appeal.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool

# Output types
- output_image
    - Applying the result image of a dragon filter. It is a styled expression that combines image-processing techniques to create unique and visually attractive results.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dragon_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'saturation': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 16.0, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 16.0, 'step': 0.01}), 'brightness': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 16.0, 'step': 0.01}), 'sharpness': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 6.0, 'step': 0.01}), 'highpass_radius': ('FLOAT', {'default': 6.0, 'min': 0.0, 'max': 255.0, 'step': 0.01}), 'highpass_samples': ('INT', {'default': 1, 'min': 0, 'max': 6.0, 'step': 1}), 'highpass_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 3.0, 'step': 0.01}), 'colorize': (['true', 'false'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_dragan_filter'
    CATEGORY = 'WAS Suite/Image/Filter'

    def apply_dragan_filter(self, image, saturation, contrast, sharpness, brightness, highpass_radius, highpass_samples, highpass_strength, colorize):
        WTools = WAS_Tools_Class()
        tensor_images = []
        for img in image:
            tensor_images.append(pil2tensor(WTools.dragan_filter(tensor2pil(img), saturation, contrast, sharpness, brightness, highpass_radius, highpass_samples, highpass_strength, colorize)))
        tensor_images = torch.cat(tensor_images, dim=0)
        return (tensor_images,)
```