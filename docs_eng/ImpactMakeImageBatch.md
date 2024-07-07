# Documentation
- Class name: MakeImageBatch
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `MakeImageBatch' node is designed to group multiple images into a single batch for further processing in an efficient manner. It ensures that all images in the batch have the same size and connects them along the batch dimensions by resizeing them where necessary. The node plays a key role in preparing uniform data sets for image processing tasks, such as mass neural network training or bulk image operations.

# Input types
## Required
- image1
    - The `image1' parameter is the first image to be used as a reference for image batch sizes. It is vital because, if the following images are different sizes, they will be adjusted to match their dimensions. Node functions depend on this parameter to create a single batch for downstream tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- kwargs
    - The `kwargs' parameter allows for the inclusion of additional images in the batch. Each image provided through this parameter is processed in the same way as `image1' to ensure the consistency of the batch. The `kwargs' flexibility allows nodes to adapt to the variable numbers of images in different scenarios and enhances their usefulness.
    - Comfy dtype: COMBO[str, IMAGE]
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- image_batch
    - The `image_batch' output is a connected batch of images that have been resized to maintain consistency within the batch. This output is important because it provides the basis for subsequent image processing tasks and ensures that batches are ready for operations such as neural network input or batch image editing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MakeImageBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image1': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, **kwargs):
        image1 = kwargs['image1']
        del kwargs['image1']
        images = [value for value in kwargs.values()]
        if len(images) == 0:
            return (image1,)
        else:
            for image2 in images:
                if image1.shape[1:] != image2.shape[1:]:
                    image2 = comfy.utils.common_upscale(image2.movedim(-1, 1), image1.shape[2], image1.shape[1], 'lanczos', 'center').movedim(1, -1)
                image1 = torch.cat((image1, image2), dim=0)
            return (image1,)
```