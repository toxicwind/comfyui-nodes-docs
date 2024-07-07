# Documentation
- Class name: DecomposeSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The DecomposeSEGS node is designed to break down complex SEGS data into more manageable components. It is designed to simplify the SEGS data structure to facilitate analysis and operation. The node plays an important role in the data pre-processing process, ensuring that SEGS data are correctly disaggregated for subsequent processing.

# Input types
## Required
- segs
    - The'segs' parameter is essential for the Decompose SEGS node because it represents input data that needs to be broken down. It is a key component that directly affects the operation and output quality of the node.
    - Comfy dtype: SEGS
    - Python dtype: Type[impact.core.SEG]

# Output types
- SEGS_HEADER
    - The SEGS_HEADER output provides a structured representation of head information extracted from SEGS data. It is important to understand the context and metadata associated with SEGS data.
    - Comfy dtype: SEGS_HEADER
    - Python dtype: Dict[str, Any]
- SEG_ELT
    - The SEG_ELT output contains the decomposition element of the SEGS data. It is the key output for further analysis and is essential for downstream tasks requiring detailed information.
    - Comfy dtype: SEG_ELT
    - Python dtype: List[impact.core.SEG]

# Usage tips
- Infra type: CPU

# Source code
```
class DecomposeSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('SEGS_HEADER', 'SEG_ELT')
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs):
        return segs
```