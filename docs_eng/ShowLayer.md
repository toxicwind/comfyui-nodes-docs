# Documentation
- Class name: ShowLayer
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The ShowLayer class is designed to manage and display visual elements in a complex structure. It focuses on positioning and scaling layers according to the parameters provided, enabling complex visual combinations to be created.

# Input types
## Required
- edit
    - The `edit' parameter is essential for determining how the ShowLayer class works. It determines whether the function is to edit existing visual elements or to create new elements in a combination.
    - Comfy dtype: EDIT
    - Python dtype: PIL.Image.Image
- x
    - The 'x' parameter specifies the horizontal position of the visual element in the group. It is essential for the correct alignment of the layer and the desired visual effect.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The `y' parameter defines the vertical position of the visual element and works with the `x' parameter to establish the exact position of the layer in the visual combination.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The `width' parameter is essential in determining the horizontal dimensions of the visual elements. It affects the overall scale and layout of the combination and ensures that the elements are appropriate in size and spacing.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter corresponds to the vertical dimension of the visual element and complements the `width' parameter, controlling the size of the visual element in the combination.
    - Comfy dtype: INT
    - Python dtype: int
- z_index
    - The 'z_index' parameter establishes the stacking order of the visual elements. It is essential to create the layering effect, where the elements with a higher value of 'z_index' are shown above the lower value element.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- scale_option
    - The `scale_option' parameter provides flexibility on how the visual elements are scalded. It allows scaling by width, altitude or whole, affecting the visual appearance and the way the elements interact in a combination.
    - Comfy dtype: COMBO
    - Python dtype: str
- layers
    - The 'layers' parameter is a pool of visual elements that the ShowLayer class can operate. It is important in constructing the configuration and determining the visual hierarchy.
    - Comfy dtype: LAYER
    - Python dtype: List[PIL.Image.Image]

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class ShowLayer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'edit': ('EDIT',), 'x': ('INT', {'default': 0, 'min': -100, 'max': 8192, 'step': 1, 'display': 'number'}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1, 'display': 'number'}), 'width': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'z_index': ('INT', {'default': 0, 'min': 0, 'max': 100, 'step': 1, 'display': 'number'}), 'scale_option': (['width', 'height', 'overall'],)}, 'optional': {'layers': ('LAYER', {'default': None})}}
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = True

    def run(self, edit, x, y, width, height, z_index, scale_option, layers):
        return ()
```