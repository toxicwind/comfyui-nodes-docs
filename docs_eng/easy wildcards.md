# Documentation
- Class name: wildcardsPrompt
- Category: EasyUse/Prompt
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class is designed to process and modify text input by replacing options and wildcards, enhancing the multifunctionality and interactivity of text. It produces a modified output text by identifying the patterns and keywords in the input and replacing them with the corresponding elements in the predefined dictionary or by random selection.

# Input types
## Required
- text
    - Text parameters are essential for the operation of nodes because they provide the original content to be processed. They are the basis for all replacements and modifications and are a key input for achieving the node's purpose.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seed
    - Seed parameters introduce repeatability in the randomization process within the node. By setting specific torrents, you can control randomity in options and wildcard replacements to ensure consistent results in different operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- text
    - The output text is the result of node processing in which the original input text has been replaced and enhanced. It represents the crystallization of node functions and shows the converted content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class wildcardsPrompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        wildcard_list = get_wildcard_list()
        return {'required': {'text': ('STRING', {'default': '', 'multiline': True, 'dynamicPrompts': False, 'placeholder': '(Support Lora Block Weight and wildcard)'}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'] + wildcard_list,), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM}), 'multiline_mode': ('BOOLEAN', {'default': False})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('text', 'populated_text')
    OUTPUT_IS_LIST = (True, True)
    OUTPUT_NODE = True
    FUNCTION = 'main'
    CATEGORY = 'EasyUse/Prompt'

    @staticmethod
    def main(*args, **kwargs):
        prompt = kwargs['prompt'] if 'prompt' in kwargs else None
        seed = kwargs['seed']
        if prompt:
            easyCache.update_loaded_objects(prompt)
        text = kwargs['text']
        if 'multiline_mode' in kwargs and kwargs['multiline_mode']:
            populated_text = []
            text = text.split('\n')
            for t in text:
                populated_text.append(process(t, seed))
        else:
            populated_text = [process(text, seed)]
            text = [text]
        return {'ui': {'value': [seed]}, 'result': (text, populated_text)}
```