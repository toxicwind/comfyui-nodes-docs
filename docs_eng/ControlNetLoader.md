# Documentation
- Class name: ControlNetLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ContractorNetLoader node is designed to efficiently load and integrate the control network into the system. It is a key component of an application that needs to operate and analyse the control network structure. The node abstractes the complexity of the loading control network and ensures the flow and reliability of the loading process.

# Input types
## Required
- control_net_name
    - The control_net_name parameter is essential to identify the specific control network to be loaded. It plays a key role in the operation of the node by pointing the node to the right resource, thereby influencing the execution and outcome of the process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- CONTROL_NET
    - The output of the ControlNetLoader node is a control network structure, which is important for follow-up processing and analysis in the system. Control of the network covers the rules and interactions that govern specific systems, making it the basic output of applications that rely on control of network logic.
    - Comfy dtype: COMBO[str]
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class ControlNetLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'control_net_name': (folder_paths.get_filename_list('controlnet'),)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'loaders'

    def load_controlnet(self, control_net_name):
        controlnet_path = folder_paths.get_full_path('controlnet', control_net_name)
        controlnet = comfy.controlnet.load_controlnet(controlnet_path)
        return (controlnet,)
```