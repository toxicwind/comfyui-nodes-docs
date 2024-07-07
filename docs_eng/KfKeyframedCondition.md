# Documentation
- Class name: KfKeyframedCondition
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfKeyframedCondition node is designed to integrate condition elements into the key frame structure, allowing for the operation and conversion of data at different points in time. It plays a key role in dynamic adjustment of conditions in the sequence to ensure a smooth and consistent transition between states.

# Input types
## Required
- conditioning
    - The conditioning parameter is essential to define the initial state or condition that will be applied in a given frame. It sets the basis for subsequent conversions and plug-ins and affects the overall behaviour of the sequence.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]
## Optional
- time
    - The time parameter specifies the time position in which the conditions will be attached to the sequence. It is essential to determine the order of conditions and their impact on the system's evolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- interpolation_method
    - The plug-in method determines how conditions transition between the key frames. It is important for creating the natural flow of the conditions and can greatly influence the final output of the sequence.
    - Comfy dtype: COMBO[linear, easeIn, easeOut, easeInOut]
    - Python dtype: str

# Output types
- kf_cond_t
    - The kf_cond_t output represents the key frame conditions for the specified time, including the post-conversion conditions and their plug-in method. It is a key component of the sequence that guides the system state.
    - Comfy dtype: KEYFRAMED_CONDITION
    - Python dtype: kf.Keyframe
- kf_cond_pooled
    - When an output of kf_cond_pooled exists, it provides an additional layer of conditions to be applied at the specified time. It contributes to the complexity and nuances of the system's evolving state.
    - Comfy dtype: KEYFRAMED_CONDITION
    - Python dtype: Optional[kf.Keyframe]
- cond_dict
    - Cond_dict output is a dictionary with detailed information on conditions, including any pool output. It serves as a reference for specifying the state of the time conditions for further analysis and processing.
    - Comfy dtype: Dict[str, torch.Tensor]
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class KfKeyframedCondition:
    """
    Attaches a condition to a keyframe
    """
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CONDITION',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING', {}), 'time': ('FLOAT', {'default': 0, 'step': 1}), 'interpolation_method': (list(kf.interpolation.EASINGS.keys()), {'default': 'linear'})}}

    def main(self, conditioning, time, interpolation_method):
        (cond_tensor, cond_dict) = conditioning[0]
        cond_tensor = cond_tensor.clone()
        kf_cond_t = kf.Keyframe(t=time, value=cond_tensor, interpolation_method=interpolation_method)
        cond_pooled = cond_dict.get('pooled_output')
        cond_dict = deepcopy(cond_dict)
        kf_cond_pooled = None
        if cond_pooled is not None:
            cond_pooled = cond_pooled.clone()
            kf_cond_pooled = kf.Keyframe(t=time, value=cond_pooled, interpolation_method=interpolation_method)
            cond_dict['pooled_output'] = cond_pooled
        return ({'kf_cond_t': kf_cond_t, 'kf_cond_pooled': kf_cond_pooled, 'cond_dict': cond_dict},)
```