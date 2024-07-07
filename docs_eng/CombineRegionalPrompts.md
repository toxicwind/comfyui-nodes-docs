# Documentation
- Class name: CombineRegionalPrompts
- Category: ImpactPack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The CombineRegionalPrompts node is designed to combine multiple sets of regional tips into a single collection. It plays a key role in simplifying the regional data entry process by ensuring that all relevant tips are brought together efficiently and without redundancies, thus contributing to a more coherent and comprehensive analysis of regional information.

# Input types
## Required
- regional_prompts1
    - The regional_prompts1 parameter is essential for the CombineRegionalPrompts node, as it is the main input and contains a regional reminder that needs to be merged. It is essential for the implementation of the node, as the quality and relevance of the polymer node directly influences subsequent analysis and results.
    - Comfy dtype: REGIONAL_PROMPTS
    - Python dtype: List[str]

# Output types
- combined_prompts
    - Combined_prompts output parameters represent the result of combining multiple regional reminders into a consistent list. This output is important because it provides the basis for further processing and analysis within the ImpactPack/Regional category to ensure that consolidated data are available for follow-up operations.
    - Comfy dtype: REGIONAL_PROMPTS
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class CombineRegionalPrompts:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'regional_prompts1': ('REGIONAL_PROMPTS',)}}
    RETURN_TYPES = ('REGIONAL_PROMPTS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Regional'

    def doit(self, **kwargs):
        res = []
        for (k, v) in kwargs.items():
            res += v
        return (res,)
```