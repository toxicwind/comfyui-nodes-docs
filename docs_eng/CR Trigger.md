# Documentation
- Class name: CR_Trigger
- Category: Comfyroll/Utils/Index
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Trigger nodes are designed to perform a condition check to determine whether the given index matches the specified trigger value. It plays a key role in controlling data flow and implementation in the system, allowing for selective processing based on index conditions.

# Input types
## Required
- index
    - The `index' parameter is essential for the operation of the node because it indicates the current position or identifier in the sequence being evaluated. It is used to create a condition that, when that condition is met, the node triggers the response.
    - Comfy dtype: INT
    - Python dtype: int
- trigger_value
    - The `trigger_value' parameter defines the particular value that the index must match so that the node considers the condition to be satisfied. It is the key determinant in the node decision-making process and directly influences the output of the node.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- index
    - The `index' output reflects the current index value of the node assessment. It is important because it provides a reference for the location in the sequence examined.
    - Comfy dtype: INT
    - Python dtype: int
- trigger
    - The `trigger' output is a boolean value that indicates whether the index matches the trigger value. It is essential to rely on downstream processes that know whether conditions are met.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - The `show_help' output provides a URL link to the node document and provides users with a direct reference to the node's use guide and additional information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Trigger:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'trigger_value': ('INT', {'default': 1, 'min': 0, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('index', 'trigger', 'show_help')
    FUNCTION = 'trigger'
    CATEGORY = icons.get('Comfyroll/Utils/Index')

    def trigger(self, index, trigger_value):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Index-Nodes#cr-trigger'
        return (index, index == trigger_value, show_help)
```