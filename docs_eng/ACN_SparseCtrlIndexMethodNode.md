# Documentation
- Class name: SparseIndexMethodNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The node is used to retrieve the dilution control network by providing a series of unique indexes. It ensures that the index is a valid integer and is used to quote specific elements in a larger data set or structure.

# Input types
## Required
- indexes
    - The " indexes " parameter is a comma-separated integer string used to identify elements in a unique data set. It is essential for the operation of nodes, as it directly affects which elements are selected for processing.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- method
    - The output'method' is an example of SparseIndexMethod, customized according to the index provided. It represents the core function of SparseIndexMethodNode, making it possible to select and process specific elements in a thin control network.
    - Comfy dtype: SPARSE_METHOD
    - Python dtype: SparseIndexMethod

# Usage tips
- Infra type: CPU

# Source code
```
class SparseIndexMethodNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'indexes': ('STRING', {'default': '0'})}}
    RETURN_TYPES = ('SPARSE_METHOD',)
    FUNCTION = 'get_method'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl'

    def get_method(self, indexes: str):
        idxs = []
        unique_idxs = set()
        str_idxs = [x.strip() for x in indexes.strip().split(',')]
        for str_idx in str_idxs:
            try:
                idx = int(str_idx)
                if idx in unique_idxs:
                    raise ValueError(f"'{idx}' is duplicated; indexes must be unique.")
                idxs.append(idx)
                unique_idxs.add(idx)
            except ValueError:
                raise ValueError(f"'{str_idx}' is not a valid integer index.")
        if len(idxs) == 0:
            raise ValueError(f'No indexes were listed in Sparse Index Method.')
        return (SparseIndexMethod(idxs),)
```