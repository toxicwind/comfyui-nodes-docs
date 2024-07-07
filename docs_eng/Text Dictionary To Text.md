# Documentation
- Class name: WAS_Dictionary_to_Text
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Dictionary_to_Text node is designed to convert the given dictionary into a text expression. It plays a key role in transforming structured data into readable formats, which are essential for a variety of applications, such as data analysis, reporting and user interfaces. The node streamlines the process of generating human-readable text from a complex dictionary structure and enhances the overall workflow for data presentation.

# Input types
## Required
- dictionary
    - The `dictionary' parameter is essential for the operation of the node, because it is a node processing process to generate the main input into the text. It is a structured expression of the data, which is interpreted and converted to text format. The quality of the output text depends heavily on the structure and content of the entered dictionary.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Output types
- text
    - `text' output is the result of the node conversion process, which receives the entry of a dictionary and generates text expression. This output is important because it provides a human readable format that can be easily understood and can be used in a variety of contexts, such as documents, communications or further data processing.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dictionary_to_Text:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dictionary': ('DICT',)}, 'optional': {}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'dictionary_to_text'
    CATEGORY = 'WAS Suite/Text'

    def dictionary_to_text(self, dictionary):
        return (str(dictionary),)
```