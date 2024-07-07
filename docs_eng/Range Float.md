# Documentation
- Class name: RangeFloat
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The RangeFloat node is designed to create a series of floating points within a specified range. It generates a list of numbers by a given step length from a starting point to an end point, and then selects a number from this list according to the seed value. This node is particularly useful in situations where there is a need to control digital randomization, for example in simulations or data processing tasks.

# Input types
## Required
- start
    - The parameter'start' defines the beginning of the range in which the number is generated. It is vital because it sets the initial point of the sequence and determines the direction of the range (whether increased or reduced). This parameter directly affects the overall behaviour of the output numbers and nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end
    - The parameter 'end' specifies the end of the range. It is vital because it determines the final value in the sequence that produces the number. The value 'end' is used in conjunction with the'start' and'step' parameters and determines the total number of numbers generated in the range.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- step
    - The parameter'step' determines the increment between each successive number in the generation sequence. It is important because it controls the density of the range number. A smaller step produces a more fine particle size output, while a larger step leads to a more rough distribution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The parameter'seed' is used to introduce controlled random elements when selecting numbers from the generated list. It is important because it ensures that the selection process is replicable and can be adjusted to obtain different results without changing the bottom range.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- selected_number
    - Output'selected_number' represents the number of floating points selected from the sequence generated. It is important because it is the main result of node operations and can be used for further processing or analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- representation
    - The output'representation' provides a string expression of the selected number, which is very useful for recording, displaying or requiring a text format.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class RangeFloat:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start': ('FLOAT', {'default': 0, 'min': 0, 'step': 0.0001, 'max': 18446744073709551615}), 'end': ('FLOAT', {'default': 0, 'min': 0, 'step': 0.0001, 'max': 18446744073709551615}), 'step': ('FLOAT', {'default': 0, 'min': 0, 'step': 0.0001, 'max': 18446744073709551615}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('FLOAT', 'STRING')
    FUNCTION = 'generate'
    CATEGORY = 'Mikey/Utils'

    def generate(self, start, end, step, seed):
        range_ = np.arange(start, end, step)
        list_of_numbers = list(range_)
        offset = seed % len(list_of_numbers)
        return (list_of_numbers[offset], f'{list_of_numbers[offset]}')
```