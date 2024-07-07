# Documentation
- Class name: SelectEveryNthImage
- Category: Video Helper Suite 🎥🅥🅗🅢/image
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The `select_images'method for the SecretEveryNthImage node is designed to efficiently select and retrieve subsets from a larger collection of images. It operates by selecting every n image specified by the user, allowing for the creation of a streamlined sequence that keeps the original order. This feature is particularly suitable for the reduction of a need for a representative image, without the need to process the application of the entire data set.

# Input types
## Required
- images
    - The “images” parameter is the set of image data to be processed by the node. It is the basis for node operations, as it represents the input data set from which the image is selected. The execution and output of the node depends heavily on the content and structure of this parameter.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- select_every_nth
    - The'select_every_nth'parameter determines the frequency of selecting images from input pools. It is a key determinant in node operations, as it directly affects the number of images returned in output. The parameter ensures that the selection process is systematic and predictable, based on the specified spacing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The IMAGE output consists of a subset of the images selected in the input collection. This output is important because it represents the direct result of node operations and provides users with a selection of image sequences based on the specified selection criteria.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- count
    - The " count" output provides the total number of images selected from the input pool. This information is valuable for users as it helps to understand the scope of the selection process and evaluates the output in the context of the original data set.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SelectEveryNthImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'select_every_nth': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/image'
    RETURN_TYPES = ('IMAGE', 'INT')
    RETURN_NAMES = ('IMAGE', 'count')
    FUNCTION = 'select_images'

    def select_images(self, images: Tensor, select_every_nth: int):
        sub_images = images[0::select_every_nth]
        return (sub_images, sub_images.size(0))
```