# Documentation
- Class name: unCLIPConditioning
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The unCLIPConditioning node is designed to modify and enhance the modem's reconciliation input, allowing for more detailed control of the generation process. This is achieved by adding additional parameters to the reconciliation input, which can include factors such as intensity and noise enhancement to improve the output result.

# Input types
## Required
- conditioning
    - The reconciliation parameter is essential because it defines the basic input that will guide model output. It is a set of elements that play a decisive role in determining the characteristics and properties that generate the content.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, dict]]
- clip_vision_output
    - As the basis of the reconciliation process, this parameter provides the model with a reference for the desired output. It plays a crucial role in shaping the final result and ensuring that it is consistent with the desired direction.
    - Comfy dtype: CLIP_VISION_OUTPUT
    - Python dtype: Dict[str, Any]
- strength
    - Strength parameters are used as modifiers to regulate input, allowing fine-tuning of model output to reach the desired level of detail or intensity.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_augmentation
    - This parameter introduces a certain amount of randomity in the reconciliation process, which can lead to more diverse and creative output. This is an important aspect for increasing the generation of diversity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - The output reconciliation represents an enhanced and modified input adjusted to the parameters provided. This optimized input will eventually guide the model generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, dict]]

# Usage tips
- Infra type: CPU

# Source code
```
class unCLIPConditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'clip_vision_output': ('CLIP_VISION_OUTPUT',), 'strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'noise_augmentation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'apply_adm'
    CATEGORY = 'conditioning'

    def apply_adm(self, conditioning, clip_vision_output, strength, noise_augmentation):
        if strength == 0:
            return (conditioning,)
        c = []
        for t in conditioning:
            o = t[1].copy()
            x = {'clip_vision_output': clip_vision_output, 'strength': strength, 'noise_augmentation': noise_augmentation}
            if 'unclip_conditioning' in o:
                o['unclip_conditioning'] = o['unclip_conditioning'][:] + [x]
            else:
                o['unclip_conditioning'] = [x]
            n = [t[0], o]
            c.append(n)
        return (c,)
```