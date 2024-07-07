# Documentation
- Class name: SwitchByIndex
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

SwitchByIndex is a node to select elements from two input lists based on a specified index, allowing the combination and extension of data structures.

# Input types
## Required
- A
    - The parameter 'A' is the first input list and is essential for the operation of the node, as it provides the main data source.
    - Comfy dtype: ANY
    - Python dtype: List[Any]
- B
    - The parameter `B' represents the second input list, which adds the `A' list to the node data processing.
    - Comfy dtype: ANY
    - Python dtype: List[Any]
- index
    - The parameter 'index' is essential to select a particular element from the group list and influences the output of the node.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- flat
    - The parameter 'flat' determines whether the output list should be levelled to influence the structure of the final result.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- C
    - Output 'C' is a list of elements in two input lists that may be modified by the 'index' and 'flat' parameters.
    - Comfy dtype: ANY
    - Python dtype: List[Any]
- count
    - The output 'count' provides the total number of elements in the 'C' list, reflecting the data aggregation of nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SwitchByIndex:

    @classmethod
    def INPUT_TYPES(cls):
        return {'optional': {'A': (any_type,), 'B': (any_type,)}, 'required': {'index': ('INT', {'default': -1, 'min': -1, 'max': 1000, 'step': 1, 'display': 'number'}), 'flat': (['off', 'on'],)}}
    RETURN_TYPES = (any_type, 'INT')
    RETURN_NAMES = ('C', 'count')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, False)

    def run(self, A=[], B=[], index=-1, flat='on'):
        flat = flat[0]
        C = []
        index = index[0]
        for a in A:
            C.append(a)
        for b in B:
            C.append(b)
        if flat == 'on':
            C = flatten_list(C)
        if index > -1:
            try:
                C = [C[index]]
            except Exception as e:
                C = []
        return (C, len(C))
```