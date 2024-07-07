# Documentation
- Class name: WAS_Text_Shuffle
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Shuffle node `shuffle'method is designed to rearrange the order of the elements in the given text string. It breaks the text into a list of elements by using a given separator, randomly disrupts the list, and then regroups the elements into a new string. This method is particularly suitable for tasks that require random text elements, such as data enhancement or the creation of diversified output from a fixed input set.

# Input types
## Required
- text
    - The parameter 'text' means the input text that will be broken. It is the basic part of the node operation, because the entire process revolves around the elements of the text. The parameter is important because it has a direct effect on the output and determines the content and structure of the post-disruption text.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- separator
    - The parameter'separator' defines the separator that is used to divide the input text into separate elements before disrupting. It is essential to determine how the text is divided and how the elements are rearranged. The default value is a comma, but can be adjusted to any character or string according to the specific requirements of the text being processed.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - The parameter'seed' is an optional integer to initialize the random number generator and to ensure that the order of disruption is recreated. This is particularly important in a scenario where multiple nodes are expected to achieve consistent results. By providing seeds, users can control randomity, and the same disruption order can be obtained every time they run the node using the same input and feed values.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- shuffled_text
    - The output parameter'shuffled_text' means the text obtained after disrupting the process. It is a direct reflection of the input text after the elements are randomly rearranged. This output is important because it is the main result of node operations and the basis for any subsequent processing or analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Shuffle:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'separator': ('STRING', {'default': ',', 'multiline': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'shuffle'
    CATEGORY = 'WAS Suite/Text/Operations'

    def shuffle(self, text, separator, seed):
        if seed is not None:
            random.seed(seed)
        text_list = text.split(separator)
        random.shuffle(text_list)
        new_text = separator.join(text_list)
        return (new_text,)
```