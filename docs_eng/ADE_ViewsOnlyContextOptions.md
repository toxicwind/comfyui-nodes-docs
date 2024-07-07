# Documentation
- Class name: ViewAsContextOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The ViewAsContextOptionsNode class'crete_options' method is designed to generate a set of context options that determine how the context of the view is dealt with and animated. It allows a self-defined percentage of the beginning of animations and the number of guaranteed steps to ensure smooth passage between different settings.

# Input types
## Required
- view_opts_req
    - Parameters'view_opts_req' are essential to define the view options required for the context of the animation. It lays the foundation for the context's interpretation and operation within the context of the animation.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions
## Optional
- start_percent
    - The parameter'start_percent' specifies the starting percentage of the animation, allowing the user to control the initial state of the animation. This is an optional parameter that allows a micro-mobilization of the beginning of the drawing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - The parameter 'guarantee_steps' provides a mechanism for maintaining the continuity and stability of the animation by ensuring a minimum number of steps in its operation.
    - Comfy dtype: INT
    - Python dtype: int
- prev_context
    - Parameters'prev_content' allow for the inclusion of previous context options in a new set, enabling the method to be constructed in the current context state, and promoting more complex or hierarchical animation settings.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Output types
- CONTEXT_OPTS
    - Output 'CONTEXT_OPTS' represents the newly created or updated set of context options that will influence subsequent animation or processing steps.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Usage tips
- Infra type: CPU

# Source code
```
class ViewAsContextOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'view_opts_req': ('VIEW_OPTS',)}, 'optional': {'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX}), 'prev_context': ('CONTEXT_OPTIONS',)}}
    RETURN_TYPES = ('CONTEXT_OPTIONS',)
    RETURN_NAMES = ('CONTEXT_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts'
    FUNCTION = 'create_options'

    def create_options(self, view_opts_req: ContextOptions, start_percent: float=0.0, guarantee_steps: int=1, prev_context: ContextOptionsGroup=None):
        if prev_context is None:
            prev_context = ContextOptionsGroup()
        prev_context = prev_context.clone()
        context_options = ContextOptions(context_schedule=ContextSchedules.VIEW_AS_CONTEXT, start_percent=start_percent, guarantee_steps=guarantee_steps, view_options=view_opts_req, use_on_equal_length=True)
        prev_context.add(context_options)
        return (prev_context,)
```