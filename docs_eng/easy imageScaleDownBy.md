# Documentation
- Class name: imageScaleDownBy
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is intended to resize the image by scaling down the size of the image, while maintaining the integrity of the visual content and reducing the size of the document in order to process or store it more efficiently.

# Input types
## Required
- images
    - The images entered are the main data to be processed by the nodes. They are essential to the operation of the nodes because they determine the visual expression and quality of the output.
    - Comfy dtype: COMBO[numpy.ndarray]
    - Python dtype: numpy.ndarray
- scale_by
    - This parameter defines the zoom factor for image size. It is very important because it directly affects the final size and width ratio of the adjusted image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- images
    - The output consists of reconfigured images, which are now smaller in size, but which retain important visual elements of the original image and are prepared for further processing or storage.
    - Comfy dtype: COMBO[numpy.ndarray]
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class imageScaleDownBy(imageScaleDown):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'scale_by': ('FLOAT', {'default': 0.5, 'min': 0.01, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'EasyUse/Image'
    FUNCTION = 'image_scale_down_by'

    def image_scale_down_by(self, images, scale_by):
        width = images.shape[2]
        height = images.shape[1]
        new_width = int(width * scale_by)
        new_height = int(height * scale_by)
        return self.image_scale_down(images, new_width, new_height, 'center')
```