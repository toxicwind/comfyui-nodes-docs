# Documentation
- Class name: CR_IndexReset
- Category: Comfyroll/Utils/Index
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_IndexReset is designed to reset given indexes to specified values, ensuring continuity and correctness of indexing operations within the system. It plays a key role in maintaining the integrity of the data series by providing a direct mechanism for re-introduction of index counters.

# Input types
## Required
- index
    - The `index' parameter is essential for identifying specific locations or serial numbers that need to be replaced in a data set or operation. It directly influences the execution of nodes by determining which index is reallocated to `reset_to' values.
    - Comfy dtype: INT
    - Python dtype: int
- reset_to
    - The `reset_to' parameter defines a new starting point for the index after the reset operation. It is essential for setting the correct initial value that `index' will be assigned after the reset, thus affecting the system's subsequent behaviour.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- index
    - The `index' output reflects a reset index value that represents a new location or serial number in the data set or operation.
    - Comfy dtype: INT
    - Python dtype: int
- reset_to
    - The `reset_to' output is the value reset to the index, indicating the new initial point of the index in the system.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The'show_help' output provides a URL link to a document to obtain further help or information about node operations. This is particularly useful for users seeking additional guidance on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IndexReset:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 1, 'min': 0, 'max': 10000, 'forceInput': True}), 'reset_to': ('INT', {'default': 1, 'min': 0, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'INT', 'STRING')
    RETURN_NAMES = ('index', 'reset_to', 'show_help')
    FUNCTION = 'reset'
    CATEGORY = icons.get('Comfyroll/Utils/Index')

    def reset(self, index, reset_to):
        index = reset_to
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Index-Nodes#cr-index-reset'
        return (index, reset_to, show_help)
```