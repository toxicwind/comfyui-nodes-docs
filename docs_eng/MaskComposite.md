# Documentation
- Class name: MaskComposite
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The MaskComposite node is designed to perform a variety of operations for mask images, allowing the combination of source and target masking to be specified. It plays a key role in image-processing workflows that require masking, for example, in computer visual or graphic design applications.

# Input types
## Required
- destination
    - The target parameter is the base mask that will be modified through the operation. It is essential because it determines the initial state of the mask before applying any modification.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- source
    - The source parameter indicates the mask that you want to combine with the target mask. Its role is critical because it contributes to the end result of the mask operation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- x
    - The x parameter specifies the horizontal position of the source mask relative to the target mask. It is important because it determines the location of the source in the target mask.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y parameter defines the vertical position of the source mask vis-à-vis the target mask. It is important to determine the vertical position of the source in the target mask.
    - Comfy dtype: INT
    - Python dtype: int
- operation
    - Operational parameters indicate the type of combination to be executed between the source mask and the target mask. It is essential because it defines the logic of the mask merge.
    - Comfy dtype: COMBO['multiply', 'add', 'subtract', 'and', 'or', 'xor']
    - Python dtype: str

# Output types
- output
    - Output parameter is the result of a masking operation. It contains the final state of application of all converted masks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MaskComposite:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'destination': ('MASK',), 'source': ('MASK',), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'operation': (['multiply', 'add', 'subtract', 'and', 'or', 'xor'],)}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'combine'

    def combine(self, destination, source, x, y, operation):
        output = destination.reshape((-1, destination.shape[-2], destination.shape[-1])).clone()
        source = source.reshape((-1, source.shape[-2], source.shape[-1]))
        (left, top) = (x, y)
        (right, bottom) = (min(left + source.shape[-1], destination.shape[-1]), min(top + source.shape[-2], destination.shape[-2]))
        (visible_width, visible_height) = (right - left, bottom - top)
        source_portion = source[:, :visible_height, :visible_width]
        destination_portion = destination[:, top:bottom, left:right]
        if operation == 'multiply':
            output[:, top:bottom, left:right] = destination_portion * source_portion
        elif operation == 'add':
            output[:, top:bottom, left:right] = destination_portion + source_portion
        elif operation == 'subtract':
            output[:, top:bottom, left:right] = destination_portion - source_portion
        elif operation == 'and':
            output[:, top:bottom, left:right] = torch.bitwise_and(destination_portion.round().bool(), source_portion.round().bool()).float()
        elif operation == 'or':
            output[:, top:bottom, left:right] = torch.bitwise_or(destination_portion.round().bool(), source_portion.round().bool()).float()
        elif operation == 'xor':
            output[:, top:bottom, left:right] = torch.bitwise_xor(destination_portion.round().bool(), source_portion.round().bool()).float()
        output = torch.clamp(output, 0.0, 1.0)
        return (output,)
```