# Documentation
- Class name: PruneByMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The PruneByMask node is designed to screen images selectively from a group of images based on the quality of the mask. Specifically, it retains only those images where the average pixel value of the mask reaches or exceeds the 0.5 threshold, ensuring that follow-up processing is concentrated on images with sufficient clarity.

# Input types
## Required
- image
    - Image parameters represent the series of images that you want to process. This is a key input, because the filtering of nodes depends entirely on the content of these images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask parameter corresponds to the relevant mask for the image in the batch. Node evaluates the average pixel value of the mask to determine which images are retained in the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- filtered_images
    - The filtered_images output contains a subset of input images that have passed node filter criteria based on the average pixel value of their relevant mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PruneByMask:
    """
    Filters out the images in a batch that don't have an associated mask with an average pixel value of at least 0.5.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'mask': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'prune'
    CATEGORY = 'Masquerade Nodes'

    def prune(self, image, mask):
        mask = tensor2mask(mask)
        mean = torch.mean(torch.mean(mask, dim=2), dim=1)
        return (image[mean >= 0.5],)
```