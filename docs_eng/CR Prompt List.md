# Documentation
- Class name: CR_PromptList
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_PromptList node is designed to process and operate text data in the form of a list. It accepts multi-line text input and allows users to add text before and after each line of text, and selects the range of lines in the list by specifying the starting index and the maximum number of lines. The function of the node is focused on creating a list of hints and text text from the input text, which can be used for various purposes, such as generating tips or organizing text data for the AI model.

# Input types
## Required
- multiline_text
    - The multiline_text parameter is the main input of the node and contains text that will be split into the list. It supports multiline input, allowing the processing of complex and detailed text data.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prepend_text
    - The prepend_text parameter allows the user to specify a string that will be added to the beginning of each line in the output list. This can be in a format from the defined list or by adding a context to the text.
    - Comfy dtype: STRING
    - Python dtype: str
- append_text
    - Append_text parameters enable the user to add a string at the end of each row in the output list, which is very useful for expanding the text or adding additional information.
    - Comfy dtype: STRING
    - Python dtype: str
- start_index
    - Start_index parameters determine the node in the list from which the rows will be selected. It provides control over the subsets of the list to be processed.
    - Comfy dtype: INT
    - Python dtype: int
- max_rows
    - The max_rows parameter setting will contain the maximum number of rows in the output list. It will help limit the size of the list and manage the amount of data being processed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- prompt
    - Prompt output is a list of strings in which each string consists of a pre-text, a line in a multi-line text, and a back-to-back text. This can be used to create a hint for an AI application.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- body_text
    - The body_text output is a string list that represents the line selected from the input of a multi-line text. It is the main element of further processing or analysis.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Show_help output provides a URL link to a document or help page associated with node functions. This is very useful for users seeking more information on how to use nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PromptList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prepend_text': ('STRING', {'multiline': False, 'default': ''}), 'multiline_text': ('STRING', {'multiline': True, 'default': 'body_text'}), 'append_text': ('STRING', {'multiline': False, 'default': ''}), 'start_index': ('INT', {'default': 0, 'min': 0, 'max': 9999}), 'max_rows': ('INT', {'default': 1000, 'min': 1, 'max': 9999})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('prompt', 'body_text', 'show_help')
    OUTPUT_IS_LIST = (True, True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List')

    def make_list(self, multiline_text, prepend_text='', append_text='', start_index=0, max_rows=9999):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-prompt-list'
        lines = multiline_text.split('\n')
        start_index = max(0, min(start_index, len(lines) - 1))
        end_index = min(start_index + max_rows, len(lines))
        selected_rows = lines[start_index:end_index]
        prompt_list_out = [prepend_text + line + append_text for line in selected_rows]
        body_list_out = selected_rows
        return (prompt_list_out, body_list_out, show_help)
```