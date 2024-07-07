# Documentation
- Class name: CR_DataBusOut
- Category: Comfyroll/Pipe/Bus
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_DataBusOut is a node used to produce data seamlessly through the plumbing system. As a key component of the data-processing workflow, it ensures that data can be transmitted efficiently from one phase to the next. The function of the node focuses on managing and facilitating data flows, highlighting its role in maintaining the integrity and continuity of information exchange within the system.

# Input types
## Required
- pipe
    - The ‘pipe’ parameter is essential for the operation of the CR_DataBusout node, as it represents a conduit for the transmission of data. It is a channel that allows for the orderly transmission of information and emphasizes its importance in the implementation of the node.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]

# Output types
- pipe
    - The 'pipe'output parameter is the conduit that carries the processed data. It is the key element of the node function, as it is responsible for transmitting the data to the follow-up phase of the workflow.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]
- any1
    - The `any1'output parameter represents a common data element processed by a node. It demonstrates the ability of the node to process various data types and contributes to the flexibility of the data processing pipeline.
    - Comfy dtype: Any
    - Python dtype: Any
- any2
    - The `any2'output parameter is another example of the multifunctionality of node processing different types of data. It further emphasizes the role of nodes in adapting to different data structures in the pipeline.
    - Comfy dtype: Any
    - Python dtype: Any
- any3
    - The `any3'output parameter, like `any1' and `any2', shows the ability of nodes to process and transmit data elements. It is part of the broader data management strategy used by nodes.
    - Comfy dtype: Any
    - Python dtype: Any
- any4
    - The `any4'output parameter continues to demonstrate the adaptability of nodes in managing various data inputs. It is essential for a comprehensive data-processing approach for nodes.
    - Comfy dtype: Any
    - Python dtype: Any
- show_help
    - The'show_help'output provides a link to the document for further help. It is a valuable resource for users seeking more information about node operations and functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_DataBusOut:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}}
    RETURN_TYPES = ('PIPE_LINE', any_type, any_type, any_type, any_type, 'STRING')
    RETURN_NAMES = ('pipe', 'any1', 'any2', 'any3', 'any4', 'show_help')
    FUNCTION = 'data_out'
    CATEGORY = icons.get('Comfyroll/Pipe/Bus')

    def data_out(self, any1=None, any2=None, any3=None, any4=None, pipe=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-data-bus-out'
        (new_any1, new_any2, new_any3, new_any4) = pipe
        return (pipe, new_any1, new_any2, new_any3, new_any4, show_help)
```