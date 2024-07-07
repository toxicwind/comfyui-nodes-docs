# Documentation
- Class name: ControlNetApply
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The 'apply_controlnet'method in the ControlNetApply class is designed to integrate the control signal into the neural network processing process. It receives condition data, control networks, images and a strength parameter to regulate the influence of the control network on the image. The purpose of this method is to use the guidance of the control network to enhance the image, ensuring that the conditions for output reflect anticipated adjustments based on the specified strength.

# Input types
## Required
- conditioning
    - The `conventioning' parameter is essential to the operation of the node because it provides the control network with the initial status or context in which its modifications are applied. This is a key input that directly affects the results of image processing.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- control_net
    - The `control_net' parameter defines the network that will guide changes to the image. It is a necessary input that plays a central role in forming the final output for node processing.
    - Comfy dtype: CONTROL_NET
    - Python dtype: torch.nn.Module
- image
    - The 'image'parameter is the object of the control network modification. It represents the data that will be enhanced or modified according to the control signal provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- strength
    - The'strength' parameter adjusts the intensity of the network's influence on the image. It is an optional input that allows fine-tuning to be applied to the degree of modification of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - Output 'conventioning' indicates the modified state after applying the influence of the control network. It is important because it carries with it the final adjustment of the original image data.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ControlNetApply:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'apply_controlnet'
    CATEGORY = 'conditioning'

    def apply_controlnet(self, conditioning, control_net, image, strength):
        if strength == 0:
            return (conditioning,)
        c = []
        control_hint = image.movedim(-1, 1)
        for t in conditioning:
            n = [t[0], t[1].copy()]
            c_net = control_net.copy().set_cond_hint(control_hint, strength)
            if 'control' in t[1]:
                c_net.set_previous_controlnet(t[1]['control'])
            n[1]['control'] = c_net
            n[1]['control_apply_to_uncond'] = True
            c.append(n)
        return (c,)
```