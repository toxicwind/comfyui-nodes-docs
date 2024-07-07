# Documentation
- Class name: SeargeOperatingMode
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class covers the operational settings for searching and generating (SRG) workflows, allowing customizing workflow patterns and alert strategies.

# Input types
## Required
- workflow_mode
    - To determine the mode of operation of the workflow, this can significantly affect the type of output generated and the overall efficiency of the process.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- prompting_mode
    - Sets the alert mode that guides the generation process and influences the creativity and relevance of the results.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- batch_size
    - The number of inputs specified for processing in individual operations will affect the volume of throughput and resource utilization of the system.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- data
    - An optional data stream can be used to provide additional context or information for the workflow.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- data
    - Include updated data streams that apply the operating model settings, which are essential for the next steps in the workflow.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOperatingMode:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'workflow_mode': (UI.WORKFLOW_MODES, {'default': UI.WF_MODE_TEXT_TO_IMAGE}), 'prompting_mode': (UI.PROMPTING_MODES, {'default': UI.PROMPTING_DEFAULT}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4, 'step': 1})}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(workflow_mode, prompting_mode, batch_size):
        return {UI.F_WORKFLOW_MODE: workflow_mode, UI.F_PROMPTING_MODE: prompting_mode, UI.F_BATCH_SIZE: batch_size}

    def get(self, workflow_mode, prompting_mode, batch_size, data=None):
        if data is None:
            data = {}
        data[UI.S_OPERATING_MODE] = self.create_dict(workflow_mode, prompting_mode, batch_size)
        return (data,)
```