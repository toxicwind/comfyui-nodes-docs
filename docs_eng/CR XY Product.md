# Documentation
- Class name: CR_XYProduct
- Category: Comfyroll/List/Utils
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_XYProduct node is designed to perform cross-linking operations for the two string lists. It accepts two multi-line text inputes and generates all possible combinations of elements in the two lists, creating a Cartesian volume. This node is particularly useful in exploring all possible pairing scenarios between the two data sets.

# Input types
## Required
- text_x
    - The parameter 'text_x'is a multi-line text input that indicates the first string list to be used for cross-linking operations. It plays a key role in determining the elements that will be associated with the elements in 'text_y '.
    - Comfy dtype: STRING
    - Python dtype: str
- text_y
    - The parameter 'text_y' is another multi-line text input that indicates a list of the second string to be used in the cross-link operation. It works with 'text_x' to generate the Cartesian volume.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- x_values
    - Output 'x_values' is a string list that represents the first input item in the list after a cross-link operation. It contains the first element of each single combination.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- y_values
    - Output 'y_values'is a string list that represents the second input list element after a cross-link operation. It contains the second element of each single combination.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Output'show_help' provides a URL link for further help or information about node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYProduct:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_x': ('STRING', {'multiline': True}), 'text_y': ('STRING', {'multiline': True})}}
    RETURN_TYPES = (any_type, any_type, 'STRING')
    RETURN_NAMES = ('x_values', 'y_values', 'show_help')
    OUTPUT_IS_LIST = (True, True, False)
    FUNCTION = 'cross_join'
    CATEGORY = icons.get('Comfyroll/List/Utils')

    def cross_join(self, text_x, text_y):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-xy-product'
        list1 = text_x.strip().split('\n')
        list2 = text_y.strip().split('\n')
        cartesian_product = list(product(list1, list2))
        (x_values, y_values) = zip(*cartesian_product)
        return (list(x_values), list(y_values), show_help)
```