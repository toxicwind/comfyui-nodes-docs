# Documentation
- Class name: ControlNetApplyAdvanced
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ControlNetApplyAdvanced node is designed to apply the control network to a set of conditions to improve the accuracy and control of the generation process. It operates by adjusting the effects of both positive and negative conditions, allowing for fine-tuning of the output according to the specific image characteristics and the required intensity.

# Input types
## Required
- positive
    - The 'positive' input represents the desired characteristics that should be highlighted in the output. It is essential to guide the generation process towards the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - The "negative" input contains features that should be avoided in the output. It plays an important role in extracting elements that are not needed.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- control_net
    - The " control_net " parameter is the pre-configuration network used to manage the application of control tips. It is essential for the function of the node and determines how conditions are applied.
    - Comfy dtype: CONTROL_NET
    - Python dtype: ControlNet
- image
    - The "image " input is the visual data that will be used to control the network. It is an essential component because it defines the context of the condition process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- strength
    - The “strength” parameter determines the intensity of the control network’s influence on the output. It is a key factor in the extent of change caused by the control conditions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The " start_percent " parameter specifies the starting point for controlling network effects relative to the size of the image. It is important in defining the initial scope of the control application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - The "end_percent" parameter marks the end point of control of the network's influence. It is essential in defining the range of control of the network's influence output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- positive
    - The “positive” output is the refined condition data adjusted by the control network to ensure that the required characteristics become more prominent in the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - The “negative” output reflects the condition data that minimizes the required characteristics by controlling network applications.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ControlNetApplyAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('positive', 'negative')
    FUNCTION = 'apply_controlnet'
    CATEGORY = 'conditioning'

    def apply_controlnet(self, positive, negative, control_net, image, strength, start_percent, end_percent):
        if strength == 0:
            return (positive, negative)
        control_hint = image.movedim(-1, 1)
        cnets = {}
        out = []
        for conditioning in [positive, negative]:
            c = []
            for t in conditioning:
                d = t[1].copy()
                prev_cnet = d.get('control', None)
                if prev_cnet in cnets:
                    c_net = cnets[prev_cnet]
                else:
                    c_net = control_net.copy().set_cond_hint(control_hint, strength, (start_percent, end_percent))
                    c_net.set_previous_controlnet(prev_cnet)
                    cnets[prev_cnet] = c_net
                d['control'] = c_net
                d['control_apply_to_uncond'] = False
                n = [t[0], d]
                c.append(n)
            out.append(c)
        return (out[0], out[1])
```