# Documentation
- Class name: CR_ApplyControlNet
- Category: ControlNet
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ApplyControlNet is designed to integrate the control network into the image generation process, allowing the application of specific conditions and adjustments to improve the output. It plays a key role in enhancing the control and quality of the image generation by using intensity parameters and switch mechanisms.

# Input types
## Required
- conditioning
    - Conditional parameters are essential to define the initial state or context of the image generation. They provide the basis for controlling the operation of the network and have a significant impact on the characteristics of the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- control_net
    - Controls the network parameters as a guiding framework for generating images according to the conditions provided. It is the key component for achieving the results required for node operations.
    - Comfy dtype: CONTROL_NET
    - Python dtype: comfy.controlnet.ControlNet
- image
    - Image input is the original material that the control network will process. It is the basis of the node function, as it is the entity that will be converted under the influence of the control network.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- switch
    - Switch parameters determine whether to apply the influence of the control network. It is used as a switcher to enable or disable the core function of the node, thereby controlling the behaviour of the node.
    - Comfy dtype: COMBO[On, Off]
    - Python dtype: str
- strength
    - Intensity parameter reconciliation controls the strength of the network’s influence on the image-generation process. It allows fine-tuning of the network’s effects in order to achieve a balance between control and creativity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONDITIONING
    - The output conditions provide the conversion status or context of the application control network, and the fine conditions for further processing or analysis are enclosed.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- show_help
    - Show_help output provides document links to further assist and guide the effective use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ApplyControlNet:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'switch': (['On', 'Off'],), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING', 'STRING')
    RETURN_NAMES = ('CONDITIONING', 'show_help')
    FUNCTION = 'apply_controlnet'
    CATEGORY = icons.get('Comfyroll/ControlNet')

    def apply_controlnet(self, conditioning, control_net, image, switch, strength):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/ControlNet-Nodes#cr-apply-controlnet'
        if strength == 0 or switch == 'Off':
            return (conditioning, show_help)
        c = []
        control_hint = image.movedim(-1, 1)
        for t in conditioning:
            n = [t[0], t[1].copy()]
            c_net = control_net.copy().set_cond_hint(control_hint, strength)
            if 'control' in t[1]:
                c_net.set_previous_controlnet(t[1]['control'])
            n[1]['control'] = c_net
            c.append(n)
        return (c, show_help)
```