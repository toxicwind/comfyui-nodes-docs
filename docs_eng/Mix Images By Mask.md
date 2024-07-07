# Documentation
- Class name: MixByMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The MixByMask node is designed to mix two images according to the given mask. It operates by adjusting the contribution of each image to the value of the mask, allowing seamless integration of different visual elements in individual composite images.

# Input types
## Required
- image1
    - The first image that you want to mix. This is a basic input that determines the essential visual content of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image2
    - The second image that you want to mix. It provides additional visual content that will be merged with the first image according to the mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Determines how the two images mix the mask. It is a key component that controls the mixing process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- mixed_image
    - Output is a mixture of images obtained by applying a mask to an input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MixByMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image1': ('IMAGE',), 'image2': ('IMAGE',), 'mask': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'mix'
    CATEGORY = 'Masquerade Nodes'

    def mix(self, image1, image2, mask):
        (image1, image2) = tensors2common(image1, image2)
        mask = tensor2batch(mask, image1.size())
        return (image1 * (1.0 - mask) + image2 * mask,)
```