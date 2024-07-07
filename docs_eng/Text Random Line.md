# Documentation
- Class name: WAS_Text_Random_Line
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method 'text_random_line' is designed to select a random line from the given text input. It is a tool for applications that require random sampling of text lines, such as in data pre-processing or content generation tasks.

# Input types
## Required
- text
    - The parameter 'text' is the input text from which you will select random rows. It plays a key role in determining randomly selected content pools.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seed
    - The parameter'seed' is used to initialize the random number generator to ensure the replicability of the random line selection process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- random_line
    - Output 'random_line'is a random selection of rows from the input text, which is the main result of node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Random_Line:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_random_line'
    CATEGORY = 'WAS Suite/Text'

    def text_random_line(self, text, seed):
        lines = text.split('\n')
        random.seed(seed)
        choice = random.choice(lines)
        return (choice,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```