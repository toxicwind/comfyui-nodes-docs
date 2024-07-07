# Documentation
- Class name: WLSH_Save_Prompt_File
- Category: WLSH Nodes/IO
- Output node: True
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is designed to save text data into a file, providing a means of sustaining information in a human readable format. It encapsifies the process of writing text into a file, ensuring that data is stored in a specified directory and using a user-defined filename. The node's main function is to facilitate the creation and maintenance of text records, which are essential for recording experiments, recording outputs or archiving data.

# Input types
## Required
- filename
    - The file name parameter is essential to specify the name of the output file. It determines the manner in which the data are referenced and is a key part of the file identity that allows users to easily locate and quote the saved text data.
    - Comfy dtype: STRING
    - Python dtype: str
- positive
    - The positive parameter contains a text that represents the positive aspects of the data being saved or the desired results. It is important for providing the context and understanding the purpose behind preserving the information.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- path
    - The path parameter defines the directory where the file will be saved. It plays an important role in organizing the file system and ensuring that the saved file is accessible and well structured in the required location.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative parameters include text that represents the result that is not desired or that should be avoided. It is essential to clarify the intent and purpose of the data and to ensure that what is kept is correctly interpreted.
    - Comfy dtype: STRING
    - Python dtype: str
- modelname
    - Model name parameters are the model names used to generate data. They are important for tracking data sources and may be useful for future reference and analysis.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seed parameters are used to ensure the replicability of results. It is important to maintain consistency between different operations of the same process, which is essential for reliable and verifiable results.
    - Comfy dtype: INT
    - Python dtype: int
- counter
    - The counter parameters are used to attach a value to the filename, which is important for distinguishing multiple saves or versions of the same data.
    - Comfy dtype: INT
    - Python dtype: int
- time_format
    - Time format parameters specify the format to be used for the time stamp filename. It is important for adding a unique and identifiable element based on the time of creation, which is useful for sorting and locating files in chronological order.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text_data
    - Text data output represents the contents saved, including both positive and negative hints and any specified additional information. It is the result of node operations and is recorded as persistent data.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Save_Prompt_File:

    def __init__(self):
        self.output_dir = folder_paths.output_directory

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'filename': ('STRING', {'default': 'info', 'multiline': False}), 'path': ('STRING', {'default': '', 'multiline': False}), 'positive': ('STRING', {'default': '', 'multiline': True, 'forceInput': True})}, 'optional': {'negative': ('STRING', {'default': '', 'multiline': True, 'forceInput': True}), 'modelname': ('STRING', {'default': '', 'multiline': False, 'forceInput': True}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True}), 'counter': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'time_format': ('STRING', {'default': '%Y-%m-%d-%H%M%S', 'multiline': False})}}
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'save_text_file'
    CATEGORY = 'WLSH Nodes/IO'

    def save_text_file(self, positive='', negative='', seed=-1, modelname='unknown', path='', counter=0, time_format='%Y-%m-%d-%H%M%S', filename=''):
        output_path = os.path.join(self.output_dir, path)
        if output_path.strip() != '':
            if not os.path.exists(output_path.strip()):
                print(f"The path `{output_path.strip()}` specified doesn't exist! Creating directory.")
                os.makedirs(output_path, exist_ok=True)
        text_data = make_comment(positive, negative, modelname, seed, info=None)
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