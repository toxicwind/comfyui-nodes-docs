# Documentation
- Class name: ApplyInstantIDControlNet
- Category: InstantID
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

The node changes the facial features of the image based on a given embedded and key point information control network. It adjusts the facial appearance to the specified positive and negative adjustment input and allows fine-tuning of facial expressions and structures.

# Input types
## Required
- face_embeds
    - This parameter, which includes facial embedding, is essential for the operation of nodes, as it provides a basic indication of the face to be operated.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]
- control_net
    - The control network is essential for applying changes in facial features. It is a guide to changes based on the reconciliation input.
    - Comfy dtype: CONTROL_NET
    - Python dtype: torch.nn.Module
- image_kps
    - The key point information for the image is critical, as it provides the spatial context for facial features and ensures accurate adaptation to the control network.
    - Comfy dtype: IMAGE
    - Python dtype: np.ndarray
- positive
    - Positive adjustment input is used as a reference for the desired facial characteristics to guide the node towards the desired appearance.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- negative
    - Negative adjustment input is compared with the positive input, helping to avoid undesirable features and improve the accuracy of facial adjustments.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- strength
    - The intensity parameters determine the intensity of the control of the network's effects on facial features and allow for subtle or significant changes based on input values.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - This parameter defines the starting point for controlling the influence of the network, allowing nodes to apply changes gradually or from the outset.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End-point parameters specify when to end the control network adjustment to ensure the controlled transition of facial features.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- mask
    - When providing mask parameters, it allows targeted adjustments by specifying the image areas that should be applied or excluded.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- positive
    - The output's positive parameter represents a modified facial characteristic based on the input positive reconciliation, reflecting the adjustment of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- negative
    - The negative parameters of the output show the changes made to the negative adjustment of input and the ability of nodes to perfect facial features while avoiding undesirable traits.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: GPU

# Source code
```
class ApplyInstantIDControlNet:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'face_embeds': ('FACE_EMBEDS',), 'control_net': ('CONTROL_NET',), 'image_kps': ('IMAGE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'mask': ('MASK',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('positive', 'negative')
    FUNCTION = 'apply_controlnet'
    CATEGORY = 'InstantID'

    def apply_controlnet(self, face_embeds, control_net, image_kps, positive, negative, strength, start_at, end_at, mask=None):
        self.device = comfy.model_management.get_torch_device()
        if strength == 0:
            return (positive, negative)
        if mask is not None:
            mask = mask.to(self.device)
        if mask is not None and len(mask.shape) < 3:
            mask = mask.unsqueeze(0)
        image_prompt_embeds = face_embeds['cond']
        uncond_image_prompt_embeds = face_embeds['uncond']
        cnets = {}
        cond_uncond = []
        control_hint = image_kps.movedim(-1, 1)
        is_cond = True
        for conditioning in [positive, negative]:
            c = []
            for t in conditioning:
                d = t[1].copy()
                prev_cnet = d.get('control', None)
                if prev_cnet in cnets:
                    c_net = cnets[prev_cnet]
                else:
                    c_net = control_net.copy().set_cond_hint(control_hint, strength, (start_at, end_at))
                    c_net.set_previous_controlnet(prev_cnet)
                    cnets[prev_cnet] = c_net
                d['control'] = c_net
                d['control_apply_to_uncond'] = False
                d['cross_attn_controlnet'] = image_prompt_embeds.to(comfy.model_management.intermediate_device()) if is_cond else uncond_image_prompt_embeds.to(comfy.model_management.intermediate_device())
                if mask is not None and is_cond:
                    d['mask'] = mask
                    d['set_area_to_bounds'] = False
                n = [t[0], d]
                c.append(n)
            cond_uncond.append(c)
            is_cond = False
            print(cond_uncond[0])
        return (cond_uncond[0], cond_uncond[1])
```