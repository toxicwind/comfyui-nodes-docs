# Documentation
- Class name: WAS_Seed
- Category: WAS Suite/Number
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Seed node is designed to generate and operate numerical seeds that are essential to initialize random number generators or to ensure repeatability during random processes. It provides a fundamental role in numerical operations, where seed values are essential to control randomity.

# Input types
## Required
- seed
    - The `seed' parameter is essential to the operation of the node because it determines the starting point for the generation of a series of numbers. It ensures the predictability and repeatability of the random number generation process, which is important in modelling and probability models.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- seed
    - The `seed' output represents the original value seed provided to the node, which is an essential part of the follow-up operation that relies on random numbers.
    - Comfy dtype: INT
    - Python dtype: int
- number
    - The `number' output is in the form of a decimal of the seed, which can be used in the calculation of the need for an integer value and expands the application of the node in various mathematical scenarios.
    - Comfy dtype: FLOAT
    - Python dtype: float
- float
    - `float' output is the conversion of seed values to floating points, which is essential for the operation of decimals, such as scientific computing and statistical analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int
    - The `int' output provides the integer form of the seed value, which applies to operations that accept only integer input to ensure compatibility with a wide range of numeric algorithms and applications.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Seed:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('SEED', 'NUMBER', 'FLOAT', 'INT')
    RETURN_NAMES = ('seed', 'number', 'float', 'int')
    FUNCTION = 'seed'
    CATEGORY = 'WAS Suite/Number'

    def seed(self, seed):
        return ({'seed': seed}, seed, float(seed), int(seed))
```