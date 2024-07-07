# Documentation
- Class name: From_SEG_ELT_bbox
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method for the From_SEG_ELT_bbox node is designed to process and return the boundary frame coordinates of particular elements. It plays a key role in the spatial data operation of the ImpactPack tool concentration, ensuring the precise positioning of elements for further processing.

# Input types
## Required
- bbox
    - The parameter 'bbox' is essential for the operation of the node because it defines the spatial boundaries of the elements to be addressed. It directly affects the accuracy and relevance of the node output by determining the particular area of interest.
    - Comfy dtype: SEG_ELT_bbox
    - Python dtype: Tuple[int, int, int, int]

# Output types
- left
    - The parameter 'left' represents the coordinates on the leftmost side of the boundary box, marking the beginning of a horizontal span. It is essential in defining the spatial range of elements in the processed data.
    - Comfy dtype: INT
    - Python dtype: int
- top
    - The parameter 'top' indicates the coordinates above the boundary box, indicating the start of the vertical span. It is important for the vertical position of the elements in the data concentration.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - The parameter'right' indicates the coordinates to the right of the boundary frame, marking the end of the horizontal span. It is essential in determining the width of the element and its spatial boundary in the data set.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The parameter 'bottom' represents the coordinates at the bottom of the boundary box, marking the end of the vertical span. It is essential in determining the height of the element and its complete vertical range in the processing data.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class From_SEG_ELT_bbox:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bbox': ('SEG_ELT_bbox',)}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('left', 'top', 'right', 'bottom')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, bbox):
        return bbox
```