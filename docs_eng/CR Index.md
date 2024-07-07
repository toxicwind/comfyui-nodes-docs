# Documentation
- Class name: CR_Index
- Category: Comfyroll/Utils/Index
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_Index node is designed to centralize the management and retrieval of specific indexes from given data. It provides the function of an efficient index of large data sets to meet the needs of various data operations and analytical tasks. The node emphasizes simplicity and flexibility to ensure that users can easily integrate them into their workflows and process them.

# Input types
## Required
- index
    - The `index' parameter is essential to specify the location of the node within the data set from which the information will be retrieved. It directly influences the output of the node by determining the exact data point to be accessed. This parameter is essential for the data selection and filtering process in the workflow.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- print_to_console
    - The 'print_to_console' parameter allows the user to switch the output of the control table. When set to 'Yes', it enables the node to print the current index value to the control table and provides real-time feedback during the execution. This feature is particularly useful for debugging and monitoring the progress of data indexing operations.
    - Comfy dtype: COMBO['Yes', 'No']
    - Python dtype: str

# Output types
- INT
    - The 'INT' output provides index values that are retrieved from the data pool and can be further used in downstream processes. This output is important because it provides the basis for subsequent data operations and analysis and ensures the integrity and continuity of workflows.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The'show_help' output provides a URL link to the node document, allowing users to access additional information and guidance on how to use the node effectively. This is particularly useful for new users or when further clarification of the node function is needed.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Index:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 1, 'min': 0, 'max': 10000}), 'print_to_console': (['Yes', 'No'],)}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'index'
    CATEGORY = icons.get('Comfyroll/Utils/Index')

    def index(self, index, print_to_console):
        if print_to_console == 'Yes':
            print(f'[Info] CR Index:{index}')
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Index-Nodes#cr-index'
        return (index, show_help)
```