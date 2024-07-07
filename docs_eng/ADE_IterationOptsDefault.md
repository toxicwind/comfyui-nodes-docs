# Documentation
- Class name: IterationOptionsNode
- Category: Animate Diff 🎭🅐🅓/iteration opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The `create_iter_opts'method of the iterative option category is designed to configure the iterative settings for the sampling process. It allows users to specify the number of overlaps and the deviations of batches and seeds, which are essential to control the sampling process and ensure that diversified outputs are generated.

# Input types
## Required
- iterations
    - The parameter 'internations' defines the number of times the sampling process will repeat. It is a fundamental aspect of node operations, as it directly affects the number of outputs generated.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- iter_batch_offset
    - The parameter 'iter_batch_offset'is used to adjust the batch index for each batch. It functions during the sampling process and allows changes in the output sequence that is generated.
    - Comfy dtype: INT
    - Python dtype: int
- iter_seed_offset
    - Parameters 'iter_seed_offset'specify the deviation of the torrents to be used at each rotation. By changing the starting point of the random numbers generated at each rotation, this can introduce diversity into the sample.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- ITERATION_OPTS
    - Output 'ITERATION_OPTS' represents the configuration iterative option for the sampling process. It covers user-defined settings and is essential for the next steps in the sampling workflow.
    - Comfy dtype: ITERATION_OPTS
    - Python dtype: IterationOptions

# Usage tips
- Infra type: CPU

# Source code
```
class IterationOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'iterations': ('INT', {'default': 1, 'min': 1})}, 'optional': {'iter_batch_offset': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX}), 'iter_seed_offset': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX})}}
    RETURN_TYPES = ('ITERATION_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/iteration opts'
    FUNCTION = 'create_iter_opts'

    def create_iter_opts(self, iterations: int, iter_batch_offset: int=0, iter_seed_offset: int=0):
        iter_opts = IterationOptions(iterations=iterations, iter_batch_offset=iter_batch_offset, iter_seed_offset=iter_seed_offset)
        return (iter_opts,)
```