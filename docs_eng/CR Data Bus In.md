# Documentation
- Class name: CR_DataBusIn
- Category: Comfyroll/Pipe/Bus
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_DataBusin is a node for managing and routing data streams. It transmits all types of data through the pipe system to ensure that the flow is orderly and efficient within the pipe structure. This node plays a key role in data flow integration, allowing complex data operations and processing workflows.

# Input types
## Optional
- pipe
    - The 'pipe' parameter is the key element for node operations, which represents the data pipeline used to transmit information. Its flexibility allows for the processing of various data types and enhances the multifunctionality of nodes when processing different data scenarios.
    - Comfy dtype: any
    - Python dtype: Any
- any1
    - The 'any1'parameter is an optional input that can be used to inject additional data into the pipeline. It enhances the ability of nodes to process multiple data inputs and helps to upgrade the overall data processing capability of the system.
    - Comfy dtype: any
    - Python dtype: Any
- any2
    - The 'any2' parameter is another optional input that complements the data pipeline and allows for the management of more complex data structures. It plays an important role in the ability to process nodes and route more types of data.
    - Comfy dtype: any
    - Python dtype: Any
- any3
    - The 'any3' parameter is used to introduce more data elements into the pipeline. This is an optional input that helps to adapt nodes when processing various data, thereby extending the usefulness of nodes in different data processing tasks.
    - Comfy dtype: any
    - Python dtype: Any
- any4
    - The `any4' parameter, as another optional input for nodes, provides a means of incorporating more data into the pipeline. It emphasizes the ability of node designs to accommodate a variety of data inputs, which are essential for comprehensive data-processing needs.
    - Comfy dtype: any
    - Python dtype: Any

# Output types
- pipe
    - The 'pipe' output is a meta-group of processed data elements, representing node data routes and the results of processing activities. It represents the structured flow of operational information that is now ready for further use in the plumbing system.
    - Comfy dtype: tuple
    - Python dtype: Tuple[Any, ...]
- show_help
    - The'show_help' output provides a URL link to the node document, a direct reference node guide and a way to help users. It is an important tool for understanding the node function and making effective use of it in the data pipeline.
    - Comfy dtype: string
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_DataBusIn:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'pipe': (any_type,), 'any1': (any_type,), 'any2': (any_type,), 'any3': (any_type,), 'any4': (any_type,)}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('pipe', 'show_help')
    FUNCTION = 'load_data'
    CATEGORY = icons.get('Comfyroll/Pipe/Bus')

    def load_data(self, any1=None, any2=None, any3=None, any4=None, pipe=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-data-bus-in'
        (new_any1, new_any2, new_any3, new_any4) = (None, None, None, None)
        if pipe is not None:
            (new_any1, new_any2, new_any3, new_any4) = pipe
        new_any1 = any1 if any1 is not None else new_any1
        new_any2 = any2 if any2 is not None else new_any2
        new_any3 = any3 if any3 is not None else new_any3
        new_any4 = any4 if any4 is not None else new_any4
        new_pipe = (new_any1, new_any2, new_any3, new_any4)
        return (new_pipe, show_help)
```