# Documentation
- Class name: SoftControlNetWeights
- Category: Adv-ControlNet 🛂🅐🅒🅝/weights/ControlNet
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The SoftControlNetWeights class aims to manage and process the weights of the control network, which may be used in machine learning or simulation environments. It encapsulates the logic of loading and organizing these weights to ensure that they are correctly applied to influence the network’s behaviour.

# Input types
## Required
- weight_00
    - The weight_00 parameter is a floating number that contributes to the overall weight of the control network. It plays a key role in determining the initial impact on network behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- flip_weights
    - The flip_rights parameter is a boolean value that, when set, indicates that the weight should be turned or reversed when applied to the control network. This can significantly change the response of the network.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- weights
    - The weight output represents the control network weights that have been processed and organized and that are loaded and ready to be applied in the network.
    - Comfy dtype: CONTROL_NET_WEIGHTS
    - Python dtype: ControlWeights
- timestep_keyframe
    - The timestap_keyframe output is a structured expression of a time point in a network operation. It includes details such as the percentage and intensity of the start, which are essential for time control.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: TimestepKeyframe

# Usage tips
- Infra type: CPU

# Source code
```
class SoftControlNetWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'weight_00': ('FLOAT', {'default': 0.09941396206337118, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_01': ('FLOAT', {'default': 0.12050177219802567, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_02': ('FLOAT', {'default': 0.14606275417942507, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_03': ('FLOAT', {'default': 0.17704576264172736, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_04': ('FLOAT', {'default': 0.214600924414215, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_05': ('FLOAT', {'default': 0.26012233262329093, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_06': ('FLOAT', {'default': 0.3152997971191405, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_07': ('FLOAT', {'default': 0.3821815722656249, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_08': ('FLOAT', {'default': 0.4632503906249999, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_09': ('FLOAT', {'default': 0.561515625, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_10': ('FLOAT', {'default': 0.6806249999999999, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_11': ('FLOAT', {'default': 0.825, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_12': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'flip_weights': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('CONTROL_NET_WEIGHTS', 'TIMESTEP_KEYFRAME')
    RETURN_NAMES = WEIGHTS_RETURN_NAMES
    FUNCTION = 'load_weights'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/weights/ControlNet'

    def load_weights(self, weight_00, weight_01, weight_02, weight_03, weight_04, weight_05, weight_06, weight_07, weight_08, weight_09, weight_10, weight_11, weight_12, flip_weights):
        weights = [weight_00, weight_01, weight_02, weight_03, weight_04, weight_05, weight_06, weight_07, weight_08, weight_09, weight_10, weight_11, weight_12]
        weights = ControlWeights.controlnet(weights, flip_weights=flip_weights)
        return (weights, TimestepKeyframeGroup.default(TimestepKeyframe(control_weights=weights)))
```