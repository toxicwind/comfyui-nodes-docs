# Documentation
- Class name: CR_OverlayTransparentImage
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_OverlayTransparentImage node is designed to mix a transparent overlay image with a background image. It adjusts the transparency, location, rotation and scaling of the layer to achieve the required visual effects and offers a wide range of possibilities for creative applications in image processing.

# Input types
## Required
- back_image
    - Background image, overlaying the image will be placed on it. It is a canvas created as a composite image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- overlay_image
    - Displays the image with transparency over the background. It is the main visual element that will be operated in the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- transparency
    - For the level of transparency applied to the image, 0.0 indicates total lack of transparency and 1.0 indicates full transparency.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- offset_x
    - The horizontal deviation applied to overlaying the image, allowing accurate placement from its central location.
    - Comfy dtype: INT
    - Python dtype: int
- offset_y
    - A vertical deviation applied to overlay the image, allowing accurate placement from its central position.
    - Comfy dtype: INT
    - Python dtype: int
- rotation_angle
    - The angle over which the image will be rotated, in degrees, provides a method of targeting the image on demand.
    - Comfy dtype: FLOAT
    - Python dtype: float
- overlay_scale_factor
    - Overwrite the image will be scaled; values greater than 1.0 magnify the image and values less than 1.0 shrink the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - Finally synthesizes the image, overwrites the image to be applied to the background and reflects all changes made through node parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CR_OverlayTransparentImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'back_image': ('IMAGE',), 'overlay_image': ('IMAGE',), 'transparency': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.1}), 'offset_x': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'offset_y': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'rotation_angle': ('FLOAT', {'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}), 'overlay_scale_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.001})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'overlay_image'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def overlay_image(self, back_image, overlay_image, transparency, offset_x, offset_y, rotation_angle, overlay_scale_factor=1.0):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-overlay-transparent-image'
        back_image = tensor2pil(back_image)
        overlay_image = tensor2pil(overlay_image)
        overlay_image.putalpha(int(255 * (1 - transparency)))
        overlay_image = overlay_image.rotate(rotation_angle, expand=True)
        (overlay_width, overlay_height) = overlay_image.size
        new_size = (int(overlay_width * overlay_scale_factor), int(overlay_height * overlay_scale_factor))
        overlay_image = overlay_image.resize(new_size, Image.Resampling.LANCZOS)
        center_x = back_image.width // 2
        center_y = back_image.height // 2
        position_x = center_x - overlay_image.width // 2 + offset_x
        position_y = center_y - overlay_image.height // 2 + offset_y
        back_image.paste(overlay_image, (position_x, position_y), overlay_image)
        return (pil2tensor(back_image),)
```