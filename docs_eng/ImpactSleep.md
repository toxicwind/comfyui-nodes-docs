# Documentation
- Class name: ImpactSleep
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactSleep node 'doit' method is designed to introduce delays in the execution process. It accepts a signal and a duration in seconds, and then suspends the process for a specified period of time, allowing other tasks to be scheduled or executed. This node is particularly suitable for controlling the time of operations in larger workflows.

# Input types
## Required
- signal
    - The `signal' parameter is a general input that can be used to transmit control or state information to nodes. It is important because its value may affect subsequent steps in the workflow.
    - Comfy dtype: any_typ
    - Python dtype: Any
- seconds
    - The `seconds' parameter specifies the duration of the delay to be introduced at the node. It is essential for a time-sensitive operation and can affect the overall performance of the system.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- signal_opt
    - The `signal_opt' output provides the original signal after the introduction delay to ensure that the workflow can continue with the same control or state information seamlessly.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactSleep:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'signal': (any_typ,), 'seconds': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 3600})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal_opt',)
    OUTPUT_NODE = True

    def doit(self, signal, seconds):
        time.sleep(seconds)
        return (signal,)
```