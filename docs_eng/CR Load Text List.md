# Documentation
- Class name: CR_LoadTextList
- Category: List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_LoadTextList node is designed to load text data from a file into a list format. It can handle CSV and TXT file extensions, providing a multifunctional way to absorb text information for further processing. This node plays a key role in data preparation and applies to applications that require text input.

# Input types
## Required
- input_file_path
    - Input_file_path parameters specify the directory in which the text file is located. This is essential for the successful location and reading of the file at the node, thus affecting the execution of the node and the results of the list of text data loaded.
    - Comfy dtype: STRING
    - Python dtype: str
- file_name
    - The file_name parameter indicates the name of the text file to be loaded, and does not include its extension. It is the key component for identifying specific files in a given directory, affecting the operation of nodes and the text data to be loaded.
    - Comfy dtype: STRING
    - Python dtype: str
- file_extension
    - The file_extension parameter indicates the type of text file that you want to load, which can be 'txt' or 'csv'. This option determines the way in which node handles the file and affects the structure and format of the result text list.
    - Comfy dtype: COMBO['txt', 'csv']
    - Python dtype: Literal['txt', 'csv']

# Output types
- list
    - List output parameters represent loaded text data organized in string lists. Each element corresponds to a line in the text file and provides a direct way of accessing and operating text data.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Show_help output provides a document URL for further help. This is very useful for users seeking more information about the use and functions of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadTextList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_file_path': ('STRING', {'multiline': False, 'default': ''}), 'file_name': ('STRING', {'multiline': False, 'default': ''}), 'file_extension': (['txt', 'csv'],)}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'load_list'
    CATEGORY = icons.get('Comfyroll/List')

    def load_list(self, input_file_path, file_name, file_extension):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-load-value-list'
        filepath = input_file_path + '\\' + file_name + '.' + file_extension
        print(f'CR Load Values: Loading {filepath}')
        list = []
        if file_extension == 'csv':
            with open(filepath, 'r') as csv_file:
                for row in csv_file:
                    list.append(row)
        elif file_extension == 'txt':
            with open(filepath, 'r') as txt_file:
                for row in txt_file:
                    list.append(row)
        else:
            pass
        return (list, show_help)
```