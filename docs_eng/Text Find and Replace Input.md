# Documentation
- Class name: WAS_Search_and_Replace_Input
- Category: WAS Suite/Text/Search
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Search_and_Replace_Input node is designed to perform search and replacement operations for given text. It efficiently locates all specified substrings in the text and replaces them with new substrings. This node is particularly suitable for pre-processing text data, where the need to update or correct particular phrases is common. It contributes to the entire workflow by ensuring that the text is accurately adapted to the needs of users.

# Input types
## Required
- text
    - The `text' parameter is the main input of the node, representing the text that will be searched and possibly modified. It is vital because it determines the context in which the search and replacement operation will take place. The node results depend heavily on the content and structure of the `text' parameter.
    - Comfy dtype: STRING
    - Python dtype: str
- find
    - The 'find' parameter specifies the substring that the node will search in 'text'. It plays a key role in identifying the text parts that need to be replaced. The validity of the search and replacement operation is directly affected by the accuracy of the 'find'parameter.
    - Comfy dtype: STRING
    - Python dtype: str
- replace
    - The `replace' parameter defines the new substrings that will be found to replace the `find' parameter. It is important because it determines the end result of the text after the replacement process. The `replace' value selection can significantly change the meaning or structure of the result text.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result_text
    - 'Result_text' output contains all text modified after the replacement has been completed. It is a direct reflection of the input 'text', in which the 'find' sub-character is replaced by the'replace' substring. This output is important because it represents the final state of text processing.
    - Comfy dtype: STRING
    - Python dtype: str
- replacement_count_number
    - `Replacement_count_number' gives a count of how many times the 'find' substring has been replaced by the'replace' substring in the text. This value output is useful for analysis or recording purposes and provides insight into the extent to which the text has been modified.
    - Comfy dtype: NUMBER
    - Python dtype: float
- replacement_count_float
    - ‘Replacement_account_float’ output is the same as ‘replacement_account_number’, but is counted in the form of floating points. This output is very useful where further calculation or statistical analysis of replacement counts is required.
    - Comfy dtype: FLOAT
    - Python dtype: float
- replacement_count_int
    - ‘Replacement_count_int’ output provides a replacement count in in integer form. This output is particularly useful when exact replacements are required for the application of an integer, such as data recording or integer-based calculations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Search_and_Replace_Input:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'find': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'replace': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = (TEXT_TYPE, 'NUMBER', 'FLOAT', 'INT')
    RETURN_NAMES = ('result_text', 'replacement_count_number', 'replacement_count_float', 'replacement_count_int')
    FUNCTION = 'text_search_and_replace'
    CATEGORY = 'WAS Suite/Text/Search'

    def text_search_and_replace(self, text, find, replace):
        count = 0
        new_text = text
        while find in new_text:
            new_text = new_text.replace(find, replace, 1)
            count += 1
        return (new_text, count, float(count), int(count))

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```