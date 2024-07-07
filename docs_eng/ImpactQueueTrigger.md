# Documentation
- Class name: ImpactQueueTrigger
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Impact QueueTrigger method 'doit' is designed to trigger operations in the management system. When using signals and mode calls, it decides whether to activate the process by sending an order to PromptServer's example. The node plays a key role in controlling the process and starting the operation on predefined terms.

# Input types
## Required
- signal
    - The “signal” parameter is essential for the operation of the node, as it represents the input that determines the conditions for triggering the process. Its emergence is necessary for the proper operation of the node, and it directly affects the decision-making process for initiating follow-up action.
    - Comfy dtype: any_typ
    - Python dtype: Any
## Optional
- mode
    - The'mode'parameter is an optional switcher that specifies whether the node should trigger the operation. It has a default value set at True, which means that the operation will trigger the operation by default. This parameter allows the behaviour of the node to be controlled without changing the main input signal.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- signal_opt
    - The "signal_opt" output represents the signal that is optimized or processed after the node has been executed. It covers the outcome of the trigger decision and transmits the signal for further use or analysis within the system.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactQueueTrigger:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'signal': (any_typ,), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'Trigger', 'label_off': "Don't trigger"})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal_opt',)
    OUTPUT_NODE = True

    def doit(self, signal, mode):
        if mode:
            PromptServer.instance.send_sync('impact-add-queue', {})
        return (signal,)
```