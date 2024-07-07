# Documentation
- Class name: TextSplitByDelimiter
- Category: ♾️Mixlab/GPT
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node divides text data on the basis of a given separator to extract structured information from unstructured text. It is designed to process large data sets efficiently and to provide users with simple and powerful tools for text analysis and pre-processing tasks.

# Input types
## Required
- text
    - Enter the text as the main data source for node operations. Its quality and format directly influence the validity of the split process and the accuracy of the extracts.
    - Comfy dtype: STRING
    - Python dtype: str
- delimiter
    - The separator parameter determines the criteria for separating the text. It plays a vital role in determining how the text is divided, thus influencing the structure of the output.
    - Comfy dtype: COMBO
    - Python dtype: str
- start_index
    - Start_index parameters define where the split process starts in the text. It affects the initial segments of the selected output and can be used to skip parts of the text that are not required.
    - Comfy dtype: INT
    - Python dtype: int
- skip_every
    - The skip_every parameter determines the frequency of skipping a segment during the split. It plays an important role in controlling the density of the output and helps to focus on specific interest areas in the text.
    - Comfy dtype: INT
    - Python dtype: int
- max_count
    - The max_count parameter sets a ceiling on the number of extracts. It is important in managing the range of outputs and ensuring that nodes do not process too much data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- segmented_text
    - Output is a list of text segments that are extracted from input parameters. Each segment represents part of the original text and is structured according to the given separator and other input criteria.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class TextSplitByDelimiter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'delimiter': (['newline', 'comma'],), 'start_index': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1, 'display': 'number'}), 'skip_every': ('INT', {'default': 0, 'min': 0, 'max': 10, 'step': 1, 'display': 'number'}), 'max_count': ('INT', {'default': 10, 'min': 1, 'max': 1000, 'step': 1, 'display': 'number'})}}
    INPUT_IS_LIST = False
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    OUTPUT_IS_LIST = (True,)
    CATEGORY = '♾️Mixlab/GPT'

    def run(self, text, delimiter, start_index, skip_every, max_count):
        arr = []
        if delimiter == 'newline':
            arr = [line for line in text.split('\n') if line.strip()]
        elif delimiter == 'comma':
            arr = [line for line in text.split(',') if line.strip()]
        arr = arr[start_index:start_index + max_count * (skip_every + 1):skip_every + 1]
        return (arr,)
```