# Documentation
- Class name: WAS_Text_Load_Line_From_File
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Load_Line_From_File node is designed to read and process text lines from a specified file. It can handle individual or multiple lines of text and provides the function of loading text by index or automatically on the basis of a counter. The node also maintains the historical records of the text files visited, facilitating the retrieval of previously loaded text data.

# Input types
## Required
- file_path
    - The file_path parameter specifies the location of the text file to read. This is a key parameter because the operation of the node depends on successful access to the file on this path. Any error in the file path will prevent the node from performing its intended function.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- dictionary_name
    - Dictionary_name parameters define the key that the loaded text line will store in the result dictionary. It allows the user to tag text data to make it easier to quote and organize in the context of the application.
    - Comfy dtype: STRING
    - Python dtype: str
- label
    - The label parameter is used to identify and manage different text batches in the application. It helps track and organize text streams in the system, especially when multiple text sources are involved.
    - Comfy dtype: STRING
    - Python dtype: str
- mode
    - The mode parameter determines the method by which node can be retrieved from the text file. It can be set to 'automatic' for sequential access, or to 'index' for loading specific lines according to their location in the file.
    - Comfy dtype: COMBO[automatic, index]
    - Python dtype: str
- index
    - When the mode is set to 'index', the index parameter applies. It specifies the zero-based position of the line that you want to load from the text file. This allows direct access to the specific line in the file.
    - Comfy dtype: INT
    - Python dtype: int
- multiline_text
    - Multiline_text parameters provide an alternative way to provide text to nodes. Nodes will directly process the text provided through this parameter, rather than read from the document. This is particularly useful for dynamic or inner text processing scenarios.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Output types
- line_text
    - Line_text output contains the actual text lines retrieved from the file according to the specified mode and index. This is the main output of text data processed by nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- dictionary
    - Dictionary output is a collection of text lines that are indexed to the dictionary_name parameters. It is used as a structured way to access and use text data in the application.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[str]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Load_Line_From_File:

    def __init__(self):
        self.HDB = WASDatabase(WAS_HISTORY_DATABASE)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'file_path': ('STRING', {'default': '', 'multiline': False}), 'dictionary_name': ('STRING', {'default': '[filename]', 'multiline': False}), 'label': ('STRING', {'default': 'TextBatch', 'multiline': False}), 'mode': (['automatic', 'index'],), 'index': ('INT', {'default': 0, 'min': 0, 'step': 1})}, 'optional': {'multiline_text': (TEXT_TYPE, {'forceInput': True})}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        if kwargs['mode'] != 'index':
            return float('NaN')
        else:
            m = hashlib.sha256()
            if os.path.exists(kwargs['file_path']):
                with open(kwargs['file_path'], 'rb') as f:
                    m.update(f.read())
                return m.digest().hex()
            else:
                return False
    RETURN_TYPES = (TEXT_TYPE, 'DICT')
    RETURN_NAMES = ('line_text', 'dictionary')
    FUNCTION = 'load_file'
    CATEGORY = 'WAS Suite/Text'

    def load_file(self, file_path='', dictionary_name='[filename]', label='TextBatch', mode='automatic', index=0, multiline_text=None):
        if multiline_text is not None:
            lines = multiline_text.strip().split('\n')
            if mode == 'index':
                if index < 0 or index >= len(lines):
                    cstr(f'Invalid line index `{index}`').error.print()
                    return ('', {dictionary_name: []})
                line = lines[index]
            else:
                line_index = self.HDB.get('TextBatch Counters', label)
                if line_index is None:
                    line_index = 0
                line = lines[line_index % len(lines)]
                self.HDB.insert('TextBatch Counters', label, line_index + 1)
            return (line, {dictionary_name: lines})
        if file_path == '':
            cstr('No file path specified.').error.print()
            return ('', {dictionary_name: []})
        if not os.path.exists(file_path):
            cstr(f'The path `{file_path}` specified cannot be found.').error.print()
            return ('', {dictionary_name: []})
        file_list = self.TextFileLoader(file_path, label)
        (line, lines) = (None, [])
        if mode == 'automatic':
            (line, lines) = file_list.get_next_line()
        elif mode == 'index':
            if index >= len(file_list.lines):
                index = index % len(file_list.lines)
            (line, lines) = file_list.get_line_by_index(index)
        if line is None:
            cstr('No valid line was found. The file may be empty or all lines have been read.').error.print()
            return ('', {dictionary_name: []})
        file_list.store_index()
        update_history_text_files(file_path)
        return (line, {dictionary_name: lines})

    class TextFileLoader:

        def __init__(self, file_path, label):
            self.WDB = WDB
            self.file_path = file_path
            self.lines = []
            self.index = 0
            self.load_file(file_path, label)

        def load_file(self, file_path, label):
            stored_file_path = self.WDB.get('TextBatch Paths', label)
            stored_index = self.WDB.get('TextBatch Counters', label)
            if stored_file_path != file_path:
                self.index = 0
                self.WDB.insert('TextBatch Counters', label, 0)
                self.WDB.insert('TextBatch Paths', label, file_path)
            else:
                self.index = stored_index
            with open(file_path, 'r', encoding='utf-8', newline='\n') as file:
                self.lines = [line.strip() for line in file]

        def get_line_index(self):
            return self.index

        def set_line_index(self, index):
            self.index = index
            self.WDB.insert('TextBatch Counters', 'TextBatch', self.index)

        def get_next_line(self):
            if self.index >= len(self.lines):
                self.index = 0
            line = self.lines[self.index]
            self.index += 1
            if self.index == len(self.lines):
                self.index = 0
            cstr(f'{cstr.color.YELLOW}TextBatch{cstr.color.END} Index: {self.index}').msg.print()
            return (line, self.lines)

        def get_line_by_index(self, index):
            if index < 0 or index >= len(self.lines):
                cstr(f'Invalid line index `{index}`').error.print()
                return (None, [])
            self.index = index
            line = self.lines[self.index]
            cstr(f'{cstr.color.YELLOW}TextBatch{cstr.color.END} Index: {self.index}').msg.print()
            return (line, self.lines)

        def store_index(self):
            self.WDB.insert('TextBatch Counters', 'TextBatch', self.index)
```