# Documentation
- Class name: ReferenceControlFinetune
- Category: Adv-ControlNet 🛂🅐🅒🅝/Reference
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

ReferenceControlFinetune is a control network micro-reconciliation point for advanced image-processing tasks. It uses a system of standardization of attention and self-adaptation to achieve a high level of integrity in style migration and content adaptation. The node plays a key role in enhancing the control of the generation process, allowing fine-tuning of the final output.

# Input types
## Required
- attn_style_fidelity
    - The antn_style_fieldity parameter controls the validity of the attention mechanism in the application of style conversion. It is essential to balance style effects with the preservation of content details, thus affecting the aesthetic results as a whole.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_ref_weight
    - The antn_ref_weight parameter determines the weight of reference in the attention mechanism and influences the extent to which style conversions are guided by reference content.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_strength
    - The antn_strength parameter adjusts the intensity of the attention mechanism to the style process, allowing for control of the intensity of the application style.
    - Comfy dtype: FLOAT
    - Python dtype: float
- adain_style_fidelity
    - The application of adain_style_fieldity parameters to determine the level of calibration of self-adaptation examples is essential to maintain the integrity of the original image features while applying the style.
    - Comfy dtype: FLOAT
    - Python dtype: float
- adain_ref_weight
    - The adin_ref_weight parameter sets the reference weight from the adaptation case to the standardization, affecting the strength of the reference style applied to the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- adain_strength
    - The adain_strength parameter defines the overall strength of the effects of the standardization of the self-adaptation example and allows fine-tuned styles to fit into the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- control_net
    - The output of the RefenceControlFinetune node is a control network that covers fine-tuned parameters and mechanisms for advanced style control and operation. It is a key component of the follow-up image generation task.
    - Comfy dtype: CONTROL_NET
    - Python dtype: comfy.controlnet.ControlBase

# Usage tips
- Infra type: GPU

# Source code
```
class ReferenceControlFinetune:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'attn_style_fidelity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'attn_ref_weight': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'attn_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'adain_style_fidelity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'adain_ref_weight': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'adain_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONTROL_NET',)
    FUNCTION = 'load_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/Reference'

    def load_controlnet(self, attn_style_fidelity: float, attn_ref_weight: float, attn_strength: float, adain_style_fidelity: float, adain_ref_weight: float, adain_strength: float):
        ref_opts = ReferenceOptions(reference_type=ReferenceType.ATTN_ADAIN, attn_style_fidelity=attn_style_fidelity, attn_ref_weight=attn_ref_weight, attn_strength=attn_strength, adain_style_fidelity=adain_style_fidelity, adain_ref_weight=adain_ref_weight, adain_strength=adain_strength)
        controlnet = ReferenceAdvanced(ref_opts=ref_opts, timestep_keyframes=None)
        return (controlnet,)
```