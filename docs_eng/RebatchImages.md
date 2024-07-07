# Documentation
- Class name: ImageRebatch
- Category: image/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageRebatch node is designed to reorganize image data into batches efficiently. It receives a set of images and a specified batch size, then processes them to create smaller batches that can be used for parallel processing or batch-based machine learning tasks. The node plays a key role in optimizing image data processing, allowing for more efficient training and reasoning workflows.

# Input types
## Required
- images
    - The `images' parameter is the collection of image data that the node will process. It is the basic raw material for the node operation, which is batched. The function of the node depends directly on the quality and format of the input image, which affects the efficiency and outcome of the batch processing.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- batch_size
    - The `batch_size' parameter determines the number of images to be included in each output batch. It is a key parameter that determines the particle size of the batch process, directly affects the performance of the node and subsequent processing or training steps. The proper selection of the batch size is important for balancing memory use and calculating efficiency.
    - Comfy dtype: INT
    - Python dtype: Tuple[int]

# Output types
- output_list
    - 'output_list' is a list of image batches generated by nodes. Each batch is an image sheet prepared according to the size of the specified batch. This output is important because it represents the main deliverer of the node and can be further processed or entered into a follow-on node or model in the machine learning process.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageRebatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('IMAGE',)
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'rebatch'
    CATEGORY = 'image/batch'

    def rebatch(self, images, batch_size):
        batch_size = batch_size[0]
        output_list = []
        all_images = []
        for img in images:
            for i in range(img.shape[0]):
                all_images.append(img[i:i + 1])
        for i in range(0, len(all_images), batch_size):
            output_list.append(torch.cat(all_images[i:i + batch_size], dim=0))
        return (output_list,)
```