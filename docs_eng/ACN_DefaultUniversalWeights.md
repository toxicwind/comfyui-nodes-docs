# Documentation
- Class name: DefaultWeights
- Category: Adv-ControlNet 🛂🅐🅒🅝/weights
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The 'load_weights' method at the DefaultWeights nodes is designed to initialize and return a default control weight and corresponding time-step key group. It is the basic building component for the control network, ensuring that the system has a baseline concentration of rights to operate.

# Input types

# Output types
- CONTROL_NET_WEIGHTS
    - CONTROL_NET_WEIGHS output parameters represent the default control weight of the network. It is a key element in shaping control of network behaviour, as it defines the initial weight to be used in subsequent calculations and adjustments.
    - Comfy dtype: ControlWeights
    - Python dtype: ControlWeights
- TIMESTEP_KEYFRAME
    - TIMESTEP_KEYFRAME output parameters encapsulate key frames that are reconnected to control. It plays an important role in controlling the network’s temporal dynamics, providing a structured approach to managing and applying weights over time.
    - Comfy dtype: TimestepKeyframeGroup
    - Python dtype: TimestepKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class DefaultWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ('CONTROL_NET_WEIGHTS', 'TIMESTEP_KEYFRAME')
    RETURN_NAMES = WEIGHTS_RETURN_NAMES
    FUNCTION = 'load_weights'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/weights'

    def load_weights(self):
        weights = ControlWeights.default()
        return (weights, TimestepKeyframeGroup.default(TimestepKeyframe(control_weights=weights)))
```