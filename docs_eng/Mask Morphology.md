# Documentation
- Class name: MaskMorphologyNode
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The MaskMorphologyNode class is designed to perform morphological operations for image masking. It provides the functions of inflation, corrosion, calculation and closure, which are essential for image processing tasks (e.g. noise and feature enhancement).

# Input types
## Required
- image
    - The image parameter is a volume, which indicates an input image mask. It is essential for the operation of the node, as morphological changes are applied directly to this image data.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- distance
    - Distance parameters determine the range of morphological operations, such as the size of the core used for inflation or corrosion. It significantly influences the outcome of node treatment.
    - Comfy dtype: INT
    - Python dtype: int
- op
    - The operating parameters specify the type of morphological operation that you want to perform, which can be inflated, corroded, run-off or shut-down. The direct effect of this option applies to the conversion of image masks.
    - Comfy dtype: COMBO['dilate', 'erode', 'open', 'close']
    - Python dtype: str

# Output types
- output_image
    - The output image is the result of the application of the selected morphological operation to the input of the image. It is a conversion version of the original image mask, reflecting the effects of the selected operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MaskMorphologyNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'distance': ('INT', {'default': 5, 'min': 0, 'max': 128, 'step': 1}), 'op': (['dilate', 'erode', 'open', 'close'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'morph'
    CATEGORY = 'Masquerade Nodes'

    def morph(self, image, distance, op):
        image = tensor2mask(image)
        if op == 'dilate':
            image = self.dilate(image, distance)
        elif op == 'erode':
            image = self.erode(image, distance)
        elif op == 'open':
            image = self.erode(image, distance)
            image = self.dilate(image, distance)
        elif op == 'close':
            image = self.dilate(image, distance)
            image = self.erode(image, distance)
        return (image,)

    def erode(self, image, distance):
        return 1.0 - self.dilate(1.0 - image, distance)

    def dilate(self, image, distance):
        kernel_size = 1 + distance * 2
        image = image.unsqueeze(1)
        out = torchfn.max_pool2d(image, kernel_size=kernel_size, stride=1, padding=kernel_size // 2).squeeze(1)
        return out
```