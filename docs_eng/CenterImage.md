# Documentation
- Class name: CenterImage
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The CenterImage node is designed to process the image and center it in the given canvas, focusing on the specified area. It does so by calculating the coordinates and dimensions required, taking into account the margins provided. The function of the node is not limited to simple placement; it also creates a mask corresponding to the centre area, which enhances its applicability in various image processing tasks.

# Input types
## Required
- canvas
    - The canvas parameter is necessary because it represents the basic image that will be executed in the centre. It is the basis for node execution, which directly affects the grid and mask of output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- left
    - The left parameter specifies the left distance from the centre operation. It is essential to determine the exact position of the image in the canvas and helps to make the end look in the centre.
    - Comfy dtype: INT
    - Python dtype: int
- top
    - The top parameter defines the upper margin of the central process. It plays an important role in the vertical placement of the image and influences the overall middle layout.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - The right parameter sets the right-hand distance of the image in the canvas. It is an important factor for horizontal positioning and helps to accurately construct the frame of the image in the centre.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The bottom parameter indicates the lower margin of the image that is required for the centre. It is essential for vertical alignment and ensures that the image is correctly included within the canvas boundary.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- grid
    - The grid output provides the coordinates and dimensions of the image inside the canvas. This information is essential for further image processing or operational tasks.
    - Comfy dtype: _GRID
    - Python dtype: Tuple[int, int, int, int]
- mask
    - The mask output is a binary image that depicts the area of the medium image. It is very important in applications such as masking, filtering or partitioning in the image-processing workflow.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CenterImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'canvas': ('IMAGE',), 'left': ('INT', {'default': 24, 'min': 0, 'max': 5000, 'step': 1, 'display': 'number'}), 'top': ('INT', {'default': 24, 'min': 0, 'max': 5000, 'step': 1, 'display': 'number'}), 'right': ('INT', {'default': 24, 'min': 0, 'max': 5000, 'step': 1, 'display': 'number'}), 'bottom': ('INT', {'default': 24, 'min': 0, 'max': 5000, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = ('_GRID', 'MASK')
    RETURN_NAMES = ('grid', 'mask')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = False

    def run(self, canvas, left, top, right, bottom):
        canvas = tensor2pil(canvas)
        grid = centerImage((left, top, right, bottom), canvas)
        mask = createMask(canvas, left, top, canvas.width - left - right, canvas.height - top - bottom)
        return (grid, pil2tensor(mask))
```