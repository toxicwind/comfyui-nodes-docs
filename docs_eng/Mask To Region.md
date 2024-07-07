# Documentation
- Class name: MaskToRegion
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The MaskToRegion node is designed to handle the given mask and to identify a rectangular area, which adapts to the mask under specified constraints. It intelligently adjusts the size of the border box to suit the mask, while maintaining the required attributes, such as vertical ratio, segregability or multipliers. The node plays a key role in applications that require accurate handling of the mask area, such as image partitioning or target detection.

# Input types
## Required
- mask
    - The'mask' parameter is essential because it defines the input mask from the derived area. It is the primary data source for node operations to produce the desired output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- padding
    - The 'pading' parameter allows for additional space around the mask, which may be critical in the application of buffer zones that need to be set aside around objects of interest.
    - Comfy dtype: INT
    - Python dtype: int
- constraints
    - The 'constraints' parameter is essential in determining how to adjust the size of the area. It determines whether the vertical ratio should be maintained, the exclusivability should be enforced, or the multiples of respect should be respected.
    - Comfy dtype: COMBO[keep_ratio, keep_ratio_divisible, multiple_of, ignore]
    - Python dtype: str
- constraint_x
    - When the 'constraint_x' parameter is used in conjunction with 'constraint_y', it helps to define the constraints of width and height adjustment to ensure that the output area meets the specific size requirements.
    - Comfy dtype: INT
    - Python dtype: int
- constraint_y
    - The 'constraint_y' parameter is similar to 'constraint_x', which helps to set the vertical restraints of the area and complements the horizontal constraints set by 'constraint_x'.
    - Comfy dtype: INT
    - Python dtype: int
- min_width
    - The `min_width' parameter ensures that the width of the result area is not lower than the specified minimum, which is essential to maintain the visibility of the objects included.
    - Comfy dtype: INT
    - Python dtype: int
- min_height
    - The'min_height' parameter is similar to'min_width', which ensures that the height of the area meets the minimum threshold and prevents objects from being overstretched in a vertical direction.
    - Comfy dtype: INT
    - Python dtype: int
- batch_behavior
    - The 'batch_behavior' parameter affects the treatment of the area in the batch, allowing for matching the size of all regions or ensuring a consistent vertical ratio.
    - Comfy dtype: COMBO[match_ratio, match_size]
    - Python dtype: str

# Output types
- region
    - The'region' output parameter represents the final rectangular area that contains the input mask after applying all specified constraints and adjustments. It is a key component of a downstream task that relies on precise regional positioning.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskToRegion:
    """
    Given a mask, returns a rectangular region that fits the mask with the given constraints
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('IMAGE',), 'padding': ('INT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'constraints': (['keep_ratio', 'keep_ratio_divisible', 'multiple_of', 'ignore'],), 'constraint_x': ('INT', {'default': 64, 'min': 2, 'max': VERY_BIG_SIZE, 'step': 1}), 'constraint_y': ('INT', {'default': 64, 'min': 2, 'max': VERY_BIG_SIZE, 'step': 1}), 'min_width': ('INT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'min_height': ('INT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'batch_behavior': (['match_ratio', 'match_size'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'get_region'
    CATEGORY = 'Masquerade Nodes'

    def get_region(self, mask, padding, constraints, constraint_x, constraint_y, min_width, min_height, batch_behavior):
        mask = tensor2mask(mask)
        mask_size = mask.size()
        mask_width = int(mask_size[2])
        mask_height = int(mask_size[1])
        is_empty = ~torch.gt(torch.max(torch.reshape(mask, [mask_size[0], mask_width * mask_height]), dim=1).values, 0.0)
        mask[is_empty, 0, 0] = 1.0
        boxes = masks_to_boxes(mask)
        mask[is_empty, 0, 0] = 0.0
        min_x = torch.max(boxes[:, 0] - padding, torch.tensor(0.0))
        min_y = torch.max(boxes[:, 1] - padding, torch.tensor(0.0))
        max_x = torch.min(boxes[:, 2] + padding, torch.tensor(mask_width))
        max_y = torch.min(boxes[:, 3] + padding, torch.tensor(mask_height))
        width = max_x - min_x
        height = max_y - min_y
        target_width = torch.max(width, torch.tensor(min_width))
        target_height = torch.max(height, torch.tensor(min_height))
        if constraints == 'keep_ratio':
            target_width = torch.max(target_width, target_height * constraint_x // constraint_y)
            target_height = torch.max(target_height, target_width * constraint_y // constraint_x)
        elif constraints == 'keep_ratio_divisible':
            max_factors = torch.min(constraint_x // target_width, constraint_y // target_height)
            max_factor = int(torch.max(max_factors).item())
            for i in range(1, max_factor + 1):
                divisible = constraint_x % i == 0 and constraint_y % i == 0
                if divisible:
                    big_enough = ~torch.lt(target_width, constraint_x // i) * ~torch.lt(target_height, constraint_y // i)
                    target_width[big_enough] = constraint_x // i
                    target_height[big_enough] = constraint_y // i
        elif constraints == 'multiple_of':
            target_width[torch.gt(target_width % constraint_x, 0)] = (target_width // constraint_x + 1) * constraint_x
            target_height[torch.gt(target_height % constraint_y, 0)] = (target_height // constraint_y + 1) * constraint_y
        if batch_behavior == 'match_size':
            target_width[:] = torch.max(target_width)
            target_height[:] = torch.max(target_height)
        elif batch_behavior == 'match_ratio':
            ratios = torch.abs(target_width / target_height - 1)
            ratios[is_empty] = 10000
            match_ratio = torch.min(ratios, dim=0).indices.item()
            target_width = torch.max(target_width, target_height * target_width[match_ratio] // target_height[match_ratio])
            target_height = torch.max(target_height, target_width * target_height[match_ratio] // target_width[match_ratio])
        missing = target_width - width
        min_x = min_x - missing // 2
        max_x = max_x + (missing - missing // 2)
        missing = target_height - height
        min_y = min_y - missing // 2
        max_y = max_y + (missing - missing // 2)
        bad = torch.lt(min_x, 0)
        max_x[bad] -= min_x[bad]
        min_x[bad] = 0
        bad = torch.lt(min_y, 0)
        max_y[bad] -= min_y[bad]
        min_y[bad] = 0
        bad = torch.gt(max_x, mask_width)
        min_x[bad] -= max_x[bad] - mask_width
        max_x[bad] = mask_width
        bad = torch.gt(max_y, mask_height)
        min_y[bad] -= max_y[bad] - mask_height
        max_y[bad] = mask_height
        region = torch.zeros((mask_size[0], mask_height, mask_width))
        for i in range(0, mask_size[0]):
            if not is_empty[i]:
                ymin = int(min_y[i].item())
                ymax = int(max_y[i].item())
                xmin = int(min_x[i].item())
                xmax = int(max_x[i].item())
                region[i, ymin:ymax + 1, xmin:xmax + 1] = 1
        return (region,)
```