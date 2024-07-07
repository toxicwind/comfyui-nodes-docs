# Documentation
- Class name: CR_TextCycler
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextCycler node is designed to reproduce the number of times a text line is specified in the given circular structure. It is used to automate the text reproduction process to improve the efficiency of the text-processing workflow.

# Input types
## Required
- text
    - The 'text' parameter is the input text that needs to be looped. It can contain multiple lines, which are essential for the operation of nodes, as it determines what will be repeated.
    - Comfy dtype: STRING
    - Python dtype: str
- repeats
    - The'repeats' parameter indicates the number of times a line text will be copied. It is a key element that directly affects the number of text output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- loops
    - The 'loops' parameter specifies the number of times the entire text block will be looped through its repeated times. It adds an additional layer of repetition to the text processing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- show_text
    - The'show_text' output provides the final loop text after all duplicate and loop processing has been completed. It represents the result of node text operation.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextCycler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': ''}), 'repeats': ('INT', {'default': 1, 'min': 1, 'max': 99999}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 99999})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('STRING', 'show_text')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'cycle'
    CATEGORY = icons.get('Comfyroll/List')

    def cycle(self, text, repeats, loops=1):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-cycler'
        lines = text.split('\n')
        list_out = []
        for i in range(loops):
            for text_item in lines:
                for _ in range(repeats):
                    list_out.append(text_item)
        return (list_out, show_help)
```