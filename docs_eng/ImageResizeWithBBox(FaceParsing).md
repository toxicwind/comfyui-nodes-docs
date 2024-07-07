# Documentation
- Class name: ImageResizeWithBBox
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The node is intended to maintain the width and location of the boundary box while resizeing the image to ensure that key elements in the image are scalded appropriately and kept for further processing.

# Input types
## Required
- bbox
    - The boundary box parameter is essential to define the area of interest within the image. It determines the way in which the image is cropped and ensures that important features are centred and maintained during the process of resizing.
    - Comfy dtype: BBOX
    - Python dtype: torch.Tensor
- image
    - The image parameter is the main input to this node, which will be processed according to the specified adjustment size requirements. It is essential to provide visual data that will be converted and analysed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- resized_image
    - The output of the node is an adjusted image that has been adjusted to meet expectations while maintaining the position and width ratio of the boundary box for further analysis or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageResizeWithBBox:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox': ('BBOX', {}), 'image': ('IMAGE', {})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox: Tensor, image: Tensor):
        bbox_int = bbox.int()
        l = bbox_int[0]
        t = bbox_int[1]
        r = bbox_int[2]
        b = bbox_int[3]
        resized_image = functional.resize(image.permute(0, 3, 1, 2), [b - t, r - l]).permute(0, 2, 3, 1)
        return (resized_image,)
```