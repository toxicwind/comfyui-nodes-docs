# Documentation
- Class name: FileNamePrefix
- Category: Mikey/Meta
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

File NamePrefix is responsible for generating a standardized filename prefix based on the current date, custom directory name and custom text input. It ensures that the filename is unique and organized according to the specified criteria, thus facilitating document management and retrieval.

# Input types
## Required
- date
    - The parameter 'date' decides whether to include the current date in the filename prefix. It plays a key role in organizing documents in chronological order and ensuring that each document has a unique date-based identifier.
    - Comfy dtype: STRING
    - Python dtype: str
- date_directory
    - Parameter'date_directory' specifies whether to create directories based on the current date. This is essential to maintain a hierarchical file structure that classifies files by date.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- custom_directory
    - Parameter'custom_directory' allows the prefix to include user-defined directory names. It provides flexibility in organizing files according to specific items or user needs.
    - Comfy dtype: STRING
    - Python dtype: str
- custom_text
    - Parameter'custom_text' allows you to add a user-defined text string to the prefix of the filename. This can be used to add a specific label or identifier associated with the contents of the file.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - The parameter 'prompt' is used to customize the filename prefix by adding the metadata advanced. It is particularly useful when you need to include dynamic elements in the file naming protocol.
    - Comfy dtype: PROMPT
    - Python dtype: dict
- extra_pnginfo
    - Parameter'extra_pnginfo' provides additional information that can be used to refine the filename prefix. It is usually used in conjunction with the 'prompt' parameter to include more detailed context data.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict

# Output types
- filename_prefix
    - The 'filename_prefix' output is an end-generated prefix that combines all input parameters into a coherent and standardized string. It is the basis for the file naming protocol used in the system.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class FileNamePrefix:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'date': (['true', 'false'], {'default': 'true'}), 'date_directory': (['true', 'false'], {'default': 'true'}), 'custom_directory': ('STRING', {'default': ''}), 'custom_text': ('STRING', {'default': ''})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('filename_prefix',)
    FUNCTION = 'get_filename_prefix'
    CATEGORY = 'Mikey/Meta'

    def get_filename_prefix(self, date, date_directory, custom_directory, custom_text, prompt=None, extra_pnginfo=None):
        filename_prefix = ''
        if custom_directory:
            custom_directory = search_and_replace(custom_directory, extra_pnginfo, prompt)
            filename_prefix += custom_directory + '/'
        if date_directory == 'true':
            ts_str = datetime.datetime.now().strftime('%y%m%d')
            filename_prefix += ts_str + '/'
        if date == 'true':
            ts_str = datetime.datetime.now().strftime('%y%m%d%H%M%S')
            filename_prefix += ts_str
        if custom_text != '':
            custom_text = search_and_replace(custom_text, extra_pnginfo, prompt)
            custom_text = re.sub('[<>:"/\\\\|?*]', '', custom_text)
            filename_prefix += '_' + custom_text
        return (filename_prefix,)
```