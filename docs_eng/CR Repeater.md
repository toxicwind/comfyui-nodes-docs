# Documentation
- Class name: CR_Repeater
- Category: Comfyroll/List/Utils
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Repeater is a practical tool node designed to repeat the number of times the items in the list are specified. It receives a list of entries and an integer number indicating the number of times they are repeated, and then produces a new list, each of which is repeated according to the given count. This node is particularly suitable for scenarios that require multiple processing of the same data without changing the original list.

# Input types
## Required
- input_data
    - The `input_data' parameter represents the list of items to be repeated. It is an essential part of the node operation, because it determines the content of the new list to be created. The effect of this parameter is direct, because it determines what will be repeated, thus affecting the final output list.
    - Comfy dtype: any_type
    - Python dtype: List[Any]
- repeats
    - The `repeats' parameter specifies the number of times each item in the `input_data' list should be repeated. It is a key element because it directly affects the length of the output list. The `repeats' value must be a positive integer to ensure that the repetition process is meaningful and the output list is correctly formed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- list
    - The `list' output parameter is the result of a process that repeats every item from `input_data' to `repeats'. It is important because it represents the conversion version of the original list, which is the main objective of the node function.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - The'show_help' output provides a URL link to a document or help page associated with the CR_Repeater node. It serves as a quick reference for users seeking more information or help on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Repeater:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_data': (any_type,), 'repeats': ('INT', {'default': 1, 'min': 1, 'max': 99999})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('list', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'repeat_list_items'
    CATEGORY = icons.get('Comfyroll/List/Utils')

    def repeat_list_items(self, input_data, repeats):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-repeater'
        new_list = []
        if isinstance(input_data, list):
            new_list = []
            for item in input_data:
                new_list.extend([item] * repeats)
            return (new_list, show_help)
        else:
            return ([input_data] * repeats, show_help)
```