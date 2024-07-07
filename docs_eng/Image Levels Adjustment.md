# Documentation
- Class name: WAS_Image_Levels
- Category: WAS Suite/Image/Adjustment
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The node is designed to adjust the colour range of the image by adjusting the black, medium and white levels of the image, thereby increasing the overall contrast and visual appeal of the image.

# Input types
## Required
- image
    - An image parameter is essential for processing and adjusting visual content at nodes. It is used as an input and its tone level is modified according to the specified black, medium and white levels.
    - Comfy dtype: COMBO[Image]
    - Python dtype: PIL.Image
- black_level
    - The black-level parameter is essential for setting the darkest point in the image, which affects the overall contrast and tone range. It helps to define the shadow and the deepest black in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mid_level
    - Medium-level parameters play a key role in determining the midpoint of the colour range, affecting the overall balance and distribution of colours in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- white_level
    - White-level parameters are important for defining the brightest points in the image, and they contribute to the brightest and brightest whites.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output image is the result of an adjustment to the hue, showing enhanced contrasts and fine visual details through the manipulation of black, medium and white levels.
    - Comfy dtype: COMBO[Image]
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Levels:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'black_level': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'mid_level': ('FLOAT', {'default': 127.5, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'white_level': ('FLOAT', {'default': 255, 'min': 0.0, 'max': 255.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_image_levels'
    CATEGORY = 'WAS Suite/Image/Adjustment'

    def apply_image_levels(self, image, black_level, mid_level, white_level):
        tensor_images = []
        for img in image:
            img = tensor2pil(img)
            levels = self.AdjustLevels(black_level, mid_level, white_level)
            tensor_images.append(pil2tensor(levels.adjust(img)))
        tensor_images = torch.cat(tensor_images, dim=0)
        return (tensor_images,)

    class AdjustLevels:

        def __init__(self, min_level, mid_level, max_level):
            self.min_level = min_level
            self.mid_level = mid_level
            self.max_level = max_level

        def adjust(self, im):
            im_arr = np.array(im)
            im_arr[im_arr < self.min_level] = self.min_level
            im_arr = (im_arr - self.min_level) * (255 / (self.max_level - self.min_level))
            im_arr[im_arr < 0] = 0
            im_arr[im_arr > 255] = 255
            im_arr = im_arr.astype(np.uint8)
            im = Image.fromarray(im_arr)
            im = ImageOps.autocontrast(im, cutoff=self.max_level)
            return im
```