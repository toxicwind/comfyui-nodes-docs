# Documentation
- Class name: MaskListSelect
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The MaskListSelect node is designed to select and operate specific elements from a series of masks. It operates a stretch containing multiple masks and an index to identify the required mask. The primary function of the node is to extract a single mask from the list for further processing or analysis.

# Input types
## Required
- mask
    - The'mask' parameter is a volume that contains multiple masks. It is essential for the operation of the node, as it is the primary data source for extracting the required mask. The mask is expected to exist in a format that allows for individual selection.
    - Comfy dtype: "MASK"
    - Python dtype: torch.Tensor
- index
    - The 'index'parameter is an integer that specifies the location of the mask to be selected in the volume. It plays a key role in determining which mask will be extracted for further use. The default value is set at 0, corresponding to the first mask in the list.
    - Comfy dtype: "INT"
    - Python dtype: int

# Output types
- selected_mask
    - The output of the MaskListSelett node is a single mask load extracted from the input mask list. This output can be used for downstream tasks, such as mask applications, visualization or further analysis.
    - Comfy dtype: "MASK"
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskListSelect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK', {}), 'index': ('INT', {'default': 0, 'min': 0, 'step': 1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, mask: Tensor, index: int):
        return (mask[index].unsqueeze(0),)
```