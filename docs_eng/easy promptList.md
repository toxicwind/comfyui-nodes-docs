# Documentation
- Class name: promptList
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node simplifies the process of aggregation and processing text input, facilitating the creation of a list of tips in various applications. It emphasizes the efficient processing of string data to ensure that node's role in the workflow is to centralize and organize text information.

# Input types
## Required
- prompt_1
    - The main text input is used as the basis for node operations. It is essential because it sets the initial context for subsequent hint processing and aggregation.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_2
    - Additional text input increases the diversity and complexity of the tips being processed. It enhances the ability of nodes to process various text inputes.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_3
    - Further text entry is essential for the function of integrating and managing multiple hints at nodes to ensure a comprehensive approach to text processing.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_4
    - Another input that is essential for the effective organization and construction of nodes affects the coherence and relevance of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt_5
    - The final text input refines the reminder set to ensure that node handles a wide range of text input and maintains the integrity of the overall list of hints.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- optional_prompt_list
    - An optional list of tips, made available, expands the ability of nodes to manage and process a larger volume of text data and enhances the comprehensiveness of outputs.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Output types
- prompt_list
    - A consolidated list of hints, representing the output of nodes, covers processed text input in a structured and orderly manner.
    - Comfy dtype: LIST
    - Python dtype: List[str]
- prompt_strings
    - The serial version of the list of hints presents the aggregate text data as a single string for use in subsequent applications.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class promptList:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'prompt_1': ('STRING', {'multiline': True, 'default': ''}), 'prompt_2': ('STRING', {'multiline': True, 'default': ''}), 'prompt_3': ('STRING', {'multiline': True, 'default': ''}), 'prompt_4': ('STRING', {'multiline': True, 'default': ''}), 'prompt_5': ('STRING', {'multiline': True, 'default': ''})}, 'optional': {'optional_prompt_list': ('LIST',)}}
    RETURN_TYPES = ('LIST', 'STRING')
    RETURN_NAMES = ('prompt_list', 'prompt_strings')
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Prompt'

    def run(self, **kwargs):
        prompts = []
        if 'optional_prompt_list' in kwargs:
            for l in kwargs['optional_prompt_list']:
                prompts.append(l)
        for k in sorted(kwargs.keys()):
            v = kwargs[k]
            if isinstance(v, str) and v != '':
                prompts.append(v)
        return (prompts, prompts)
```