# Documentation
- Class name: StandardStaticContextOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The `create_options'method of StandardStaticContextOptionsNode is designed to generate and configure context options for animating processes. It allows customizing parameters that distinguish between frame lengths, overlaps, and other impact animations. This method is essential in setting context for animating, ensuring that frames are created in a coherent and context-sensitive manner.

# Input types
## Required
- context_length
    - Parameters `context_legth'specify the number of context frames to be taken into account in each animation step. This is essential for determining the extent of the impact of each frame on the animated result.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - The parameter `context_overlap'defines the overlap between the adjacent context in the animation sequence. This is important to ensure smooth transition and continuity in the animation.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fuse_method
    - The parameter `use_method'determines how different contexts are combined or integrated in the animation process. It may affect the overall and style coherence of the animation.
    - Comfy dtype: str
    - Python dtype: str
- use_on_equal_length
    - The symbol `use_on_equal_length'indicates whether the context option should be applied when the animated frame is equal in length. It may affect the distribution of the animated frame.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_percent
    - The parameter `start_percent'sets the starting percentage of the context options, which may affect the time when the animation begins to integrate these options.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - The parameter `guarantee_steps'ensures that the minimum number of steps of the context option is applied to the animation process to provide stability to the animation process.
    - Comfy dtype: INT
    - Python dtype: int
- view_opts
    - Parameter `view_opts' allows custom view options in context, which can change the visual representation of animations.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions
- prev_context
    - The parameter `prev_content'is used to bring the previous context options into the new context and to maintain the continuity of the animation sequence.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Output types
- CONTEXT_OPTS
    - The output `CONTEXT_OPTS' provides the configuration context options to be used in the next steps of the animation process.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Usage tips
- Infra type: CPU

# Source code
```
class StandardStaticContextOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'context_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'context_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST_STATIC,), 'use_on_equal_length': ('BOOLEAN', {'default': False}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX}), 'prev_context': ('CONTEXT_OPTIONS',), 'view_opts': ('VIEW_OPTS',)}}
    RETURN_TYPES = ('CONTEXT_OPTIONS',)
    RETURN_NAMES = ('CONTEXT_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts'
    FUNCTION = 'create_options'

    def create_options(self, context_length: int, context_overlap: int, fuse_method: str=ContextFuseMethod.PYRAMID, use_on_equal_length=False, start_percent: float=0.0, guarantee_steps: int=1, view_opts: ContextOptions=None, prev_context: ContextOptionsGroup=None):
        if prev_context is None:
            prev_context = ContextOptionsGroup()
        prev_context = prev_context.clone()
        context_options = ContextOptions(context_length=context_length, context_stride=None, context_overlap=context_overlap, context_schedule=ContextSchedules.STATIC_STANDARD, fuse_method=fuse_method, use_on_equal_length=use_on_equal_length, start_percent=start_percent, guarantee_steps=guarantee_steps, view_options=view_opts)
        prev_context.add(context_options)
        return (prev_context,)
```