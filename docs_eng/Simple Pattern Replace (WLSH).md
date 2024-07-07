# Documentation
- Class name: WLSH_Simple_Pattern_Replace
- Category: WLSH Nodes/text
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

This node can replace entries in the list provided in a particular pattern in a text string, increasing the diversity of text-processing operations.

# Input types
## Required
- input_string
    - The input_string parameter is the text that needs to be identified and replaced. It is essential for the operation of the node, as it is the basis for all replacement activities.
    - Comfy dtype: STRING
    - Python dtype: str
- list_string
    - List_string parameters provide a string pool to replace identification patterns. They play a key role in determining the diversity and randomity of replacements.
    - Comfy dtype: STRING
    - Python dtype: str
- pattern
    - The Pattern parameter defines the particular sequence or structure of the text that needs to be replaced. It is essential to guide the search and replacement process of the nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- delimiter
    - The delimiter parameter is used to divide the list_string into separate elements, which are then selected to replace the recognised mode. It is important in organizing the replacement option.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seed
    - The random number generator during the initial replacement of the Seed parameter ensures that the replacement is replicable. It contributes to the predictability and consistency of node output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- string
    - The output of the node is a modified version of the input string, in which the recognized mode is replaced by the element in the list_string, reflecting the text conversion capacity of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Simple_Pattern_Replace:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_string': ('STRING', {'multiline': True, 'forceInput': True}), 'list_string': ('STRING', {'default': f''}), 'pattern': ('STRING', {'default': f'$var'}), 'delimiter': ('STRING', {'default': f','}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('string',)
    FUNCTION = 'replace_string'
    CATEGORY = 'WLSH Nodes/text'

    def replace_string(self, input_string, list_string, pattern, delimiter, seed):
        pattern = re.escape(pattern).strip()
        regex = re.compile(pattern)
        matches = regex.findall(input_string)
        if not matches:
            return (input_string,)
        if seed is not None:
            random.seed(seed)
        if delimiter not in list_string:
            raise ValueError('Delimiter not found in list_string')

        def replace(match):
            return random.choice(list_string.split(delimiter))
        new_string = regex.sub(replace, input_string)
        return (new_string,)
```