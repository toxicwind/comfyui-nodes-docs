# Documentation
- Class name: SaveMetaData
- Category: Mikey/Meta
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

The `save_metadata'method is designed to organize and store metadata associated with images. It creates a text file containing relevant information, such as time stampes, filename prefixes, and additional details provided by the user. This method ensures that metadata for each image are systematically recorded and easily accessible.

# Input types
## Required
- image
    - The image parameter is necessary because it is the visual content that metadata will relate to. This is a necessary input and plays a central role in the operation of the node, because it is the subject of the metadata that are being saved.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or similar image object
## Optional
- filename_prefix
    - The prefix parameter is used to define the beginning of the file name for the metadata file. Although it is not mandatory, it is important for organizing the document in a meaningful way and, if not provided, can be set as the default value.
    - Comfy dtype: STRING
    - Python dtype: str
- timestamp_prefix
    - The time stamp prefix parameter determines whether to include a time stamp in the filename. It provides a way to organize files in chronological order, defaulting to 'true', indicating that a time stamp should be included.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- counter
    - The counter parameter is used to attach a digital counter to a file name to ensure uniformity and prevent file overlay. The default setting is 'true', highlighting its importance in maintaining file integrity.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- prompt
    - A reminder parameter is an optional input that can be used to provide additional context or information that may be relevant to the metadata. It enhances the description of the metadata, not a mandatory requirement.
    - Comfy dtype: PROMPT
    - Python dtype: dict
- extra_pnginfo
    - Additional png information parameters are used to contain additional information specific to the image, such as notes or other details. This optional input allows for the preservation of a more comprehensive metadata set.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict

# Output types
- save_metadata
    - The output of the save_metadata method is a dictionary of filenames and subfolders containing saved metadata. This output provides confirmation of the saving operation and the location of the saved metadata.
    - Comfy dtype: COMBO[filename, subfolder]
    - Python dtype: Dict[str, Union[str, Dict[str, str]]]

# Usage tips
- Infra type: CPU

# Source code
```
class SaveMetaData:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'filename_prefix': ('STRING', {'default': ''}), 'timestamp_prefix': (['true', 'false'], {'default': 'true'}), 'counter': (['true', 'false'], {'default': 'true'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_metadata'
    CATEGORY = 'Mikey/Meta'
    OUTPUT_NODE = True

    def save_metadata(self, image, filename_prefix, timestamp_prefix, counter, prompt=None, extra_pnginfo=None):
        filename_prefix = search_and_replace(filename_prefix, extra_pnginfo, prompt)
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, folder_paths.get_output_directory(), 1, 1)
        ts_str = datetime.datetime.now().strftime('%y%m%d%H%M')
        filen = ''
        if timestamp_prefix == 'true':
            filen += ts_str + '_'
        filen = filen + filename_prefix
        if counter == 'true':
            filen += '_' + str(counter)
        filename = filen + '.txt'
        file_path = os.path.join(full_output_folder, filename)
        with open(file_path, 'w') as file:
            for (key, value) in extra_pnginfo.items():
                file.write(f'{key}: {value}\n')
            for (key, value) in prompt.items():
                file.write(f'{key}: {value}\n')
        return {'save_metadata': {'filename': filename, 'subfolder': subfolder}}
```