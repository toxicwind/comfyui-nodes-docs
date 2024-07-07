# Documentation
- Class name: CR_8ChannelOut
- Category: Comfyroll/Pipe/Bus
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_8channelOut is designed to manage and distribute data to eight different channels. It plays a key role in ensuring that the flow of information is smooth in the pipeline and that each channel receives appropriate data for further processing or analysis.

# Input types
## Required
- pipe
    - The 'pipe' parameter is essential because it serves as a channel for data transmission and subsequent distribution in eight channels. Its correct configuration is essential for the operation of nodes and for the integrity of data streams.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]

# Output types
- pipe
    - The `pipe' output, representing the raw data pipeline, has been processed and is now ready for further use or analysis at downstream nodes.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]
- ch1
    - Channel 1 'ch1'is one of eight channels to receive the data part of 'pipe '. It is important for processing or processing data specifically related to the channel.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch2
    - Channel 2 'ch2' is another channel that handles specific parts of the data. It applies to tasks assigned to this particular channel in node operations.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch3
    - Channel 3 'ch3'is used to further divert data, allowing for parallel or specialized processing of different data segments.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch4
    - Channel 4 'ch4' is one of several channels managed by nodes, each playing a different role in data distribution and processing.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch5
    - Channel 5 'ch5'is designated for specific types of data processing to ensure that node functions are consistent with the specific requirements of the workflow.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch6
    - Channel 6 'ch6' is part of a node multichannel structure that meets diverse data-processing needs in complex systems.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch7
    - Channel 7 'ch7' is a dedicated channel within nodes to optimize the handling of specific data streams to improve the efficiency of work processes.
    - Comfy dtype: any_type
    - Python dtype: Any
- ch8
    - Channel 8 'ch8' is the last of the node packages and the data have been distributed in all designated channels for full processing.
    - Comfy dtype: any_type
    - Python dtype: Any
- show_help
    - The'show_help' output provides a URL link to the node document and provides users with a direct reference node guide and a way to use the description.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_8ChannelOut:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}}
    RETURN_TYPES = ('PIPE_LINE', any_type, any_type, any_type, any_type, any_type, any_type, any_type, any_type, 'STRING')
    RETURN_NAMES = ('pipe', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'show_help')
    FUNCTION = 'data_out'
    CATEGORY = icons.get('Comfyroll/Pipe/Bus')

    def data_out(self, ch1=None, ch2=None, ch3=None, ch4=None, ch5=None, ch6=None, ch7=None, ch8=None, pipe=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-8-channel-out'
        (new_ch1, new_ch2, new_ch3, new_ch4, new_ch5, new_ch6, new_ch7, new_ch8) = pipe
        return (pipe, new_ch1, new_ch2, new_ch3, new_ch4, new_ch5, new_ch6, new_ch7, new_ch8, show_help)
```