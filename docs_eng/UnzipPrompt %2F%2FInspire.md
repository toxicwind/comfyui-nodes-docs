# Documentation
- Class name: UnzipPrompt
- Category: InspirePack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

It is a key component of the workflow that needs to process the compressed data to ensure that the data is readily available and properly formatted for follow-up.

# Input types
## Required
- zipped_prompt
    - The zpped_prompt parameter is necessary because it contains compressed data for node design processing. It directly affects the operation and output quality of the node, because the main function of the node is to extract and process the contents of this input.
    - Comfy dtype: ZIPPED_PROMPT
    - Python dtype: bytes

# Output types
- positive
    - Positive output represents the content successfully extracted and processed from zipped_prompt. It is a key result of node operations, indicating that the data are properly processed and ready for further use.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative output provides information on any problems or errors encountered during the processing of zipped_prompt. This output is important for understanding the success or failure of node operations and, if necessary, for troubleshooting.
    - Comfy dtype: STRING
    - Python dtype: str
- name
    - Name output usually contains a file name or identifier for zpped_prompt. This output is useful for tracking and quoting processed data in workflows.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class UnzipPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'zipped_prompt': ('ZIPPED_PROMPT',)}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative', 'name')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'

    def doit(self, zipped_prompt):
        return zipped_prompt
```