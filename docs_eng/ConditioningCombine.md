# Documentation
- Class name: ConditioningCombine
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditioningCombine is designed to combine two conditions into a single output. It plays a key role in simplifying the data processing process by ensuring that consolidated condition information is used effectively in subsequent model operations.

# Input types
## Required
- conditioning_1
    - The first condition input is essential for the operation of the node, as it provides a part of the data required for the assembly process. It significantly influences the final output through the initial state of the contribution condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- conditioning_2
    - The second condition input is equally important, supplementing the first input and completing the data set needed to generate the combined output of the node. Its contribution to the achievement of a consistent and comprehensive condition result is indispensable.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Output types
- combined_conditioning
    - The output of the ConditionCombine node is the post-combined condition data, which is a combination of two input conditions. This output is the key information for next steps in the workflow and can be used to guide model predictions or further processing of impacts.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningCombine:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning_1': ('CONDITIONING',), 'conditioning_2': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'combine'
    CATEGORY = 'conditioning'

    def combine(self, conditioning_1, conditioning_2):
        return (conditioning_1 + conditioning_2,)
```