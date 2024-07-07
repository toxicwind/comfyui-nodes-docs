# Documentation
- Class name: WAS_Image_Crop_Location
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `image_crop_location'is designed to refine the image accurately according to the specified coordinates. It allows the rectangular area of the image to be selected by defining the top, left, right and bottom boundaries. This method is important for the interest areas within the focus image and may enhance the follow-up image processing tasks by focusing on the relevant visual content.

# Input types
## Required
- image
    - Enter the image as the main data object for node operations. It is essential for node functions, as the entire operation revolves around the operation of this image. The image parameters directly influence the execution of nodes and the resulting cropping of images.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- top
    - The parameter 'top'specifies the vertical starting point for the crop operation. It is important because it determines the upper boundary of the crop area. This parameter is used in conjunction with 'bottom' and defines the height of the crop.
    - Comfy dtype: INT
    - Python dtype: int
- left
    - Parameter 'Left' sets the horizontal starting point for the crop. It is important because it establishes the left boundary of the area to be cropped. Together with 'right', it helps to determine the width of the final crop.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - Parameter 'right' defines the horizontal endpoint of the crop. It is essential to determine the width of the crop by calculating the difference between 'right'and 'left'. It ensures that the correct width is maintained in the image after the crop.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The parameter 'bottom' indicates the vertical end point of the crop. It is vital because it sets the lower boundary of the crop. Together with 'top', it determines the vertical range of the crop area.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_image
    - Output 'cropped_image' is the result of the crop operation. It represents the area within the specified boundary in the input image. This output is important because it is the main output of the node function and provides a focus view of the image content.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- crop_data
    - The output 'crop_data' provides metadata about the crop operation, including the size of the crop and the coordinates of the crop area. This information is valuable for understanding the specifics of the crop and can be used for further processing or analysis.
    - Comfy dtype: CROP_DATA
    - Python dtype: Tuple[int, Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Crop_Location:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'top': ('INT', {'default': 0, 'max': 10000000, 'min': 0, 'step': 1}), 'left': ('INT', {'default': 0, 'max': 10000000, 'min': 0, 'step': 1}), 'right': ('INT', {'default': 256, 'max': 10000000, 'min': 0, 'step': 1}), 'bottom': ('INT', {'default': 256, 'max': 10000000, 'min': 0, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'CROP_DATA')
    FUNCTION = 'image_crop_location'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_crop_location(self, image, top=0, left=0, right=256, bottom=256):
        image = tensor2pil(image)
        (img_width, img_height) = image.size
        crop_top = max(top, 0)
        crop_left = max(left, 0)
        crop_bottom = min(bottom, img_height)
        crop_right = min(right, img_width)
        crop_width = crop_right - crop_left
        crop_height = crop_bottom - crop_top
        if crop_width <= 0 or crop_height <= 0:
            raise ValueError('Invalid crop dimensions. Please check the values for top, left, right, and bottom.')
        crop = image.crop((crop_left, crop_top, crop_right, crop_bottom))
        crop_data = (crop.size, (crop_left, crop_top, crop_right, crop_bottom))
        crop = crop.resize((crop.size[0] // 8 * 8, crop.size[1] // 8 * 8))
        return (pil2tensor(crop), crop_data)
```