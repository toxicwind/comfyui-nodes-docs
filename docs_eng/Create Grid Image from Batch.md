# Documentation
- Class name: WAS_Image_Grid_Image_Batch
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Grid_Image_Batch node's `smart_grid_image' function is designed to profile a group of images intelligently into a grid layout. It dynamically adjusts the size of each image to the maximum cell size specified, while maintaining the original width ratio. The node also provides options for adding coloured borders around each image to better visual differentiation. The main objective is to enable the creation of visual attractions and well-organized image grids, which are particularly useful for presentation and image aggregation.

# Input types
## Required
- images
    - The 'image'parameter is the number of nodes that will be processed to create a grid of images. This is a key input, because all the actions of the nodes revolve around arranging the images. This parameter directly affects the composition and visual results of the output grid.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- number_of_columns
    - The 'number_of_collumns' parameter specifies the number of columns in the grid that you generate. It plays an important role in determining the grid layout and influences how the image is distributed over the width of the grid. The default value is 6, but can be adjusted according to the required grid configuration.
    - Comfy dtype: INT
    - Python dtype: int
- max_cell_size
    - The'max_cell_size'parameter sets the maximum size (in pixels) of each cell in the grid. It is important to control the overall size of the grid and to ensure that the image is properly scaled. The default value is 256 pixels, but can be modified according to different display needs.
    - Comfy dtype: INT
    - Python dtype: int
- add_border
    - The 'add_border' parameter is a boolean symbol, and when set to True, the indicator node adds a border around each image in the grid. This enhances the visual separation of the image, especially for the grid that needs to distinguish individual images.
    - Comfy dtype: BOOL
    - Python dtype: bool
- border_red
    - The 'border_red'parameter defines the red fraction of the border colour when you add a border to the image. It helps customize the skin of the border and uses it with 'border_green' and 'border_blue' to create a full border colour.
    - Comfy dtype: INT
    - Python dtype: int
- border_green
    - The 'border_green' parameter sets the green fraction of the border colour. When the 'add_border' is enabled, it works with 'border_red' and 'border_blue' to determine the exact colour of the border.
    - Comfy dtype: INT
    - Python dtype: int
- border_blue
    - The 'border_blue'parameter specifies the blue fraction of the border colour. It is one of the three colour fractions that determines the visual style of the border when applied to the image, together with 'border_red' and 'border_green'.
    - Comfy dtype: INT
    - Python dtype: int
- border_width
    - The 'border_width' parameter determines the thickness of the border around each image. It is an important style element that can influence the overall look of the grid and make the image more visible.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - 'output_image' is the result grid image of the input image that is arranged into a structured layout. It represents the final result of node processing and contains visual alignment and style selection by input parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Grid_Image_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'border_width': ('INT', {'default': 3, 'min': 0, 'max': 100, 'step': 1}), 'number_of_columns': ('INT', {'default': 6, 'min': 1, 'max': 24, 'step': 1}), 'max_cell_size': ('INT', {'default': 256, 'min': 32, 'max': 2048, 'step': 1}), 'border_red': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'border_green': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'border_blue': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'smart_grid_image'
    CATEGORY = 'WAS Suite/Image/Process'

    def smart_grid_image(self, images, number_of_columns=6, max_cell_size=256, add_border=False, border_red=255, border_green=255, border_blue=255, border_width=3):
        cols = number_of_columns
        border_color = (border_red, border_green, border_blue)
        images_resized = []
        max_row_height = 0
        for tensor_img in images:
            img = tensor2pil(tensor_img)
            (img_w, img_h) = img.size
            aspect_ratio = img_w / img_h
            if img_w > img_h:
                cell_w = min(img_w, max_cell_size)
                cell_h = int(cell_w / aspect_ratio)
            else:
                cell_h = min(img_h, max_cell_size)
                cell_w = int(cell_h * aspect_ratio)
            img_resized = img.resize((cell_w, cell_h))
            if add_border:
                img_resized = ImageOps.expand(img_resized, border=border_width // 2, fill=border_color)
            images_resized.append(img_resized)
            max_row_height = max(max_row_height, cell_h)
        max_row_height = int(max_row_height)
        total_images = len(images_resized)
        rows = math.ceil(total_images / cols)
        grid_width = cols * max_cell_size + (cols - 1) * border_width
        grid_height = rows * max_row_height + (rows - 1) * border_width
        new_image = Image.new('RGB', (grid_width, grid_height), border_color)
        for (i, img) in enumerate(images_resized):
            x = i % cols * (max_cell_size + border_width)
            y = i // cols * (max_row_height + border_width)
            (img_w, img_h) = img.size
            paste_x = x + (max_cell_size - img_w) // 2
            paste_y = y + (max_row_height - img_h) // 2
            new_image.paste(img, (paste_x, paste_y, paste_x + img_w, paste_y + img_h))
        if add_border:
            new_image = ImageOps.expand(new_image, border=border_width, fill=border_color)
        return (pil2tensor(new_image),)
```