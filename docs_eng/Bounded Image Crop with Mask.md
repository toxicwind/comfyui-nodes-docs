# Documentation
- Class name: WAS_Bounded_Image_Crop_With_Mask
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `bounded_image_crop_with_mask'aims to crop images according to the boundary intelligence defined by the corresponding mask. It enhances the image by focusing on the area of interest as described by the mask, while applying a fill to ensure that the area under the crop is kept in the horizontal ratio or size required.

# Input types
## Required
- image
    - Enter the image that will be cropped according to the mask. It is the main object of the operation and determines what will be retained after the crop.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, PIL.Image.Image]
- mask
    - Defines the mask of the area of interest in the image. It is essential to identify the boundary of the crop operation and to determine which parts of the image are important.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, PIL.Image.Image]
## Optional
- padding_left
    - To add the fill to the left of the crop image. This parameter is optional and can be adjusted to control the final width of the crop area.
    - Comfy dtype: INT
    - Python dtype: int
- padding_right
    - To be added to the fill on the right side of the crop image. It works with the fill on the left side to ensure that the cropped image meets a specific size.
    - Comfy dtype: INT
    - Python dtype: int
- padding_top
    - The fill to be added to the top of the crop image. This fill helps to maintain the aspect ratio of the crop or achieve the required height.
    - Comfy dtype: INT
    - Python dtype: int
- padding_bottom
    - To add the fill to the bottom of the crop image. It ensures that the cropped image has sufficient space below the area of interest defined by the mask.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_image
    - Crops the image results of the operation, including fills of interested areas and applications defined by mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_bounds
    - Defines the coordinates of the area boundary in the original image.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Bounded_Image_Crop_With_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'image': ('IMAGE',), 'mask': ('MASK',), 'padding_left': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'padding_right': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'padding_top': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'padding_bottom': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE_BOUNDS')
    FUNCTION = 'bounded_image_crop_with_mask'
    CATEGORY = 'WAS Suite/Image/Bound'

    def bounded_image_crop_with_mask(self, image, mask, padding_left, padding_right, padding_top, padding_bottom):
        image = image.unsqueeze(0) if image.dim() == 3 else image
        mask = mask.unsqueeze(0) if mask.dim() == 2 else mask
        mask_len = 1 if len(image) != len(mask) else len(image)
        cropped_images = []
        all_bounds = []
        for i in range(len(image)):
            if mask_len == 1 and i == 0 or mask_len > 0:
                rows = torch.any(mask[i], dim=1)
                cols = torch.any(mask[i], dim=0)
                (rmin, rmax) = torch.where(rows)[0][[0, -1]]
                (cmin, cmax) = torch.where(cols)[0][[0, -1]]
                rmin = max(rmin - padding_top, 0)
                rmax = min(rmax + padding_bottom, mask[i].shape[0] - 1)
                cmin = max(cmin - padding_left, 0)
                cmax = min(cmax + padding_right, mask[i].shape[1] - 1)
            all_bounds.append([rmin, rmax, cmin, cmax])
            cropped_images.append(image[i][rmin:rmax + 1, cmin:cmax + 1, :])
            return (torch.stack(cropped_images), all_bounds)
```