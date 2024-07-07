# Documentation
- Class name: SeargePipelineTerminator
- Category: UI.CATEGORY_MAGIC
- Output node: True
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergePipelineTerminator node is designed to manage and terminate the ongoing data processing pipeline. It plays a key role in ensuring that the data flow is properly closed without leaving any residual process, thereby preserving the efficiency and integrity of the system.

# Input types
## Optional
- data
    - The `data' parameter is essential to the operation of the node because it provides the input flow needed to terminate the pipe. Its existence ensures that the node can accurately identify and close the relevant data processing pipe.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- result
    - The'reult' output represents the result of the pipeline termination process. It is important because it provides confirmation that the pipeline has been successfully terminated to ensure that the system can continue without any pending data-processing tasks.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, bool]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePipelineTerminator:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ()
    FUNCTION = 'trigger'
    OUTPUT_NODE = True
    CATEGORY = UI.CATEGORY_MAGIC

    def trigger(self, data=None):
        access = PipelineAccess(data)
        access.terminate_pipeline()
        return {}
```