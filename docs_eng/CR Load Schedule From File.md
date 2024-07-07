# Documentation
- Class name: CR_LoadScheduleFromFile
- Category: Comfyroll/Animation/Schedule
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_LoadScheduleFromFile is a node used to import dispatch data from files, which facilitates the management and organization of animation sequences. It serves as a bridge between file systems and animation workflows, allowing users to load key frames or hint data and interpret them into available formats that can be further processed in animation processes.

# Input types
## Required
- input_file_path
    - Input_file_path parameters specify the directory where the schedule file is located. This is essential to properly identify and access files containing schedule data.
    - Comfy dtype: STRING
    - Python dtype: str
- file_name
    - The file_name parameter indicates the name of the schedule file to be loaded. It plays an important role in document identification and is essential for node processing the correct datasets.
    - Comfy dtype: STRING
    - Python dtype: str
- file_extension
    - The file_extension parameter determines the format of the schedule file and allows nodes to apply the correct resolution method. It is an important factor in ensuring that the data is read and interpreted accurately.
    - Comfy dtype: COMBO['txt', 'csv']
    - Python dtype: str

# Output types
- SCHEDULE
    - The SCHEDULE output provides the content of the schedule file parsed and can be used in animated environments. It represents structured data extracted from the file.
    - Comfy dtype: STRING
    - Python dtype: List[List[str]]
- show_text
    - Show_text output provides a text expression for the profiled dispatch data, which can be used for display or debugging purposes in the application.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadScheduleFromFile:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_file_path': ('STRING', {'multiline': False, 'default': ''}), 'file_name': ('STRING', {'multiline': False, 'default': ''}), 'file_extension': (['txt', 'csv'],)}}
    RETURN_TYPES = ('SCHEDULE', 'STRING')
    RETURN_NAMES = ('SCHEDULE', 'show_text')
    FUNCTION = 'csvinput'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def csvinput(self, input_file_path, file_name, file_extension):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Schedule-Nodes#cr-load-schedule-from-file'
        filepath = input_file_path + '\\' + file_name + '.' + file_extension
        print(f'CR Load Schedule From File: Loading {filepath}')
        lists = []
        if file_extension == 'csv':
            with open(filepath, 'r') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    lists.append(row)
        else:
            with open(filepath, 'r') as txt_file:
                for row in txt_file:
                    parts = row.strip().split(',', 1)
                    if len(parts) >= 2:
                        second_part = parts[1].strip('"')
                        lists.append([parts[0], second_part])
        return (lists, str(lists))
```