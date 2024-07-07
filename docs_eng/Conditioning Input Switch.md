# Documentation
- Class name: WAS_Conditioning_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `conventioning_input_switch'is designed to select conditionally between two input conditions according to the Boolean sign. It acts as a logical switch in the workflow, allowing dynamic route data according to specified conditions, and is essential to control the flow of information in a complex system.

# Input types
## Required
- conditioning_a
    - The parameter 'conventioning_a' indicates the first input condition to be selected when the boolean mark is true. It plays a key role in determining node output, as it directly affects the data passed by the system.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, comfy.sd.CONDITIONING]
- conditioning_b
    - The parameter 'conventioning_b' is the alternative input condition to be used when the Boolean mark is false. When the condition is not met, it is essential to provide an alternative path to the data stream, ensuring the flexibility of nodes when dealing with different scenarios.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, comfy.sd.CONDITIONING]
## Optional
- boolean
    - The parameter 'boolean' is used as a control signal to determine which conditions to enter. When set to be true, select 'convention_a'; when set to be false, select 'convention_b'. It is a key parameter because it directly determines the behaviour of nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_conditioning
    - Output'selected_conventioning' means the input conditions selected on the basis of the provided Boolean logo. It is important because it determines the next steps and processes in the workflow and may affect the final outcome.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, comfy.sd.CONDITIONING]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Conditioning_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'conditioning_a': ('CONDITIONING',), 'conditioning_b': ('CONDITIONING',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'conditioning_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def conditioning_input_switch(self, conditioning_a, conditioning_b, boolean=True):
        if boolean:
            return (conditioning_a,)
        else:
            return (conditioning_b,)
```