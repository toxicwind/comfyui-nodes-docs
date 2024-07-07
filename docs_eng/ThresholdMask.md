# Documentation
- Class name: ThresholdMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Thresholdmask node is designed to convert images into binary masks based on specified thresholds. It plays a key role in the image split task by identifying which pixels are interested and which are not. The node streamlines the complexity of images by applying binary classification, thus facilitating downstream processing and analysis.

# Input types
## Required
- mask
    - The `mask' parameter is an input image that requires a threshold processing. It is essential for the operation of the node, as it directly affects the quality and accuracy of the output mask. The value of the parameter determines which pixels are included in the final mask based on the threshold values provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- value
    - The `value' parameter sets a threshold for mask conversion. It is very important because it determines the cut-off point for pixels contained in the mask. Higher values will lead to a more conservative mask with fewer pixels, while lower values will contain more pixels.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- mask
    - Output `mask' is the binary expression of the input image, where pixels are classified as objects or objects, based on thresholds. This binary mask is essential for applications such as object detection and partition in the image processing workflow.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ThresholdMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'value': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'image_to_mask'

    def image_to_mask(self, mask, value):
        mask = (mask > value).float()
        return (mask,)
```