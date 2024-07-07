# Documentation
- Class name: RemoveControlNet
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node aims to improve the clarity and focus of the data set by processing and refining input data by removing control-related elements.

# Input types
## Required
- conditioning
    - The reconciliation parameter is essential because it is the main input for node operations. It contains the data that will be processed to achieve the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, dict]]

# Output types
- conditioning
    - The output is a refined version of the input data to remove the control element, which is essential for further analysis or processing.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, dict]]

# Usage tips
- Infra type: CPU

# Source code
```
class RemoveControlNet:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, conditioning):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            if 'control' in n[1]:
                del n[1]['control']
            if 'control_apply_to_uncond' in n[1]:
                del n[1]['control_apply_to_uncond']
            c.append(n)
        return (c,)
```