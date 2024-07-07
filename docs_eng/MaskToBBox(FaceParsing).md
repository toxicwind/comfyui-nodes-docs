# Documentation
- Class name: MaskToBBox
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The node class covers the function of converting facial mask data into boundary frame coordinates, allowing for the positioning of facial features in the image for further analysis.

# Input types
## Required
- mask
    - The mask parameter is a volume that represents the face mask and is essential for identifying the interest areas in the image. It directly affects the accuracy and quality of the boundary frame generated.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
## Optional
- pad
    - Pad parameters allow the border frame coordinates to be adjusted by filling the edges. This is important to fine-tune the boundary box and make it better adapted to the facial features of the image as a whole.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- BBOX
    - The output provides a list of clusters, each of which represents the coordinates of a boundary box. These coordinates are important for locating facial features and can be used for subsequent processing steps.
    - Comfy dtype: List[Tuple[INT, INT, INT, INT]]
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class MaskToBBox:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'pad': ('INT', {'default': 0, 'min': 0, 'step': 1})}}
    RETURN_TYPES = ('BBOX',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, mask: Tensor, pad: int):
        result = ops.masks_to_boxes(mask)
        if pad != 0:
            for item in result:
                item[0] = item[0] - pad
                item[1] = item[1] - pad
                item[2] = item[2] + pad
                item[3] = item[3] + pad
        return (result,)
```