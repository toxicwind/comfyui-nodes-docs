# Documentation
- Class name: pipeBatchIndex
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

PipeBatchIndex allows batch data to be operated in the current line and allows for the selection and processing of specific batch indexes. It is essential to optimize batch processing tasks by allowing for targeted data processing, thereby enhancing workflows.

# Input types
## Required
- pipe
    - The `pipe' parameter represents the data flow line being processed. It contains samples and other relevant information necessary for batch operations and is essential for achieving the target data processing.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- batch_index
    - The 'batch_index' parameter specifies the batch index to be processed in the stream line. It is important because it guides nodes to the right batch for processing.
    - Comfy dtype: INT
    - Python dtype: int
- length
    - The `length' parameter determines the number of elements to be processed from the batch. It affects the scope of the operation and is essential for managing the size of the data to be operated.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- my_unique_id
    - The `my_unique_id' parameter is an optional identifier that can be used to track specific examples of node execution. It helps to distinguish the different run of nodes in complex workflows.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - The ‘pipe’ output is a modified data stream that now contains processed sample batches. It is a key output because it carries the results of batch operations and enters them into the follow-up phase of the stream.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class pipeBatchIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'batch_index': ('INT', {'default': 0, 'min': 0, 'max': 63}), 'length': ('INT', {'default': 1, 'min': 1, 'max': 64})}, 'hidden': {'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Pipe'

    def doit(self, pipe, batch_index, length, my_unique_id=None):
        samples = pipe['samples']
        (new_samples,) = LatentFromBatch().frombatch(samples, batch_index, length)
        new_pipe = {**pipe, 'samples': new_samples}
        del pipe
        return (new_pipe,)
```