# Documentation
- Class name: ImagePaste
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The ImagePaste node is designed to integrate the foreground image seamlessly into the designated location of the background image. It is designed to achieve this by converting the image's stint into an PIL image, operating the alpha channel for transparency, and pasting the foreground to the background at the exact coordinates. This node is essential for accurately controlling the image synthesis task in which the image is placed.

# Input types
## Required
- background_image
    - The background image is where the future will be pasted. It is essential for the final appearance of the output as a composite canvas.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- foreground_image
    - is the image that will be placed on the background image. It is important because it defines the themes or elements that are visible in the final image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- x_position
    - In the background, the top left corner of the foreground image will be placed horizontally. It is important because it determines the specific location of the image in the combination.
    - Comfy dtype: INT
    - Python dtype: int
- y_position
    - In the background, the upper left corner of the foreground image will be placed in a vertical position. It works with x_position to set the exact position where the image is pasted.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The image results that you get when you paste the foreground to the background at a given location. It represents the final combination and is the main output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImagePaste:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'background_image': ('IMAGE',), 'foreground_image': ('IMAGE',), 'x_position': ('INT', {'default': 0, 'min': -10000, 'max': 10000}), 'y_position': ('INT', {'default': 0, 'min': -10000, 'max': 10000})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'paste'
    CATEGORY = 'Mikey/Image'

    def tensor2pil(self, image):
        image_np = np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
        if image_np.shape[0] == 4:
            return Image.fromarray(image_np.transpose(1, 2, 0), 'RGBA')
        else:
            return Image.fromarray(image_np.transpose(1, 2, 0), 'RGB')

    def paste(self, background_image, foreground_image, x_position, y_position):
        background_image = tensor2pil(background_image)
        foreground_image = tensor2pil(foreground_image)
        if foreground_image.mode != 'RGBA':
            foreground_image = foreground_image.convert('RGBA')
        (r, g, b, alpha) = foreground_image.split()
        background_image.paste(foreground_image, (x_position, y_position), mask=alpha)
        return (pil2tensor(background_image),)
```