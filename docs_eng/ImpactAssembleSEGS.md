# Documentation
- Class name: AssembleSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The AssembleSEGS node is designed to combine the head and the elements into a coherent structure. It plays a key role in the aggregation of the data to ensure that the head and the elements are correctly assembled into a complete segment.

# Input types
## Required
- seg_header
    - The `seg_header' parameter is essential to define the metadata of the split process. It determines the interpretation and structure of the split element in the final output.
    - Comfy dtype: SEGS_HEADER
    - Python dtype: List[str]
- seg_elt
    - The `seg_elt' parameter is necessary because it contains the actual data elements that need to be separated. It influences the execution of the node by determining what the final split will contain.
    - Comfy dtype: SEG_ELT
    - Python dtype: List[Any]

# Output types
- output
    - The output of the AssembleSEGS node is a structured set of partitions that combines head and elements. It is important because it represents the final form of the split data and is prepared for further processing or analysis.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[List[str], List[Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class AssembleSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seg_header': ('SEGS_HEADER',), 'seg_elt': ('SEG_ELT',)}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, seg_header, seg_elt):
        return ((seg_header[0], seg_elt),)
```