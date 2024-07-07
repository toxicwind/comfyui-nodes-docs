# Documentation
- Class name: SeargeCustomPromptMode
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is intended to facilitate customization of the hint mode in the user interface, especially for data flow processing. It allows dynamic adjustments in data presentation and interaction, and enhances user experience by allowing custom input processing.

# Input types
## Optional
- data
    - The 'data' parameter serves as a channel for data streams to be operated by nodes. It is critical in determining the content and structure of the information that nodes process and customize.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Union[Dict[str, Any], None]

# Output types
- data
    - Output the 'data'parameter represents the modified data flow processed by the node. It encapsifies the custom reminder mode and any changes made to the original data structure.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeCustomPromptMode:

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
        data[UI.S_CUSTOM_PROMPTING] = self.create_dict('example')
        return (data,)
```