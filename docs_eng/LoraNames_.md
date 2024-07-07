# Documentation
- Class name: CreateLoraNames
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node simplifies the process of extracting and organizing names from the given text, particularly for processing the list of Lora font names. It simplifies the input text, removes any redundant characters or empty lines, separates the name from its file extension, and provides a clean list of names and hints for further use.

# Input types
## Required
- lora_names
    - Enter the text that contains the name of the Lora font, which is expected to exist in multi-line format for use. This parameter is essential because it is the main data source for node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- lora_names
    - The list of Lora font names that have been cleaned up and processed does not contain any redundant characters or empty rows and is prepared for further processing or use.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- prompt
    - The list of tips derived from the name of Lora removes the file extension and applies to the creation of creative or thematic content.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class CreateLoraNames:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'lora_names': ('STRING', {'multiline': True, 'default': '\n'.join(folder_paths.get_filename_list('loras')), 'dynamicPrompts': False})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('lora_names', 'prompt')
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True, True)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'

    def run(self, lora_names):
        lora_names = lora_names.split('\n')
        lora_names = [name for name in lora_names if name.strip()]
        prompts = [os.path.splitext(n)[0] for n in lora_names]
        return (lora_names, prompts)
```