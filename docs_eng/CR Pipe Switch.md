# Documentation
- Class name: CR_InputSwitchPipe
- Category: Comfyroll/Pipe
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_InputSwitchPipe node is designed to manage the flow of data between different processing conduits based on the selection of input. It determines which of the two channels provided, 'pipe1' or 'pipe2', should be used in the follow-up stream by assessing the 'Input' parameter. This node plays a key role in creating working streams of conditions based on input conditions that require different processing paths.

# Input types
## Required
- Input
    - The `Input' parameter is essential for determining the active pipeline. It accepts an integer value, with 1 indicating that `pipe1' will be used, and any other value will mean `pipe2'. This selection mechanism is essential to guide the workflow through the required processing path.
    - Comfy dtype: INT
    - Python dtype: int
- pipe1
    - The `pipe1' parameter indicates the first pipe option available for the node. If the `Input' parameter is set to 1, it will be a activated pipe object. This allows seamless integration of the predefined processing path into the workflow.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Any
- pipe2
    - The `pipe2' parameter is an alternative pipe option for nodes. When the `Input' parameter is not equal to 1, it becomes active and provides a secondary path for data processing in the workflow.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Any

# Output types
- PIPE_LINE
    - The `PIPE_LINE' output is a conduit selected on the basis of the `Input' parameter. It is an output that will be passed to further processing, representing `pipe1' or `pipe2' selected on the basis of input.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Any
- show_help
    - The `show_help' output provides a URL that points to the document page for further help. It is a constant string that always points to the GitHub wiki page at the CR_InputSwitchPipe node and provides a direct link to the use and functionality of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_InputSwitchPipe:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2}), 'pipe1': ('PIPE_LINE',), 'pipe2': ('PIPE_LINE',)}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('PIPE_LINE', 'show_help')
    OUTPUT_NODE = True
    FUNCTION = 'switch_pipe'
    CATEGORY = icons.get('Comfyroll/Pipe')

    def switch_pipe(self, Input, pipe1, pipe2):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-pipe-switch'
        if Input == 1:
            return (pipe1, show_help)
        else:
            return (pipe2, show_help)
```