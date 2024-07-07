# Documentation
- Class name: CR_IncrementIndex
- Category: Comfyroll/Utils/Index
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_InclementIndex is designed to perform a simple but critical operation in data processing and iterative tasks. It accepts an initial index and a space value, then increases the index at a specified interval. This function is essential for browsing the location of a list, array or any sequential data structure. The node also provides a link to the document so that users can obtain more guidance when needed.

# Input types
## Required
- index
    - The " index " parameter is the starting point of the incremental operation. It is important because it determines where the increment begins. This parameter is essential to ensure the correct sequence and indexing in subsequent operations.
    - Comfy dtype: INT
    - Python dtype: int
- interval
    - The " interval " parameter defines the size of the step that the index will increase. It is important because it determines the spacing between increment values and affects the manner in which the number series is generated.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- index
    - The "index" output reflects a new location after adding the original index at intervals. It is essential to maintain the correct progress through the data series.
    - Comfy dtype: INT
    - Python dtype: int
- interval
    - The " interval " output is the same as the input interval, indicating the size of the step used for the increment. It can be used in further operations that require the spacing value.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The “show_help” output provides a URL link to the node document, providing users with more detailed information and direct references to guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IncrementIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 1, 'min': -10000, 'max': 10000, 'forceInput': True}), 'interval': ('INT', {'default': 1, 'min': -10000, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'INT', 'STRING')
    RETURN_NAMES = ('index', 'interval', 'show_help')
    FUNCTION = 'increment'
    CATEGORY = icons.get('Comfyroll/Utils/Index')

    def increment(self, index, interval):
        index += interval
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Index-Nodes#cr-index-increment'
        return (index, show_help)
```