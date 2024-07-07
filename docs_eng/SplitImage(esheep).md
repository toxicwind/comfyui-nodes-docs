# Documentation
- Class name: ImageSplitNode
- Category: util
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The node is designed to divide images into smaller subsets that facilitate processing by decomposing large image data sets into manageable blocks. It enhances workflows by allowing parallel processing, and can improve the efficiency of computing tasks. In the process of partitioning, node maintains the integrity of the image.

# Input types
## Required
- images
    - The input parameter 'images' is a set of image data that will be processed at nodes. It is essential for the operation of nodes, as it is the main input to the image partition function. The quality and format of the image significantly influences subsequent processing and output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- split_images
    - The output of the nodes consists of multiple image subsets, which are the result of the image partitioning process. The subsets are ready for further processing and can be used for various downstream tasks, such as feature extraction or model training.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageSplitNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',)}}
    MAX_SIZE = 6
    RETURN_TYPES = ['IMAGE'] * 6
    FUNCTION = 'main'
    CATEGORY = 'util'

    def main(self, images):
        items = torch.chunk(images, self.MAX_SIZE)
        padding_size = self.MAX_SIZE - len(items)
        if padding_size > 0:
            items = items + tuple([create_empty_image()] * padding_size)
        return items
```