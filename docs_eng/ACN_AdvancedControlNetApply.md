# Documentation
- Class name: AdvancedControlNetApply
- Category: Adv-ControlNet 🛂🅐🅒🅝
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The AdvancedControlNetApply node is designed to apply the control signal to the neural network model. It integrates both positive and negative regulatory input and controls the network to influence model output. The node can adjust the strength and scope of the control signal to ensure a fine and precise manipulation of model behaviour.

# Input types
## Required
- positive
    - Entering the reconciliation is essential to guide the model towards the desired results. It serves as a reference for the model to learn and apply in its generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[Tensor, Iterable[Tuple[str, Dict]]]
- negative
    - Negative adjustment input helps the model avoid the desired output by providing examples that should be excluded during the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[Tensor, Iterable[Tuple[str, Dict]]]
- control_net
    - The control network is a key component that determines how model output is affected. It is used to apply specific control signals to different parts of the model.
    - Comfy dtype: CONTROL_NET
    - Python dtype: ControlBase
- image
    - Image input provides a visual context for the model, which is essential for generating outputs consistent with the visual information provided.
    - Comfy dtype: IMAGE
    - Python dtype: Tensor
- strength
    - The strength parameters determine the strength of the control signal applied to the model. It allows fine-tuning of the influence of the network on model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The starting percentage parameter defines the starting point for controlling the impact of the signal and allows the control effect to take effect at the time.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - End percentage parameters mark the end point for controlling the impact of the signal, making the duration of the control effect manageable.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- mask_optional
    - The optional mask input, which can be used to selectively apply control signals to specific areas of model output, provides a means of fine-tuning local control effects.
    - Comfy dtype: MASK
    - Python dtype: Optional[Tensor]
- model_optional
    - Model_optional parameters allow for the provision of another model that can be used to further refine the control signals applied to the main model.
    - Comfy dtype: MODEL
    - Python dtype: Optional[ModelPatcher]
- timestep_kf
    - Time-step key input is the time structure used to define the control signal and allows for dynamic control over time.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: Optional[TimestepKeyframeGroup]
- latent_kf_override
    - Potential key frame coverage allows custom control signals to affect the potential space of the model and provides a method that directly affects the internal expression of the model.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: Optional[LatentKeyframeGroup]
- weights_override
    - The weight-over parameters allow the designation of custom weights for the control network and allow for higher-level control over the fine-tuning of the control signal.
    - Comfy dtype: CONTROL_NET_WEIGHTS
    - Python dtype: Optional[ControlWeights]

# Output types
- positive
    - The output is representing the modified reconciliation input of the application control network, reflecting the model's understanding of the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[Tensor, Iterable[Tuple[str, Dict]]]
- negative
    - Negative output includes a modified reconciliation input that is based on the control network and that the model should avoid.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[Tensor, Iterable[Tuple[str, Dict]]]
- model_opt
    - The optional model output provides any updates or improvements to the model during the application control network.
    - Comfy dtype: MODEL
    - Python dtype: Optional[ModelPatcher]

# Usage tips
- Infra type: GPU

# Source code
```
class AdvancedControlNetApply:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'mask_optional': ('MASK',), 'timestep_kf': ('TIMESTEP_KEYFRAME',), 'latent_kf_override': ('LATENT_KEYFRAME',), 'weights_override': ('CONTROL_NET_WEIGHTS',), 'model_optional': ('MODEL',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'MODEL')
    RETURN_NAMES = ('positive', 'negative', 'model_opt')
    FUNCTION = 'apply_controlnet'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝'

    def apply_controlnet(self, positive, negative, control_net, image, strength, start_percent, end_percent, mask_optional: Tensor=None, model_optional: ModelPatcher=None, timestep_kf: TimestepKeyframeGroup=None, latent_kf_override: LatentKeyframeGroup=None, weights_override: ControlWeights=None):
        if strength == 0:
            return (positive, negative, model_optional)
        if model_optional:
            model_optional = model_optional.clone()
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
                    c_net = convert_to_advanced(control_net.copy()).set_cond_hint(control_hint, strength, (start_percent, end_percent))
                    if is_advanced_controlnet(c_net):
                        c_net.disarm()
                        if c_net.require_model:
                            if not model_optional:
                                raise Exception(f"Type '{type(c_net).__name__}' requires model_optional input, but got None.")
                            c_net.patch_model(model=model_optional)
                        if timestep_kf is not None:
                            c_net.set_timestep_keyframes(timestep_kf)
                        if latent_kf_override is not None:
                            c_net.latent_keyframe_override = latent_kf_override
                        if weights_override is not None:
                            c_net.weights_override = weights_override
                        c_net.verify_all_weights()
                        if mask_optional is not None:
                            mask_optional = mask_optional.clone()
                            if len(mask_optional.shape) < 3:
                                mask_optional = mask_optional.unsqueeze(0)
                            c_net.set_cond_hint_mask(mask_optional)
                    c_net.set_previous_controlnet(prev_cnet)
                    cnets[prev_cnet] = c_net
                d['control'] = c_net
                d['control_apply_to_uncond'] = False
                n = [t[0], d]
                c.append(n)
            out.append(c)
        return (out[0], out[1], model_optional)
```