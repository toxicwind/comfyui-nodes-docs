# Documentation
- Class name: CR_TextBlacklist
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_TextBlacklist is a text-processing tool node that is used to purify text content by replacing a specified blacklist vocabulary to conform to content specifications or personal preferences.

# Input types
## Required
- text
    - The parameter 'text' is the input text to be processed by the node. It is essential because it is the content that will be scanned to find the blacklist vocabulary and may be modified.
    - Comfy dtype: STRING
    - Python dtype: str
- blacklist_words
    - Parameter 'blacklist_words' contains words that need to be replaced in the input text. Each line in the parameter represents a separate word that you want to blacklist.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- replacement_text
    - Parameter 'Replacement_text' specifies the text that will be used to replace any blacklist vocabulary found in the input. It provides a way to customize the output text to meet specific needs.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - The output of the CR_TextBlacklist node is a modified text in which the blacklist word has been specified for replacement. It represents the final result of the text-processing operation.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Parameter'show_help' provides a document URL link to obtain further help or information about the use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextBlacklist:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': '', 'forceInput': True}), 'blacklist_words': ('STRING', {'multiline': True, 'default': ''})}, 'optional': {'replacement_text': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'replace_text'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def replace_text(self, text, blacklist_words, replacement_text=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-blacklist'
        text_out = text
        for line in blacklist_words.split('\n'):
            if line.strip():
                text_out = text_out.replace(line.strip(), replacement_text)
        return (text_out, show_help)
```