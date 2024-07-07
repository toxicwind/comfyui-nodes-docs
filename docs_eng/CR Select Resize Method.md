# Documentation
- Class name: CR_SelectResizeMethod
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SelectResizeMethod node is designed to provide a selection mechanism for different image scaling methods, such as 'Fit' and 'Crop'. It acts as a decision-making point in the image synthesizing workflow, allowing users to select methods based on their specific needs for image operations.

# Input types
## Required
- method
    - The `method' parameter is essential for determining the method used to resize the image. It determines whether the image will be resized to fit the given size, or whether it will be cropped to fully match these dimensions.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- method
    - Output'method'represents the image scaling method selected by the user. It is a key determinant of the next steps in the image processing process.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a document URL link for further help. It is particularly useful for users who need more information about scaling methods or node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SelectResizeMethod:

    @classmethod
    def INPUT_TYPES(cls):
        methods = ['Fit', 'Crop']
        return {'required': {'method': (methods,)}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('method', 'show_help')
    FUNCTION = 'set_switch'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def set_switch(self, method):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-select-resize-method'
        return (method, show_help)
```