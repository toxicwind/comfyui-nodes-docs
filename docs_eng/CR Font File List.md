# Documentation
- Class name: CR_FontFileList
- Category: Comfyroll/List/IO
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_FontFileList is a node used to generate a list of font files in the specified directory. It can obtain fonts from the font directory of the system, a directory specific to Comfyroll, or a user-defined folder. This node can handle a large number of font files and provide options to specify the maximum number of lines to start indexing and list, ensuring efficient data processing and retrieval.

# Input types
## Required
- source_folder
    - The source_folder parameter determines the directory in which the font files will be listed. It can be set to'system' to list the fonts in the system font directory, 'Comfyroll' to list the fonts in the Comfyroll directory, or 'from folder' to specify a custom folder path.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- start_index
    - Start_index parameters are used to specify the starting point in the list of font files. It allows the selection of subsets of fonts from the beginning of the list, which is particularly useful for large font pools.
    - Comfy dtype: INT
    - Python dtype: int
- max_rows
    - The max_rows parameter sets the maximum number of font files that you want to list. It is a key setup to control the size of the output list and manage memory use effectively.
    - Comfy dtype: INT
    - Python dtype: int
- folder_path
    - The file_path parameter is an optional input that allows the user to specify a custom directory path when the source_folder is set to 'from folder'. It allows nodes to list font files from the user-defined location.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- LIST
    - LIST output provides a list of font filenames that are selected from the specified directory based on input parameters. It is a key output that is further processed or displayed in the application.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Show_help output provides a URL link to a document to get additional guidance on using the node. It is particularly useful for users seeking more information or troubleshooting.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_FontFileList:

    @classmethod
    def INPUT_TYPES(s):
        comfyroll_font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        comfyroll_file_list = [f for f in os.listdir(comfyroll_font_dir) if os.path.isfile(os.path.join(comfyroll_font_dir, f)) and f.lower().endswith('.ttf')]
        sources = ['system', 'Comfyroll', 'from folder']
        return {'required': {'source_folder': (sources,), 'start_index': ('INT', {'default': 0, 'min': 0, 'max': 9999}), 'max_rows': ('INT', {'default': 1000, 'min': 1, 'max': 9999})}, 'optional': {'folder_path': ('STRING', {'default': 'C:\\Windows\\Fonts', 'multiline': False})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('LIST', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List/IO')

    def make_list(self, source_folder, start_index, max_rows, folder_path='C:\\Windows\\Fonts'):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-font-file-list'
        if source_folder == 'system':
            system_root = os.environ.get('SystemRoot')
            system_font_dir = os.path.join(system_root, 'Fonts')
            file_list = [f for f in os.listdir(system_font_dir) if os.path.isfile(os.path.join(system_font_dir, f)) and f.lower().endswith('.ttf')]
        elif source_folder == 'Comfyroll':
            comfyroll_font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
            file_list = [f for f in os.listdir(comfyroll_font_dir) if os.path.isfile(os.path.join(comfyroll_font_dir, f)) and f.lower().endswith('.ttf')]
        elif source_folder == 'from folder':
            if folder_path != '' and folder_path is not None:
                if not os.path.exists(folder_path):
                    print(f'[Warning] CR Font File List: The folder_path `{folder_path}` does not exist')
                    return None
                font_dir = folder_path
                file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
            else:
                print(f'[Warning] CR Font File List: No folder_path entered')
                return None
        else:
            pass
        start_index = max(0, min(start_index, len(file_list) - 1))
        end_index = min(start_index + max_rows, len(file_list))
        selected_files = file_list[start_index:end_index]
        return (selected_files, show_help)
```