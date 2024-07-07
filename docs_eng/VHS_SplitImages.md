# Documentation
- Class name: SplitImages
- Category: Video Helper Suite 🎥🅥🅗🅢/image
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The SpringImages node is designed to divide a series of images into two different groups based on the specified index. It plays a key role in the image processing workflow, where data fragmentation is essential for subsequent operations, such as analysis, sorting or special processing of different subsets.

# Input types
## Required
- images
    - The 'image'parameter is the collection of image data that the node will process. It is the basis for node operations, because it determines what is to be divided. The effect of this parameter on node execution is direct, because all logic of the node revolves around dividing this input.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- split_index
    - The'split_index'parameter defines the location where the input image is divided into two groups. It is essential for determining the size of each group and therefore affects the outcome of the node operation. The default values ensure a balanced split unless otherwise specified.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE_A
    - The 'IMAGE_A' output contains the first set of images in the split operation results. It represents part of the original image collection and is important for further processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- A_count
    - The 'A_count' output provides the number of the first group of images, which is determined by the split operation. This count is important to track the distribution of the images or to know the downstream processing of the group size.
    - Comfy dtype: INT
    - Python dtype: int
- IMAGE_B
    - The 'IMAGE_B' output saves a split second group of images. It is the equivalent of 'IMAGE_A' and is equally important for the next steps that may involve different treatment or assessment of the two groups.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- B_count
    - The 'B_count' output shows the number of images that enter the second group after a split. This information is valuable for understanding the division of data sets and can inform further analysis or processing steps.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SplitImages:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'split_index': ('INT', {'default': 0, 'step': 1, 'min': BIGMIN, 'max': BIGMAX})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/image'
    RETURN_TYPES = ('IMAGE', 'INT', 'IMAGE', 'INT')
    RETURN_NAMES = ('IMAGE_A', 'A_count', 'IMAGE_B', 'B_count')
    FUNCTION = 'split_images'

    def split_images(self, images: Tensor, split_index: int):
        group_a = images[:split_index]
        group_b = images[split_index:]
        return (group_a, group_a.size(0), group_b, group_b.size(0))
```