# Documentation
- Class name: CR_OutputScheduleToFile
- Category: Comfyroll/Animation/Schedule
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_OutputScheduleToFile is designed to export scheduling data to file management. It receives parameters such as the path to the output file, filename, scheduler and file extension, and then generates the file in the specified format to ensure that the file name only avoids overlaying the existing file.

# Input types
## Required
- output_file_path
    - The output_file_path parameter specifies the directory where the output file is to be saved. It is essential for determining the location of the file and is necessary for the operation of the node, as it guides where the output should be stored.
    - Comfy dtype: STRING
    - Python dtype: str
- file_name
    - The file_name parameter defines the basic name of the output file, excluding extensions. It plays an important role in the identification document and is necessary to create a single filename that does not conflict with existing files in the directory.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule
    - The schedule parameter contains the data that will be written to the file. It is a key input, as it represents the content of the node responsible for the output. The format of the schedule data is expected to be written into the text or CSV file.
    - Comfy dtype: SCHEDULE
    - Python dtype: List[Any]
## Optional
- file_extension
    - The file_extension parameter determines the format of the output file. It is optional, but important because it determines the type of data structure that the document will have. Node supports the 'txt' and 'csv' extensions, which correspond to different text formats.
    - Comfy dtype: COMBO['txt', 'csv']
    - Python dtype: str

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class CR_OutputScheduleToFile:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'output_file_path': ('STRING', {'multiline': False, 'default': ''}), 'file_name': ('STRING', {'multiline': False, 'default': ''}), 'file_extension': (['txt', 'csv'],), 'schedule': ('SCHEDULE',)}}
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = 'csvoutput'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def csvoutput(self, output_file_path, file_name, schedule, file_extension):
        filepath = output_file_path + '\\' + file_name + '.' + file_extension
        index = 2
        if output_file_path == '' or file_name == '':
            print(f'[Warning] CR Output Schedule To File. No file details found. No file output.')
            return ()
        while os.path.exists(filepath):
            if os.path.exists(filepath):
                filepath = output_file_path + '\\' + file_name + str(index) + '.' + file_extension
                index = index + 1
            else:
                break
        print(f'[Info] CR Output Schedule To File: Saving to {filepath}')
        if file_extension == 'csv':
            with open(filepath, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(schedule)
        else:
            with open(filepath, 'w', newline='') as text_writer:
                for line in schedule:
                    str_item = f'{line[0]},"{line[1]}"\n'
                    text_writer.write(str_item)
        return ()
```