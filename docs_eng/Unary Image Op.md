# Documentation
- Class name: UnaryImageOp
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The UnaryImageOp node is designed to perform multiple single input image operations. It provides a series of monolithic operations, such as image reverses, averages, rounds, clippings, and absolute values calculations. These operations are essential for image pre-processing and feature extraction, allowing the operation of image data to meet specific analytical or visual needs.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input to the UnaryImageop node. It represents the image data that will be subject to a single-dimensional operation. The image properties directly influence the output of the node, making it an essential part of the node execution.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- op
    - The op-parameter specifies the monolithic operation to be applied to the image. It is the key determinant of the node function, as it determines the type of conversion to be performed. The selection of the operation significantly alters the properties of the result image and affects downstream processing.
    - Comfy dtype: COMBO['invert', 'average', 'round', 'clamp', 'abs']
    - Python dtype: str

# Output types
- result
    - The result parameter represents the output of a monolithic operation applied to the input image. It contains the image data converted after the specified operation is performed. This output is important because it provides the basis for any subsequent image analysis or processing steps.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class UnaryImageOp:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'op': (['invert', 'average', 'round', 'clamp', 'abs'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'op_image'
    CATEGORY = 'Masquerade Nodes'

    def op_image(self, image, op):
        image = tensor2rgb(image)
        if op == 'invert':
            return (1.0 - image,)
        elif op == 'average':
            mean = torch.mean(torch.mean(image, dim=2), dim=1)
            return (mean.unsqueeze(1).unsqueeze(2).repeat(1, image.shape[1], image.shape[2], 1),)
        elif op == 'round':
            return (torch.round(image),)
        elif op == 'clamp':
            return (torch.min(torch.max(image, torch.tensor(0.0)), torch.tensor(1.0)),)
        elif op == 'abs':
            return (torch.abs(image),)
```