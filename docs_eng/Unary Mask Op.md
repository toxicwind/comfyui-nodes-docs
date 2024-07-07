# Documentation
- Class name: UnaryMaskOp
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The UnaryMaskop node is designed to perform multiple monolithic operations for the given mask image. It provides a set of methods to operate the mask, such as reverse masking, average pixel values, rounding, clipping to a certain range, and taking absolute values. These operations are essential for the pre-processing steps of the image-processing task, which may require different forms of representation of the mask.

# Input types
## Required
- image
    - The image parameter is essential for the UnaryMaskop node, as it represents an input mask image that will be operated in a single dollar. The function of the node is directly related to the quality and format of the input, which affects the results of the operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- op
    - The operational parameter determines the specific monolithic operation that will be applied to the input mask. It is a key component because it determines the type of change that will occur and affects the final result of node execution.
    - Comfy dtype: COMBO['invert', 'average', 'round', 'clamp', 'abs']
    - Python dtype: str

# Output types
- result
    - The result parameter encapsifies the result of a single-dimensional operation applied to the input mask. It is an important output because it reflects a changed mask that can be used for further processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class UnaryMaskOp:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'op': (['invert', 'average', 'round', 'clamp', 'abs'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'op_mask'
    CATEGORY = 'Masquerade Nodes'

    def op_mask(self, image, op):
        image = tensor2mask(image)
        if op == 'invert':
            return (1.0 - image,)
        elif op == 'average':
            mean = torch.mean(torch.mean(image, dim=2), dim=1)
            return (mean.unsqueeze(1).unsqueeze(2).repeat(1, image.shape[1], image.shape[2]),)
        elif op == 'round':
            return (torch.round(image),)
        elif op == 'clamp':
            return (torch.min(torch.max(image, torch.tensor(0.0)), torch.tensor(1.0)),)
        elif op == 'abs':
            return (torch.abs(image),)
```