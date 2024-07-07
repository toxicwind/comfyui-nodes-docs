# Documentation
- Class name: WAS_Tensor_Batch_to_Image
- Category: WAS Suite/Latent/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method `tensor_batch_to_image'is designed to convert a batch of images into a single image expression. It is a key step in the image processing process, allowing for bulk data to be converted to formats that can be easily used or displayed.

# Input types
## Required
- images_batch
    - The parameter `images_batch'is critical because it contains a batch of images to be converted to a single image. It plays a central role in the operation of nodes, determining the source data of the conversion process.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- batch_image_number
    - Parameter `batch_image_number'determines which image is selected for conversion from a batch of images. Its value influences the execution of the node by specifying the index of the image required in the batch.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output `image'is the result of the conversion process, representing the image selected from a group of images. It is important because it is a direct output of node functions and contains the converted data.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Tensor_Batch_to_Image:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images_batch': ('IMAGE',), 'batch_image_number': ('INT', {'default': 0, 'min': 0, 'max': 64, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'tensor_batch_to_image'
    CATEGORY = 'WAS Suite/Latent/Transform'

    def tensor_batch_to_image(self, images_batch=[], batch_image_number=0):
        count = 0
        for _ in images_batch:
            if batch_image_number == count:
                return (images_batch[batch_image_number].unsqueeze(0),)
            count = count + 1
        cstr(f'Batch number `{batch_image_number}` is not defined, returning last image').error.print()
        return (images_batch[-1].unsqueeze(0),)
```