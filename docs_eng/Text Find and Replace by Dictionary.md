# Documentation
- Class name: WAS_Search_and_Replace_Dictionary
- Category: WAS Suite/Text/Search
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The node is designed to search and replace the given text with the provided dictionary. It wisely replaces the text that appears in the dictionary key with the corresponding value to ensure that it is replaced in a controlled manner so as to avoid overlaying the text segments that you do not want to replace.

# Input types
## Required
- text
    - Enter text that will be searched and replaced. This is the main data that the node will process in order to achieve the expected results.
    - Comfy dtype: STRING
    - Python dtype: str
- dictionary
    - A dictionary, where the key is the term that the text is searching for, and the value is the term that will replace the key. It plays a key role in determining node output.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, str]
## Optional
- replacement_key
    - A string that is used to wrap the keys in the dictionary before you search the text. It helps to prevent unexpected replacements in the text.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seeds for the random number generator to control the randomity of the replacement process. It ensures repeatability to obtain a definitive result.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_text
    - Applys the search and replacement operation to generate text. It reflects changes made according to the input dictionary and parameters.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Search_and_Replace_Dictionary:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'dictionary': ('DICT',), 'replacement_key': ('STRING', {'default': '__', 'multiline': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_search_and_replace_dict'
    CATEGORY = 'WAS Suite/Text/Search'

    def text_search_and_replace_dict(self, text, dictionary, replacement_key, seed):
        random.seed(seed)
        new_text = text
        for term in dictionary.keys():
            tkey = f'{replacement_key}{term}{replacement_key}'
            tcount = new_text.count(tkey)
            for _ in range(tcount):
                new_text = new_text.replace(tkey, random.choice(dictionary[term]), 1)
                if seed > 0 or seed < 0:
                    seed = seed + 1
                    random.seed(seed)
        return (new_text,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```