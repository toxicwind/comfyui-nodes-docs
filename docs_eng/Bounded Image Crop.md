# Documentation
- Class name: WAS_Bounded_Image_Crop
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Function `bounded_image_crop'is designed to tailor images according to the specified boundary intelligence to ensure that the area is within the effective size of the image. It plays a key role in the pre-processing of the image and does not distort the entire image structure by focusing on the area of interest.

# Input types
## Required
- image
    - The parameter 'image'is the core input of the node, representing the image data to be cut. It is essential for the execution of the node, because it determines the content to be processed. The size and quality of the image directly influences the result of the crop operation.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, PIL.Image.Image]
- image_bounds
    - The parameter 'image_bounds' defines the area in which the image is to be cut. It is essential to specify the exact coordinates of the crop operation. The correctness of these boundaries is crucial because they determine the final appearance of the cropped image.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]

# Output types
- cropped_image
    - The output parameter 'cropped_image 'is the result of the crop operation. It is important because it is a direct output of the node function and contains the result of the input image crop area.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Bounded_Image_Crop:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'image': ('IMAGE',), 'image_bounds': ('IMAGE_BOUNDS',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'bounded_image_crop'
    CATEGORY = 'WAS Suite/Image/Bound'

    def bounded_image_crop(self, image, image_bounds):
        image = image.unsqueeze(0) if image.dim() == 3 else image
        bounds_len = 1 if len(image_bounds) != len(image) else len(image)
        cropped_images = []
        for idx in range(len(image)):
            if bounds_len == 1 and idx == 0 or bounds_len > 1:
                (rmin, rmax, cmin, cmax) = image_bounds[idx]
                if rmin > rmax or cmin > cmax:
                    raise ValueError('Invalid bounds provided. Please make sure the bounds are within the image dimensions.')
            cropped_images.append(image[idx][rmin:rmax + 1, cmin:cmax + 1, :])
        return (torch.stack(cropped_images, dim=0),)
```