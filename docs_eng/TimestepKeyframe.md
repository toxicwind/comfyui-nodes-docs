# Documentation
- Class name: TimestepKeyframeNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/keyframes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

TimestepKeyframameNode is a key component in the process of generating an advanced control network key frame. It is designed to facilitate the creation and operation of the key frame according to specified parameters, such as percentage and intensity. This node plays a crucial role in defining animated or simulated time structures to ensure smooth and consistent transitions between states.

# Input types
## Required
- start_percent
    - Start_percent parameters define the initial position of the key frame in the time line, which is essential for determining the sequence of events in the animation. It affects how the key frame interacts with other elements and helps with the overall animation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- strength
    - Strength parameters adjust the impact of the key frame on the overall animation. It allows fine-tuning of the impact of the key frame to ensure that it contributes to the animation in a manner consistent with the creative vision.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cn_weights
    - cn_rights parameters specify the weight to be applied to the control network, which is essential for creating animated responses to key frames. It is a key aspect of achieving desired results and outcomes.
    - Comfy dtype: CONTROL_NET_WEIGHTS
    - Python dtype: ControlWeights
- latent_keyframe
    - The latent_keyframe parameter provides a method for incorporating potential key frames into animations, adding depth and complexity to the sequence of events. It is an important tool for creating complex and detailed animations.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Output types
- TIMESTEP_KF
    - The output of TimestepKeyframeNode, which represents a moment in an animation with specific properties (e.g. starting percentage and strength). This output is very important because it forms the basis for animating follow-up and rendering.
    - Comfy dtype: TIMESTEP_KEYFRAME
    - Python dtype: TimestepKeyframe

# Usage tips
- Infra type: CPU

# Source code
```
class TimestepKeyframeNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'prev_timestep_kf': ('TIMESTEP_KEYFRAME',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'cn_weights': ('CONTROL_NET_WEIGHTS',), 'latent_keyframe': ('LATENT_KEYFRAME',), 'null_latent_kf_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'inherit_missing': ('BOOLEAN', {'default': True}), 'guarantee_usage': ('BOOLEAN', {'default': True}), 'mask_optional': ('MASK',)}}
    RETURN_NAMES = ('TIMESTEP_KF',)
    RETURN_TYPES = ('TIMESTEP_KEYFRAME',)
    FUNCTION = 'load_keyframe'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/keyframes'

    def load_keyframe(self, start_percent: float, strength: float=1.0, cn_weights: ControlWeights=None, control_net_weights: ControlWeights=None, latent_keyframe: LatentKeyframeGroup=None, prev_timestep_kf: TimestepKeyframeGroup=None, prev_timestep_keyframe: TimestepKeyframeGroup=None, null_latent_kf_strength: float=0.0, inherit_missing=True, guarantee_usage=True, mask_optional=None, interpolation: str=SI.NONE):
        control_net_weights = control_net_weights if control_net_weights else cn_weights
        prev_timestep_keyframe = prev_timestep_keyframe if prev_timestep_keyframe else prev_timestep_kf
        if not prev_timestep_keyframe:
            prev_timestep_keyframe = TimestepKeyframeGroup()
        else:
            prev_timestep_keyframe = prev_timestep_keyframe.clone()
        keyframe = TimestepKeyframe(start_percent=start_percent, strength=strength, interpolation=interpolation, null_latent_kf_strength=null_latent_kf_strength, control_weights=control_net_weights, latent_keyframes=latent_keyframe, inherit_missing=inherit_missing, guarantee_usage=guarantee_usage, mask_hint_orig=mask_optional)
        prev_timestep_keyframe.add(keyframe)
        return (prev_timestep_keyframe,)
```