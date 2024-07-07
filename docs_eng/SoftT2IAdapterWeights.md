# Documentation
- Class name: SoftT2IAdapterWeights
- Category: Adv-ControlNet 🛂🅐🅒🅝/weights/T2IAdapter
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The SoftT2IAdapterWeights node is intended to facilitate the matching of network weights in order to convert the time frame to input fit-in weights. It streamlines the weight distribution process and ensures compatibility with bottom-level control network mechanisms.

# Input types
## Required
- weight_00
    - The weight_00 parameter is essential for initializing the base level of the control weight, affecting the overall effect of the time-critical frame conversion process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_01
    - The weight_01 parameter is essential for adjusting the weight of intermediate control and directly affects the fine transformation of the time-critical frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_02
    - The weight_02 parameter is critical in fine-tuning the weight of high-level control and determines the accuracy of the time-critical frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_03
    - The weight_03 parameter is essential to define the ultimate control weight and determines the final result of a time-critical frame shift.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- flip_weights
    - When the flip_rights parameters are enabled, the effect of the weight of control is reversed and another perspective is provided during the distribution and conversion of weights.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- CONTROL_NET_WEIGHTS
    - The output CONTROL_NET_WEIGHTS represents the right of control weights properly arranged and converted and is prepared for further processing in time-critical frames.
    - Comfy dtype: CONTROL_NET_WEIGHTS
    - Python dtype: ControlWeights
- TIMESTEP_KEYFRAME
    - The output TIMESTEP_KEYFRAME provides a structured time-step key group, seals the control weight and prepares for integration into the control network.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: TimestepKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class SoftT2IAdapterWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'weight_00': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_01': ('FLOAT', {'default': 0.62, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_02': ('FLOAT', {'default': 0.825, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_03': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'flip_weights': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('CONTROL_NET_WEIGHTS', 'TIMESTEP_KEYFRAME')
    RETURN_NAMES = WEIGHTS_RETURN_NAMES
    FUNCTION = 'load_weights'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/weights/T2IAdapter'

    def load_weights(self, weight_00, weight_01, weight_02, weight_03, flip_weights):
        weights = [weight_00, weight_01, weight_02, weight_03]
        weights = get_properly_arranged_t2i_weights(weights)
        weights = ControlWeights.t2iadapter(weights, flip_weights=flip_weights)
        return (weights, TimestepKeyframeGroup.default(TimestepKeyframe(control_weights=weights)))
```