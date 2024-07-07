# Documentation
- Class name: ImpactLogicalOperators
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of ImpactLogicalOperators nodes is designed to perform logical calculations for two booleans. It represents the basic concept of logical reasoning in the abstract, in which nodes process input to produce individual boolean output according to the specified operators. The node plays a key role in the decision-making process, and the outcome depends on the logical relationship between the two conditions.

# Input types
## Required
- operator
    - The `operator' parameter determines the type of logical operation to be performed. It is essential because it determines the logical relationship between the node and the two boolean input, thus affecting the execution and final output of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- bool_a
    - The 'bool_a' parameter represents the first boolean input for logical operations. It is important because it constitutes half of the logical comparison or connection that node is designed to evaluate.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- bool_b
    - The `bool_b' parameter is the second input for the logical operation. It is essential because it supplements the first boolean input `bool_a' to complete the logical expression for node processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - The `redult' parameter is the result of a boolean operation performed by a node. It represents the final output obtained after assessing the logical relationship between the two input values.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactLogicalOperators:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'operator': (['and', 'or', 'xor'],), 'bool_a': ('BOOLEAN', {'forceInput': True}), 'bool_b': ('BOOLEAN', {'forceInput': True})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = ('BOOLEAN',)

    def doit(self, operator, bool_a, bool_b):
        if operator == 'and':
            return (bool_a and bool_b,)
        elif operator == 'or':
            return (bool_a or bool_b,)
        else:
            return (bool_a != bool_b,)
```