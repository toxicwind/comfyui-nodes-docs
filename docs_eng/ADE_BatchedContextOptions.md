# Documentation
- Class name: BatchedContextOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

Catched ContextoptionsNode aims to manage and generate context options for animation sequences. It provides a structured approach to defining the length of each context, the starting percentage and the guarantee steps to ensure consistency and efficiency of animation workflows.

# Input types
## Required
- context_length
    - The context_legth parameter specifies the duration of the context window, which is essential for determining the range of each animation segment. It directly affects the ability of the node to animate the time line.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- start_percent
    - Start_percent parameters specify the starting point of the context in the animation sequence, allowing micromobilization of the initial focus of the drawing. By controlling the starting position of each context, it plays an important role in the overall animation strategy.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - The guarante_steps parameter ensures at least the number of steps per context to provide protection against premature termination. It is important to maintain the integrity of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- prev_context
    - Prev_content parameters allow the continuation or modification of existing context options so that nodes can be constructed in their previous state. This is essential to maintain continuity in the animation process.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Output types
- CONTEXT_OPTS
    - Output CONTEXT_OPTS represents a set of context options that are generated or updated by nodes. These options are essential to guide the next steps in the animation process.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: ContextOptionsGroup

# Usage tips
- Infra type: CPU

# Source code
```
class BatchedContextOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'context_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX})}, 'optional': {'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'guarantee_steps': ('INT', {'default': 1, 'min': 0, 'max': BIGMAX}), 'prev_context': ('CONTEXT_OPTIONS',)}}
    RETURN_TYPES = ('CONTEXT_OPTIONS',)
    RETURN_NAMES = ('CONTEXT_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts'
    FUNCTION = 'create_options'

    def create_options(self, context_length: int, start_percent: float=0.0, guarantee_steps: int=1, prev_context: ContextOptionsGroup=None):
        if prev_context is None:
            prev_context = ContextOptionsGroup()
        prev_context = prev_context.clone()
        context_options = ContextOptions(context_length=context_length, context_overlap=0, context_schedule=ContextSchedules.BATCHED, start_percent=start_percent, guarantee_steps=guarantee_steps)
        prev_context.add(context_options)
        return (prev_context,)
```