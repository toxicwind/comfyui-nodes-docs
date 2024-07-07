# Documentation
- Class name: WLSH_Build_Filename_String
- Category: WLSH Nodes/text
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node generates the only filename string by combining time stampes, model names, seeds and counters into customable templates. It is designed to create identifiable and organized filenames for various applications.

# Input types
## Required
- filename
    - base name, the final filename is constructed on this basis. It serves as a template for inserting other parameters.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- modelname
    - The name of the model, which is used to identify and include it in the filename.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Values used to increase diversity and uniqueness of filenames.
    - Comfy dtype: INT
    - Python dtype: int
- counter
    - An integer is used to create a series of filenames when used with the same base filenames and parameters.
    - Comfy dtype: SEED
    - Python dtype: int
- time_format
    - Defines the format for the time stamp to insert the filename.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- filename
    - The final output is a formatted string that represents the built filename and contains all the parameters provided.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Build_Filename_String:

    def __init__(s):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'filename': ('STRING', {'%time_%seed': 'info', 'multiline': False})}, 'optional': {'modelname': ('STRING', {'default': '', 'multiline': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'counter': ('SEED', {'default': 0}), 'time_format': ('STRING', {'default': '%Y-%m-%d-%H%M%S', 'multiline': False})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('filename',)
    FUNCTION = 'build_filename'
    CATEGORY = 'WLSH Nodes/text'

    def build_filename(self, filename='ComfyUI', modelname='model', time_format='%Y-%m-%d-%H%M%S', seed=0, counter=0):
        filename = make_filename(filename, seed, modelname, counter, time_format)
        return filename
```