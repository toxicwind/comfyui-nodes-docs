# Documentation
- Class name: InvertMask
- Category: segment_anything
- Output node: False
- Repo Ref: https://github.com/storyicon/comfyui_segment_anything

The InvertMask node is designed to reverse the value of the double mask. It plays a key role in various image split tasks, where it is necessary to reverse the mask to highlight different areas of interest. The node functions effectively by subtracting 1 from the input mask, turning the polarity of the mask.

# Input types
## Required
- mask
    - The `mask' parameter is a two-value mask, which the node reverses. It is essential for the operation of the node, because it directly determines the output. The reverse mask is used to identify or isolate certain areas in the image, which is essential for the purpose of partitioning.
    - Comfy dtype: np.ndarray
    - Python dtype: numpy.ndarray

# Output types
- MASK
    - The `MASK' output is an inverted version of a mask. It is important because it represents the result of node operations and provides a binary mask with inverted values that can be used to split further processing or analysis in the workflow.
    - Comfy dtype: np.ndarray
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class InvertMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',)}}
    CATEGORY = 'segment_anything'
    FUNCTION = 'main'
    RETURN_TYPES = ('MASK',)

    def main(self, mask):
        out = 1.0 - mask
        return (out,)
```