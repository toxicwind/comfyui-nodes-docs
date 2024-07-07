# Documentation
- Class name: WAS_Dictionary_Convert
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `dictionary_convert'method is designed to convert a dictionary string expression into an available dictionary object. It plays a key role in the pre-processing phase of text-based applications to ensure that input data are properly formatted for subsequent processing.

# Input types
## Required
- dictionary_text
    - The parameter `dictionary_text'is necessary because it provides the original text that needs to be converted to a dictionary. Its correct formatting is essential for the successful implementation of the node function.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- converted_dictionary
    - Output `converted_dictionary'is very important because it represents a structured dictionary object generated during the conversion process. It is ready for use in the application’s follow-up operation.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dictionary_Convert:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dictionary_text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = ('DICT',)
    FUNCTION = 'dictionary_convert'
    CATEGORY = 'WAS Suite/Text'

    def dictionary_convert(self, dictionary_text):
        return (ast.literal_eval(dictionary_text),)
```