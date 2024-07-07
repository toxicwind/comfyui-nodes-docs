# Documentation
- Class name: WAS_Text_Load_From_File
- Category: WAS Suite/IO
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Load_From_File node is designed to load text data from the specified file path into a structured format. It reads the contents of the file and organizes the text into a list, excluding comments or empty lines. The node can also rename the identifier of the file according to the given dictionary name, allowing for more flexible data processing.

# Input types
## Required
- file_path
    - The file_path parameter is essential to the operation of the node because it specifies the location of the file to be loaded. Node reads the file on this path and handles its contents. Without a valid file path, the node will not work as expected.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- dictionary_name
    - Dictionary_name parameters allow the user to assign a custom name to the identifier of the text file, which is very useful for organizing and referencing data within the application. If not provided, the node will use the filename by default as the identifier.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- joined_text
    - This output is important because it provides a clean, single string that can be easily processed or displayed.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- dictionary
    - Dictionary output is a structured expression of the contents of a file in which the identifier of the file is a key and the list of rows processed is a value. This output is important because it organizes text data in a manner that is easily accessible and operational in the application.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[str]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Load_From_File:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'file_path': ('STRING', {'default': '', 'multiline': False}), 'dictionary_name': ('STRING', {'default': '[filename]', 'multiline': False})}}
    RETURN_TYPES = (TEXT_TYPE, 'DICT')
    FUNCTION = 'load_file'
    CATEGORY = 'WAS Suite/IO'

    def load_file(self, file_path='', dictionary_name='[filename]]'):
        filename = os.path.basename(file_path).split('.', 1)[0] if '.' in os.path.basename(file_path) else os.path.basename(file_path)
        if dictionary_name != '[filename]':
            filename = dictionary_name
        if not os.path.exists(file_path):
            cstr(f'The path `{file_path}` specified cannot be found.').error.print()
            return ('', {filename: []})
        with open(file_path, 'r', encoding='utf-8', newline='\n') as file:
            text = file.read()
        update_history_text_files(file_path)
        import io
        lines = []
        for line in io.StringIO(text):
            if not line.strip().startswith('#'):
                if not line.strip().startswith('\n') or not line.strip().startswith('\r') or (not line.strip().startswith('\r\n')):
                    line = line.replace('\n', '').replace('\r', '').replace('\r\n', '')
                lines.append(line.replace('\n', '').replace('\r', '').replace('\r\n', ''))
        dictionary = {filename: lines}
        return ('\n'.join(lines), dictionary)
```