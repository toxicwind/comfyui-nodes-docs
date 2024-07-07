# Documentation
- Class name: imageScaleDownToSize
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is intended to resize the image to the specified size, while maintaining the vertical ratio and ensuring that the adjusted image adapts to the size required. Adjusts the zoom factor according to the maximum or minimum dimensions selected, allowing control of how the image is scaled.

# Input types
## Required
- images
    - The images that you enter are the main data to be processed at the node. They are essential to the running of the node, because the whole function revolves around adjusting the images to the desired size.
    - Comfy dtype: COMBO[numpy.ndarray]
    - Python dtype: numpy.ndarray
- size
    - The size parameters determine the target size in which the input image will be scaled. It is the key factor in determining the appearance and size of the output.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- mode
    - Model parameter impact scaling is based on the maximum or minimum dimension of the image. This affects the ultimate width ratio and scaling direction.
    - Comfy dtype: boolean
    - Python dtype: bool

# Output types
- output_image
    - The output image is the result of node processing in which the input image has been resized according to the specified parameters. It represents the actual operation of the node function.
    - Comfy dtype: numpy.ndarray
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class imageScaleDownToSize(imageScaleDownBy):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'size': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'max', 'label_off': 'min'})}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'EasyUse/Image'
    FUNCTION = 'image_scale_down_to_size'

    def image_scale_down_to_size(self, images, size, mode):
        width = images.shape[2]
        height = images.shape[1]
        if mode:
            scale_by = size / max(width, height)
        else:
            scale_by = size / min(width, height)
        scale_by = min(scale_by, 1.0)
        return self.image_scale_down_by(images, scale_by)
```