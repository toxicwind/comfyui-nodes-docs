# Documentation
- Class name: CR_RandomMultilineValues
- Category: Comfyroll/Utils/Random
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_RandomMultilineValues is designed to generate random multi-line text based on the specified value type and formatting options. It produces strings in various formats, such as binary, decimal, natural, hexadecimal, alpha, alpha-numeric or custom-defined. Node allows the number of rows and the length of each string to be set and ensures that output is highly common to different cases.

# Input types
## Required
- seed
    - Seed parameters are used to initialize the random number generator to produce repeatable results. It is essential to ensure consistency in the random text generated, especially when debugging or requiring random values from the same sequence.
    - Comfy dtype: INT
    - Python dtype: int
- value_type
    - The value type parameter determines the format in which the text is generated. It can be set to binary, decimal, natural, hexadecimal, alphabetic, alphanumeric or custom-defined, which determines the character set used to generate random text.
    - Comfy dtype: STRING
    - Python dtype: str
- rows
    - Line parameters specify the number of lines in which the text is generated. It directly affects the length of the output and allows users to control the amount of data generated.
    - Comfy dtype: INT
    - Python dtype: int
- string_length
    - String length parameters define the number of characters per line in the text generated. It is essential for setting the particle size of each text string.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- custom_values
    - When the value type is set as a custom, thecustom_values parameter allows the user to define its own character set to generate random text. This provides flexibility for specific cases that require non-standard character sets.
    - Comfy dtype: STRING
    - Python dtype: str
- prepend_text
    - Prepend_text parameters add a fixed string at the beginning of each line of the text generated. This is very useful for adding an output prefix, which may be important for formatting or context purposes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- multiline_text
    - Multiline_text output contains the generated random text formatted as multiple lines according to the number of rows and string length parameters specified. It represents the main result of node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help output provides a URL link to the node document page, providing additional information and guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomMultilineValues:

    @classmethod
    def INPUT_TYPES(cls):
        types = ['binary', 'decimal', 'natural', 'hexadecimal', 'alphabetic', 'alphanumeric', 'custom']
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'value_type': (types,), 'rows': ('INT', {'default': 5, 'min': 1, 'max': 2048}), 'string_length': ('INT', {'default': 5, 'min': 1, 'max': 1024}), 'custom_values': ('STRING', {'multiline': False, 'default': '123ABC'}), 'prepend_text': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('multiline_text', 'show_help')
    FUNCTION = 'generate'
    CATEGORY = icons.get('Comfyroll/Utils/Random')

    def generate(self, value_type, rows, string_length, custom_values, seed, prepend_text):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-random-multiline-values'
        random.seed(seed)
        if value_type == 'binary':
            choice_str = '01'
        elif value_type == 'decimal':
            choice_str = '0123456789'
        elif value_type == 'natural':
            choice_str = '123456789'
        elif value_type == 'hexadecimal':
            choice_str = '0123456789ABCDEF'
        elif value_type == 'alphabetic':
            choice_str = string.ascii_letters
        elif value_type == 'alphanumeric':
            choice_str = string.ascii_letters + string.digits
        elif value_type == 'custom':
            choice_str = custom_values
        else:
            pass
        multiline_text = '\n'.join([prepend_text + ''.join((random.choice(choice_str) for _ in range(string_length))) for _ in range(rows)])
        return (multiline_text, show_help)
```