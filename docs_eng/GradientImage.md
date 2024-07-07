# Documentation
- Class name: GradientImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The GradientImage node is designed to generate a gradient image from the specified starting colour to the end of the colour. It is seamlessly integrated with the image processing library to create a visually attractive gradient that can be used for various applications, such as background or design elements.

# Input types
## Required
- width
    - The width parameters determine the width of the gradient image generated. It is a key factor in setting the size of the image, which in turn affects the visual layout and design of the whole.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the gradient image. It works with width to determine the overall size of the image, which is essential for adapting the image to a given design space.
    - Comfy dtype: INT
    - Python dtype: int
- start_color_hex
    - Start_color_hex parameters specify the hexadecimal colour code at the beginning of the gradient. It is a basic input that determines the starting point of the colour transition in the gradient image.
    - Comfy dtype: STRING
    - Python dtype: str
- end_color_hex
    - End_color_hex parameters define the hexadecimal colour code at the end of the gradient. It is essential to determine the final colour of the gradient, thus completing the colour transition.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - IMAGE output provides incremental images that can be used for a variety of applications, such as visual presentations or graphic design projects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - MASK output includes a masked image that can be used to selectively edit or apply specific effects to specific areas of a gradient image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class GradientImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'start_color_hex': ('STRING', {'multiline': False, 'default': '#FFFFFF', 'dynamicPrompts': False}), 'end_color_hex': ('STRING', {'multiline': False, 'default': '#000000', 'dynamicPrompts': False})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False)

    def run(self, width, height, start_color_hex, end_color_hex):
        (im, mask) = generate_gradient_image(width, height, start_color_hex, end_color_hex)
        output_dir = folder_paths.get_temp_directory()
        (full_output_folder, filename, counter, subfolder, _) = folder_paths.get_save_image_path('tmp_', output_dir)
        image_file = f'{filename}_{counter:05}.png'
        image_path = os.path.join(full_output_folder, image_file)
        im.save(image_path, compress_level=6)
        im = pil2tensor(im)
        mask = pil2tensor(mask)
        return {'ui': {'images': [{'filename': image_file, 'subfolder': subfolder, 'type': 'temp'}]}, 'result': (im, mask)}
```