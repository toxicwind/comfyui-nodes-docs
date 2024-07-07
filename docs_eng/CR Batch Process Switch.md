# Documentation
- Class name: CR_BatchProcessSwitch
- Category: Comfyroll/Utils/Process
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_BatchProcessSwitch node is designed to provide a mechanism for switching between different types of image input. It is based on input selection of intelligent route processing processes that allow processing of individual images and image batches. In a scenario that needs to adapt to the dynamics of the type of input to process logic, the node is essential to ensure the flexibility and efficiency of the image processing workflow.

# Input types
## Required
- Input
    - The 'Input'parameter is essential because it determines the type of image processing to be performed. It determines whether the node will process a single image or an image batch, thus affecting the next steps and output in the workflow.
    - Comfy dtype: COMBO[image, image batch]
    - Python dtype: str
## Optional
- image
    - The 'image 'parameter is used to process individual images. It is important because it represents the input of individual image processing tasks, enabling nodes to handle operations specific to images.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]
- image_batch
    - The `image_batch'parameter is essential for processing a set of images. It allows nodes to manage and process image batches efficiently, applying to scenarios that require batch operations.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, List[torch.Tensor]]

# Output types
- IMAGE
    - The 'IMAGE'output parameter represents the selection of a processed image or image batch based on input. It is the key result of node operations and contains the result of the image processing task.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor, List[torch.Tensor]]
- show_help
    - The'show_help' output provides a document link for further help. It is important because it provides users with a resource to understand the function and use of nodes in more detail.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_BatchProcessSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': (['image', 'image batch'],)}, 'optional': {'image': ('IMAGE',), 'image_batch': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Process')

    def switch(self, Input, image=None, image_batch=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Process-Nodes#cr-batch-process-switch'
        if Input == 'image':
            return (image, show_help)
        else:
            return (image_batch, show_help)
```