# Documentation
- Class name: SeargeSaveFolderInputs
- Category: Searge/_deprecated_/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

This node class is designed to facilitate the process of saving data to the specified folder as an intermediary between the user and the preservation function. It emphasizes ease of use and ensures that the data is directed to the right location as requested by the user.

# Input types
## Required
- save_to
    - The `save_to' parameter is essential for determining the destination folder of the data. It is a string that specifies the path in which the data will be saved and its correct use is essential for the successful execution of the node function.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- save_to
    - Output `save_to' represents the recognized folder path in which the data will be saved. This is the key message that marks the successful operation of the node and the correct route of the data.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeSaveFolderInputs:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'save_to': (SeargeParameterProcessor.SAVE_TO, {'default': SeargeParameterProcessor.SAVE_TO[0]})}}
    RETURN_TYPES = ('SAVE_FOLDER',)
    RETURN_NAMES = ('save_to',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Inputs'

    def get_value(self, save_to):
        return (save_to,)
```