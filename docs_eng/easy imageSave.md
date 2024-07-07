# Documentation
- Class name: imageSaveSimple
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node streamlines the preservation of image data and provides a mechanism for the direct preservation of visual output. It supports optional image compression and preview generation to ensure that images can be easily used for subsequent use or inspection.

# Input types
## Required
- images
    - The Images parameter is necessary because it carries visual data that you need to save. It affects the whole operation by deciding what to store and what to look for.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- filename_prefix
    - The name_prefix is used to pre-defined the naming protocol for the preservation of images, which is essential for organizing and identifying files in the output directory.
    - Comfy dtype: STRING
    - Python dtype: str
- only_preview
    - Only_preview parameters control whether to generate and save a preview of the image. It affects the operation of the node by determining the type of output to be generated.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- None
    - The output of this node is not a data object, but an action to save the image. No return value indicates that the saving process has been completed.
    - Comfy dtype: None
    - Python dtype: None

# Usage tips
- Infra type: CPU

# Source code
```
class imageSaveSimple:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.prefix_append = ''
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'ComfyUI'}), 'only_preview': ('BOOLEAN', {'default': False})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save'
    OUTPUT_NODE = True
    CATEGORY = 'EasyUse/Image'

    def save(self, images, filename_prefix='ComfyUI', only_preview=False, prompt=None, extra_pnginfo=None):
        if only_preview:
            PreviewImage().save_images(images, filename_prefix, prompt, extra_pnginfo)
            return ()
        else:
            return SaveImage().save_images(images, filename_prefix, prompt, extra_pnginfo)
```