# Documentation
- Class name: AnimateDiffSlidingWindowOptions
- Category: Animate Diff
- Output node: False
- Repo Ref: https://github.com/ArtVentureX/comfyui-animatediff.git

The node class covers the configuration options needed to set slide window animations. It is designed to manage parameters that control frame generation in the video sequence and ensure consistency in the animation flow. The node is designed to provide a structured way to define the time and spatial characteristics of animations, such as the length of the context, the length of steps between frames, and the degree of overlap between successive contexts.

# Input types
## Required
- context_length
    - The context_length parameter sets the number of consecutive frames to be considered at each step of the animation. It is essential to determine the context of the model operation, thus affecting the continuity and continuity of the creation of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- context_stride
    - The context_stride parameter specifies the spacing between the frames in the slide window. It affects the way an animation moves from one context to the next and helps the rhythm and pace of the overall animation.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - Context_overlap parameters define the number of overlap frames between continuous slide windows. This is essential to maintain smooth transitions and ensure that animations do not appear to be inconsistent or unstable.
    - Comfy dtype: INT
    - Python dtype: int
- context_schedule
    - The context_schedule parameter controls the distribution of frames in the slide window and allows the use of various modes, such as homogeneity or non-event distribution. This affects the visual dynamics of the animation and the narrative process.
    - Comfy dtype: ENUM
    - Python dtype: ContextSchedules.CONTEXT_SCHEDULE_ENUM
- closed_loop
    - The closed_loop parameter determines whether the animation should loop back to the beginning when it reaches the end. This affects the overall structure and presentation of the animation and may create seamless or circular narratives.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- sliding_window_opts
    - The output represents a configured TradingContext object, encapsulating all parameters required during the animation process. It is a key component in generating a consistent and smooth transition of video sequences.
    - Comfy dtype: OBJECT
    - Python dtype: SlidingContext

# Usage tips
- Infra type: CPU

# Source code
```
class AnimateDiffSlidingWindowOptions:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'context_length': ('INT', {'default': SLIDING_CONTEXT_LENGTH, 'min': 2, 'max': 32}), 'context_stride': ('INT', {'default': 1, 'min': 1, 'max': 32}), 'context_overlap': ('INT', {'default': 4, 'min': 0, 'max': 32}), 'context_schedule': (ContextSchedules.CONTEXT_SCHEDULE_LIST, {'default': ContextSchedules.UNIFORM}), 'closed_loop': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('SLIDING_WINDOW_OPTS',)
    FUNCTION = 'init_options'
    CATEGORY = 'Animate Diff'

    def init_options(self, context_length, context_stride, context_overlap, context_schedule, closed_loop):
        ctx = SlidingContext(context_length=context_length, context_stride=context_stride, context_overlap=context_overlap, context_schedule=context_schedule, closed_loop=closed_loop)
        return (ctx,)
```