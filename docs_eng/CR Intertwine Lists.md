# Documentation
- Class name: CR_IntertwineLists
- Category: Comfyroll/List/Utils
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_IntertwineLists is a practical tool node designed to group two lists into single lists, each of which is a connection to the corresponding elements in the input list. It is used to woven multiple data streams into coherent structures that facilitate complex data operations and analysis.

# Input types
## Required
- list1
    - List1 is the first input list to be combined with the second list. It plays a vital role in the operation of the node, as it constitutes half of the final list.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- list2
    - List2 is the second input list that will be interwoven with the first list. It is as important as list1 because it adds list1 to create a new list with a combination of elements.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Output types
- combined_list
    - The grouping list is the output of the node, which contains elements derived from the interwoven input list. It is important because it represents an integrated data structure for further processing.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Show_help output provides a URL link to the document for further help and guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IntertwineLists:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'list1': ('STRING', {'multiline': True, 'default': '', 'forceInput': True}), 'list2': ('STRING', {'multiline': True, 'default': '', 'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List/Utils')

    def make_list(self, list1, list2):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-intertwine-lists'
        min_length = min(len(list1), len(list2))
        combined_list = []
        combined_element = str(list1) + ', ' + str(list2)
        combined_list.append(combined_element)
        return (combined_list, show_help)
```