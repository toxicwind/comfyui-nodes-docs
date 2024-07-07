# Documentation
- Class name: WAS_Text_List_to_Text
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The SAS_Text_List_to_Text node is designed to merge a series of text strings into a single text string. It achieves this by inserting a given separator between each element of the list, effectively consolidating them into a coherent sequence. This node plays a key role in the text-processing workflow that requires multiple text inputation into a uniform format.

# Input types
## Required
- delimiter
    - The separator parameter defines the character or string to be used when connecting elements of the text list to one another. It is essential to determine the format of the final consolidated text and can significantly influence the readability and structure of the output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_list
    - The text_list parameter is the collection of a series of text stringes that the node will process. This is a mandatory input that indicates that the node needs these data to perform its functions. The node operations depend directly on the content and structure of the text_list, which determines the final output after the connection process.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Output types
- merged_text
    - Merged_text output is the result of using the specified separator to connect to text_list. It means that the grouped text is a single string that can be used for further processing or analysis in downstream tasks.
    - Comfy dtype: TEXT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_List_to_Text:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'delimiter': ('STRING', {'default': ', '}), 'text_list': ('LIST', {'forceInput': True})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_list_to_text'
    CATEGORY = 'WAS Suite/Text'

    def text_list_to_text(self, delimiter, text_list):
        if delimiter == '\\n':
            delimiter = '\n'
        merged_text = delimiter.join(text_list)
        return (merged_text,)
```