# Documentation
- Class name: convertKeyframeKeysToBatchKeys
- Category: FizzNodes 📅🅕🅝/HelperNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The 'concat' method in the 'convert Keyframe KeysToBatchKeys' node is designed to process key frame data in a single batch efficiently. It achieves this by multiplying the number of key frames entered by the number of potential dimensions, thereby creating a continuous sequence suitable for batch operations. This method is essential for optimizing the processing of key frame data in large-scale animations or simulations.

# Input types
## Required
- input
    - The 'input'parameter represents the number of key frames to be addressed. It is an essential part of node operations, as it directly affects the size of the batch created, and thus the efficiency of the next step.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- num_latents
    - The 'num_latents' parameter specifies the potential dimensions of the key frame data to be considered. It is essential to determine the final structure of the batch, ensuring that the data is properly organized to fit downstream tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The'reult' output provides the calculated batch key sequence, which is a multiplier of the number of key frame counts and potential dimensions. This output is important because it forms the basis for further processing and analysis in animated or simulated flow lines.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class convertKeyframeKeysToBatchKeys:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'input': ('INT', {'forceInput': True, 'default': 0}), 'num_latents': ('INT', {'default': 16})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'concat'
    CATEGORY = 'FizzNodes 📅🅕🅝/HelperNodes'

    def concat(self, input, num_latents):
        c = input * num_latents - 1
        return (c,)
```