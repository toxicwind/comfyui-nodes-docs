# Documentation
- Class name: SeargePipelineStart
- Category: UI.CATEGORY_MAGIC
- Output node: True
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergePipelineStart node is the starting point for the data-processing stream. It is responsible for initializing the stream line using the given workflow version and optional data stream. This node ensures that the flow line is correctly set and configured before it starts processing.

# Input types
## Required
- wf_version
    - wf_version parameters specify the process version to be used in the current line. This is essential to determine the correct settings and operations that the current line will perform.
    - Comfy dtype: str
    - Python dtype: str
- data
    - The data parameter indicates that an optional data stream can be entered into the current line. It may contain the initial data required for processing, which is essential for the flow line to produce meaningful results.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Union[Dict, None]
- additional_data
    - The additional_data parameter provides a way to provide additional data to the flow line. This can be used to enrich the main data stream with additional information.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Union[Dict, None]
- prompt
    - The prompt parameter is used to provide text tips that may guide processing within the stream line. It may be hidden and usually used for internal guidance rather than for direct processing.
    - Comfy dtype: str
    - Python dtype: Union[str, None]
- extra_pnginfo
    - Extra_pnginfo parameters are additional information for PNG images that can be processed by the current line. It is optional and can contain metadata or other relevant details.
    - Comfy dtype: str
    - Python dtype: Union[str, None]

# Output types
- data
    - The data from the SeergePipelineStart node represents the initial stream of data after the current line is activated. It includes any changes or settings applied by the node and is the basis for further treatment within the stream line.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePipelineStart:

    def __init__(self):
        self.pipeline = Pipeline()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'wf_version': (Defs.WORKFLOW_VERSIONS,)}, 'optional': {'data': ('SRG_DATA_STREAM',), 'additional_data': ('SRG_DATA_STREAM',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'trigger'
    OUTPUT_NODE = True
    CATEGORY = UI.CATEGORY_MAGIC

    def trigger(self, wf_version, data=None, additional_data=None, prompt=None, extra_pnginfo=None):
        if data is None:
            print('Warning: Pipeline Start - missing data stream')
        else:
            if additional_data is not None:
                data = data | additional_data
            self.pipeline.start(data)
            access = PipelineAccess(data)
            self.pipeline.enable(access.get_active_setting(UI.S_OPERATING_MODE, UI.F_WORKFLOW_MODE) != UI.NONE)
            mb_hidden = {Names.F_MAGIC_BOX_PROMPT: prompt, Names.F_MAGIC_BOX_EXTRA_PNGINFO: extra_pnginfo}
            mb_version = {Names.F_MAGIC_BOX_EXTENSION: Defs.VERSION, Names.F_MAGIC_BOX_WORKFLOW: wf_version}
            access.update_in_pipeline(Names.S_MAGIC_BOX_HIDDEN, mb_hidden)
            access.update_in_pipeline(Names.S_MAGIC_BOX_VERSION, mb_version)
            if data is not None:
                data[Names.S_MAGIC_BOX_HIDDEN] = mb_hidden
                data[Names.S_MAGIC_BOX_VERSION] = mb_version
        return (data,)
```