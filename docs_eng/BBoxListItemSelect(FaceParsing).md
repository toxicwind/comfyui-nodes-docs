# Documentation
- Class name: BBoxListItemSelect
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The node is able to select a specific border box from the list based on the index value provided, while ensuring that the selection process does not exceed the list limit. It is intended to simplify the process of accessing individual boundary box data in larger data pools.

# Input types
## Required
- bbox_list
    - This parameter is a list of boundary boxes that serve as data sets for the selection of the required boundary boxes based on the index. It is essential for the operation of the node, as it defines the range of possible options.
    - Comfy dtype: BBOX_LIST
    - Python dtype: List[Dict[str, Union[int, float]]]
- index
    - This parameter determines the location of the boundary box from the list. It is very important because it directly affects the items that are ultimately retrieved from the border box list.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- BBOX
    - Output is a single border box that represents the selection of items from the input list based on the index provided. It is the result of node operations and is valuable for further processing.
    - Comfy dtype: BBOX
    - Python dtype: Dict[str, Union[int, float]]

# Usage tips
- Infra type: CPU

# Source code
```
class BBoxListItemSelect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox_list': ('BBOX_LIST', {}), 'index': ('INT', {'default': 0, 'min': 0, 'step': 1})}}
    RETURN_TYPES = ('BBOX',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox_list: list, index: int):
        item = bbox_list[index if index < len(bbox_list) - 1 else len(bbox_list) - 1]
        return (item,)
```