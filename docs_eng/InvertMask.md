# Documentation
- Class name: InvertMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `invert'method of the Invertmask node is designed to perform a simple but vital operation in image processing. It reverses the mask input to effectively transfer pixel values from 0 to 1 and vice versa, which is usually necessary for certain types of image operation or enhancement tasks. This node plays a key role in changing the visual expression of the mask, thus providing different perspectives or methods for subsequent analysis or conversion.

# Input types
## Required
- mask
    - The parameter'mask' is the input of the `invert'method, which is essential for the operation of the node. It means the original mask that needs to be reversed. The reverse process is fundamental because it can significantly change the context and application of the mask in the downstream task.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- out
    - The output of the invert method is a new mask, which is the reverse of the input mask. This output is important because it represents the conversion state of the original mask and is prepared for subsequent image processing steps.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class InvertMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',)}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'invert'

    def invert(self, mask):
        out = 1.0 - mask
        return (out,)
```