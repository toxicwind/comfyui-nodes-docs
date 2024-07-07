# Documentation
- Class name: GridOutput
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node class covers processing and output grid coordinates and dimensions to facilitate operation and positioning in grid-based systems.

# Input types
## Required
- grid
    - The grid parameter represents the coordinates and dimensions of the elements in the grid system. It is essential for determining the location and size of the elements.
    - Comfy dtype: tuple[int, int, int, int]
    - Python dtype: Tuple[int, int, int, int]

# Output types
- x
    - The x-coordinate of the grid indicates the horizontal position of the elements in the grid.
    - Comfy dtype: int
    - Python dtype: int
- y
    - The y-coordinate of the grid indicates the vertical position of the elements in the grid.
    - Comfy dtype: int
    - Python dtype: int
- width
    - The width of the elements in the grid defines the range of its horizontal extension.
    - Comfy dtype: int
    - Python dtype: int
- height
    - The height of the element in the grid defines the range of its vertical extension.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GridOutput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'grid': ('_GRID',)}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('x', 'y', 'width', 'height')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = False

    def run(self, grid):
        (x, y, w, h) = grid
        return (x, y, w, h)
```