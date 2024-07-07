# Documentation
- Class name: SRStringPromptInput
- Category: Mikey/Meta
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The SRStringPromptInput node is designed to receive and process text input, especially for string data. It plays a key role in processing string tips by integrating them into structured formats that can be used for various applications. The node ensures that the input string is correctly recorded and associated with the only identifier that can be retrieved and used in subsequent operations.

# Input types
## Required
- input_str
    - Input_str parameters are essential for the operation of nodes, as they represent text data to be processed. They are the core elements of node processing, the quality of which directly influences the output of nodes and subsequent data processing.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- unique_id
    - The unique_id parameter, although optional, plays a key role in the node by providing a unique identifier for each input string. This helps index and quote input strings for future use, thereby increasing the efficiency of the node in the management and retrieval of data.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- prompt
    - When using the prompt parameter, it adds a layer of context to the input string by linking the input string to a specific hint. This is particularly useful when the input needs to be understood in a given context, thus enriching the function of the node.
    - Comfy dtype: PROMPT
    - Python dtype: dict

# Output types
- output
    - The output of the SRStringPromptInput node is a processed input string that has been successfully recorded and associated with the only identifier and hint provided. This output is important because it confirms that the input data has been successfully integrated into the system.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SRStringPromptInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_str': ('STRING', {'forceInput': True})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'add'
    CATEGORY = 'Mikey/Meta'

    def add(self, input_str, unique_id=None, prompt=None):
        prompt.get(str(unique_id))['inputs']['sr_val'] = input_str
        return (input_str,)
```