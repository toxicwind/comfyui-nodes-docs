# Documentation
- Class name: DuplicateImages
- Category: Video Helper Suite 🎥🅥🅗🅢/image
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The DuplicateImages node is designed to replicate a given set of images with a specified number of times. It is used to increase image data and apply to scenarios such as machine learning, where larger data sets can improve model training. The function of the node is very direct: it accepts an image array and an integer multiplier, and then returns a new array, containing the duplicated number of images, as well as the total number of images.

# Input types
## Required
- images
    - The 'image'parameter is the key input for the DuplicateImages node because it represents the image set to be copied. The node processes this input to create multiple copies, which is essential for certain image processing tasks or data enhancement strategies.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- multiply_by
    - The'multiply_by' parameter determines how many times each image in the 'images' input will be copied. It is an integer that directly affects the size of the output data set and is therefore a key factor for node operations in data enhancement purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The 'IMAGE' output parameter represents the duplicated image array. This is the main result of the DuplicateImages node, which contains all original images that are repeated according to the'multiply_by' parameter.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- count
    - The 'count' output parameter provides the total number of duplicate images. This integer value helps track the size of the dataset, which may be important for further processing or analysis.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class DuplicateImages:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'multiply_by': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/image'
    RETURN_TYPES = ('IMAGE', 'INT')
    RETURN_NAMES = ('IMAGE', 'count')
    FUNCTION = 'duplicate_input'

    def duplicate_input(self, images: Tensor, multiply_by: int):
        full_images = []
        for n in range(0, multiply_by):
            full_images.append(images)
        new_images = torch.cat(full_images, dim=0)
        return (new_images, new_images.size(0))
```