# Documentation
- Class name: CR_ImageGridPanel
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ImageGridPanel is a node designed to create and organize the image grid efficiently. It accepts a series of images and arranges them into structured grid layouts that can be used for various purposes, such as previewing or group displays. The node provides custom options for borders and contour settings to enhance the visual appeal of the grid. It is particularly suitable for workflows that need to process the image batch into a single, coherent grid.

# Input types
## Required
- images
    - The `images' parameter is a series of images that are sorted into a grid. This input is essential because it defines the content of the final grid. The images are processed and combined to form the grid layout.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- border_thickness
    - The 'border_tickness' parameter is specified for the border thickness around each image in the grid. It allows custom grid appearances and can be adjusted according to the required aesthetics.
    - Comfy dtype: INT
    - Python dtype: int
- border_color
    - The 'border_color'parameter determines the border colour around each image. It is an important aspect of node custom, allowing the user to match the border colour to the overall design theme.
    - Comfy dtype: COLOR
    - Python dtype: str
- outline_thickness
    - The 'outline_tickness' parameter sets the thickness of the contour around each image. This is an optional feature that can be used to sharpen images in the grid.
    - Comfy dtype: INT
    - Python dtype: int
- outline_color
    - The `outline_color' parameter defines the colour of the contour around each image. It complements the border and enhances the visual differentiation of each image in the grid.
    - Comfy dtype: COLOR
    - Python dtype: str
- max_columns
    - The'max_columns' parameter indicates the maximum number of columns in the grid. It is a key parameter that controls the layout of the grid and influences the distribution of images.
    - Comfy dtype: INT
    - Python dtype: int
- border_color_hex
    - The 'border_collor_hex' parameter allows a custom hexadecimal colour to set the border colour. It provides the user with additional flexibility to specify the exact border colour that may not be in the predefined colour option.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The 'image'output is a result grid panel consisting of input images, arranged in a structured layout. It represents the final product of node operations, which can be further used or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - The `show_help' output provides a URL link to the document page to obtain additional guidance and information on the use and functions of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageGridPanel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'border_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'border_color': (COLORS,), 'outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'outline_color': (COLORS[1:],), 'max_columns': ('INT', {'default': 5, 'min': 0, 'max': 256})}, 'optional': {'border_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, images, border_thickness, border_color, outline_thickness, outline_color, max_columns, border_color_hex='#000000'):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-image-grid-panel'
        border_color = get_color_values(border_color, border_color_hex, color_mapping)
        images = [tensor2pil(image) for image in images]
        images = apply_outline_and_border(images, outline_thickness, outline_color, border_thickness, border_color)
        combined_image = make_grid_panel(images, max_columns)
        image_out = pil2tensor(combined_image)
        return (image_out, show_help)
```