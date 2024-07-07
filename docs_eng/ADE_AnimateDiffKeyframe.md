# Documentation
- Class name: ADKeyframeNode
- Category: Animate Diff 🎭🅐🅓
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The ADKeyframeNode class is the key frame for managing animated differences. It provides the functionality for loading and operating the key frames to ensure consistency and clarity in the animation sequence. This node is essential for creating smooth transitions and maintaining the integrity of the entire animation sequence.

# Input types
## Required
- start_percent
    - Start_percent parameters define the starting position of the key frame in the animation time line. It is essential to determine the timing of the animation and to ensure the correct sequencing of the key frame sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- prev_ad_keyframes
    - The prev_ad_keyframes parameter allows users to provide a set of previous frames, which will be added to the frame. This is essential to maintain continuity and build on the existing animation framework.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: ADKeyframeGroup
- scale_multival
    - Scale_multiival parameters adjust the zoom of the key frame animation. It is essential to control the intensity of animated changes and the range of a given point in the sequence.
    - Comfy dtype: MULTIVAL
    - Python dtype: Union[float, torch.Tensor]
- effect_multival
    - The object_multidal parameter is used to modify the effect intensity of the key frame. It plays a vital role in the visual impact of micromobilization drawings at a given time.
    - Comfy dtype: MULTIVAL
    - Python dtype: Union[float, torch.Tensor]
- inherit_missing
    - Inherit_missing parameters determine whether the key frame should inherit the properties from the previous key frame if they are not clearly defined. This is essential to maintain the consistent animation style throughout the sequence.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- guarantee_steps
    - The guarante_steps parameter ensures the minimum number of steps between the key frames, which is important for the smoothness and fluidity of the animation.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- AD_KEYFRAMES
    - The output of ADKeyframeNode is a set of key frames representing animated sequences with newly added or modified key frames. This output is important for the follow-up and rendering of animations.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: ADKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class ADKeyframeNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'prev_ad_keyframes': ('AD_KEYFRAMES',), 'scale_multival': ('MULTIVAL',), 'effect_multival': ('MULTIVAL',), 'inherit_missing': ('BOOLEAN', {'default': True}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX})}}
    RETURN_TYPES = ('AD_KEYFRAMES',)
    FUNCTION = 'load_keyframe'
    CATEGORY = 'Animate Diff 🎭🅐🅓'

    def load_keyframe(self, start_percent: float, prev_ad_keyframes=None, scale_multival: Union[float, torch.Tensor]=None, effect_multival: Union[float, torch.Tensor]=None, inherit_missing: bool=True, guarantee_steps: int=1):
        if not prev_ad_keyframes:
            prev_ad_keyframes = ADKeyframeGroup()
        prev_ad_keyframes = prev_ad_keyframes.clone()
        keyframe = ADKeyframe(start_percent=start_percent, scale_multival=scale_multival, effect_multival=effect_multival, inherit_missing=inherit_missing, guarantee_steps=guarantee_steps)
        prev_ad_keyframes.add(keyframe)
        return (prev_ad_keyframes,)
```