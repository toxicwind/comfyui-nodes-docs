# Documentation
- Class name: WAS_Text_Save
- Category: WAS Suite/IO
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Save node is designed to manage the process of saving text data to a file. It processes the creation of a directory, checks empty text, and generates a filename with proper fill and separator. The node ensures that the saved file has a unique name and is stored in the specified path.

# Input types
## Required
- text
    - Text parameters represent the content of the text that you want to save to the file. It is the basic part of node operations, as it is the main data being managed.
    - Comfy dtype: STRING
    - Python dtype: str
- path
    - Path parameters specify the directory where the text file will be saved. It is essential to determine the location of the file in the file system.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- filename_prefix
    - Filename prefix parameters set the initial character of the filename. It helps to save the file's uniqueness and organization.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_delimiter
    - The filename separator parameter defines the character that separates the prefix from the digital part of the file name. It helps to distinguish the different parts of the file name.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_number_padding
    - The file name numerically fills parameters to determine the number of digits to be used in the numerical part of the filename. It ensures that the file name is in a consistent format.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- text
    - The text output parameter returns the text saved to the file, providing confirmation that the data is written.
    - Comfy dtype: STRING
    - Python dtype: str
- ui
    - ui output parameter is used to provide user interface feedback. It usually contains a string expression for saved text.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: Dict[str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Save:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'forceInput': True}), 'path': ('STRING', {'default': './ComfyUI/output/[time(%Y-%m-%d)]', 'multiline': False}), 'filename_prefix': ('STRING', {'default': 'ComfyUI'}), 'filename_delimiter': ('STRING', {'default': '_'}), 'filename_number_padding': ('INT', {'default': 4, 'min': 2, 'max': 9, 'step': 1})}}
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'save_text_file'
    CATEGORY = 'WAS Suite/IO'

    def save_text_file(self, text, path, filename_prefix='ComfyUI', filename_delimiter='_', filename_number_padding=4):
        tokens = TextTokens()
        path = tokens.parseTokens(path)
        filename_prefix = tokens.parseTokens(filename_prefix)
        if not os.path.exists(path):
            cstr(f"The path `{path}` doesn't exist! Creating it...").warning.print()
            try:
                os.makedirs(path, exist_ok=True)
            except OSError as e:
                cstr(f'The path `{path}` could not be created! Is there write access?\n{e}').error.print()
        if text.strip() == '':
            cstr(f'There is no text specified to save! Text is empty.').error.print()
        delimiter = filename_delimiter
        number_padding = int(filename_number_padding)
        file_extension = '.txt'
        filename = self.generate_filename(path, filename_prefix, delimiter, number_padding, file_extension)
        file_path = os.path.join(path, filename)
        self.writeTextFile(file_path, text)
        update_history_text_files(file_path)
        return (text, {'ui': {'string': text}})

    def generate_filename(self, path, prefix, delimiter, number_padding, extension):
        pattern = f'{re.escape(prefix)}{re.escape(delimiter)}(\\d{{{number_padding}}})'
        existing_counters = [int(re.search(pattern, filename).group(1)) for filename in os.listdir(path) if re.match(pattern, filename)]
        existing_counters.sort(reverse=True)
        if existing_counters:
            counter = existing_counters[0] + 1
        else:
            counter = 1
        filename = f'{prefix}{delimiter}{counter:0{number_padding}}{extension}'
        while os.path.exists(os.path.join(path, filename)):
            counter += 1
            filename = f'{prefix}{delimiter}{counter:0{number_padding}}{extension}'
        return filename

    def writeTextFile(self, file, content):
        try:
            with open(file, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
        except OSError:
            cstr(f'Unable to save file `{file}`').error.print()
```