# Documentation
- Class name: WAS_Image_Tile_Batch
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Tile_Batch node method `tile_image'is designed to divide individual images into smaller maps of a specified number. It intelligently manages the partitioning to maintain horizontal and horizontal comparisons and to ensure that the maps are distributed equally on the image. This function is particularly suitable for applications that require detailed viewing of images or processing large images in a more manageable manner.

# Input types
## Required
- image
    - The 'image 'parameter is the main input of the node, which represents the image that is to be divided into blocks. Its role is vital, because the entire operation of the node revolves around the processing of this image. The quality and properties of the input image directly influence the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- num_tiles
    - The 'num_tiles' parameter determines the total number of blocks to which the input image will be divided. It is an optional parameter with a default value of 6, allowing the user to specify the particle size of the flattening process. This parameter significantly affects the size and number of the output drawings.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGES
    - The 'IMAGES'output parameter is a collection of blocks generated from input images. Each block is part of the original image, and the grouping reflects the structure defined by the 'num_tiles' parameter. This output is important because it is a direct result of node processing.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Tile_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'num_tiles': ('INT', {'default': 4, 'max': 64, 'min': 2, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGES',)
    FUNCTION = 'tile_image'
    CATEGORY = 'WAS Suite/Image/Process'

    def tile_image(self, image, num_tiles=6):
        image = tensor2pil(image.squeeze(0))
        (img_width, img_height) = image.size
        num_rows = int(num_tiles ** 0.5)
        num_cols = (num_tiles + num_rows - 1) // num_rows
        tile_width = img_width // num_cols
        tile_height = img_height // num_rows
        tiles = []
        for y in range(0, img_height, tile_height):
            for x in range(0, img_width, tile_width):
                tile = image.crop((x, y, x + tile_width, y + tile_height))
                tiles.append(pil2tensor(tile))
        tiles = torch.stack(tiles, dim=0).squeeze(1)
        return (tiles,)
```