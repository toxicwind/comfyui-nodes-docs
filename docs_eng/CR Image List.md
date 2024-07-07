# Documentation
- Class name: CR_ImageList
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImageList node is designed to manage and organize the list of images. It allows users to enter separate images and their corresponding aliases and to group them into a single list of images. This node is particularly suitable for applications that need to be processed together or to display a collection of images.

# Input types
## Optional
- image_1
    - The 'image_1 'parameter indicates the first image that can be added to the image list. It plays a key role in the operation of the node by contributing to the final collection of images managed by the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- alias1
    - The 'alias1 'parameter is an optional string that can be used to provide aliases for 'image_1 '. This is very useful for referencing images in a more readable format.
    - Comfy dtype: STRING
    - Python dtype: str
- image_list
    - The 'image_list' parameter is a group list of aliases and images. This parameter is important because it allows nodes to process a pre-existing image and a collection of aliases.
    - Comfy dtype: image_LIST
    - Python dtype: List[Tuple[str, Union[str, torch.Tensor]]]

# Output types
- IMAGE_LIST
    - The 'IMAGE_LIST' output is a list of image aliases matched to their corresponding image. It represents a collection of all input images and aliases processed by nodes.
    - Comfy dtype: image_LIST
    - Python dtype: List[Tuple[str, Union[str, torch.Tensor]]]
- show_help
    - The'show_help' output provides a URL linked to the document for more help. This is particularly useful for users seeking more information on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageList:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'image_1': ('IMAGE',), 'alias1': ('STRING', {'multiline': False, 'default': ''}), 'image_2': ('IMAGE',), 'alias2': ('STRING', {'multiline': False, 'default': ''}), 'image_3': ('IMAGE',), 'alias3': ('STRING', {'multiline': False, 'default': ''}), 'image_4': ('IMAGE',), 'alias4': ('STRING', {'multiline': False, 'default': ''}), 'image_5': ('IMAGE',), 'alias5': ('STRING', {'multiline': False, 'default': ''}), 'image_list': ('image_LIST',)}}
    RETURN_TYPES = ('IMAGE_LIST', 'STRING')
    RETURN_NAMES = ('IMAGE_LIST', 'show_help')
    FUNCTION = 'image_list'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def image_list(self, image_1=None, alias1=None, image_2=None, alias2=None, image_3=None, alias3=None, image_4=None, alias4=None, image_5=None, alias5=None, image_list=None):
        images = list()
        if image_list is not None:
            image_tup = [(alias1, image_1)]
            images.extend([l for l in image_list])
        if image_1 != None:
            (images.extend([(alias1, image_1)]),)
        if image_2 != None:
            (images.extend([(alias2, image_2)]),)
        if image_3 != None:
            (images.extend([(alias3, image_3)]),)
        if image_4 != None:
            (images.extend([(alias4, image_4)]),)
        if image_5 != None:
            (images.extend([(alias5, image_5)]),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-image-list'
        return (images, show_help)
```