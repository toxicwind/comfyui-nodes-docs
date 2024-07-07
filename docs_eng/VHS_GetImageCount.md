# Documentation
- Class name: GetImageCount
- Category: Video Helper Suite 🎥🅥🅗🅢/image
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The GetImageCount node is designed to efficiently determine the total number of images that exist in the given data concentration. It is a key component of the video processing workflow and provides a direct method of understanding the size of the data set without the need for in-depth understanding of the complexity of individual image data. The main objective of the node is to provide a simple and reliable count, which is essential for planning and managing computing resources.

# Input types
## Required
- images
    - The 'image'parameter is the input data set that contains image data. It is the basic element of node operations because it directly affects the count results. Node processes this input to determine the total number of images, which is essential for various downstream tasks (e.g. analysis, indexing and resource allocation).
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- count
    - ‘account’ output provides the total number of images processed at nodes. It is a single integer value, which indicates the size of the dataset in terms of the number of images. This output is important for users who need to know the size of the dataset for further processing or informed decision-making on application needs.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GetImageCount:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/image'
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('count',)
    FUNCTION = 'count_input'

    def count_input(self, images: Tensor):
        return (images.size(0),)
```