# Documentation
- Class name: WAS_Image_Crop_Square_Location
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Crop_Square_Location node is designed to process images and tailor them to rectangular shapes based on assigned position coordinates. It is intelligently adjusted to ensure that the result image is rectangular, even if the specified area is not fully rectangular. This node is particularly suitable for applications requiring uniform image sizes, such as social media post or data input for machine learning models.

# Input types
## Required
- image
    - The image parameter is the input image that the node will process. It is essential for the operation of the node, because it is the object of the crop operation. The content and size of the image will directly influence the outcome of the cutting process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- x
    - The x parameter specifies the horizontal coordinates from the centre of the crop operation. It plays a key role in determining the location of the area of the crop in the image. If no specific values are provided, the default values are set to ensure that the centre is cropped.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y-parameter defines the vertical coordinates from the centre. Similar to the x-parameter, it is essential for the precise location of the crop in the image. If there is no value specified by the user, the default ensures that the centre is cropped.
    - Comfy dtype: INT
    - Python dtype: int
- size
    - The size parameter determines the square edge length of the crop. It is the key determinant for achieving the desired output size. The node ensures that the crop is as close to this size as possible and does not exceed the image boundary.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_image
    - The cropped image output is the result of the cropping process. It is a rectangular image derived from the input image, centred on the specified location coordinates. This output is important for applications that require standardized image formats.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- crop_data
    - The crop_data output provides metadata about the crop process, including the size of the image and the coordinates of the area where the crop is made. This information may be useful for further image processing or analysis.
    - Comfy dtype: CROP_DATA
    - Python dtype: Tuple[int, Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Crop_Square_Location:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'x': ('INT', {'default': 0, 'max': 24576, 'min': 0, 'step': 1}), 'y': ('INT', {'default': 0, 'max': 24576, 'min': 0, 'step': 1}), 'size': ('INT', {'default': 256, 'max': 4096, 'min': 5, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'CROP_DATA')
    FUNCTION = 'image_crop_location'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_crop_location(self, image, x=256, y=256, size=512):
        image = tensor2pil(image)
        (img_width, img_height) = image.size
        exp_size = size // 2
        left = max(x - exp_size, 0)
        top = max(y - exp_size, 0)
        right = min(x + exp_size, img_width)
        bottom = min(y + exp_size, img_height)
        if right - left < size:
            if right < img_width:
                right = min(right + size - (right - left), img_width)
            elif left > 0:
                left = max(left - (size - (right - left)), 0)
        if bottom - top < size:
            if bottom < img_height:
                bottom = min(bottom + size - (bottom - top), img_height)
            elif top > 0:
                top = max(top - (size - (bottom - top)), 0)
        crop = image.crop((left, top, right, bottom))
        crop_data = (crop.size, (left, top, right, bottom))
        crop = crop.resize((crop.size[0] // 8 * 8, crop.size[1] // 8 * 8))
        return (pil2tensor(crop), crop_data)
```