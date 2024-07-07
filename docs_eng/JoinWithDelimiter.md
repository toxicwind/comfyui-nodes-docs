# Documentation
- Class name: JoinWithDelimiter
- Category: ♾️Mixlab/Prompt
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node links the list of text strings to a single string and uses the specified separator to separate the items. It is intended to simplify the text grouping process and to provide a direct solution for creating a uniform text output from multiple inputs.

# Input types
## Required
- text_list
    - The list of text strings that you want to connect to. This parameter is important because it forms the basis for node operations and determines the content and quantity of text that you want to merge.
    - Comfy dtype: ANY
    - Python dtype: List[str]
- delimiter
    - Characters or strings that separate elements in text_list. The selection of separator affects the readability and structure of the result string.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- result
    - , all of the text_list elements are connected with the specified separator.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class JoinWithDelimiter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_list': (any_type,), 'delimiter': (['newline', 'comma', 'backslash', 'space'],)}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,)

    def run(self, text_list, delimiter):
        delimiter = delimiter[0]
        if delimiter == 'newline':
            delimiter = '\n'
        elif delimiter == 'comma':
            delimiter = ','
        elif delimiter == 'backslash':
            delimiter = '\\'
        elif delimiter == 'space':
            delimiter = ' '
        t = ''
        if isinstance(text_list, list):
            t = join_with_(text_list, delimiter)
        return (t,)
```