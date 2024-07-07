# Documentation
- Class name: ImageCropWithBBox
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The ImageCropWithBox node is designed to process images according to border frame coordinates and to edit areas of interest. It plays a key role in concentrating computational resources in specific areas of the image, thereby increasing the efficiency of subsequent image analysis missions.

# Input types
## Required
- bbox
    - The `bbox' parameter is essential because it defines the area in which the image is to be cropped. It directly influences the operation of the node by specifying the coordinates of the cropping process.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
- image
    - The `image' parameter is the basic input for the ImageCropWithBbox node, as it represents the original image data to be processed. The quality and format of the image data are essential for the accuracy of the crop operation.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor

# Output types
- cropped_image
    - The `cropped_image' output contains the results of the crop operation. It is important because it shows the area of the original image specified by the `bbox' parameter for further analysis or processing.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageCropWithBBox:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox': ('BBOX', {}), 'image': ('IMAGE', {})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox: Tensor, image: Tensor):
        results = []
        image_permuted = image.permute(0, 3, 1, 2)
        for image_item in image_permuted:
            bbox_int = bbox.int()
            l = bbox_int[0]
            t = bbox_int[1]
            r = bbox_int[2]
            b = bbox_int[3]
            cropped_image = functional.crop(image_item, t, l, b - t, r - l)
            result = cropped_image.permute(1, 2, 0).unsqueeze(0)
            results.append(result)
        try:
            final = torch.cat(results, dim=0)
        except:
            final = results
        return (final,)
```