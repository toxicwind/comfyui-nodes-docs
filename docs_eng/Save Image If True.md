# Documentation
- Class name: SaveImageIfTrue
- Category: Mikey/Image
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

Method's'save_image_if_true'is designed to save images to files under conditions. It assesses a condition of preservation and, if the conditions are met, uses the 'SaveImagesmike' class to implement the actual image preservation process, including the processing of metadata and file naming protocols.

# Input types
## Required
- image
    - Image parameters are essential for the operation of nodes because they represent images that may be saved. Their quality and content directly influence the outcome of the preservation process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- save_condition
    - Save_convention parameters as switches to the saving process. It is important because its value (0 or 1) determines whether the image will be saved.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- filename_prefix
    - The filename_prefix parameter is important for defining the prefix for saving the image file. It can customize the naming protocol, especially for files saved by the organization.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - Reult parameters encapsulate the results of the saving operation. It includes details such as file names and subfolders for image preservation, which provide a record of the preservation process.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Union[str, Dict[str, str]]]

# Usage tips
- Infra type: CPU

# Source code
```
class SaveImageIfTrue:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'save_condition': ('INT', {'default': 0, 'min': 0, 'max': 1}), 'filename_prefix': ('STRING', {'default': ''})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_image_if_true'
    OUTPUT_NODE = True
    CATEGORY = 'Mikey/Image'

    def save_image_if_true(self, image, save_condition, filename_prefix, prompt=None, extra_pnginfo=None):
        if save_condition == 1:
            save_images = SaveImagesMikey()
            result = save_images.save_images(image, filename_prefix, prompt, extra_pnginfo, positive_prompt='', negative_prompt='')
            return result
        else:
            return {'save_image_if_true': {'filename': '', 'subfolder': ''}}
```