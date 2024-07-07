# Documentation
- Class name: FloatSlider
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The floatSlider node is designed to regularize the given number to a specified range, ensuring that it falls between the minimum and the maximum. It zooms the number to a standard scale, providing a single value that can be used to calculate the context in which the relative location is essential.

# Input types
## Required
- number
    - The parameter 'number' indicates the value to be normalized within the specified range. It is vital because it directly influences the output of the node and determines the position of the number to be normalized at the standard scale.
    - Comfy dtype: FLOAT
    - Python dtype: float
- min_value
    - The parameter'min_value' defines the lower limit of the range of unicoded numbers. It plays an important role in ensuring that output values are subject to desired limits.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_value
    - Parameter'max_value'sets a ceiling for the scope of the uniformity. It is critical in scaling the input numbers to ensure that they do not exceed the specified maximum value.
    - Comfy dtype: FLOAT
    - Python dtype: float
- step
    - The parameter'step' is used to control the particle size of the number to be normalized. It affects the manner in which the number is adjusted in the range and affects the accuracy of the value to be normalized.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- scaled_number
    - Output'scaled_number'means that the input number is resized to fit the specified range. It is important because it provides a standard measure that can be used for further analysis or processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class FloatSlider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'number': ('FLOAT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'step': 0.001, 'display': 'slider'}), 'min_value': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.001, 'display': 'number'}), 'max_value': ('FLOAT', {'default': 1, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.001, 'display': 'number'}), 'step': ('FLOAT', {'default': 0.001, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.001, 'display': 'number'})}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, number, min_value, max_value, step):
        if number < min_value:
            number = min_value
        elif number > max_value:
            number = max_value
        scaled_number = (number - min_value) / (max_value - min_value)
        return (scaled_number,)
```