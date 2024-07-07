# Documentation
- Class name: ImageBatchToImageList
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImageBatchToImageList node is designed to convert a group of images into a list of individual images. As a practical tool in the ImpactPack category, it facilitates the conversion from batch processing to individual image processing, which is essential for certain downstream tasks that require image-by-image operations.

# Input types
## Required
- image
    - The 'image'parameter is the input batch that you want to process. It is vital because it determines the content that will be converted to a single image list. The function of the node depends directly on the quality and format of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- images
    - The 'images' output is a list of individual images derived from the input batch. Each image in the list corresponds to an element in the original batch and applies to applications that require individual image operations or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageBatchToImageList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, image):
        images = [image[i:i + 1, ...] for i in range(image.shape[0])]
        return (images,)
```