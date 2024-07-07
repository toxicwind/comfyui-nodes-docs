# Documentation
- Class name: AddMetaData
- Category: Mikey/Meta
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

The AddMetaData node is designed to enrich image data by adding text information to it. It does so by attaching the specified text value to the metadata of the image, which may include dynamic elements such as data from dates or other nodes in the workflow. This node plays a key role in creating comprehensive metadata that enhances the usefulness and context of the image and applies to various applications.

# Input types
## Required
- image
    - The image parameter is essential because it is the primary data object of the node operation. It represents the image that will add metadata. The node is executed around this image, making it an essential part of the process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or similar image object
- label
    - tab parameter as a metadata descriptor. It is a necessary field to provide a text identifier for the metadata attached to the image. This label is important because it classifies and describes the metadata that are being added.
    - Comfy dtype: STRING
    - Python dtype: str
- text_value
    - The text value parameter is essential to the function of the node, as it defines the text that will be included in the image metadata. This text can be static or dynamic, allowing flexibility to enrich the metadata.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prompt
    - The optional hint parameter can be used to inject dynamic data into metadata. When metadata require information from other nodes or components in the workflow, it is particularly useful and allows for a more interactive and context-sensitive metadata creation process.
    - Comfy dtype: PROMPT
    - Python dtype: dict or str
- extra_pnginfo
    - Additional PNG information parameters, while optional, can provide additional context or details specific to the image. It can be used to store additional information that is not a direct part of the main metadata but that is still relevant for certain applications or analyses.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict or str

# Output types
- image_with_metadata
    - The output of the AddMetaData node is the original image with the added metadata. This output represents the result of the node process, in which the image is now enriched with the specified text value for further use or distribution.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or similar image object

# Usage tips
- Infra type: CPU

# Source code
```
class AddMetaData:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'label': ('STRING', {'multiline': False, 'placeholder': 'Label for metadata'}), 'text_value': ('STRING', {'multiline': True, 'placeholder': 'Text to add to metadata'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'add_metadata'
    CATEGORY = 'Mikey/Meta'
    OUTPUT_NODE = True

    def add_metadata(self, image, label, text_value, prompt=None, extra_pnginfo=None):
        label = search_and_replace(label, extra_pnginfo, prompt)
        text_value = search_and_replace(text_value, extra_pnginfo, prompt)
        if extra_pnginfo is None:
            extra_pnginfo = {}
        if label in extra_pnginfo:
            extra_pnginfo[label] += ', ' + text_value
        else:
            extra_pnginfo[label] = text_value
        return (image,)
```