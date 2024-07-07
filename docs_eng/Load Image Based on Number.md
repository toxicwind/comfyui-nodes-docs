# Documentation
- Class name: LoadImgFromDirectoryBasedOnIndex
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The node is intended to load the image from the specified directory based on the index provided. It ensures that the directory exists, and then selects an image file from the list of image files that are sorted in the directory. The function of the node is to search the image and convert it into a sheet format suitable for further processing.

# Input types
## Required
- image_directory
    - The image_directory parameter specifies the path to the directory containing the image file. It is essential for the operation of the node, as it determines the origin of the image to be loaded.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seed
    - Seed parameters are used to determine the index of the image file that is loaded from the sorted file list. It affects the selection process and ensures a certain randomity in image retrieval.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The image output provides images loaded in volume format, which is essential for downstream tasks requiring image data in numerical form.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- filename
    - The filename output returns the name of the loaded image file, which is very useful for recording, tracking or additional processing that requires file recognition.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImgFromDirectoryBasedOnIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image_directory': ('STRING', {'multiline': False, 'placeholder': 'Image Directory'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'filename')
    FUNCTION = 'load'
    CATEGORY = 'Mikey/Image'

    def load(self, image_directory, seed):
        if not os.path.exists(image_directory):
            raise Exception(f'Image directory {image_directory} does not exist')
        files = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f)) and f.endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif'))]
        files.sort()
        offset = seed % len(files)
        filename = files[offset].split('/')[-1]
        img = Image.open(files[offset])
        img = pil2tensor(img)
        return (img, filename)
```