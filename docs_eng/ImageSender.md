# Documentation
- Class name: ImageSender
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImageSender node is designed to facilitate the transmission of image data. It processes a series of images, assigns prefixes to their filenames and sends them to the specified server endpoint. This node plays a key role in the workflow by enabling seamless exchange of visual content between systems.

# Input types
## Required
- images
    - The 'image' parameter is essential for the ImageSender node, as it represents a collection of visual data to be processed and transmitted. Its proper selection and format directly influences the ability of the node to perform the task.
    - Comfy dtype: IMAGE
    - Python dtype: List[bytes]
## Optional
- filename_prefix
    - Defines a common prefix for the filename of the image being processed using the 'filename_prefix' parameter. This helps to organize and identify the image in a systematic way in the receiving system.
    - Comfy dtype: STRING
    - Python dtype: str
- link_id
    - The 'link_id'parameter is an identifier that links the image to a specific link or context in the receiving system. It helps target the transfer and reference of image data.
    - Comfy dtype: INT
    - Python dtype: int
- prompt
    - The 'prompt' parameter, although optional, can be used to provide additional context or instructions for image processing. It enhances the function of nodes by allowing for more subtle control of image processing.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The 'extra_pnginfo'parameter allows for the inclusion of additional metadata or information in the PNG image. This is useful for enhancing image data with such additional details as the receiving system may require.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- result
    - The ImageSender output contains the results of the image transfer process. It includes the images sent and any relevant metadata and provides a comprehensive overview of node operations.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageSender(nodes.PreviewImage):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'ImgSender'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    OUTPUT_NODE = True
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, images, filename_prefix='ImgSender', link_id=0, prompt=None, extra_pnginfo=None):
        result = nodes.PreviewImage().save_images(images, filename_prefix, prompt, extra_pnginfo)
        PromptServer.instance.send_sync('img-send', {'link_id': link_id, 'images': result['ui']['images']})
        return result
```