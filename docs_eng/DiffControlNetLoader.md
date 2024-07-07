# Documentation
- Class name: DiffControlNetLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The DiffControlNetLoader node is designed to load the control network into the given model framework. It abstractes the complexity of positioning and integrated control networks and ensures that the model is seamlessly enhanced through the control mechanism.

# Input types
## Required
- model
    - Model parameters are essential for the DiffControlNetLoader node, as they represent the framework within which the control network will be integrated. They are the building blocks for the control network to interact with the existing architecture of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- control_net_name
    - The control_net_name parameter specifies the only identifier for the control network to be loaded. It is essential for the operation of the node, as it guides the retrieval and application of the correct control network configuration.
    - Comfy dtype: folder_paths.get_filename_list('controlnet')
    - Python dtype: str

# Output types
- CONTROL_NET
    - The output CONTROL_NET represents the installed control network and prepares for integration with the models provided. It covers the control mechanisms that will be applied to enhance model function.
    - Comfy dtype: CONTROL_NET
    - Python dtype: comfy.controlnet.ControlNet

# Usage tips
- Infra type: CPU

# Source code
```
class DiffControlNetLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'control_net_name': (folder_paths.get_filename_list('controlnet'),)}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'loaders'

    def load_controlnet(self, model, control_net_name):
        controlnet_path = folder_paths.get_full_path('controlnet', control_net_name)
        controlnet = comfy.controlnet.load_controlnet(controlnet_path, model)
        return (controlnet,)
```