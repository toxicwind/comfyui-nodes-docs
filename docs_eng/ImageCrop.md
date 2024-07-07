# Documentation
- Class name: ImageCrop
- Category: image/transform
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageCrop node is designed to operate the image by cropping it to the specified area. It allows the rectangular part of the image defined by the given width, height and coordinates (x,y). The function of the node is critical to the interest area within the focus image, which is critical for tasks such as object detection or image analysis.

# Input types
## Required
- image
    - The image parameter is the input image that the node will process. It is the basis for the node operation, because it is the object of the crop action. The content and format of the image significantly influences the execution of the node and the cropping of the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or numpy.ndarray
- width
    - Width parameters specify the width of the crop area in pixels. It is an important aspect of the node function because it determines the horizontal range of the crop area. The width values directly affect the size of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters define the vertical range of the crop area, in pixels. It plays a key role in node operations, as it determines the size of the output image in a vertical direction. The selection of the height is essential for the final appearance of the crop.
    - Comfy dtype: INT
    - Python dtype: int
- x
    - The x-parameter represents the horizontal starting point of the crop operation in the image. It is vital because it sets the left edge of the crop area. The x-value directly affects the image part selected for the crop.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y parameter determines the vertical starting point of the crop operation. It is important because it sets the top edge of the area to be cropped. The y-value determines the exact part of the image to be included in the final output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_image
    - Cropped image output parameters represent the result of the crop operation. It is an important output because it contains the final image that has been cropped to the specified size. The quality and content of the clipped image are directly related to the input parameters provided to the node.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class ImageCrop:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'crop'
    CATEGORY = 'image/transform'

    def crop(self, image, width, height, x, y):
        x = min(x, image.shape[2] - 1)
        y = min(y, image.shape[1] - 1)
        to_x = width + x
        to_y = height + y
        img = image[:, y:to_y, x:to_x, :]
        return (img,)
```