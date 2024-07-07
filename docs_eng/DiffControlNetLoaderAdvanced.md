# Documentation
- Class name: DiffControlNetLoaderAdvanced
- Category: Adv-ControlNet 🛂🅐🅒🅝
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The DiffControlNetLoaderAdvanced node is designed to load and manage an advanced control network for complex model operations. It ensures compatibility with the type of weight expected in the model and validates the integrity of the control network weight.

# Input types
## Required
- model
    - Model parameters are essential for nodes because they define the basic models that will apply the control network. By determining the context in which the control network operates, they directly influence the execution of the nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- control_net_name
    - The control_net_name parameter specifies the name of the control network to be loaded. It plays a key role in identifying the correct control network configuration of the model, influencing the function of the node and the results of the control application.
    - Comfy dtype: CONTROLNET
    - Python dtype: str
## Optional
- timestep_keyframe
    - The optional Timestep_keyframe parameter allows the designation of time-related key frames in the control network. It can fine-tune the behavior of the network over time and provide more sophisticated control over model operating processes.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: TimestepKeyframeGroup

# Output types
- CONTROL_NET
    - The output CONTROL_NET represents the installed control network, which is prepared for application to the model. It covers the configuration and weight of the control network and is an essential part of the follow-up model operation.
    - Comfy dtype: CONTROLNET
    - Python dtype: ControlNet

# Usage tips
- Infra type: CPU

# Source code
```
class DiffControlNetLoaderAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'control_net_name': (folder_paths.get_filename_list('controlnet'),)}, 'optional': {'timestep_keyframe': ('TIMESTEP_KEYFRAME',)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝'

    def load_controlnet(self, control_net_name, model, timestep_keyframe: TimestepKeyframeGroup=None):
        controlnet_path = folder_paths.get_full_path('controlnet', control_net_name)
        controlnet = load_controlnet(controlnet_path, timestep_keyframe, model)
        if is_advanced_controlnet(controlnet):
            controlnet.verify_all_weights()
        return (controlnet,)
```