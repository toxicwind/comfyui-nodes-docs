# Documentation
- Class name: MergeImages
- Category: Video Helper Suite 🎥🅥🅗🅢/image
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The `merge' method of the MergeImages nodes is designed to combine two sets of images into a single array. It deals intelligently with the differences in image sizes by applying scaling and cropping techniques based on specified consolidation strategies. When further processing or visualization is required, this method is essential for preparing a unified image data set.

# Input types
## Required
- images_A
    - The parameter 'images_A' indicates the first set of images to be merged. When two sets of images differ in size, it plays a key role in determining the final size and structure of the merged image arrays.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- images_B
    - The parameter 'images_B' indicates the second group of images that you want to merge. Its dimensions are coordinated with 'images_A' to ensure consistency of output and make an important contribution to the final composition of the merged image set.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- merge_strategy
    - The parameter'merge_strategy'determines how to combine two sets of images. It is essential to resolve the size mismatch and to guide the scaling and cropping process to hold the visual consistency in the combined output.
    - Comfy dtype: str
    - Python dtype: str
- scale_method
    - Parameter'scale_method'is a technology used to resize images to match sizes. It is a key component of the image consolidation process, ensuring that images are scalded appropriately without compromising quality.
    - Comfy dtype: str
    - Python dtype: str
- crop
    - Parameter 'crop' determines how the image should be cropped after scaling to adapt to the merged image array. It is important to maintain the vertical ratio and overall visual appeal of the image that eventually merges.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- IMAGE
    - Output 'IMAGE' means the merged image array, which is the end result of the consolidation process. It contains visual data from the combination of 'images_A' and 'images_B'according to the specified integration strategy and scaling parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- count
    - Output 'count'provides the total number of images in the merged array. This integer value is important for relying on indexes and further processing steps that know the exact number of images.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class MergeImages:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images_A': ('IMAGE',), 'images_B': ('IMAGE',), 'merge_strategy': (MergeStrategies.list_all,), 'scale_method': (ScaleMethods.list_all,), 'crop': (CropMethods.list_all,)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/image'
    RETURN_TYPES = ('IMAGE', 'INT')
    RETURN_NAMES = ('IMAGE', 'count')
    FUNCTION = 'merge'

    def merge(self, images_A: Tensor, images_B: Tensor, merge_strategy: str, scale_method: str, crop: str):
        images = []
        if images_A.shape[3] != images_B.shape[3] or images_A.shape[2] != images_B.shape[2]:
            images_A = images_A.movedim(-1, 1)
            images_B = images_B.movedim(-1, 1)
            A_size = images_A.shape[3] * images_A.shape[2]
            B_size = images_B.shape[3] * images_B.shape[2]
            use_A_as_template = True
            if merge_strategy == MergeStrategies.MATCH_A:
                pass
            elif merge_strategy == MergeStrategies.MATCH_B:
                use_A_as_template = False
            elif merge_strategy in (MergeStrategies.MATCH_SMALLER, MergeStrategies.MATCH_LARGER):
                if A_size <= B_size:
                    use_A_as_template = True if merge_strategy == MergeStrategies.MATCH_SMALLER else False
            if use_A_as_template:
                images_B = comfy.utils.common_upscale(images_B, images_A.shape[3], images_A.shape[2], scale_method, crop)
            else:
                images_A = comfy.utils.common_upscale(images_A, images_B.shape[3], images_B.shape[2], scale_method, crop)
            images_A = images_A.movedim(1, -1)
            images_B = images_B.movedim(1, -1)
        images.append(images_A)
        images.append(images_B)
        all_images = torch.cat(images, dim=0)
        return (all_images, all_images.size(0))
```