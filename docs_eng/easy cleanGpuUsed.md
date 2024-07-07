# Documentation
- Class name: cleanGPUUsed
- Category: EasyUse/Logic
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is designed to optimize the calculation of resources by managing the GPU memory. The main function is to release any unused GPU memory to ensure that the follow-up operation is efficient and does not be interrupted by insufficient memory.

# Input types
## Required
- anything
    - The parameter does not directly affect the execution of the node, but it is a placeholder to ensure compatibility with the various input types. It does not affect the primary function of the node.
    - Comfy dtype: COMBO[AlwaysEqualProxy(str)]
    - Python dtype: Union[str, AlwaysEqualProxy]
## Optional
- unique_id
    - This parameter, although optional, can be used to track the execution of nodes. It helps to record logs and debugging processes.
    - Comfy dtype: str
    - Python dtype: Optional[str]
- extra_pnginfo
    - This optional parameter can store additional information relevant to node execution. It is not critical to node operations, but it may be useful for further analysis.
    - Comfy dtype: str
    - Python dtype: Optional[str]

# Output types

# Usage tips
- Infra type: GPU

# Source code
```
class cleanGPUUsed:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'anything': (AlwaysEqualProxy('*'), {})}, 'optional': {}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    OUTPUT_NODE = True
    FUNCTION = 'empty_cache'
    CATEGORY = 'EasyUse/Logic'

    def empty_cache(self, anything, unique_id=None, extra_pnginfo=None):
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        return ()
```