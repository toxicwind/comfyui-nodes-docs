# Documentation
- Class name: EmptySEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The EmptySEGS node 'doit' method is designed to generate an empty partition structure. It is intended to provide a baseline or placeholder when the data are not physically divided. When input data does not require detailed partition, this node is essential to ensure the integrity of the workflow while avoiding unnecessary complexity.

# Input types
## Optional
- input_data
    - Although the `input_data' parameter is not necessary, it can be used, if necessary, to transmit additional context or data to the EmptySEGS node. It may be used to enhance the function of the node or to integrate with other systems that may need to enter data for operation.
    - Comfy dtype: Any
    - Python dtype: Any

# Output types
- SEGS
    - The output parameter'SEGS' represents the result of the EmptySEGS node operation. It provides an empty array, the first of which is the shape of the split dimension, and the second is a list that usually contains split data but is empty in this case. This output format allows seamless integration with the system that is expected to divide the result, even if the actual partition is not performed.
    - Comfy dtype: Tuple[int, List[Any]]
    - Python dtype: Tuple[int, List[Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class EmptySEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self):
        shape = (0, 0)
        return ((shape, []),)
```