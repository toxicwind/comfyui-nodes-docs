# Documentation
- Class name: CR_ImagePanel
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ImagePanel node is used to group multiple images into an image panel according to the specified layout direction. It supports the addition of frames and contours to the image, enhances visual effects and allows custom colours. It applies to creating image grids or to organizing multiple preview images into a single image band, which is widely applied to image presentation and layout design.

# Input types
## Required
- image_1
    - The first image to be combined is the basis on which the image panel is built.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- border_thickness
    - The thickness of the border to define the width of the image border and enhance the visual effect of the image edge.
    - Comfy dtype: INT
    - Python dtype: int
- border_color
    - The colour of the border, which allows the user to customize the colour of the border to accommodate different design requirements.
    - Comfy dtype: COLOR
    - Python dtype: str
- outline_thickness
    - The thickness of the contour defines the width of the contour of the image and is used to enhance the visual boundary of the image.
    - Comfy dtype: INT
    - Python dtype: int
- outline_color
    - The colour of the contour, the user can customize the contour colour to match the design theme.
    - Comfy dtype: COLOR
    - Python dtype: str
- layout_direction
    - Layout direction determines whether the image is horizontal or vertical, affecting the layout structure of the final image panel.
    - Comfy dtype: COMBO[horizontal, vertical]
    - Python dtype: str
## Optional
- image_2
    - The second optional image is used to be displayed with the first image in the image panel.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_3
    - The third optional image is used to display the first two images in the image panel.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_4
    - The fourth optional image is used to display the first three images in the image panel.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- border_color_hex
    - The hexadecimal value of the border colour provides another way to specify the border colour accurately.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The grouped image panel contains the final image of all input images organized according to the specified layout direction and style.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - A link to the help document through which users can obtain more information about how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImagePanel:

    @classmethod
    def INPUT_TYPES(s):
        directions = ['horizontal', 'vertical']
        return {'required': {'image_1': ('IMAGE',), 'border_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'border_color': (COLORS,), 'outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'outline_color': (COLORS[1:],), 'layout_direction': (directions,)}, 'optional': {'image_2': ('IMAGE',), 'image_3': ('IMAGE',), 'image_4': ('IMAGE',), 'border_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, image_1, border_thickness, border_color, outline_thickness, outline_color, layout_direction, image_2=None, image_3=None, image_4=None, border_color_hex='#000000'):
        border_color = get_color_values(border_color, border_color_hex, color_mapping)
        images = []
        images.append(tensor2pil(image_1))
        if image_2 is not None:
            images.append(tensor2pil(image_2))
        if image_3 is not None:
            images.append(tensor2pil(image_3))
        if image_4 is not None:
            images.append(tensor2pil(image_4))
        images = apply_outline_and_border(images, outline_thickness, outline_color, border_thickness, border_color)
        combined_image = combine_images(images, layout_direction)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-image-panel'
        return (pil2tensor(combined_image), show_help)
```