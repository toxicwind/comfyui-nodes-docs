# Documentation
- Class name: CR_TextList
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextList node is designed to process and operate text data, especially for creating lists from multi-line text input. It allows users to select a subset of text lines based on the initial index and the maximum number of lines to include. It provides a simplified method for text list management within the Comfyroll framework.

# Input types
## Required
- multiline_text
    - The'multiline_text' parameter is the main input of the node, accepting text blocks that may contain multiple lines. It plays a key role in determining the source material that will generate the list.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- start_index
    - The'start_index' parameter specifies where the list generation in the text should start. It is important to control the starting point of the text line contained in the final list.
    - Comfy dtype: INT
    - Python dtype: int
- max_rows
    - The `max_rows' parameter sets a limit on the number of text lines to be included in the list. It is important to define the range of text data to be processed and returned by nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- selected_rows
    - The `seleted_rows' output contains text lines selected according to input parameters. It represents the core result of the node operation and encapsulates the processed text data.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - The ‘show_help’ output provides a URL link to a document to obtain further help or guidance on the use of nodes. This is a valuable resource for users seeking more information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'multiline_text': ('STRING', {'multiline': True, 'default': 'text'}), 'start_index': ('INT', {'default': 0, 'min': 0, 'max': 9999}), 'max_rows': ('INT', {'default': 1000, 'min': 1, 'max': 9999})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List')

    def make_list(self, multiline_text, start_index, max_rows, loops):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-text-list'
        lines = multiline_text.split('\n')
        start_index = max(0, min(start_index, len(lines) - 1))
        end_index = min(start_index + max_rows, len(lines))
        selected_rows = lines[start_index:end_index]
        return (selected_rows, show_help)
```