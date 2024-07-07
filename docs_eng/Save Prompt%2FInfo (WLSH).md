# Documentation
- Class name: WLSH_Save_Prompt_File_Info
- Category: WLSH Nodes/IO
- Output node: True
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is intended to preserve text information about the tip experiment and to ensure that details such as positive and negative hints, model names and other relevant metadata are stored and organized safely. It facilitates the preservation of valuable data for future reference and analysis.

# Input types
## Required
- filename
    - The filename parameter is essential because it defines the basic name of the file that saves the hint information. This is essential for identifying and organizing the data that you save.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positive parameter contains the text of the positive hint used in the experiment. It is important because it sets the context for the data to be saved and is part of the record to be kept in the document.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The negative parameter saves the negative hint text, which is also part of the experimental data. This is necessary to preserve the integrity of the information and future analysis.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seed parameters are used to ensure the repeatability of the experiment. It is an important part of the record because it allows the experiment to be repeated under the same conditions.
    - Comfy dtype: INT
    - Python dtype: int
- modelname
    - Model name parameters indicate the model name to be used in the experiment. This is essential for tracking data sources and future references.
    - Comfy dtype: STRING
    - Python dtype: str
- counter
    - The counter parameter is an integer that can be used to distinguish the number of experiments that you have saved or followed. It helps to save the tissue and indexing of files.
    - Comfy dtype: INT
    - Python dtype: int
- time_format
    - The time format parameter determines the format of the time stamp in the filename. It is important to maintain a consistent and readable structure for saving files.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- path
    - Path parameters specify the directory where the file will be saved. It plays an important role in organizing files in the file system and ensuring that data are stored in the desired location.
    - Comfy dtype: STRING
    - Python dtype: str
- info
    - The information parameter contains other metadata about the experiment, such as configuration settings and other details. It enriches the data saved through more context and facilitates comprehensive analysis.
    - Comfy dtype: INFO
    - Python dtype: Dict[str, Any]

# Output types
- text_data
    - Text data represents the information compiled from the input, including both positive and negative hints, model names and other metadata. It is the content to be stored in the text file.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Save_Prompt_File_Info:

    def __init__(self):
        self.output_dir = folder_paths.output_directory

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'filename': ('STRING', {'default': 'info', 'multiline': False}), 'path': ('STRING', {'default': '', 'multiline': False}), 'positive': ('STRING', {'default': '', 'multiline': True, 'forceInput': True})}, 'optional': {'negative': ('STRING', {'default': '', 'multiline': True, 'forceInput': True}), 'modelname': ('STRING', {'default': '', 'multiline': False, 'forceInput': True}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True}), 'counter': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'time_format': ('STRING', {'default': '%Y-%m-%d-%H%M%S', 'multiline': False}), 'info': ('INFO',)}}
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'save_text_file'
    CATEGORY = 'WLSH Nodes/IO'

    def save_text_file(self, positive='', negative='', seed=-1, modelname='unknown', info=None, path='', counter=0, time_format='%Y-%m-%d-%H%M%S', filename=''):
        output_path = os.path.join(self.output_dir, path)
        if output_path.strip() != '':
            if not os.path.exists(output_path.strip()):
                print(f"The path `{output_path.strip()}` specified doesn't exist! Creating directory.")
                os.makedirs(output_path, exist_ok=True)
        text_data = make_comment(positive, negative, modelname, seed, info)
        filename = make_filename(filename, seed, modelname, counter, time_format)
        self.writeTextFile(os.path.join(output_path, filename + '.txt'), text_data)
        return (text_data,)

    def writeTextFile(self, file, content):
        try:
            with open(file, 'w') as f:
                f.write(content)
        except OSError:
            print(f'Error: Unable to save file `{file}`')
```