# Documentation
- Class name: SeargePreviewImage
- Category: UI
- Output node: True
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

This node facilitates image preview by saving the image in a temporary directory, allowing users to visualize the output of image processing tasks without affecting the main workflow.

# Input types
## Required
- enabled
    - This parameter controls whether to activate the image preview function and determines whether the node continues the image preservation process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- images
    - The input images that you want to preview and save; they are the main objects of the node operation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- prompt
    - An optional text description associated with the image can be used to provide context or other information for the image preview.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The additional metadata that can be embedded into the saved image enhances the information available for each image file.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, str]

# Output types
- images
    - The original image provided as input is now accompanied by preview, allowing visualization in UI.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePreviewImage(nodes.SaveImage):

    def __init__(self):
        super().__init__()
        self.output_dir = folder_paths.get_temp_directory()
        self.type = 'temp'
        self.prefix_append = '_temp_' + ''.join((random.choice('abcdefghijklmnopqrstupvxyz') for _ in range(5)))

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'enabled': ('BOOLEAN', {'default': True})}, 'optional': {'images': ('IMAGE',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'preview_images'
    CATEGORY = UI.CATEGORY_UI

    def preview_images(self, enabled, images=None, prompt=None, extra_pnginfo=None):
        if images is None or not enabled:
            return {'result': (images,), 'ui': {'images': list()}}
        saved_images = nodes.SaveImage.save_images(self, images, 'srg_sdxl_preview', prompt, extra_pnginfo)
        saved_images['result'] = (images,)
        return saved_images
```