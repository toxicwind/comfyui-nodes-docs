# Documentation
- Class name: CR_ImageListSimple
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ImageListSimple nodes are designed to compile multiple images into a single structured format. By integrating multiple image sources into a coherent list, it streamlines the processing of multiple image sources, thus facilitating subsequent image processing tasks.

# Input types
## Optional
- image_1
    - The 'image_1 'parameter is one of the optional image inputes that can be provided to nodes. It functions in a list of images that can help the final output.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_2
    - The 'image_2' parameter is another optional image input for nodes. It is essential to increase the diversity of image lists and ensures full collection of visual data.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_3
    - The 'image_3'parameter is used to introduce another optional image into the processing process of the node. It contains a larger list of images and enhances the function of the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_4
    - The 'image_4' parameter allows for the inclusion of an additional optional image. It is important for expanding the range of images that can be processed by nodes.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_5
    - The 'image_5'parameter is the last optional image input acceptable to nodes. It ensures that nodes can process a wide range of image inputs and maximize their multifunctionality.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_list_simple
    - The 'image_list_simple' parameter is an optional input that allows a pre-existing list of images to be entered into the node. It is essential for users who want to use a planned list of images rather than a separate input.
    - Comfy dtype: IMAGE_LIST_SIMPLE
    - Python dtype: Union[List[str], List[torch.Tensor]]

# Output types
- IMAGE_LIST_SIMPLE
    - The 'IMAGE_LIST_SIMPLE' output is an integrated list of images processed by nodes. It is important because it forms the basis for further image operation or analysis.
    - Comfy dtype: IMAGE_LIST_SIMPLE
    - Python dtype: List[torch.Tensor]
- show_help
    - The'show_help' output provides a document URL link for further help. It is useful for users who need additional guidance on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageListSimple:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'image_1': ('IMAGE',), 'image_2': ('IMAGE',), 'image_3': ('IMAGE',), 'image_4': ('IMAGE',), 'image_5': ('IMAGE',), 'image_list_simple': ('IMAGE_LIST_SIMPLE',)}}
    RETURN_TYPES = ('IMAGE_LIST_SIMPLE', 'STRING')
    RETURN_NAMES = ('IMAGE_LIST_SIMPLE', 'show_help')
    FUNCTION = 'image_list_simple'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def image_list_simple(self, image_1=None, image_2=None, image_3=None, image_4=None, image_5=None, image_list_simple=None):
        images = list()
        if image_list_simple is not None:
            images.append((l for l in image_list_simple))
        if image_1 != None:
            (images.append(image_1),)
        if image_2 != None:
            images.append(image_2)
        if image_3 != None:
            images.append(image_3)
        if image_4 != None:
            (images.append(image_4),)
        if image_5 != None:
            (images.append(image_5),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-image-list-simple'
        return (images, show_help)
```