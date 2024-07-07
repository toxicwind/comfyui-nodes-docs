# Documentation
- Class name: ScaledSoftMaskedUniversalWeights
- Category: Adv-ControlNet 🛂🅐🅒🅝/weights
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

Class `ScaledSoft MaskedUniversalWeights'aims to process and apply a soft mask to the base weight of the control network. It accepts a mask stretch and two multipliers to zoom the mask value to ensure that they fall within a specified range. The method also provides the option of locking the minimum and maximum value of the mask, preventing any adjustment beyond the given limit. This function is essential for fine-tuning the impact of control on network output.

# Input types
## Required
- mask
    - The parameter'mask'is a volume that defines the soft mask to be applied to the control weight. It plays a key role in determining the extent to which the base weight is modified. The value of the mask is scaled according to the multiplier provided, making it a key component in the weight adjustment process.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
- min_base_multiplier
    - The parameter'min_base_multiplier'sets the lower limit of the zoom mask value. It is essential to control the minimum impact of the mask on the weight of control. This parameter ensures that the mask is not too subtle and allows for clear and obvious adjustments in network behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_base_multiplier
    - The parameter'max_base_multiplier'determines the upper limit of the zoom mask value. It is essential to control the maximum impact of the mask on the weight of control. By setting this parameter, the user can prevent the mask from overriding the base weight, maintaining the balance between the original weight and the modified weight.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONTROL_NET_WEIGHTS
    - The output 'CONTROL_NET_WEIGHTS' represents the adjusted control weight of the network following the application of the scalable soft mask. This output is important because it directly affects the final output of the control network and reflects modifications based on input mask and multipliers.
    - Comfy dtype: ControlWeights
    - Python dtype: comfy.ControlWeights
- TIMESTEP_KEYFRAME
    - The output 'TIMESTEP_KEYFRAME'provides a default key frame with the weight of control at a given point in time. It is important to define the time structure of the weight of control and allows dynamic adjustments over time.
    - Comfy dtype: TimestepKeyframe
    - Python dtype: comfy.TimestepKeyframe

# Usage tips
- Infra type: CPU

# Source code
```
class ScaledSoftMaskedUniversalWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'min_base_multiplier': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'max_base_multiplier': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('CONTROL_NET_WEIGHTS', 'TIMESTEP_KEYFRAME')
    RETURN_NAMES = WEIGHTS_RETURN_NAMES
    FUNCTION = 'load_weights'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/weights'

    def load_weights(self, mask: Tensor, min_base_multiplier: float, max_base_multiplier: float, lock_min=False, lock_max=False):
        mask = mask.clone()
        x_min = 0.0 if lock_min else mask.min()
        x_max = 1.0 if lock_max else mask.max()
        if x_min == x_max:
            mask = torch.ones_like(mask) * max_base_multiplier
        else:
            mask = linear_conversion(mask, x_min, x_max, min_base_multiplier, max_base_multiplier)
        weights = ControlWeights.universal_mask(weight_mask=mask)
        return (weights, TimestepKeyframeGroup.default(TimestepKeyframe(control_weights=weights)))
```