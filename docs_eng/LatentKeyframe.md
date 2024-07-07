# Documentation
- Class name: LatentKeyframeNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/keyframes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

The node is intended to manage and operate the key frame in the control network, focusing on the integration of new key frames based on batch indexes and intensity parameters. It facilitates the organization and flow of key frame data and ensures the smooth operation of the control network.

# Input types
## Required
- batch_index
    - Batch index is a key parameter that determines the location of the key frame in the batch process. It is essential for nodes to properly organize and quote the key frame to ensure accurate data flow and synchronization within the system.
    - Comfy dtype: INT
    - Python dtype: int
- strength
    - The strength parameter influences the weight of the key frame in controlling the network as a whole. It is important in determining the impact of the key frame on the final output, and thus plays a key role in the function of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- prev_latent_kf
    - This parameter represents the previous set of key frames that nodes use to construct and integrate. It is important to maintain continuity and consistency in controlling network operations.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Output types
- LATENT_KF
    - Output is the updated key frame group that contains the newly added key frame. This is important because it represents progress in controlling the network and reflects changes and adjustments made through node operations.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class LatentKeyframeNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_index': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX, 'step': 1}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'prev_latent_kf': ('LATENT_KEYFRAME',)}}
    RETURN_NAMES = ('LATENT_KF',)
    RETURN_TYPES = ('LATENT_KEYFRAME',)
    FUNCTION = 'load_keyframe'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/keyframes'

    def load_keyframe(self, batch_index: int, strength: float, prev_latent_kf: LatentKeyframeGroup=None, prev_latent_keyframe: LatentKeyframeGroup=None):
        prev_latent_keyframe = prev_latent_keyframe if prev_latent_keyframe else prev_latent_kf
        if not prev_latent_keyframe:
            prev_latent_keyframe = LatentKeyframeGroup()
        else:
            prev_latent_keyframe = prev_latent_keyframe.clone()
        keyframe = LatentKeyframe(batch_index, strength)
        prev_latent_keyframe.add(keyframe)
        return (prev_latent_keyframe,)
```