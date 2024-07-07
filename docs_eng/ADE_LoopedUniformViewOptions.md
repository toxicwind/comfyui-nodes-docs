# Documentation
- Class name: LoopedUniformViewOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts/view opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The circular homogenous view option node is intended to generate a uniform set of view options for circular animations. It provides a systematic way to define the length, length and overlap of views within the closed loop structure, allowing the visual consistency and consistency of the animation sequence.

# Input types
## Required
- view_length
    - View length parameters specify the length of each view in the animation sequence, which is essential for determining the overall scope and detail of the animation. It directly affects the number of frames and the comprehensiveness of the circular view generated.
    - Comfy dtype: INT
    - Python dtype: int
- view_stride
    - View step parameters define the interval between successive views in the animation, affecting the smoothness and continuity of the transition between frames. It is an important factor in creating a consistent animation process.
    - Comfy dtype: INT
    - Python dtype: int
- view_overlap
    - The view overlap parameters determine the degree of overlap between adjacent views in the loop, which is essential to maintain visual continuity and prevent sudden changes that could disrupt the audience's experience.
    - Comfy dtype: INT
    - Python dtype: int
- closed_loop
    - Closed ring signs indicate whether an animated sequence should form a closed ring, which is essential to create seamless transitions and ensure that animations can be played in an uninterrupted cycle.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- fuse_method
    - Integration methodology parameters allow for the specification of integration techniques to be applied in the group view, which enhances the visual quality and consistency of animations.
    - Comfy dtype: ContextFuseMethod.LIST
    - Python dtype: str
- use_on_equal_length
    - The use_on_equal_length parameters, when encountered, determine whether to apply certain conditions, may optimize animations for some scenarios.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- VIEW_OPTS
    - The VIEW_OPTS output provides a structured set of options to define the parameters of the loop animation view. These options include length, length, overlap and other settings that are essential for animation execution and visual outcomes.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions

# Usage tips
- Infra type: CPU

# Source code
```
class LoopedUniformViewOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'view_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'view_stride': ('INT', {'default': 1, 'min': 1, 'max': STRIDE_MAX}), 'view_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX}), 'closed_loop': ('BOOLEAN', {'default': False})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST,), 'use_on_equal_length': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('VIEW_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts/view opts'
    FUNCTION = 'create_options'

    def create_options(self, view_length: int, view_overlap: int, view_stride: int, closed_loop: bool, fuse_method: str=ContextFuseMethod.PYRAMID, use_on_equal_length=False):
        view_options = ContextOptions(context_length=view_length, context_stride=view_stride, context_overlap=view_overlap, context_schedule=ContextSchedules.UNIFORM_LOOPED, closed_loop=closed_loop, fuse_method=fuse_method, use_on_equal_length=use_on_equal_length)
        return (view_options,)
```