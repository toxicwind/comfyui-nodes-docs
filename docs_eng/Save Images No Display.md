# Documentation
- Class name: SaveImageNoDisplay
- Category: Mikey/Image
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

The method'save_images_no_display'is designed to save a series of images to the specified directory without showing them. It is responsible for converting image data into formats suitable for preservation, applying metadata, and organizing files in a structured manner according to the parameters provided.

# Input types
## Required
- images
    - The parameter 'images' is necessary because it contains raw image data that need to be saved. It plays a key role in determining node implementation, as it is the main input into the image preservation process.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: List[torch.Tensor]
- sub_directory
    - Parameter'sub_directory' specifies a subfolder in the output directory, and the image will be saved in this subfolder. This is important for organizing images in a structured way.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- filename_text_1
    - Parameter 'filename_text_1' allows customization of file names by providing a text string that will be included in the name of the saved file.
    - Comfy dtype: str
    - Python dtype: Optional[str]
- extra_metadata
    - The parameter 'extra_metadata'is used to add additional information to the metadata of the image file. This may include various types of data that provide context or detailed information about the image.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- ui
    - The 'ui'parameter in the output contains information about the images saved, including their filenames and subfolders. This output is important because it provides feedback on the results of the image preservation operation.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, List[Dict[str, Union[str, int, Dict[str, Any]]]]}

# Usage tips
- Infra type: CPU

# Source code
```
class SaveImageNoDisplay(SaveImagesMikeyML):

    def __init__(self):
        super().__init__()
    RETURN_TYPES = ()
    FUNCTION = 'save_images_no_display'
    OUTPUT_NODE = True
    CATEGORY = 'Mikey/Image'

    def save_images_no_display(self, images, sub_directory, filename_text_1, filename_text_2, filename_text_3, filename_separator, timestamp, counter_type, filename_text_1_pos, filename_text_2_pos, filename_text_3_pos, timestamp_pos, timestamp_type, counter_pos, extra_metadata, prompt=None, extra_pnginfo=None):
        self.save_images(images, sub_directory, filename_text_1, filename_text_2, filename_text_3, filename_separator, timestamp, counter_type, filename_text_1_pos, filename_text_2_pos, filename_text_3_pos, timestamp_pos, timestamp_type, counter_pos, extra_metadata, prompt, extra_pnginfo)
        return (None,)
```