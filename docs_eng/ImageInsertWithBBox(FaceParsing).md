# Documentation
- Class name: ImageInsertWithBBox
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The node is designed to insert a picture into the location of a specified border box for another image, which is essential for applications such as human face resolution and object tracking. It addresses the process of resizing, filling and covering to ensure seamless insertion of the source image into the target image, contributing to the overall understanding and analysis of visual content.

# Input types
## Required
- bbox
    - The boundary box parameter is essential to define the area in which the image is inserted. It directly affects the crop and placement of the image in the target, ensuring accurate positioning and integration.
    - Comfy dtype: BBOX
    - Python dtype: torch.Tensor
- image_src
    - The source image is the main visual content that will be inserted into the target image. Its quality and dimensions are essential for the final output, as it determines how the inserted image is integrated with the background.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image
    - Image parameters represent the target image to which the source image will be inserted. The characteristics of the image, such as resolution and colour space, are important for the overall processing and final result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- result
    - Output is the final image after the source image is inserted into the specified boundary box. It represents a successful integration of two visual elements, which is essential for further analysis and visualization tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImageInsertWithBBox:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox': ('BBOX', {}), 'image_src': ('IMAGE', {}), 'image': ('IMAGE', {})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox: Tensor, image_src: Tensor, image: Tensor):
        bbox_int = bbox.int()
        l = bbox_int[0]
        t = bbox_int[1]
        r = bbox_int[2]
        b = bbox_int[3]
        image_permuted = image.permute(0, 3, 1, 2)
        resized = functional.resize(image_permuted, [b - t, r - l])
        (_, h, w, c) = image_src.shape
        padded = functional.pad(resized, [l, t, w - r, h - b])
        src_permuted = image_src.permute(0, 3, 1, 2)
        mask = torch.zeros(src_permuted.shape)
        mask[:, :, t:b, l:r] = 1
        result = torch.where(mask == 0, src_permuted, padded)
        final = result.permute(0, 2, 3, 1)
        return (final,)
```