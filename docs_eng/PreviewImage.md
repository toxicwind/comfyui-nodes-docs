# Documentation
- Class name: PreviewImage
- Category: Image Processing
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The PreviewImage node is designed to facilitate preview and processing of image data. It generates temporary images for displaying or further processing to ensure that images are managed and stored efficiently. The main objective of the node is to simplify the workflow of image processing tasks by providing seamless image preview interfaces.

# Input types
## Required
- images
    - The `images' parameter is essential for the PreviewImage node because it is used as an input for image data that needs to be previewed. It directly affects the operation of the node, by deciding what to process and display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- prompt
    - The `prompt' parameter, although optional, can be used to provide additional context or instructions to guide the processing of image data in the PreviewImage node. It can be enhanced by allowing more sophisticated control over the image preview process.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter is an optional input that contains additional information relevant to the PNG image format. This may include metadata or other details that are important for the correct interpretation and display of the image.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- preview_image
    - The `preview_image' output provides the processed preview image data. It is a key element of the PreviewImage node function and represents the final result of the image preview process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PreviewImage(SaveImage):

    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.type = 'temp'
        self.prefix_append = '_temp_' + ''.join((random.choice('abcdefghijklmnopqrstupvxyz') for x in range(5)))
        self.compress_level = 1

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
```