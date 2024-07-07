# Documentation
- Class name: ImageBatchSplitter
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The ImageBatchSplitter node is designed to efficiently manage and operate the image batch by dividing the image batch into smaller subsets based on user-defined counts. It ensures that the batch size is matched to the specified count, even if the total number of images cannot be broken down. The node plays a vital role in preparing data for further processing (which requires a uniform batch size) and helps machine learning or overall data pipeline management in image processing workflows.

# Input types
## Required
- images
    - The 'image' parameter is the main input for the ImageBatchSplitter node, representing the collection of image data to be processed. The parameter directly affects the operation and output quality of the node because the node operates and organizes the images in a subset based on'split_count'.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image]
## Optional
- split_count
    - The `split_count' parameter is essential for the function of the ImageBatchSplitter node. It determines how many intended subsets of the input image are divided. It affects the particle size of the output and is essential to ensure that the processed data meet the requirements of the downstream machine learning model or image processing task.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output of the ImageBatchSpliter node is a group of components containing processed images that organize subsets according to the'split_count' parameters. This output is essential for subsequent operations that require a uniform batch size and facilitates smooth flow of data in the process.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageBatchSplitter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'split_count': ('INT', {'default': 4, 'min': 0, 'max': 50, 'step': 1})}}
    RETURN_TYPES = ByPassTypeTuple(('IMAGE',))
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, images, split_count):
        cnt = min(split_count, len(images))
        res = [image.unsqueeze(0) for image in images[:cnt]]
        if split_count >= len(images):
            lack_cnt = split_count - cnt + 1
            empty_image = empty_pil_tensor()
            for x in range(0, lack_cnt):
                res.append(empty_image)
        elif cnt < len(images):
            remained_cnt = len(images) - cnt
            remained_image = images[-remained_cnt:]
            res.append(remained_image)
        return tuple(res)
```