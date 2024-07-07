# Documentation
- Class name: SRIntPromptInput
- Category: Mikey/Meta
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The SRIntPromptInput node is designed to integrate the integer into a structured reminder format. It plays a key role in data pre-processing, ensuring that the integer value is correctly embedded in the reminder structure, thus facilitating subsequent operations that rely on this structured data.

# Input types
## Required
- input_int
    - The parameter 'input_int' is essential for the operation of the node because it means that the integer value is to be merged into the reminder. Its correct input is essential for the structured formatting of the reminder, affecting subsequent processing.
    - Comfy dtype: INT
    - Python dtype: int
- unique_id
    - The parameter 'unique_id' is the only identifier used to refer to a particular entry in the reminder. It is essential to ensure that the integer input is correctly associated with the anticipated context in the reminder structure.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- prompt
    - The parameter 'prompt' is a dictionary that contains structured tips. It is essential because it is an integer input that affects the final output of the node.
    - Comfy dtype: PROMPT
    - Python dtype: Dict[str, Dict[str, str]]
## Optional
- extra_pnginfo
    - The parameter 'extra_pnginfo', although optional, can provide additional context or metadata that may be relevant to the reminder. It enhances the abundance of structured data and may affect how the subsequent node explains the hint.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str

# Output types
- output_int
    - The parameter 'output_int' represents the original integer value that has been successfully integrated into the reminder. It marks the completion of the primary function of the node and is essential for continuity of data streams in subsequent operations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SRIntPromptInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_int': ('INT', {'forceInput': True})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('output_int',)
    FUNCTION = 'add'
    CATEGORY = 'Mikey/Meta'

    def add(self, input_int, extra_pnginfo, unique_id, prompt):
        prompt.get(str(unique_id))['inputs']['sr_val'] = str(input_int)
        return (input_int,)
```