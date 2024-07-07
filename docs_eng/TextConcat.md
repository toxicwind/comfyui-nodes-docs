# Documentation
- Class name: TextConcat
- Category: Mikey/Text
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The TextConcat node is designed to group multiple strings into single strings efficiently. It achieves this function by accepting text lists and separators, and then by using the specified separator to connect the text string provided. This node is very useful in creating a coherent string from different message segments, which is critical in text processing and data preparation tasks.

# Input types
## Required
- delimiter
    - The separator parameter is a string that is used to separate text when it is entered in a string. It plays a key role in determining the final format of the output string, allowing the user to control the space and separation between string text.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- text1
    - The text 1 parameter represents the first text input that can be linked to the other text. It is optional and, if provided, it will be included in the final string.
    - Comfy dtype: STRING
    - Python dtype: str
- text2
    - The text2 parameter is another optional text input that can be included in the chain process. It allows further customization of the final string.
    - Comfy dtype: STRING
    - Python dtype: str
- text3
    - The text3 parameter is another additional optional text input in the chain. It expands the function to include more text elements in the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- text4
    - The text 4 parameter is another optional input that can be linked to other text. It provides further flexibility in the output string that you want to build.
    - Comfy dtype: STRING
    - Python dtype: str
- text5
    - The text5 parameter is the last optional text input for a string. It provides the last chance to add text before the string is finally determined.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- concatenated_text
    - The final string that you use to connect all input text with a given separator. It represents the result of the chain process and is the main output of the TextConcat node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TextConcat:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'delimiter': ('STRING', {'default': ' '})}, 'optional': {'text1': ('STRING', {'default': ''}), 'text2': ('STRING', {'default': ''}), 'text3': ('STRING', {'default': ''}), 'text4': ('STRING', {'default': ''}), 'text5': ('STRING', {'default': ''})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'concat'
    CATEGORY = 'Mikey/Text'

    def concat(self, delimiter, text1, text2, text3, text4, text5):
        texts = []
        if text1:
            texts.append(text1)
        if text2:
            texts.append(text2)
        if text3:
            texts.append(text3)
        if text4:
            texts.append(text4)
        if text5:
            texts.append(text5)
        text = delimiter.join(texts)
        return (text,)
```