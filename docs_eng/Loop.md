# Documentation
- Class name: Loop
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

Loop Node class encapsulates an iterative process that can perform a series of cycles of operations or algorithms. It is designed to facilitate duplication of task control streams, allowing dynamic adjustment and integration with user-defined logic in a circular structure.

# Input types
## Required
- required
    - This parameter is essential to define the conditions for cycle execution. As a gatekeeper, it ensures that the loop only functions if the specified requirements are met, thus affecting the overall implementation process and operational results.
    - Comfy dtype: COMBO[None]
    - Python dtype: Dict[str, Any]

# Output types
- LOOP
    - The output of the Loop node is the result of the node itself, encapsulating an iterative process. It represents the climax of the cycle sequence and provides a structured and controlled way of exporting the final state of the cycle execution.
    - Comfy dtype: NODE[Loop]
    - Python dtype: Loop

# Usage tips
- Infra type: CPU

# Source code
```
class Loop:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('LOOP',)
    FUNCTION = 'run'
    CATEGORY = 'DragNUWA'

    def run(self):
        return (self,)
```