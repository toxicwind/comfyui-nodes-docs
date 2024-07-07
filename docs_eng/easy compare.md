# Documentation
- Class name: Compare
- Category: EasyUse/Logic/Math
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

Compare node facilitates the assessment of the logical comparison between the two inputs and provides a direct method of determining the relationship between the values. It is designed to support various comparisons and provides a flexible and intuitive way of integrating the logic of conditions into the workflow. Through the abstract comparison process, this node enhances the ability to make decisions based on data attributes and helps to build more dynamic and responsive systems.

# Input types
## Required
- a
    - The parameter 'a' represents the first number of operations in a comparison operation. It is the core of the node function, because it sets the baseline value for comparison with the second number of operations. The significance of the parameter lies in its role in determining the results of the logical comparison.
    - Comfy dtype: *
    - Python dtype: Any
- b
    - The parameter 'b' is the second number of operations used to compare. Its significance derives from its comparison with the first number of operations, and it is this parameter that is combined with the comparison function that determines the results of the comparison.
    - Comfy dtype: *
    - Python dtype: Any
- comparison
    - The parameter 'comparison' is a logical exercise to define how to compare two operations. It is vital because it determines the nature of the assessment and directly affects the results of the comparison.
    - Comfy dtype: COMBO[compare_functions]
    - Python dtype: str

# Output types
- boolean
    - The output 'boolean' represents the result of a logical comparison that provides a binary result reflecting the relationship between the two input operations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Compare:

    @classmethod
    def INPUT_TYPES(s):
        s.compare_functions = list(COMPARE_FUNCTIONS.keys())
        return {'required': {'a': (AlwaysEqualProxy('*'), {'default': 0}), 'b': (AlwaysEqualProxy('*'), {'default': 0}), 'comparison': (s.compare_functions, {'default': 'a == b'})}}
    RETURN_TYPES = ('BOOLEAN',)
    RETURN_NAMES = ('boolean',)
    FUNCTION = 'compare'
    CATEGORY = 'EasyUse/Logic/Math'

    def compare(self, a, b, comparison):
        return (COMPARE_FUNCTIONS[comparison](a, b),)
```