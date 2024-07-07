# Documentation
- Class name: CR_SelectISOSize
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SelectISOSize is designed to provide the appropriate size for the ISO paper size selected by the user. It plays an important role in applications that require standard paper size to ensure that output meets international standards.

# Input types
## Required
- iso_size
    - The parameter 'iso_size' is essential for determining the specific ISO paper size. It influences the execution of the node by specifying the sizes that will be returned.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- width
    - Output 'width' means the width size of the selected ISO paper size. It is important for applications that require precise paper size specifications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Output 'height'provides the high size of the selected ISO paper size. It is essential to ensure that the paper size meets the specifications required for various printing or design tasks.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Output'show_help' provides a URL link to the help page for more information about ISO paper size. This is useful for users seeking additional guidance or clarification on the subject.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SelectISOSize:

    @classmethod
    def INPUT_TYPES(cls):
        sizes = list(iso_sizes.keys())
        return {'required': {'iso_size': (sizes,)}}
    RETURN_TYPES = ('INT', 'INT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'show_help')
    FUNCTION = 'get_size'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def get_size(self, iso_size):
        if iso_size in iso_sizes:
            (width, height) = iso_sizes[iso_size]
        else:
            print('Size not found.')
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-select-iso-size'
        return (width, height, show_help)
```