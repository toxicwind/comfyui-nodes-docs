# Documentation
- Class name: LoadImagesFromDirectoryUpload
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The LoadImagesFromDirectoryUpload node is designed to load image data from the specified directory. It streamlines the process of accessing and preparing images for further processing or analysis, abstracting the complexity of file processing and directory navigation.

# Input types
## Required
- directory
    - The `directory' parameter specifies the source directory for which the image is loaded. This is essential for determining the scope and content of the image data that the node will process.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- image_load_cap
    - The `image_load_cap' parameter is optional, which allows for limiting the number of images to be loaded from the directory. It provides a method for controlling the amount of data to be processed, which may be very important in optimizing the use of resources.
    - Comfy dtype: INT
    - Python dtype: int
- skip_first_images
    - The'skip_first_images' parameter allows nodes to skip the number of images specified at the beginning of the directory. This may be useful in cases where some images are not related to the current task or analysis.
    - Comfy dtype: INT
    - Python dtype: int
- select_every_nth
    - The'select_every_nth' parameter is used to select images from the directory at fixed intervals defined by the parameter value. This helps to simplify the process when only a subset of images is needed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The `IMAGE' output provides the loaded image data, which is the main result of node operations. It represents the visual content that can be further operated or analysed.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- MASK
    - `MASK' output, when applicable, provides binary or classification masks associated with the image loaded. This is very useful for tasks that require partitioning or classification based on interested areas in the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- INT
    - If available, the `INT' output type may represent additional numerical data or metadata associated with the image. It provides quantitative information to supplement visual data.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImagesFromDirectoryUpload:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        directories = []
        for item in os.listdir(input_dir):
            if not os.path.isfile(os.path.join(input_dir, item)) and item != 'clipspace':
                directories.append(item)
        return {'required': {'directory': (directories,)}, 'optional': {'image_load_cap': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX, 'step': 1}), 'skip_first_images': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX, 'step': 1}), 'select_every_nth': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'MASK', 'INT')
    FUNCTION = 'load_images'
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'

    def load_images(self, directory: str, **kwargs):
        return load_images(directory, **kwargs)

    @classmethod
    def IS_CHANGED(s, directory: str, **kwargs):
        return is_changed_load_images(directory, **kwargs)

    @classmethod
    def VALIDATE_INPUTS(s, directory: str, **kwargs):
        return validate_load_images(directory)
```