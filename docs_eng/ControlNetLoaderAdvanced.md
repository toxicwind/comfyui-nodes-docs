# Documentation
- Class name: ControlNetLoaderAdvanced
- Category: Adv-ControlNet 🛂🅐🅒🅝
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The `load_controlnet'method at the ContractorNetLoaderAdvanced node is designed to efficiently load and manage network configurations. It is a key component of the system that allows seamless integration of control networks into workflows. This method abstracts the complexity of loading and processing control networks and provides users with a simple visual interface to access them.

# Input types
## Required
- control_net_name
    - The parameter `control_net_name'is essential to identify the specific control network to be loaded. It plays a key role in the implementation of the node, determining which control network configuration will be used in the system.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- timestep_keyframe
    - The optional parameter `timestep_keyframe'allows the designation of key frames related to time steps, which can influence the way the control network is applied in the course of time change.
    - Comfy dtype: TimestepKeyframeGroup
    - Python dtype: TimestepKeyframeGroup

# Output types
- CONTROL_NET
    - The output `CONTROL_NET' represents the loaded control network and is a core element in the operation of the system. It covers the network's structure and parameters and is prepared for use in various tasks and analyses.
    - Comfy dtype: Tensor
    - Python dtype: Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ControlNetLoaderAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'control_net_name': (folder_paths.get_filename_list('controlnet'),)}, 'optional': {'timestep_keyframe': ('TIMESTEP_KEYFRAME',)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝'

    def load_controlnet(self, control_net_name, timestep_keyframe: TimestepKeyframeGroup=None):
        controlnet_path = folder_paths.get_full_path('controlnet', control_net_name)
        controlnet = load_controlnet(controlnet_path, timestep_keyframe)
        return (controlnet,)
```