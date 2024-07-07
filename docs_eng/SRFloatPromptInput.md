# Documentation
- Class name: SRFloatPromptInput
- Category: Mikey/Meta
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The SRFloatPromptInput node is designed to process and manage floating point values. It plays a key role in receiving and storing input values, which are then used in subsequent computing operations. This node ensures that input is a floating point, thereby preserving the integrity of data throughout the system.

# Input types
## Required
- input_float
    - The input_float parameter is essential for the operation of the node, because it means the floating point value to be processed. It is a necessary input, indicating its fundamental importance in the node function. The node relies on this parameter to perform its assigned tasks.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- unique_id
    - The unique_id parameter is used as an identifier for input_float values in node operations. Although it is not mandatory, it can be used to track and quote specific inputs, enhance node management and organize data.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- prompt
    - Prompt parameters are used to facilitate interaction with nodes and allow custom input processes. It is an optional input that can be used to adjust nodes to specific requirements or circumstances.
    - Comfy dtype: PROMPT
    - Python dtype: dict

# Output types
- result
    - The result parameter represents the output after the node handles input_float. It marks the completion of the node operation and returns the result to the user for further use or analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SRFloatPromptInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_float': ('FLOAT', {'forceInput': True})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'add'
    CATEGORY = 'Mikey/Meta'

    def add(self, input_float, unique_id=None, prompt=None):
        prompt.get(str(unique_id))['inputs']['sr_val'] = str(input_float)
        return (input_float,)
```