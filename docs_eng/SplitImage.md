# Documentation
- Class name: SplitImage
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The SpringImage node is designed to divide the image entered into a smaller image grid and generate the corresponding mask. It enhances the image-processing workflow by enabling the creation of a segment output that can be used for various applications, such as image editing, feature extraction and data enhancement.

# Input types
## Required
- image
    - An image parameter is essential because it is the main input for node operations. It determines the quality and resolution of the images and masks generated. The characteristics of the image directly influence the validity of the nodes in dividing and masking.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- num
    - Num parameters determine how many segments the image will be divided. It is very important because it affects the detail level of the particle size and the mask that divides the image. Higher values will lead to more segments, which may be useful for detailed analysis or processing.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- seed
    - Seed parameters are used to control the randomity of grid coordinates. It is important to ensure repeatability in the image partitioning process, especially when nodes are used in larger workflows that require consistent results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- grids
    - The grids output is a collection of split images derived from the original input. It represents the main result of the node operation and shows the validity of the partition.
    - Comfy dtype: _GRID
    - Python dtype: List[Tuple[int, int, int, int]]
- grid
    - The grid output is a single split image selected on the basis of the Seed parameter. It is important because it provides a detailed view of a particular segment that can be used to focus on analysis or further processing.
    - Comfy dtype: _GRID
    - Python dtype: Tuple[int, int, int, int]
- mask
    - Mass output is a binary image corresponding to the selected grid. It is essential to isolate and highlight the particular area of the image for further analysis or operation.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class SplitImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'num': ('INT', {'default': 4, 'min': 1, 'max': 500, 'step': 1, 'display': 'number'}), 'seed': ('INT', {'default': 4, 'min': 1, 'max': 500, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = ('_GRID', '_GRID', 'MASK')
    RETURN_NAMES = ('grids', 'grid', 'mask')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = False

    def run(self, image, num, seed):
        image = tensor2pil(image)
        grids = splitImage(image, num)
        if seed > num:
            num = int(seed / 500 * num) - 1
        else:
            num = seed - 1
        num = max(0, num)
        g = grids[num]
        (x, y, w, h) = g
        mask = createMask(image, x, y, w, h)
        mask = pil2tensor(mask)
        return (grids, g, mask)
```