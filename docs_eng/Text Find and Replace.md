# Documentation
- Class name: WAS_Search_and_Replace
- Category: WAS Suite/Text/Search
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node is designed to search for and replace the given text. It recognizes the number of times a substring appears in the text and replaces it with a different substring. The function of the node is to facilitate text operations and data cleansing tasks by replacing the interface with a direct string.

# Input types
## Required
- text
    - Text parameters are the main input of the node, which contains the text to be processed. It is essential because it determines the context in which search and replacement operations will take place. The execution and results of the node are directly influenced by the content and structure of the text provided.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- find
    - The search parameter specifies the substring in which the node will search in the text. It plays an important role in determining the scope of the operation, as the node will be replaced with this substring. The validity of the node depends on the accuracy of the substring provided in this parameter.
    - Comfy dtype: STRING
    - Python dtype: str
- replace
    - The replacement parameter defines the substrings that will be used to replace the number of times the search parameter appears in the text. It is essential for the conversion process, as it determines what the replacement will be. The ability of the node to modify the text is directly related to the value assigned to this parameter.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result_text
    - The result of the node function is represented by the final state of the text with the specified replacement.
    - Comfy dtype: STRING
    - Python dtype: str
- replacement_count_number
    - The output parameter provides a count of how many times a substring has been replaced in the text. This value is important because it quantifys the range of replacement operations performed by the node.
    - Comfy dtype: NUMBER
    - Python dtype: int
- replacement_count_float
    - Replacement_count_float output parameters provide replacement counts in the form of floating points. Where further calculation or analysis of replacement counts is required, it may be useful to use decimals for replacement counts.
    - Comfy dtype: FLOAT
    - Python dtype: float
- replacement_count_int
    - Replacement_count_int output parameters present replacement counts in integer form. It is expressed as a direct value of the total number of replacements and can be used in various calculations or statistical settings.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Search_and_Replace:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'find': ('STRING', {'default': '', 'multiline': False}), 'replace': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = (TEXT_TYPE, 'NUMBER', 'FLOAT', 'INT')
    RETURN_NAMES = ('result_text', 'replacement_count_number', 'replacement_count_float', 'replacement_count_int')
    FUNCTION = 'text_search_and_replace'
    CATEGORY = 'WAS Suite/Text/Search'

    def text_search_and_replace(self, text, find, replace):
        (modified_text, count) = self.replace_substring(text, find, replace)
        return (modified_text, count, float(count), int(count))

    def replace_substring(self, text, find, replace):
        (modified_text, count) = re.subn(find, replace, text)
        return (modified_text, count)
```