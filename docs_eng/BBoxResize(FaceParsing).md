# Documentation
- Class name: BBoxResize
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The BBoxResize node is designed to adjust the size of the boundary box (BBOX) to the new image size. It performs a zoom operation to ensure that the boundary frame coordinates are proportionately resized without changing their relative position in the image. This node is essential for maintaining the integrity of the object detection at different image resolution.

# Input types
## Required
- bbox
    - The parameter 'bbox' means the border frame coordinates that need to be resized. It is essential for the operation of the node because it determines the initial position and size of the object in the image.
    - Comfy dtype: BBOX
    - Python dtype: torch.Tensor
- width_old
    - The parameter 'width_old' specifies the original image width relative to the boundary frame coordinates. It is necessary to calculate the correct zoom factor for the new dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- height_old
    - The parameter 'height_old' defines the original height of the image. It plays a key role in the resizeing process, ensuring that the vertical ratio of the boundary frame is maintained.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The parameter 'width' represents the new width of the adjusted image. It is the key input for the coordinates of the adjusted boundary box.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The parameter 'height'represents the new height after the image is resized. It is essential to maintain the vertical ratio of the boundary box during the resizeing process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- BBOX
    - Output 'BBOX' is the border frame coordinates of the adjusted size, which has been adjusted to fit the new image size. It is important because it provides the updated position and size of the object in the adjusted image.
    - Comfy dtype: BBOX
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BBoxResize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox': ('BBOX', {}), 'width_old': ('INT', {}), 'height_old': ('INT', {}), 'width': ('INT', {}), 'height': ('INT', {})}}
    RETURN_TYPES = ('BBOX',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox: Tensor, width_old: int, height_old: int, width: int, height: int):
        newBbox = bbox.clone()
        bbox_values = newBbox.float()
        l = bbox_values[0] / width_old * width
        t = bbox_values[1] / height_old * height
        r = bbox_values[2] / width_old * width
        b = bbox_values[3] / height_old * height
        newBbox[0] = l
        newBbox[1] = t
        newBbox[2] = r
        newBbox[3] = b
        return (newBbox,)
```