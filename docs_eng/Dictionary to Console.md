# Documentation
- Class name: WAS_Dictionary_To_Console
- Category: WAS Suite/Debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Dictionary_To_Console node is designed to facilitate the debugging process by exporting the contents of the dictionary to the control table. It enhances the visibility of the data through formatting and printing, making it easier to review and analyse the structure and values of the dictionary.

# Input types
## Required
- dictionary
    - Dictionary parameters are essential to the operation of the node, because it is the data structure that will be printed to the control table. It is necessary and plays a central role in the function of the node, which determines the information to be displayed for debug purposes.
    - Comfy dtype: DICT
    - Python dtype: Dict[Any, Any]
## Optional
- label
    - The label parameter is used to provide a descriptive title for the output and to enhance the readability of the output from the control table. Although it is not necessary, it increases clarity when debugs multiple dictionary output simultaneously.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- dictionary
    - The output of the node is the original dictionary that is imported. This allows further processing or debugging, if required, to ensure that the data is still available in the follow-up operation in the workflow.
    - Comfy dtype: DICT
    - Python dtype: Dict[Any, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dictionary_To_Console:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dictionary': ('DICT',), 'label': ('STRING', {'default': f'Dictionary Output', 'multiline': False})}}
    RETURN_TYPES = ('DICT',)
    OUTPUT_NODE = True
    FUNCTION = 'text_to_console'
    CATEGORY = 'WAS Suite/Debug'

    def text_to_console(self, dictionary, label):
        if label.strip() != '':
            print(f'\x1b[34mWAS Node Suite \x1b[33m{label}\x1b[0m:\n')
            from pprint import pprint
            pprint(dictionary, indent=4)
            print('')
        else:
            cstr(f'\x1b[33mText to Console\x1b[0m:\n')
            pprint(dictionary, indent=4)
            print('')
        return (dictionary,)
```