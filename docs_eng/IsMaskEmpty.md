# Documentation
- Class name: IsMaskEmptyNode
- Category: util
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The IsmaskEmptyNode class is designed to assess the internal content of the mask load and determine whether it is entirely zero. This node plays a key role in image processing and machine learning workflows, with the importance of the presence of an empty mask. It contributes an abstract binary result to the decision-making process that can be used to trigger follow-up action or filter unnecessary data.

# Input types
## Required
- mask
    - The parameter'mask'is a mass that represents the mask to be assessed. It is essential for the operation of the node, because it directly affects whether the mask is considered empty. The mass should contain a number, with zero indicating an empty or non-important area.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- boolean_number
    - Output 'boolean_number'is a value for a boolean value, which indicates whether the input mask is empty. Value 1 means the mask is empty (all zero) and value 0 means the mask contains non-zero elements.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class IsMaskEmptyNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',)}}
    RETURN_TYPES = ['NUMBER']
    RETURN_NAMES = ['boolean_number']
    FUNCTION = 'main'
    CATEGORY = 'util'

    def main(self, mask):
        return (torch.all(mask == 0).int().item(),)
```