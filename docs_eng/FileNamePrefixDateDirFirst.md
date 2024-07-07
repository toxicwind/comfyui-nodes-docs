# Documentation
- Class name: FileNamePrefixDateDirFirst
- Category: Mikey/Meta
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

File NamePrefixDateDirFirst is designed to generate filename prefixes based on the current date and time and to provide options with custom directories and text. It provides a systematic method for naming files, which can be custom-made according to specific requirements.

# Input types
## Required
- date
    - The date parameter decides whether to include the current date in the filename prefix. It plays a key role in ensuring that the prefix is generated to reflect the time frame.
    - Comfy dtype: STRING
    - Python dtype: str
- date_directory
    - Date_directory parameters control whether a directory named after the current date should be added to the filename prefix. This is essential to place the file organization in a date-based hierarchical structure.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- custom_directory
    - Custom directory parameters allow the user-defined directory to be included in the filename prefix. It enhances node flexibility by enabling directory customization.
    - Comfy dtype: STRING
    - Python dtype: str
- custom_text
    - Custom text parameters allow the addition of a specific text to the prefix of the filename. It provides a method for including a unique identifier or descriptive text in the prefix.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- filename_prefix
    - The filename prefix output provides a pre-generation prefix that can be part of the filename. It contains the date, directory and custom text elements specified in the input parameter.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class FileNamePrefixDateDirFirst:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'date': (['true', 'false'], {'default': 'true'}), 'date_directory': (['true', 'false'], {'default': 'true'}), 'custom_directory': ('STRING', {'default': ''}), 'custom_text': ('STRING', {'default': ''})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('filename_prefix',)
    FUNCTION = 'get_filename_prefix'
    CATEGORY = 'Mikey/Meta'

    def get_filename_prefix(self, date, date_directory, custom_directory, custom_text, prompt=None, extra_pnginfo=None):
        filename_prefix = ''
        if date_directory == 'true':
            ts_str = datetime.datetime.now().strftime('%y%m%d')
            filename_prefix += ts_str + '/'
        if custom_directory:
            custom_directory = search_and_replace(custom_directory, extra_pnginfo, prompt)
            filename_prefix += custom_directory + '/'
        if date == 'true':
            ts_str = datetime.datetime.now().strftime('%y%m%d%H%M%S')
            filename_prefix += ts_str
        if custom_text != '':
            custom_text = search_and_replace(custom_text, extra_pnginfo, prompt)
            custom_text = re.sub('[<>:"/\\\\|?*]', '', custom_text)
            filename_prefix += '_' + custom_text
        return (filename_prefix,)
```