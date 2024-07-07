# Documentation
- Class name: ImpactConditionalStopIteration
- Category: ImpactPack/Logic
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The "doit" method of the ImpactConditionalStation node is designed to control the execution process according to conditions. When called on real terms, it sends a signal to stop the iterative process. The node plays a key role in managing the execution process in the workflow, allowing conditional interruptions when certain conditions are met.

# Input types
## Required
- cond
    - The parameter 'cond' is a boolean value, which determines whether an overlap should be stopped. It is essential for the operation of the node, as it directly affects the decision-making process regarding the continuation or termination of an overlap.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- None
    - The 'doit' method does not return any output. It is a non-returning method, the sole purpose of which is to send a'stop-internation' signal when the conditions are real, thus affecting the process of control.
    - Comfy dtype: DICT
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactConditionalStopIteration:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'cond': ('BOOLEAN', {'forceInput': True})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ()
    OUTPUT_NODE = True

    def doit(self, cond):
        if cond:
            PromptServer.instance.send_sync('stop-iteration', {})
        return {}
```