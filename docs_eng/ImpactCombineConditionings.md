# Documentation
- Class name: CombineConditionings
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

CombineConditions is a practical tool node designed to combine multiple conditions into individual outputs. It plays a key role in simplifying the integration of conditions into complex data operations. This node ensures that different conditions are effectively integrated, thus facilitating seamless workflows in downstream applications.

# Input types
## Required
- conditioning1
    - The parameter 'convention1' is the input of the node into the main condition of the other input. It is essential for the operation of the node, as it forms the basis for the final mix of conditions output. The validity of the node depends to a large extent on the relevance and quality of the conditions data provided.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Output types
- combined_conditioning
    - The output 'combined_convention'means that all input conditions are combined into a unified structure. It contains the collective effects of each condition and makes it suitable for further processing at the subsequent stages of the workflow.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CombineConditionings:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning1': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, **kwargs):
        res = []
        for (k, v) in kwargs.items():
            res += v
        return (res,)
```