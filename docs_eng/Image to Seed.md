# Documentation
- Class name: WAS_Image_To_Seed
- Category: WAS Suite/Image/Analyze
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The function `image_to_seed'is designed to convert a series of images into a corresponding seed collection. It uses the inherent properties of each image to produce a unique identifier that can be used in various applications, such as image indexing or retrieval systems. The node plays a key role in the analysis process, enabling visual data to be converted to forms that are both compact and representative of the original content.

# Input types
## Required
- images
    - The parameter 'images' is essential to the operation of the node, because it is the input data processed by the node. Each image is converted into a seed through a series of operations. Entering the quality and properties of the image directly affects the seed generated and its subsequent application.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Output types
- seeds
    - Output'seeds' is an integer list of seeds derived from the input of images. Each torrent is a Hashi-based summary of image content, providing a concise and unique representation. This output is important because it provides the basis for further processing or analysis of downstream tasks.
    - Comfy dtype: INT
    - Python dtype: List[int]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_To_Seed:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',)}}
    RETURN_TYPES = ('INT',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'image_to_seed'
    CATEGORY = 'WAS Suite/Image/Analyze'

    def image_to_seed(self, images):
        seeds = []
        for image in images:
            image = tensor2pil(image)
            seeds.append(image2seed(image))
        return (seeds,)
```