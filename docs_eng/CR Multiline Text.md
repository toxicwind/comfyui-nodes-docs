# Documentation
- Class name: CR_MultilineText
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_MultilineText is designed to process and operate text data, providing functions such as converting text from CSV formatting, splitting strings according to the given separator, and removing unnecessary characters. It plays a key role in text pre-processing of various applications, ensuring that text is properly formatted for downstream tasks.

# Input types
## Required
- text
    - The `text' parameter is the main input of the node and can contain data in multi-line text or CSV format. It is essential for the operation of the node, as it determines the content to be processed and converted.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- convert_from_csv
    - The `convert_from_csv' parameter allows the user to specify whether the input text should be considered CSV data. When enabled, the node will interpret the text in accordance with the CSV rules, which is important for converting table data into available formats.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- csv_quote_char
    - The `csv_quate_char' parameter defines the characters used to refer to fields in CSV data, which is essential when parsing CSV text to ensure accuracy and processing fields containing comma or line breaks.
    - Comfy dtype: STRING
    - Python dtype: str
- remove_chars
    - The `remove_chars' parameter indicates whether certain characters should be removed from the text. This is important for cleaning the text and preparing it for further analysis or processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- chars_to_remove
    - The `chars_to_remove' parameter specifies the characters that need to be removed from the text when the `remove_chars' option is enabled. It plays an important role in the custom text cleanup process.
    - Comfy dtype: STRING
    - Python dtype: str
- split_string
    - The `split_string' parameter determines whether the input text should be divided into separate values based on separator. This function is essential for dissecting complex strings into manageable parts.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- multiline_text
    - The'multiline_text' output contains all converted text. It represents the final state of the text and is ready for follow-up action.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help'output provides a link to a document or help page associated with the node. It is a quick reference for users seeking more information or help on how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_MultilineText:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': True}), 'convert_from_csv': ('BOOLEAN', {'default': False}), 'csv_quote_char': ('STRING', {'default': "'", 'choices': ["'", '"']}), 'remove_chars': ('BOOLEAN', {'default': False}), 'chars_to_remove': ('STRING', {'multiline': False, 'default': ''}), 'split_string': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('multiline_text', 'show_help')
    FUNCTION = 'text_multiline'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def text_multiline(self, text, chars_to_remove, split_string=False, remove_chars=False, convert_from_csv=False, csv_quote_char="'"):
        new_text = []
        text = text.rstrip(',')
        if convert_from_csv:
            csv_reader = csv.reader(io.StringIO(text), quotechar=csv_quote_char)
            for row in csv_reader:
                new_text.extend(row)
        if split_string:
            if text.startswith("'") and text.endswith("'"):
                text = text[1:-1]
                values = [value.strip() for value in text.split("', '")]
                new_text.extend(values)
            elif text.startswith('"') and text.endswith('"'):
                text = text[1:-1]
                values = [value.strip() for value in text.split('", "')]
                new_text.extend(values)
            elif ',' in text and text.count("'") % 2 == 0:
                text = text.replace("'", '')
                values = [value.strip() for value in text.split(',')]
                new_text.extend(values)
            elif ',' in text and text.count('"') % 2 == 0:
                text = text.replace('"', '')
                values = [value.strip() for value in text.split(',')]
                new_text.extend(values)
        if convert_from_csv == False and split_string == False:
            for line in io.StringIO(text):
                if not line.strip().startswith('#'):
                    if not line.strip().startswith('\n'):
                        line = line.replace('\n', '')
                    if remove_chars:
                        line = line.replace(chars_to_remove, '')
                    new_text.append(line)
        new_text = '\n'.join(new_text)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-multiline-text'
        return (new_text, show_help)
```