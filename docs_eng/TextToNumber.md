# Documentation
- Class name: TextToNumber
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node abstractes the process of converting text data to values, which facilitates the analysis and processing of text-based information. It emphasizes the conversion of input text to numerical expressions, which can be further used for various computational tasks.

# Input types
## Required
- text
    - Text parameters are essential because they are the source of the extraction values. The quality and content of the text directly influences the output of the nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- random_number
    - This parameter determines whether the random number generation process is applied after extracting values from the text, adding variability to the result.
    - Comfy dtype: COMBO
    - Python dtype: str
- max_num
    - The max_num parameter sets a ceiling for random number generation to ensure that the number generated remains within the specified range.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- seed
    - Seed parameters are essential to ensure the repeatability of the random number generation process, allowing consistent results to be obtained under the same conditions.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- ui.text
    - This output contains the original text input, which is retained for reference and context purposes and is important for understanding the origin of the numerical result.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- ui.num
    - ui.num output represents the result of a value or random number extracted from the text, which is the main output of the node and is essential for subsequent calculations.
    - Comfy dtype: INT
    - Python dtype: List[int]
- result
    - The output is the final value, which is the crystallization of node processing and is essential for further analysis or operation.
    - Comfy dtype: INT
    - Python dtype: Tuple[int]

# Usage tips
- Infra type: CPU

# Source code
```
class TextToNumber:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '1'}), 'random_number': (['enable', 'disable'],), 'max_num': ('INT', {'default': 10, 'min': 2, 'max': 10000000000, 'step': 1, 'display': 'number'})}, 'optional': {'seed': (any_type, {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, text, random_number, max_num, seed=0):
        numbers = re.findall('\\d+', text)
        result = 0
        for n in numbers:
            result = int(n)
        if random_number == 'enable' and result > 0:
            result = random.randint(1, max_num)
        return {'ui': {'text': [text], 'num': [result]}, 'result': (result,)}
```