# Documentation
- Class name: WAS_Latent_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `latent_input_switch' method of the WAS_Latent_Input_Switch node is designed to select one of the two potential expressions conditionally according to the Boolean sign. It is used as a logical switch to guide the flow of potential data in the neural network waterline, allowing for flexible operations for input of different model structures.

# Input types
## Required
- latent_a
    - The parameter 'latent_a' indicates one of the potential indications of a conditional selection. It plays a key role in the operation of the node, as it determines the true-time output of the Boolean mark, thus influencing subsequent processing steps.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, np.ndarray]
- latent_b
    - The parameter 'latet_b' is another potential indication that if the boolean mark is false, it needs to be selected. It is essential for the function of the node, as it determines the output under specified conditions and guides subsequent neural network operations.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, np.ndarray]
## Optional
- boolean
    - The parameter 'boolean' is the control signal for the node decision-making process. Its importance is that it directly influences which potential expression it selects, thus influencing the overall behavior of the neural network.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latent_output
    - 'latent_output' represents the potential expression of the boolean logo selection given to nodes. It is the end result of node operations and is essential for further treatment in the neural network.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, np.ndarray]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Latent_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'latent_a': ('LATENT',), 'latent_b': ('LATENT',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'latent_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def latent_input_switch(self, latent_a, latent_b, boolean=True):
        if boolean:
            return (latent_a,)
        else:
            return (latent_b,)
```