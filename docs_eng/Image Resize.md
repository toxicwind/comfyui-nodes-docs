# Documentation
- Class name: WAS_Image_Rescale
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Rescale node is designed to convert images by scaling them down to specified factors or adjusting them to specified widths and heights. It provides flexibility to select the scaling mode, whether simply resize or resize with oversampling to improve quality. The node can handle various resampling filters to meet different image quality requirements.

# Input types
## Required
- image
    - Enter the image is the core element of the conversion process. It determines the object of the scaling or resizing operation. The quality and size of the input image directly influences the results of the node execution.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- mode
    - Model parameters determine whether the image will be scaled by factor or adjusted to a specific size. It is essential for setting the type of conversion that the node will perform.
    - Comfy dtype: STRING
    - Python dtype: str
- supersample
    - When the supersample parameter is set to 'true', it allows for a more high-quality process of resizing by scaling the image to a larger size and then adjusting it to the target size.
    - Comfy dtype: STRING
    - Python dtype: str
- resampling
    - Re-sampling parameters select the filter that you want to resize the image. Different filters produce different results in terms of image quality and clarity.
    - Comfy dtype: STRING
    - Python dtype: str
- rescale_factor
    - Rescale_factor defines the zoom factor for the image. It is a multiplier that determines the extent of the image size adjustment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- resize_width
    - Resize_width sets the target width of the adjusted image. When the mode is set to'resize', this is an important parameter that determines the new width of the image.
    - Comfy dtype: INT
    - Python dtype: int
- resize_height
    - Resize_height sets the target height of the adjusted image. It works with resize_width to determine the final size of the image in'resize' mode.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- scaled_image
    - Scaled_image is the output of the node, representing the image converted after application of the scaling or resizing operation. It is important because it reflects the results of the desired function of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Rescale:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'mode': (['rescale', 'resize'],), 'supersample': (['true', 'false'],), 'resampling': (['lanczos', 'nearest', 'bilinear', 'bicubic'],), 'rescale_factor': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 16.0, 'step': 0.01}), 'resize_width': ('INT', {'default': 1024, 'min': 1, 'max': 48000, 'step': 1}), 'resize_height': ('INT', {'default': 1536, 'min': 1, 'max': 48000, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_rescale'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_rescale(self, image, mode='rescale', supersample='true', resampling='lanczos', rescale_factor=2, resize_width=1024, resize_height=1024):
        scaled_images = []
        for img in image:
            scaled_images.append(pil2tensor(self.apply_resize_image(tensor2pil(img), mode, supersample, rescale_factor, resize_width, resize_height, resampling)))
        scaled_images = torch.cat(scaled_images, dim=0)
        return (scaled_images,)

    def apply_resize_image(self, image: Image.Image, mode='scale', supersample='true', factor: int=2, width: int=1024, height: int=1024, resample='bicubic'):
        (current_width, current_height) = image.size
        if mode == 'rescale':
            (new_width, new_height) = (int(current_width * factor), int(current_height * factor))
        else:
            new_width = width if width % 8 == 0 else width + (8 - width % 8)
            new_height = height if height % 8 == 0 else height + (8 - height % 8)
        resample_filters = {'nearest': 0, 'bilinear': 2, 'bicubic': 3, 'lanczos': 1}
        if supersample == 'true':
            image = image.resize((new_width * 8, new_height * 8), resample=Image.Resampling(resample_filters[resample]))
        resized_image = image.resize((new_width, new_height), resample=Image.Resampling(resample_filters[resample]))
        return resized_image
```