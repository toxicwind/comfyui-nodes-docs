# Documentation
- Class name: ImpactQueueTriggerCountdown
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Impact QueueTrigerCountdown method is designed to manage the countdown and trigger mechanism in the queue system. It drives the countdown and determines whether to trigger an event according to aggregates and current patterns. The node plays a key role in controlling the workflow in the queue-based workflow.

# Input types
## Required
- count
    - The parameter 'count' is used to track the current position in the countdown sequence. It is essential to determine the progress of the queue and the timing of the trigger event.
    - Comfy dtype: INT
    - Python dtype: int
- total
    - The parameter'total' defines the maximum count until the trigger conditions are met. It is important for setting the number of steps expected during the countdown.
    - Comfy dtype: INT
    - Python dtype: int
- mode
    - The parameter'mode' determines whether the node should trigger an event. It is an important switch that controls the active status of the countdown mechanism.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- unique_id
    - The parameter'unique_id' is used to identify nodes in the system for feedback and queue management. It plays a vital role in ensuring accurate communication and tracking in the workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- signal
    - Parameter'signal' is an optional input that can be used to transmit additional information or controls to nodes. It provides flexibility for nodes to operate.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- signal_opt
    - The output'signal_opt' allows optional transmission of a signal that can be used for further processing or communication in the system.
    - Comfy dtype: ANY
    - Python dtype: Any
- count
    - Output 'count' reflects the count that is updated after the node operation. It is important to track the countdown in the queue.
    - Comfy dtype: INT
    - Python dtype: int
- total
    - The output'total' provides total values, which are essential for understanding the remaining steps in the countdown sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactQueueTriggerCountdown:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'count': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'total': ('INT', {'default': 10, 'min': 1, 'max': 18446744073709551615}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'Trigger', 'label_off': "Don't trigger"})}, 'optional': {'signal': (any_typ,)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ, 'INT', 'INT')
    RETURN_NAMES = ('signal_opt', 'count', 'total')
    OUTPUT_NODE = True

    def doit(self, count, total, mode, unique_id, signal=None):
        if mode:
            if count < total - 1:
                PromptServer.instance.send_sync('impact-node-feedback', {'node_id': unique_id, 'widget_name': 'count', 'type': 'int', 'value': count + 1})
                PromptServer.instance.send_sync('impact-add-queue', {})
            if count >= total - 1:
                PromptServer.instance.send_sync('impact-node-feedback', {'node_id': unique_id, 'widget_name': 'count', 'type': 'int', 'value': 0})
        return (signal, count, total)
```