# Documentation
- Class name: CreateCkptNames
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node facilitates the organization and management of the name of the check point in the machine learning project, enabling users to process and screen the list of check point names for further analysis or recovery.

# Input types
## Required
- ckpt_names
    - The input parameter is the string of the check point name, which is essential for the node identification and processing of the check point. It influences the operation of the node by identifying the contents of the filtered and organized.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ckpt_names
    - The output is a list of the names of the inspected check points and is important for further operations, such as loading a particular check point or analysing its distribution.
    - Comfy dtype: LIST[STRING]
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class CreateCkptNames:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'ckpt_names': ('STRING', {'multiline': True, 'default': '\n'.join(folder_paths.get_filename_list('checkpoints')), 'dynamicPrompts': False})}}
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('ckpt_names',)
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'

    def run(self, ckpt_names):
        ckpt_names = ckpt_names.split('\n')
        ckpt_names = [name for name in ckpt_names if name.strip()]
        return (ckpt_names,)
```