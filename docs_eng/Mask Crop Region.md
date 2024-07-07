# Documentation
- Class name: WAS_Mask_Crop_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Crop_Region node is designed to process images by identifying and tailoring areas within the mask. It uses fill and area type parameters to control cropping behaviour and to ensure that the result image segments are seamlessly integrated for applications such as game development or 3D modelling. The node plays a vital role in image pre-processing in order to obtain more tailored and visually consistent results.

# Input types
## Required
- mask
    - The mask parameter is a binary image array that defines the area to be cropped from the original image. It is essential for the operation of the node because it directly affects the selection of the image parts to be cropped.
    - Comfy dtype: np.ndarray
    - Python dtype: numpy.ndarray
## Optional
- padding
    - Fill parameters add a border around the crop area, which helps smooth the edges or retains elements that are important to the context of the image.
    - Comfy dtype: int
    - Python dtype: int
- region_type
    - Region_type parameters determine the crop strategy: is it about the main area within the mask or the secondary area. This affects the final configuration of the crop.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- cropped_mask
    - Cropped_mask output represents the volume of the area in the mask where the result is cropped. It marks the successful isolation of the area in the image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- crop_data
    - The crop_data output provides detailed information on the size and location of the crop area, which is essential for further image processing or analysis.
    - Comfy dtype: Tuple[int, Tuple[int, int, int, int]]
    - Python dtype: Tuple[int, Tuple[int, int, int, int]]
- top_int
    - Top_int output indicates the vertical position of the crop area from the top of the image.
    - Comfy dtype: int
    - Python dtype: int
- left_int
    - Left_int output indicates the horizontal position of the crop area from the left side of the image.
    - Comfy dtype: int
    - Python dtype: int
- right_int
    - The right_int output specifies the horizontal position of the right edge of the crop area in the image.
    - Comfy dtype: int
    - Python dtype: int
- bottom_int
    - Bottom_int output indicates the vertical position of the bottom edge of the crop area in the image.
    - Comfy dtype: int
    - Python dtype: int
- width_int
    - Width_int output provides the width of the crop area, which is important for adjusting the size or positioning of the image segment.
    - Comfy dtype: int
    - Python dtype: int
- height_int
    - The header_int output provides the height of the crop area, which is the key measurement value for maintaining the horizontal ratio or scaling of the image segment.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Crop_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'padding': ('INT', {'default': 24, 'min': 0, 'max': 4096, 'step': 1}), 'region_type': (['dominant', 'minority'],)}}
    RETURN_TYPES = ('MASK', 'CROP_DATA', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('cropped_mask', 'crop_data', 'top_int', 'left_int', 'right_int', 'bottom_int', 'width_int', 'height_int')
    FUNCTION = 'mask_crop_region'
    CATEGORY = 'WAS Suite/Image/Masking'

    def mask_crop_region(self, mask, padding=24, region_type='dominant'):
        mask_pil = Image.fromarray(np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        (region_mask, crop_data) = self.WT.Masking.crop_region(mask_pil, region_type, padding)
        region_tensor = pil2mask(ImageOps.invert(region_mask)).unsqueeze(0).unsqueeze(1)
        ((width, height), (left, top, right, bottom)) = crop_data
        return (region_tensor, crop_data, top, left, right, bottom, width, height)
```