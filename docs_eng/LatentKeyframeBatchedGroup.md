# Documentation
- Class name: LatentKeyframeBatchedGroupNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/keyframes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

LatentKeyframeBatchedGroupNode is designed to manage and create a set of potentially critical frames with varying degrees of intensity. It allows the potential key frames before integration and provides the function to print detailed information on the key frames. This node plays a key role in the generation and operation of the key frames within the ControlNet framework.

# Input types
## Required
- float_strengths
    - The 'float_strengths' parameter is essential for determining the strength of each key frame in the batch. It can be a stand-alone floating point number or an altruistic object with a direct influence on the creation of the key frame within the node.
    - Comfy dtype: FLOAT
    - Python dtype: Union[float, List[float]]
## Optional
- prev_latent_kf
    - The 'prev_latent_kf' parameter allows the integration of the former potential key frame groups into the current operation. This is particularly useful for building on the existing key frame structure.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: Optional[LatentKeyframeGroup]
- print_keyframes
    - If the 'print_keyframes' parameter is set to True, log records of key frame information will be enabled. This is very helpful in debuging and understanding the key frame's flow through nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- LATENT_KF
    - The 'LATENT_KF' output represents the potential critical frame batch that is obtained after processing input strength and consolidating any of the previous key frames. This is the key output that is further processed in the ControlNet system.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class LatentKeyframeBatchedGroupNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'float_strengths': ('FLOAT', {'default': -1, 'min': -1, 'step': 0.001, 'forceInput': True})}, 'optional': {'prev_latent_kf': ('LATENT_KEYFRAME',), 'print_keyframes': ('BOOLEAN', {'default': False})}}
    RETURN_NAMES = ('LATENT_KF',)
    RETURN_TYPES = ('LATENT_KEYFRAME',)
    FUNCTION = 'load_keyframe'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/keyframes'

    def load_keyframe(self, float_strengths: Union[float, list[float]], prev_latent_kf: LatentKeyframeGroup=None, prev_latent_keyframe: LatentKeyframeGroup=None, print_keyframes=False):
        prev_latent_keyframe = prev_latent_keyframe if prev_latent_keyframe else prev_latent_kf
        if not prev_latent_keyframe:
            prev_latent_keyframe = LatentKeyframeGroup()
        else:
            prev_latent_keyframe = prev_latent_keyframe.clone()
        curr_latent_keyframe = LatentKeyframeGroup()
        if type(float_strengths) in (float, int):
            logger.info('No batched float_strengths passed into Latent Keyframe Batch Group node; will not create any new keyframes.')
        elif isinstance(float_strengths, Iterable):
            for (idx, strength) in enumerate(float_strengths):
                keyframe = LatentKeyframe(idx, strength)
                curr_latent_keyframe.add(keyframe)
        else:
            raise ValueError(f'Expected strengths to be an iterable input, but was {type(float_strengths).__repr__}.')
        if print_keyframes:
            for keyframe in curr_latent_keyframe.keyframes:
                logger.info(f'keyframe {keyframe.batch_index}:{keyframe.strength}')
        for latent_keyframe in prev_latent_keyframe.keyframes:
            curr_latent_keyframe.add(latent_keyframe)
        return (curr_latent_keyframe,)
```