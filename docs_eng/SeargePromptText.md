# Documentation
- Class name: SeargePromptText
- Category: Searge/_deprecated_/Prompting
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergePromptText node is designed to manage and process text tips. It is used in a system that requires text input to generate or modify content. The primary function of the node is to retrieve and provide tips, which can be used as a basis for further processing or as input to other nodes in the system.

# Input types
## Required
- prompt
    - For the SeergePromptText node, the 'prompt' parameter is the key element of the process, which defines the text input to be processed by the node. It is expected to be a string that may contain multiple lines of text, allowing the input of complex and detailed instructions or information.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - Output 'prompt' is a processed or original text entered into the SeergePromptText node. It serves as a base data segment that can influence follow-up operations or be used as a direct response to queries.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePromptText:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'default': '', 'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Prompting'

    def get_value(self, prompt):
        return (prompt,)
```