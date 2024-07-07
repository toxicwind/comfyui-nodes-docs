# Documentation
- Class name: MakeImageList
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `MakeImageList' node is designed to aggregate image data into a list to process images in bulk. It plays a vital role in the workflow of image-related tasks by ensuring that images are organized in a manner compatible with downstream operations.

# Input types
## Required
- image1
    - The `image1' parameter is essential because it represents the first image to be included in the list. Its inclusion is necessary for the proper functioning of the node, highlighting its importance in the overall operation of the node.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, torch.Tensor]

# Output types
- images
    - The `images' output is a list of image data compiled by nodes. It is important because it is an input to the follow-up image processing task and is an important part of the image operating process.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class MakeImageList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image1': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, **kwargs):
        images = []
        for (k, v) in kwargs.items():
            images.append(v)
        return (images,)
```