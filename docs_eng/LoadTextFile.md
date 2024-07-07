# Documentation
- Class name: LoadTextFile
- Category: 😺dzNodes/WordCloud
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_WordCloud.git

The LoadTextFile node is designed to read and retrieve the contents of the specified text file. It ensures compatibility with the various character sets by opening the given path files and using the UTF-8 code. The primary function of the node is to provide text data for further processing or analysis in the workflow.

# Input types
## Required
- path
    - The `path' parameter is essential for the operation of the node, as it specifies the location of the text file to be loaded. It directly affects the ability of the node to access and read the contents of the file, which is essential for the follow-up task in the workflow.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- Text
    - The 'Text' output parameter is the content of the loaded text file. It is important because it is the main output of the node and provides text data for downstream processing or analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoadTextFile:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'path': ('STRING', {'default': 'c:\\text.txt'})}, 'optional': {}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('Text',)
    FUNCTION = 'load_text_file'
    OUTPUT_NODE = True
    CATEGORY = '😺dzNodes/WordCloud'

    def load_text_file(self, path):
        text_content = ''
        try:
            with open(os.path.normpath(path), 'r', encoding='utf-8') as f:
                text_content = ''.join((str(l) for l in f.read()))
            print('# 😺dzNodes: Load Text File -> ' + path + ' success.')
        except Exception as e:
            print('# 😺dzNodes: Load Text File -> ERROR, ' + path + ', ' + repr(e))
        return {'ui': {'text': text_content}, 'result': (text_content,)}
```