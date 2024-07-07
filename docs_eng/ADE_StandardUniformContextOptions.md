# Documentation
- Class name: StandardUniformContextOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The `create_options'method of the Standard UniformContextOptionsNode class is designed to generate a set of context options for animation and differential tasks. It configures contextual parameters, such as length, length and overlap, that control the particle size and continuity of the animation process. This method plays a key role in building an animated framework for how the animation is differentiated across frames or stages.

# Input types
## Required
- context_length
    - The parameter `context_legth'defines the range of frames or data points to be covered by the context. It is essential to determine the range of impacts of each contextual option on the animated results. This parameter directly affects the level of detail and the smoothness of the transition between different animating stages.
    - Comfy dtype: INT
    - Python dtype: int
- context_stride
    - Parameters `context_standard'specify the interval between successive context frames. It is important for the efficiency of the animation process because it affects the frequency of the introduction of information in the new context. This step setting optimizes the balance between performance and the level of detail required in the animation.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - Parameters `context_overlap'determines the extent of overlap in the context of the continuum. This overlap is essential to maintain continuity in the animated sequence, ensuring a smooth transition from one context to the next. This is particularly important when dealing with complex transformations that require gradual transition rather than sudden change.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fuse_method
    - The parameter `use_method'determines the strategy to merge or integrate different contexts in an animation. It plays an important role in the way in which the overall context is constructed and can significantly influence the consistency of the final animation and the way in which the different elements interact in it.
    - Comfy dtype: ContextFuseMethod.LIST
    - Python dtype: str
- use_on_equal_length
    - Parameters `use_on_equal_length'is a boolean symbol that is set to indicate that the context option is applied only if the context is equal in length. This is important in ensuring consistency in the animation process, especially when processing data for different lengths.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_percent
    - The parameter `start_percent'determines the starting point of the context on the animated timeline. It is essential to align the context with the particular moment or event in the animation, allowing precise time control and synchronization with other elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - Parameter `guarantee_steps'sets the minimum number of steps that will be applied in the context. It ensures that each context has a defined duration in the animation and contributes to the predictability of the overall structure and animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- view_opts
    - Parameter `view_opts'allows customisation of view options in context. It can be used to adjust visual aspects such as rendering settings or display preferences to enhance the presentation of animations.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions
- prev_context
    - The parameter `prev_content'refers to the previous set of context options used in the animation. It is important to maintain the continuity and mobility of the animation, especially when it is constructed on the basis of the previous context or when it moves from one context to another.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Output types
- CONTEXT_OPTS
    - Output `CONTEXT_OPTS'indicates a set of context options that are configured and prepared for animation. These options encapsulate parameters that define how animations evolve and evolve over time, ensuring the structure and consistency of animation sequences.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Usage tips
- Infra type: CPU

# Source code
```
class StandardUniformContextOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'context_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'context_stride': ('INT', {'default': 1, 'min': 1, 'max': STRIDE_MAX}), 'context_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST,), 'use_on_equal_length': ('BOOLEAN', {'default': False}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX}), 'prev_context': ('CONTEXT_OPTIONS',), 'view_opts': ('VIEW_OPTS',)}}
    RETURN_TYPES = ('CONTEXT_OPTIONS',)
    RETURN_NAMES = ('CONTEXT_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts'
    FUNCTION = 'create_options'

    def create_options(self, context_length: int, context_stride: int, context_overlap: int, fuse_method: str=ContextFuseMethod.PYRAMID, use_on_equal_length=False, start_percent: float=0.0, guarantee_steps: int=1, view_opts: ContextOptions=None, prev_context: ContextOptionsGroup=None):
        if prev_context is None:
            prev_context = ContextOptionsGroup()
        prev_context = prev_context.clone()
        context_options = ContextOptions(context_length=context_length, context_stride=context_stride, context_overlap=context_overlap, context_schedule=ContextSchedules.UNIFORM_STANDARD, closed_loop=False, fuse_method=fuse_method, use_on_equal_length=use_on_equal_length, start_percent=start_percent, guarantee_steps=guarantee_steps, view_options=view_opts)
        prev_context.add(context_options)
        return (prev_context,)
```