# Documentation
- Class name: MultivalScaledMaskNode
- Category: Animate Diff 🎭🅐🅓/multival
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The MultiivalScaled MaskNode class is designed to convert it by scaling up the given mask loads within the specified range. It uses linear conversions or reclassifications according to the selected zoom type to ensure that the output mask is suitable for further processing in animation or visualization applications.

# Input types
## Required
- min_float_val
    - The minimum floating point value parameter defines the lower limit of the mass scale range of the mask. It plays a vital role in setting the zoom ratio of the mask to ensure that the minimum value of the zoom is as specified.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_float_val
    - The maximum floating point value parameter sets a cap on the zoom in the mask. It is essential to determine the scale of the mask and to ensure that the maximum value after the zoom is consistent with the maximum expected.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mask
    - The mask parameter is a volume that will be scaled according to the specified minimum and maximum floating point value. It is the core element of the node operation, because the zoom is applied directly to this volume to achieve the desired multi-value effect.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- scaling
    - Zoom parameters determine the type of zoom that you want to apply to the mask load. It can be absolute or relative, and it affects how the mask value is adjusted within the specified range.
    - Comfy dtype: ScaleType.LIST
    - Python dtype: str

# Output types
- multival
    - The MultiivalScaled MaskNode output is a multi-value mass that represents a scaled mask. It is important because it is a direct result of node operations that can be used for subsequent animation or visualization tasks.
    - Comfy dtype: MULTIVAL
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MultivalScaledMaskNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'min_float_val': ('FLOAT', {'default': 0.0, 'min': 0.0, 'step': 0.001}), 'max_float_val': ('FLOAT', {'default': 1.0, 'min': 0.0, 'step': 0.001}), 'mask': ('MASK',)}, 'optional': {'scaling': (ScaleType.LIST,)}}
    RETURN_TYPES = ('MULTIVAL',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/multival'
    FUNCTION = 'create_multival'

    def create_multival(self, min_float_val: float, max_float_val: float, mask: Tensor, scaling: str=ScaleType.ABSOLUTE):
        if isinstance(min_float_val, Iterable):
            raise ValueError(f'min_float_val must be type float (no lists allowed here), not {type(min_float_val).__name__}.')
        if isinstance(max_float_val, Iterable):
            raise ValueError(f'max_float_val must be type float (no lists allowed here), not {type(max_float_val).__name__}.')
        if scaling == ScaleType.ABSOLUTE:
            mask = linear_conversion(mask.clone(), new_min=min_float_val, new_max=max_float_val)
        elif scaling == ScaleType.RELATIVE:
            mask = normalize_min_max(mask.clone(), new_min=min_float_val, new_max=max_float_val)
        else:
            raise ValueError(f"scaling '{scaling}' not recognized.")
        return MultivalDynamicNode.create_multival(self, mask_optional=mask)
```