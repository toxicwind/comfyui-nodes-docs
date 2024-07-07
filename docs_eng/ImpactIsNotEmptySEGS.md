# Documentation
- Class name: ImpactNotEmptySEGS
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The "doit" method of the ImpactNotEmptySEGS node is used to check whether the given list of paragraphs is empty, with particular attention to the second element in the list. The presence of data in a given paragraph is essential when further processing or decision-making in the logical process is required.

# Input types
## Required
- segs
    - The'segs' parameter is a list of data paragraphs. A check of its contents is essential for the operation of the 'doit' method, as it determines whether the second paragraph is not empty, which is essential for the decision-making process of the nodes.
    - Comfy dtype: SEGS
    - Python dtype: List[Any]

# Output types
- result
    - 'Result' output means that the second element in the'segs' list is not empty. It is a boolean value that is checked according to the conditions implemented by the 'doit' method and directly affects subsequent logic or operation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactNotEmptySEGS:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'segs': ('SEGS',)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('BOOLEAN',)

    def doit(self, segs):
        return (segs[1] != [],)
```