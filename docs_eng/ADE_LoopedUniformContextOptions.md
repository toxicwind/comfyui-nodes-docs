# Documentation
- Class name: LoopedUniformContextOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

LoopedUniformContextOptionsNode aims to generate a range of context options for animating purposes. It creates even distribution based on the given parameters, ensuring consistent flow of animated frames. This node is particularly suitable for creating animated loops, where homogeneity and continuity are essential.

# Input types
## Required
- context_length
    - The context_legth parameter determines the length of each of the animation sequences above. It is essential to define the range of each context and influences the overall structure of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- context_stride
    - The context_stride parameter specifies the length of time between the context. It affects the degree of connection of each context to its neighbours and the consistency of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - Context_overlap parameters define the amount of overlap between the adjacent context. This is important to ensure smooth transition between the context in the animation and to maintain visual continuity.
    - Comfy dtype: INT
    - Python dtype: int
- closed_loop
    - Closed_loop parameters indicate whether the animation should loop back to the beginning after the last context. This can be used to create a seamless, repetitive animation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- fuse_method
    - The fuse_method parameter determines how the context in the animation is integrated. It affects the mixing and consolidation of the context and the final appearance of the animation.
    - Comfy dtype: ContextFuseMethod.LIST
    - Python dtype: str
- use_on_equal_length
    - Use_on_equality_legth parameters specify whether context should be used only if the length of context meets specific conditions. This can be used to control context application according to specific criteria.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_percent
    - Start_percent parameters define the starting percentage of the context in the animation sequence. It is used to control the start of each context.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - The guarante_steps parameter ensures that each context shows at least a certain number of steps in the animation. This helps to maintain the visibility and influence of each context in the sequence.
    - Comfy dtype: INT
    - Python dtype: int
- view_opts
    - View_opts parameters provide options for viewing animations. They can include settings that affect animated displays or renderings.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions
- prev_context
    - Prev_content parameters allow the continuation of the previous context sequence. Use when extending or modifying the existing animation sequence.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Output types
- CONTEXT_OPTS
    - The output CONTEXT_OPTS provides a structured set of context options based on input parameters. These options can be used directly in the animation process.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Usage tips
- Infra type: CPU

# Source code
```
class LoopedUniformContextOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'context_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'context_stride': ('INT', {'default': 1, 'min': 1, 'max': STRIDE_MAX}), 'context_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX}), 'closed_loop': ('BOOLEAN', {'default': False})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST,), 'use_on_equal_length': ('BOOLEAN', {'default': False}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX}), 'prev_context': ('CONTEXT_OPTIONS',), 'view_opts': ('VIEW_OPTS',)}}
    RETURN_TYPES = ('CONTEXT_OPTIONS',)
    RETURN_NAMES = ('CONTEXT_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts'
    FUNCTION = 'create_options'

    def create_options(self, context_length: int, context_stride: int, context_overlap: int, closed_loop: bool, fuse_method: str=ContextFuseMethod.FLAT, use_on_equal_length=False, start_percent: float=0.0, guarantee_steps: int=1, view_opts: ContextOptions=None, prev_context: ContextOptionsGroup=None):
        if prev_context is None:
            prev_context = ContextOptionsGroup()
        prev_context = prev_context.clone()
        context_options = ContextOptions(context_length=context_length, context_stride=context_stride, context_overlap=context_overlap, context_schedule=ContextSchedules.UNIFORM_LOOPED, closed_loop=closed_loop, fuse_method=fuse_method, use_on_equal_length=use_on_equal_length, start_percent=start_percent, guarantee_steps=guarantee_steps, view_options=view_opts)
        prev_context.add(context_options)
        return (prev_context,)
```