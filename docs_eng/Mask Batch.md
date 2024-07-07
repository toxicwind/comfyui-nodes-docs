# Documentation
- Class name: WAS_Mask_Batch
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Batch node is designed to process multiple mask inputs efficiently and in bulk. It ensures that all input masks match the uniform dimensions and stacks them into individual batches for further processing. The node plays a key role in the consistent mask size data needed to prepare downstream tasks.

# Input types
## Optional
- masks_a
    - The'masks_a' parameter is an optional input that allows users to provide a set of masks for processing. It is essential for the operation of nodes, as it directly affects the data that will be processed and processed in batches.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, None]
- masks_b
    - The'masks_b' parameter is similar to'masks_a', providing another optional mask pool to be included in batch processing.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, None]
- masks_c
    - The'masks_c' parameter is another optional input for additional masks, which further enhances the flexibility of nodes in processing various mask inputs.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, None]
- masks_d
    - The'masks_d' parameter provides a set of additional masks for nodes to be processed to ensure that nodes can adapt to a wide range of mask input.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, None]

# Output types
- masks
    - The'masks' output is a batch load that contains all of the processed masks. It is important because it represents the main output of the node and is prepared for follow-up operations.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'optional': {'masks_a': ('MASK',), 'masks_b': ('MASK',), 'masks_c': ('MASK',), 'masks_d': ('MASK',)}}
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('masks',)
    FUNCTION = 'mask_batch'
    CATEGORY = 'WAS Suite/Image/Masking'

    def _check_mask_dimensions(self, tensors, names):
        dimensions = [tensor.shape[1:] for tensor in tensors]
        if len(set(dimensions)) > 1:
            mismatched_indices = [i for (i, dim) in enumerate(dimensions) if dim != dimensions[0]]
            mismatched_masks = [names[i] for i in mismatched_indices]
            raise ValueError(f'WAS Mask Batch Warning: Input mask dimensions do not match for masks: {mismatched_masks}')

    def mask_batch(self, **kwargs):
        batched_tensors = [kwargs[key] for key in kwargs if kwargs[key] is not None]
        mask_names = [key for key in kwargs if kwargs[key] is not None]
        if not batched_tensors:
            raise ValueError('At least one input mask must be provided.')
        self._check_mask_dimensions(batched_tensors, mask_names)
        batched_tensors = torch.stack(batched_tensors, dim=0)
        batched_tensors = batched_tensors.unsqueeze(1)
        return (batched_tensors,)
```