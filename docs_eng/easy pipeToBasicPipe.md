# Documentation
- Class name: pipeToBasicPipe
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The `pipeToBavicPipe' node is designed to convert complex pipeline configurations into a simplified `basic_pipe' format. It acts as an intermediary to ensure that the basic components of the pipeline are extracted and organized so that they can be more easily handled. The node plays a key role in reducing the complexity of pipe management, thereby increasing the overall efficiency of the system.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential for the operation of the node, as it represents a complex pipeline configuration that needs to be simplified. It is the main input that determines the execution of the node and the structure of the `basic_pipe' generated.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- my_unique_id
    - The `my_unique_id' parameter, although optional, can be used as the only marking conversion process. It increases traceability for operations, which may be important for debugging or tracking in complex systems.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- basic_pipe
    - The 'basic_pipe' output contains a simplified expression of the original pipe. It is a structured output that retains the core elements of the pipe, making it easier to operate and integrate into the follow-up process.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, Any, Any, Any, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class pipeToBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}, 'hidden': {'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('BASIC_PIPE',)
    RETURN_NAMES = ('basic_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Pipe'

    def doit(self, pipe, my_unique_id=None):
        new_pipe = (pipe.get('model'), pipe.get('clip'), pipe.get('vae'), pipe.get('positive'), pipe.get('negative'))
        del pipe
        return (new_pipe,)
```