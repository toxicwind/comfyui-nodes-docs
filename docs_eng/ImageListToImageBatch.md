# Documentation
- Class name: ImageListToImageBatch
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The node is designed to convert image lists efficiently into individual image batches. It does this by connecting images to the first dimension, ensuring that all images in the batch have the same shape. Node plays a key role in preparing image data for further processing (e.g. batch-based neural network operations).

# Input types
## Required
- images
    - The 'image'parameter is the list of image lengths that the node will process. It is essential for the operation of the node because it directly affects the creation of the image batch. This parameter ensures that all images are compatible and can be connected to a single batch.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Output types
- image_batch
    - The output of the node is a single image length that represents a batch of images. This batch is created by connecting the input image to the first dimension, making it suitable for downstream tasks that require bulk image data.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImageListToImageBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',)}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, images):
        if len(images) <= 1:
            return (images,)
        else:
            image1 = images[0]
            for image2 in images[1:]:
                if image1.shape[1:] != image2.shape[1:]:
                    image2 = comfy.utils.common_upscale(image2.movedim(-1, 1), image1.shape[2], image1.shape[1], 'lanczos', 'center').movedim(1, -1)
                image1 = torch.cat((image1, image2), dim=0)
            return (image1,)
```