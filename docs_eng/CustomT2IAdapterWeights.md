# Documentation
- Class name: CustomT2IAdapterWeights
- Category: Adv-ControlNet 🛂🅐🅒🅝/weights/T2IAdapter
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The CustomT2IAdapterWeights node is designed to manage and adjust the weights of the control network, especially for converting input data into the desired output shape. It emphasizes the custom weight distribution on different key frames to achieve precise control of the conversion process.

# Input types
## Required
- weight_00
    - The weight_00 parameter is essential to define the initial impact of the conversion. It sets a baseline for the initial weight of the input data in the control network, affecting the overall balance of the conversion process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_01
    - The weight_01 parameter further refines the conversion process by adjusting the intermediate weight value. It plays an important role in the transition between key frames, ensuring smooth and consistent conversions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_02
    - The weight_02 parameter is essential to control the distribution of weights at a later stage of conversion. It ensures that conversions maintain the desired direction and intensity as they move towards the final key frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_03
    - The weight_03 parameter determines the ultimate impact of the conversion, ensuring that the output closely matches the shape required. It is a key component of the accuracy required to achieve the final stage of the conversion process.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- flip_weights
    - The flip_weights parameter allows for a reversal of the weight distribution, which provides an additional layer of control for the conversion direction. This may be particularly useful when the conversion requires a reversal of the order of application of the standard weights.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- CONTROL_NET_WEIGHTS
    - The CONTROL_NET_WEIGHTS output represents the adaptive weights that are customised and arranged to control the network. These weights are essential in guiding the network to achieve the desired output shape.
    - Comfy dtype: ControlWeights
    - Python dtype: ControlWeights
- TIMESTEP_KEYFRAME
    - The TIMESTEP_KEYFRAME output is a set of key frames corresponding to a given point in the conversion process. These frames play an important role in defining the time structure and progress of the conversion.
    - Comfy dtype: TimestepKeyframeGroup
    - Python dtype: TimestepKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class CustomT2IAdapterWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'weight_00': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_01': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_02': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'weight_03': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'flip_weights': ('BOOLEAN', {'default': False})}}
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