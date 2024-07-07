# Documentation
- Class name: WAS_Control_Net_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `control_net_switch' method is designed to select one of the two control networks on the basis of a boolean intelligence. It serves as a decision node in the workflow to ensure that the appropriate control network is used at any given time, thereby increasing the flexibility and adaptability of the system.

# Input types
## Required
- control_net_a
    - The 'control_net_a' parameter represents the first control network option that can be switched to. It plays a key role in the decision-making process, because when the boolean conditions are met, the node selects the network.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Optional[Union[comfy.sd.CONTROL_NET, torch.Tensor]]
- control_net_b
    - The `control_net_b' parameter is the alternative control network that the boolean conditions may choose when the node is not met. It is essential for the function of the node and provides an option for controlling the network.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Optional[Union[comfy.sd.CONTROL_NET, torch.Tensor]]
## Optional
- boolean
    - The 'boolean' parameter, as a conditional switch, determines whether to return 'control_net_a' or 'control_net_b'. Its significance is that its true value directly determines the output of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_control_net
    - `selected_control_net' represents the control network selected by the node on the basis of the Boolean condition. It is vital because it determines the next steps in the workflow.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Union[comfy.sd.CONTROL_NET, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Control_Net_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'control_net_a': ('CONTROL_NET',), 'control_net_b': ('CONTROL_NET',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'control_net_switch'
    CATEGORY = 'WAS Suite/Logic'

    def control_net_switch(self, control_net_a, control_net_b, boolean=True):
        if boolean:
            return (control_net_a,)
        else:
            return (control_net_b,)
```