# Documentation
- Class name: GlobalSampler
- Category: InspirePack/Prompt
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

GlobalSampler nodes represent, in the abstract, a system for homogenous sampling of elements from given pools, ensuring that each element is selected with the same probability. It is designed to introduce randomity in the process, in a fair and impartial manner, which is essential for the application of random behaviour or diversity of results.

# Input types
## Required
- sampler_name
    - The sampler_name parameter is essential because it determines the sampling method to be used. It shapes the diversity and randomity of results by determining which sampling algorithms will be used that directly affect the operation of nodes.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- scheduler
    - The Scheduler parameter is essential for managing the process of sampling execution. It affects how nodes coordinate the timing and frequency of sampling and ensures that randomity is effectively introduced without affecting the process as a whole.
    - Comfy dtype: COMBO[str]
    - Python dtype: str

# Output types
- sampled_data
    - The sampled_data output contains the results of the sampling process and represents the selected element. It is the key output because it directly reflects the validity of the sampling method and the random quality achieved.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class GlobalSampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,)}}
    RETURN_TYPES = ()
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'
    OUTPUT_NODE = True

    def doit(self, **kwargs):
        return {}
```