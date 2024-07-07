# Documentation
- Class name: MaskComposite
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The MaskComposite node is designed to perform a variety of logical and arithmetic calculations for two mask loads. It plays a key role in image-processing tasks, particularly in the area of facial resolution, where it combines masks to fine-tune the segmenting of facial features. The node operates on an element-by-element basis, ensuring that the output mask is the result of the specified operation applied to each corresponding element in the input mask.

# Input types
## Required
- destination
    - The design parameter is a volume that represents the initial mask and the operation will be applied to the mask. It is essential for the implementation of the node, as it determines the base mask that will be modified according to the specified operation.
    - Comfy dtype: "MASK"
    - Python dtype: torch.Tensor
- source
    - The source parameter is another volume that will be used in conjunction with the target mass to perform the specified operation. It is essential because it provides secondary input that will interact with the target mask to produce the final mask result.
    - Comfy dtype: "MASK"
    - Python dtype: torch.Tensor
- operation
    - The operation parameter indicates the type of element-by-element operation that will be performed between the target and the source mass. It is a key determinant of how to calculate the final mask, allowing various forms of masking to be performed.
    - Comfy dtype: COMBO["multiply", "add", "subtract", "and", "or", "xor"]
    - Python dtype: str

# Output types
- mask_result
    - The mask_result output parameter is the amount of tension that you get when you apply the specified operation to input the target and source volume. It represents the mask that was eventually assembled after the operation was executed.
    - Comfy dtype: "MASK"
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskComposite:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'destination': ('MASK', {}), 'source': ('MASK', {}), 'operation': (['multiply', 'add', 'subtract', 'and', 'or', 'xor'],)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, destination: Tensor, source: Tensor, operation: str):
        mask_result = destination
        if operation == 'multiply':
            mask_result = mask_result * source
        if operation == 'add':
            mask_result = mask_result + source
        if operation == 'subtract':
            mask_result = mask_result - source
        if operation == 'and':
            mask_result = mask_result & source
        if operation == 'or':
            mask_result = mask_result | source
        if operation == 'xor':
            mask_result = mask_result ^ source
        return (mask_result,)
```