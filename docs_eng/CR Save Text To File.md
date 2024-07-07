# Documentation
- Class name: CR_SaveTextToFile
- Category: Comfyroll/Utils/Text
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SaveTextToFile is designed to save text data into a file. It provides the function of processing multi-line text and writing it into the specified file path, using the given filename and extension to ensure that the file has a unique name to avoid overlaying the existing file.

# Input types
## Required
- multiline_text
    - Parameter'multiline_text' saves the text content that you need to save. It is vital because it is the primary data that the node will process and write to the file.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- output_file_path
    - The parameter 'output_file_path'specifies the directory where the file will be saved. It is optional and if it is not provided, the default path will be used.
    - Comfy dtype: STRING
    - Python dtype: str
- file_name
    - The parameter'file_name' defines the name of the file to be created. It is important to identify the file and ensure its uniqueness.
    - Comfy dtype: STRING
    - Python dtype: str
- file_extension
    - Parameter'file_extension' determines the format of the file to be saved. It can be 'txt' or 'csv', affecting the structure of text data in the file.
    - Comfy dtype: COMBO['txt', 'csv']
    - Python dtype: str

# Output types
- show_help
    - Output'show_help' provides a URL link to the document to obtain further help or guidance on using the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SaveTextToFile:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'multiline_text': ('STRING', {'multiline': True, 'default': ''}), 'output_file_path': ('STRING', {'multiline': False, 'default': ''}), 'file_name': ('STRING', {'multiline': False, 'default': ''}), 'file_extension': (['txt', 'csv'],)}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('show_help',)
    OUTPUT_NODE = True
    FUNCTION = 'save_list'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def save_list(self, multiline_text, output_file_path, file_name, file_extension):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-save-text-to-file'
        filepath = output_file_path + '\\' + file_name + '.' + file_extension
        index = 1
        if output_file_path == '' or file_name == '':
            print(f'[Warning] CR Save Text List. No file details found. No file output.')
            return ()
        while os.path.exists(filepath):
            if os.path.exists(filepath):
                filepath = output_file_path + '\\' + file_name + '_' + str(index) + '.' + file_extension
                index = index + 1
            else:
                break
        print(f'[Info] CR Save Text List: Saving to {filepath}')
        if file_extension == 'csv':
            text_list = []
            for i in multiline_text.split('\n'):
                text_list.append(i.strip())
            with open(filepath, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for line in text_list:
                    csv_writer.writerow([line])
        else:
            with open(filepath, 'w', newline='') as text_file:
                for line in multiline_text:
                    text_file.write(line)
        return (show_help,)
```