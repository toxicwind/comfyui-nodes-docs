# Documentation
- Class name: LatentKeyframeInterpolationNode
- Category: Adv-ControlNet 🛂🅐🅒🅝/keyframes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

LatentKeyframeInterpolationNode aims to insert key frames in potential space, allowing smooth transition during generation. This is done by calculating the intermediate key frames based on specified strength and plug-in methods (which can be linear or various buffer functions). This node plays a key role in enhancing the flow and control of potential indications.

# Input types
## Required
- batch_index_from
    - The batch index that starts with the plug value defines the initial position in the key frame sequence. This is essential for determining the starting point of the transition.
    - Comfy dtype: INT
    - Python dtype: int
- strength_from
    - The strength value of the starting key frame, which affects the strength of the initial state during the plug-in process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_index_to_excl
    - The batch index that calculates the plug value does not include the index itself, defining the end position of the sequence.
    - Comfy dtype: INT
    - Python dtype: int
- strength_to
    - Ends the strength of the key frame and determines the strength of the final state after the plug value.
    - Comfy dtype: FLOAT
    - Python dtype: float
- interpolation
    - The type of plug value used between the key frames may be linear or a buffer function to achieve a more natural transition.
    - Comfy dtype: COMBO[LINEAR, EASE_IN, EASE_OUT, EASE_IN_OUT]
    - Python dtype: str
## Optional
- prev_latent_kf
    - An optional pre-existing potential key group, which provides context for the plug value, allows for a more informative process of generation.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup
- print_keyframes
    - A boolean flag, when set to true, will print the details of the key frame generated for debugging purposes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- LATENT_KF
    - The resulting plug-in potential key group represents the transition between the initial and final state.
    - Comfy dtype: LATENT_KEYFRAME
    - Python dtype: LatentKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class LatentKeyframeInterpolationNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_index_from': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX, 'step': 1}), 'batch_index_to_excl': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX, 'step': 1}), 'strength_from': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'strength_to': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'interpolation': ([SI.LINEAR, SI.EASE_IN, SI.EASE_OUT, SI.EASE_IN_OUT],)}, 'optional': {'prev_latent_kf': ('LATENT_KEYFRAME',), 'print_keyframes': ('BOOLEAN', {'default': False})}}
    RETURN_NAMES = ('LATENT_KF',)
    RETURN_TYPES = ('LATENT_KEYFRAME',)
    FUNCTION = 'load_keyframe'
    CATEGORY = 'Adv-ControlNet 🛂🅐🅒🅝/keyframes'

    def load_keyframe(self, batch_index_from: int, strength_from: float, batch_index_to_excl: int, strength_to: float, interpolation: str, prev_latent_kf: LatentKeyframeGroup=None, prev_latent_keyframe: LatentKeyframeGroup=None, print_keyframes=False):
        if batch_index_from > batch_index_to_excl:
            raise ValueError('batch_index_from must be less than or equal to batch_index_to.')
        if batch_index_from < 0 and batch_index_to_excl >= 0:
            raise ValueError('batch_index_from and batch_index_to must be either both positive or both negative.')
        prev_latent_keyframe = prev_latent_keyframe if prev_latent_keyframe else prev_latent_kf
        if not prev_latent_keyframe:
            prev_latent_keyframe = LatentKeyframeGroup()
        else:
            prev_latent_keyframe = prev_latent_keyframe.clone()
        curr_latent_keyframe = LatentKeyframeGroup()
        steps = batch_index_to_excl - batch_index_from
        diff = strength_to - strength_from
        if interpolation == SI.LINEAR:
            weights = np.linspace(strength_from, strength_to, steps)
        elif interpolation == SI.EASE_IN:
            index = np.linspace(0, 1, steps)
            weights = diff * np.power(index, 2) + strength_from
        elif interpolation == SI.EASE_OUT:
            index = np.linspace(0, 1, steps)
            weights = diff * (1 - np.power(1 - index, 2)) + strength_from
        elif interpolation == SI.EASE_IN_OUT:
            index = np.linspace(0, 1, steps)
            weights = diff * ((1 - np.cos(index * np.pi)) / 2) + strength_from
        for i in range(steps):
            keyframe = LatentKeyframe(batch_index_from + i, float(weights[i]))
            curr_latent_keyframe.add(keyframe)
        if print_keyframes:
            for keyframe in curr_latent_keyframe.keyframes:
                logger.info(f'keyframe {keyframe.batch_index}:{keyframe.strength}')
        for latent_keyframe in prev_latent_keyframe.keyframes:
            curr_latent_keyframe.add(latent_keyframe)
        return (curr_latent_keyframe,)
```