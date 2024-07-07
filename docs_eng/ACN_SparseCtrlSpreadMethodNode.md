# Documentation
- Class name: SparseSpreadMethodNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The SparseSpreadMethodNode class is designed to generate and manage thin index distributions within given ranges. It deals in abstract terms with the logic of different proliferation methods, such as homogeneity, start, end and centre, allowing flexibility in processing thin data.

# Input types
## Required
- spread
    - The parameter'spread' determines how the thin index is distributed throughout the length. It is essential for the operation of the node, as it determines the pattern of the dilution of data generation, which may significantly influence the outcome of the process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- SPARSE_METHOD
    - The output parameter 'SPARSE_METHOD' means the method used to diffuse the index. It is important because it encapsifies the logic of the chosen diffusion strategy, which is essential for downstream tasks that rely on thin index distribution.
    - Comfy dtype: SparseSpreadMethod
    - Python dtype: SparseSpreadMethod

# Usage tips
- Infra type: CPU

# Source code
```
class SparseSpreadMethodNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'spread': (SparseSpreadMethod.LIST,)}}
    RETURN_TYPES = ('SPARSE_METHOD',)
    FUNCTION = 'get_method'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/SparseCtrl'

    def get_method(self, spread: str):
        return (SparseSpreadMethod(spread=spread),)
```