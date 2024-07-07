# Documentation
- Class name: WAS_VAE_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `vae_switch'method in the `WAS_VAE_Input_Switch'node is designed to select conditionally one of the two VAE examples based on the Boolean sign. As a logical switch, it guides the processing process to one of the VAEs provided, thus achieving flexibility and conditionality in the workflow.

# Input types
## Required
- vae_a
    - The parameter `vae_a'indicates the first VAE example that may be selected by the switch. This is a key component, as the decision-making process at the node depends on whether this VAE or another will be used in the follow-up operation.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE
- vae_b
    - The parameter `vae_b'represents the second VAE example of the switch, which is an alternative option to the switch. It contains the option of allowing secondary execution paths to be provided in the function of the node and providing a diversity of treatment options.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE
## Optional
- boolean
    - The parameter `boolean’, as the control signal of the switch, determines that `vae_a' or `vae_b' will be the output of the node. Its value directly influences the decision-making process of the node, leading the output to one of the VAE examples.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_vae
    - Output `selected_vae'means the case of the VAE, selected by the switch under the Boolean condition. It is important because it represents the result of node conditions logic and the starting point for any follow-up treatment.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_VAE_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'vae_a': ('VAE',), 'vae_b': ('VAE',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('VAE',)
    FUNCTION = 'vae_switch'
    CATEGORY = 'WAS Suite/Logic'

    def vae_switch(self, vae_a, vae_b, boolean=True):
        if boolean:
            return (vae_a,)
        else:
            return (vae_b,)
```