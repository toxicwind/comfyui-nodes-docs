# Documentation
- Class name: ReferenceControlNetNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/Reference
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The RefenceControlNetNode class is designed to manage the loading and application of the control network with reference options. It encapsifies the logic of creating advanced control structures that can be used to guide the behaviour of the model generation, and provides a flexible interface to control the generation process based on the user-defined reference type and style authenticity.

# Input types
## Required
- reference_type
    - The reference type parameters determine the type of control network to be used, which has a significant impact on the style and behaviour of producing the output. It is essential for defining the method of control mechanism and its impact on the end result.
    - Comfy dtype: str
    - Python dtype: str
- style_fidelity
    - The style validity parameter adjusts the level of compliance with the reference style, affecting the style consistency of the output. It plays an important role in balancing creative output with the required style control level.
    - Comfy dtype: float
    - Python dtype: float
- ref_weight
    - Ref_weight parameters set the weights referred to in the control network, directly affecting the strength of the application control. It is essential to fine-tune the impact of control on the generation process.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- CONTROL_NET
    - The output of ReferenceControlNetNode is a control network object that encapsifies the advanced control logic. It is important for the model to be directed to the desired result by applying the specified control parameters.
    - Comfy dtype: ControlBase
    - Python dtype: comfy.controlnet.ControlBase

# Usage tips
- Infra type: CPU

# Source code
```
class ReferenceControlNetNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'reference_type': (ReferenceType._LIST,), 'style_fidelity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'ref_weight': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/Reference'

    def load_controlnet(self, reference_type: str, style_fidelity: float, ref_weight: float):
        ref_opts = ReferenceOptions.create_combo(reference_type=reference_type, style_fidelity=style_fidelity, ref_weight=ref_weight)
        controlnet = ReferenceAdvanced(ref_opts=ref_opts, timestep_keyframes=None)
        return (controlnet,)
```