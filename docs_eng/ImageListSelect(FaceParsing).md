# Documentation
- Class name: ImageListSelect
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The ImageListSelect node may select a particular image from the image list based on the index provided, enabling a single image in a batch to be analysed or processed centrally.

# Input types
## Required
- images
    - It allows nodes to identify and select target images on the basis of the index provided.
    - Comfy dtype: IMAGE
    - Python dtype: List[Image]
- index
    - The index parameter determines which image is selected from the list. It is critical in guiding the correct selection of nodes for further processing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- selected_image
    - Selected_image represents the output of the node, i.e. the image selected from the input list based on the index provided. It is the result of the node operation and is ready for follow-up.
    - Comfy dtype: IMAGE
    - Python dtype: Image

# Usage tips
- Infra type: CPU

# Source code
```
class ImageListSelect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE', {}), 'index': ('INT', {'default': 0, 'min': 0, 'step': 1})}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, images, index):
        index = index[0]
        if images is Tensor:
            return (images[index].unsqueeze(0),)
        else:
            return (images[index],)
```