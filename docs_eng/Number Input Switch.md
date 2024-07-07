# Documentation
- Class name: WAS_Number_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `number_input_switch'is designed to process value input according to a Boolean condition. It provides a multifunctional approach to the processing of numerical data by skilfully demonstrating the ability of nodes to carry out the logical operation of conditions. Node functions are concentrated on their decision-making capacity, allowing for the operation of numbers in a controlled and predictable manner.

# Input types
## Required
- number_a
    - The parameter `number_a'is essential for the operation of the node, as it represents the first value input that the node will process. Its role is important because it determines the initial dataset of the node decision-making process.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
- number_b
    - The parameter `number_b'is another value input for the node. It is important to provide a different set of values that can be used at the node when the boolean conditions are not met.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]
## Optional
- boolean
    - The parameter `boolean'as a switch determines the behaviour of the node. It is essential to determine the input set of values to be processed by the node, thus affecting the output of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- output
    - The output of `number_input_switch'is a cluster that contains the original number, its floating point expression and integer form. This comprehensive output provides a multi-faceted view of the processed numerical data and meets various downstream needs.
    - Comfy dtype: COMBO[NUMBER, FLOAT, INT]
    - Python dtype: Tuple[Union[int, float], float, int]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number_a': ('NUMBER',), 'number_b': ('NUMBER',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    FUNCTION = 'number_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def number_input_switch(self, number_a, number_b, boolean=True):
        if boolean:
            return (number_a, float(number_a), int(number_a))
        else:
            return (number_b, float(number_b), int(number_b))
```