# Documentation
- Class name: SearchAndReplace
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The SpaceAndReplace node is designed to perform a text operation task by searching for a particular mode in a given text and replacing it with a corresponding value. It can handle dynamic replacements such as dates and values from tips or additional information and make them applicable to various cases.

# Input types
## Required
- text
    - The 'text'parameter is the main input of the node, which contains text that will be searched and replaced. It contains placeholders for dynamic content, and the node will replace these placeholders with actual values.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - The'seed' parameter is used to initialize or influence the randomity of certain operations within a node. It is particularly important when executing a node requires random or pseudo-random elements.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- prompt
    - The 'prompt' parameter is optional input, providing additional context or data that nodes can be used to perform more complex replacements in the text. It is usually used to inject values from external sources.
    - Comfy dtype: STRING
    - Python dtype: Union[str, Dict[str, Any]]
- extra_pnginfo
    - The 'extra_pnginfo' parameter is another optional input that can contain additional information required for the operation of the node. It is particularly useful when it requires additional data beyond the information provided by 'prompt'.
    - Comfy dtype: STRING
    - Python dtype: Union[str, Dict[str, Any]]

# Output types
- result
    - The'redult' output contains the text after all search and replacement operations have been implemented. It reflects the final state of the text, and all the specified modes have been replaced by their corresponding values.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SearchAndReplace:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False, 'placeholder': 'Text to search and replace'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'search_and_replace'
    CATEGORY = 'Mikey/Utils'

    def search_and_replace(self, text, seed, prompt=None, extra_pnginfo=None):
        result = search_and_replace(text, extra_pnginfo, prompt)
        s = seed + 1
        return (result,)
```