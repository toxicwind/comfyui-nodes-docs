# Documentation
- Class name: SeargeEnablerInputs
- Category: Searge/_deprecated_/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class is designed to retrieve and manage the status of the system as an interface for status-related operations within a discarded framework. It covers the status acquisition process in abstract terms, emphasizing the role of node in maintaining and providing access to the current state of the system.

# Input types
## Required
- state
    - The `state' parameter is essential for the operation of the node, because it represents the current state of the system. It is the basic element that determines node behaviour and produces output.
    - Comfy dtype: COMBO[SeargeParameterProcessor.STATES]
    - Python dtype: str

# Output types
- state
    - The output `state' reflects the current state of the input supply system and marks the main function of the node as state management and retrieval.
    - Comfy dtype: COMBO[SeargeParameterProcessor.STATES]
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeEnablerInputs:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'state': (SeargeParameterProcessor.STATES, {'default': SeargeParameterProcessor.STATES[1]})}}
    RETURN_TYPES = ('ENABLE_STATE',)
    RETURN_NAMES = ('state',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Inputs'

    def get_value(self, state):
        return (state,)
```