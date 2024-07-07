# Documentation
- Class name: NoiseImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node provides multifunctional tools for the testing and visual experimentation of image data by generating a noisey image on a pure colour background according to the specified noise level.

# Input types
## Required
- width
    - Width determines the horizontal size of the output image, which is essential for defining the canvas used for noise mode applications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altitude sets the vertical size of the image and works with width to create the overall size and range of noise generation.
    - Comfy dtype: INT
    - Python dtype: int
- noise_level
    - Noise level control over the intensity of random noise applied to the image directly affects the visual effects and complexity of the end result.
    - Comfy dtype: INT
    - Python dtype: int
- color_hex
    - The colour hexadecimal system defines the basic colour of the image background, which is the basis for the noise pattern superimposed.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - Output is an image with noise that reflects input parameters and is a key piece of further analysis or operation in the image processing workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class NoiseImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 1, 'display': 'number'}), 'noise_level': ('INT', {'default': 128, 'min': 0, 'max': 8192, 'step': 1, 'display': 'slider'}), 'color_hex': ('STRING', {'multiline': False, 'default': '#FFFFFF', 'dynamicPrompts': False})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, width, height, noise_level, color_hex):
        im = create_noisy_image(width, height, 'RGB', noise_level, color_hex)
        output_dir = folder_paths.get_temp_directory()
        (full_output_folder, filename, counter, subfolder, _) = folder_paths.get_save_image_path('tmp_', output_dir)
        image_file = f'{filename}_{counter:05}.png'
        image_path = os.path.join(full_output_folder, image_file)
        im.save(image_path, compress_level=6)
        im = pil2tensor(im)
        return {'ui': {'images': [{'filename': image_file, 'subfolder': subfolder, 'type': 'temp'}]}, 'result': (im,)}
```