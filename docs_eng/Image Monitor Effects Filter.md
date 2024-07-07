# Documentation
- Class name: WAS_Image_Monitor_Distortion_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Monitor_Distribution_Filter node is designed to apply a variety of false effects to images and simulate different types of monitors or signals. It handles the input image according to the selected mode, which can be 'Disital Disposition', 'Signal Disposition' or 'TV Distribution', and uses parameters such as amplitude and deflection to control the loss of real strength. The node is very multifunctional and applies to a wide range of applications from visual effects to artistic image conversion.

# Input types
## Required
- image
    - Enter the image that is about to undergo a disfigurement process. It serves as the basis for the application of the missing effect of the node, the quality and characteristics of which have a significant impact on the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- mode
    - Determines the type of disabling effect to be applied to the image. Each mode represents a different disabling style that affects the overall look and feeling of the processed image.
    - Comfy dtype: COMBO['Digital Distortion', 'Signal Distortion', 'TV Distortion']
    - Python dtype: str
- amplitude
    - The strength of the control of the error effect. Higher amplitudes lead to more obvious distortions, while lower values produce more subtle effects.
    - Comfy dtype: INT
    - Python dtype: int
- offset
    - Adjust the location of the invalid effect to allow fine-tuning of the defunct appearance. It changes the visual dynamics of the end result by moving the defunct pattern.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output is a processed image that has been applied to a disfigured effect. It reflects the properties of the input image and displays the chosen disfigured style for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Monitor_Distortion_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'mode': (['Digital Distortion', 'Signal Distortion', 'TV Distortion'],), 'amplitude': ('INT', {'default': 5, 'min': 1, 'max': 255, 'step': 1}), 'offset': ('INT', {'default': 10, 'min': 1, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'image_monitor_filters'
    CATEGORY = 'WAS Suite/Image/Filter'

    def image_monitor_filters(self, image, mode='Digital Distortion', amplitude=5, offset=5):
        image = tensor2pil(image)
        WTools = WAS_Tools_Class()
        if mode:
            if mode == 'Digital Distortion':
                image = WTools.digital_distortion(image, amplitude, offset)
            elif mode == 'Signal Distortion':
                image = WTools.signal_distortion(image, amplitude)
            elif mode == 'TV Distortion':
                image = WTools.tv_vhs_distortion(image, amplitude)
            else:
                image = image
        return (pil2tensor(image),)
```