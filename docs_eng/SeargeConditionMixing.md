# Documentation
- Class name: SeargeConditionMixing
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the integration of search conditions into the data stream and enhances the specificity of data processing and retrieval operations.

# Input types
## Optional
- data
    - Data parameters are the main input of nodes and allow for the transmission and operation of information within the system.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Union[Dict[str, Any], None]

# Output types
- data
    - The output data are the modified version of the input and now contain search conditions that can be used in the follow-up process.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeConditionMixing:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(example):
        return {UI.EXAMPLE: example}

    def get(self, data=None):
        if data is None:
            data = {}
        data[UI.S_CONDITION_MIXING] = self.create_dict('example')
        return (data,)
```