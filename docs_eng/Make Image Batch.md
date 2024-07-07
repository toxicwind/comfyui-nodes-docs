# Documentation
- Class name: MakeImageBatch
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The `MakeImageBatch' node is designed to combine several individual images or existing image batches efficiently into a single, unified batch. This node plays a crucial role in the pre-processing phase of the image-processing task, allowing images to be entered into a format that is suitable for batch processing.

# Input types
## Required
- image1
    - The main image that is the basis for creating a batch of images. It is necessary and its existence starts the batch formation process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- image2
    - Selectable additional images that can be connected to the batch. It enhances diversity within the batch and provides more data for processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image3
    - Another optional image in the batch further expanded the data set for comprehensive analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image4
    - Additional images may be included in the batch to increase the size of the image data.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image5
    - This image is optional and adds to the complexity and richness of the image batch.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image6
    - The final optional images can be added to the batch to provide the final contribution to the size of the data set.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- result
    - Output is an integrated image batch created by adding the image sequentially. It is important because it represents the top point of the batch creation process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MakeImageBatch:
    """
    Creates a batch of images from multiple individual images or batches.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image1': ('IMAGE',)}, 'optional': {'image2': ('IMAGE',), 'image3': ('IMAGE',), 'image4': ('IMAGE',), 'image5': ('IMAGE',), 'image6': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'append'
    CATEGORY = 'Masquerade Nodes'

    def append(self, image1, image2=None, image3=None, image4=None, image5=None, image6=None):
        result = image1
        if image2 is not None:
            result = torch.cat((result, image2), 0)
        if image3 is not None:
            result = torch.cat((result, image3), 0)
        if image4 is not None:
            result = torch.cat((result, image4), 0)
        if image5 is not None:
            result = torch.cat((result, image5), 0)
        if image6 is not None:
            result = torch.cat((result, image6), 0)
        return (result,)
```