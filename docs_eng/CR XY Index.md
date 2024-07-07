# Documentation
- Class name: CR_XYIndex
- Category: Comfyroll/XY Grid
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_XYIndex node is designed to calculate the corresponding x and y coordinates in the grid structure based on the given index value. It is essential for a variety of applications, such as image processing or data indexing, as a practical tool to map linear indexes into a two-dimensional grid space.

# Input types
## Required
- x_columns
    - The parameter 'x_columns' specifies the number of columns in the grid. It is the key element for determining the grid layout and, therefore, the determining factor for calculating the x and y coordinates of the given index.
    - Comfy dtype: INT
    - Python dtype: int
- y_rows
    - The parameter 'y_rows'defines the number of rows in the grid. Together with 'x_columns', it determines the overall structure of the grid, which is essential for the accurate calculation of the grid index.
    - Comfy dtype: INT
    - Python dtype: int
- index
    - The parameter 'index' is a linear index that needs to be converted to grid coordinates. It is the core of node operations, as it is the starting point for all calculations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- x
    - Output 'x' means the x-coordinate in the grid calculated on the basis of the index provided. It is the key result of the node function, indicating the horizontal position.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - Output 'y' means the y-coordinate in the grid calculated on the basis of the index provided. It is essential to determine the vertical position of the index in the grid structure.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Output'show_help' provides a document URL link for further help. It is a useful resource for users seeking more information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYIndex:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ['Lerp']
        return {'required': {'x_columns': ('INT', {'default': 5.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_rows': ('INT', {'default': 5.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'index': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('INT', 'INT', 'STRING')
    RETURN_NAMES = ('x', 'y', 'show_help')
    FUNCTION = 'index'
    CATEGORY = icons.get('Comfyroll/XY Grid')

    def index(self, x_columns, y_rows, index):
        index -= 1
        x = index % x_columns
        y = int(index / x_columns)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes#cr-xy-index'
        return (x, y, show_help)
```