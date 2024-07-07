# Documentation
- Class name: SeparateMaskComponents
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The node is designed to separate the individual mask into a continuous component. It identifies the only segment of the mask by applying a morphological operation to the mask. The node not only returns the separated mask, but also provides a map that can be used in downstream processes to link the components to the location of their original batches.

# Input types
## Required
- mask
    - Enter the mask is the key parameter for the node because it represents the initial data from which the continuous component is to be separated. The mask structure directly affects the operation of the node and the result part.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- mask
    - The output is a series of separate masks, each of which corresponds to a unique continuous component identified in the mask. These masks are essential for further analysis or processing in batch processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_mappings
    - This output provides a map that links each separated mask to its corresponding position in the original batch. It is an important tool for maintaining the integrity of data relationships throughout the processing process.
    - Comfy dtype: INT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class SeparateMaskComponents:
    """
    Separates a mask into multiple contiguous components. Returns the individual masks created as well as a MASK_MAPPING which can be used in other nodes when dealing with batches.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'MASK_MAPPING')
    RETURN_NAMES = ('mask', 'mask_mappings')
    FUNCTION = 'separate'
    CATEGORY = 'Masquerade Nodes'

    def separate(self, mask):
        mask = tensor2mask(mask)
        thresholded = torch.gt(mask, 0).unsqueeze(1)
        (B, H, W) = mask.shape
        components = torch.arange(B * H * W, device=mask.device, dtype=mask.dtype).reshape(B, 1, H, W) + 1
        components[~thresholded] = 0
        while True:
            previous_components = components
            components = torch.nn.functional.max_pool2d(components, kernel_size=3, stride=1, padding=1)
            components[~thresholded] = 0
            if torch.equal(previous_components, components):
                break
        components = components.reshape(B, H, W)
        segments = torch.unique(components)
        result = torch.zeros([len(segments) - 1, H, W])
        index = 0
        mapping = torch.zeros([len(segments) - 1], device=mask.device, dtype=torch.int)
        for i in range(len(segments)):
            segment = segments[i].item()
            if segment == 0:
                continue
            image_index = int((segment - 1) // (H * W))
            segment_mask = components[image_index, :, :] == segment
            result[index][segment_mask] = mask[image_index][segment_mask]
            mapping[index] = image_index
            index += 1
        return (result, mapping)
```