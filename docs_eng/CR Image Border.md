# Documentation
- Class name: CR_ImageBorder
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImageBorder node is designed to add decorative borders to images to enhance their visual effects in various layouts. It allows for the thickness and colour of custom borders, and also allows the option to add a contour for additional emphasis. This node plays a key role in the graphic design workflow that requires professional and fine image presentation.

# Input types
## Required
- image
    - The image parameter is necessary because it defines the basic visual content that will apply the border. The quality and resolution of the input directly influences the final output, making it an essential element in node execution.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- top_thickness
    - The top_tickness parameter specifies the thickness of the border that should be applied to the top edge of the image. It allows fine-tuning the appearance of the border to meet the design requirements and contributes to the beauty of the image as a whole.
    - Comfy dtype: INT
    - Python dtype: int
- bottom_thickness
    - The bottom_tickness parameter determines the border thickness on the bottom edge of the image. Adjusting this parameter helps to balance the symmetry of the border design and enhances visual harmony of the image.
    - Comfy dtype: INT
    - Python dtype: int
- left_thickness
    - The left_tickness parameter controls the thickness of the left border of the image. This is an important aspect when designing the border to ensure that the image has a uniform and consistent look on all edges.
    - Comfy dtype: INT
    - Python dtype: int
- right_thickness
    - Right_tickness parameters set the thickness of the right border of the image. It works in the overall frame design to ensure that the edge of the image is visually consistent with the rest of the layout.
    - Comfy dtype: INT
    - Python dtype: int
- border_color
    - The border_color parameter is used to define the colour of the border. It is a key element of the tone and style that sets the frame of the image, affecting the overall atmosphere and presentation of the final image.
    - Comfy dtype: COLOR
    - Python dtype: str
- outline_thickness
    - Outline_tickness parameters specify the thickness of the contour line that you want to add around the image. This adds depth and focus to the image, making it more prominent in the group.
    - Comfy dtype: INT
    - Python dtype: int
- outline_color
    - The outline_color parameter determines the colour of the contour line around the image. This is an important option for designers who want to create a sense of contrast or harmony with border_color and the image itself.
    - Comfy dtype: COLOR
    - Python dtype: str
- border_color_hex
    - The border_color_hex parameter allows for the use of custom hexadecimal colours to set the border colours, providing the designer with greater flexibility and control over the exact colour shadow required.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The image output of the CR_ImageBorder node is a processed image using borders and optional contours. It represents the final visual result of the node operation and can be further used or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page for further help or guidance on using CR_ImageBorder nodes. This is a useful resource for users seeking more information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageBorder:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'top_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'bottom_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'left_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'right_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'border_color': (COLORS,), 'outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'outline_color': (COLORS[1:],)}, 'optional': {'border_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, image, top_thickness, bottom_thickness, left_thickness, right_thickness, border_color, outline_thickness, outline_color, border_color_hex='#000000'):
        images = []
        border_color = get_color_values(border_color, border_color_hex, color_mapping)
        for img in image:
            img = tensor2pil(img)
            if outline_thickness > 0:
                img = ImageOps.expand(img, outline_thickness, fill=outline_color)
            if left_thickness > 0 or right_thickness > 0 or top_thickness > 0 or (bottom_thickness > 0):
                img = ImageOps.expand(img, (left_thickness, top_thickness, right_thickness, bottom_thickness), fill=border_color)
            images.append(pil2tensor(img))
        images = torch.cat(images, dim=0)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-image-border'
        return (images, show_help)
```