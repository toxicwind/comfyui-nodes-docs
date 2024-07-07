# Documentation
- Class name: WAS_Image_Batch
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Batch node is designed to process and batch to process multiple images for further operation. It ensures that all input images have a matching size and then merges them into a single plate volume, thus contributing to efficient batch processing of image data.

# Input types
## Optional
- images_a
    - The parameter 'images_a' is used to provide a set of images to be processed in batches. It plays a vital role in the operation of nodes because it directly affects the content to be processed.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]
- images_b
    - The parameter 'images_b' is the optional image source in the batch. It is important because it allows other images to be processed with 'images_a'.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]
- images_c
    - The parameter 'images_c' is another optional image input that increases the flexibility of nodes to adapt to more image data for bulk processing.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]
- images_d
    - The parameter 'images_d' provides further optional image input capability, allowing nodes to process a wider array of images in individual batch operations.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Output types
- image
    - The 'image'output represents the volume of images that have been processed and connected. It is essential for the downstream tasks that require the harmonization of image data batches.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'images_a': ('IMAGE',), 'images_b': ('IMAGE',), 'images_c': ('IMAGE',), 'images_d': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'image_batch'
    CATEGORY = 'WAS Suite/Image'

    def _check_image_dimensions(self, tensors, names):
        reference_dimensions = tensors[0].shape[1:]
        mismatched_images = [names[i] for (i, tensor) in enumerate(tensors) if tensor.shape[1:] != reference_dimensions]
        if mismatched_images:
            raise ValueError(f'WAS Image Batch Warning: Input image dimensions do not match for images: {mismatched_images}')

    def image_batch(self, **kwargs):
        batched_tensors = [kwargs[key] for key in kwargs if kwargs[key] is not None]
        image_names = [key for key in kwargs if kwargs[key] is not None]
        if not batched_tensors:
            raise ValueError('At least one input image must be provided.')
        self._check_image_dimensions(batched_tensors, image_names)
        batched_tensors = torch.cat(batched_tensors, dim=0)
        return (batched_tensors,)
```