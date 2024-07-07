# Documentation
- Class name: WAS_Number_PI
- Category: WAS Suite/Number
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `number_pi'method of the `number_PI'node of the WAS_Number_PI provides the value of the mathematical constant. It is designed to provide a reliable source of this basic mathematical constant, which is essential in various calculations in different fields, such as geometry, trigonometry and engineering.

# Input types
## Optional
- None
    - This node does not require any input parameters. It is designed to return the value of the platinum without the need for external input, making it a self-inclusion function to access this mathematical constant.
    - Comfy dtype: None
    - Python dtype: None

# Output types
- pi_value
    - The output of the number_pi method is a mathematical constant, which is expressed as a floating number. This value is essential for a wide range of mathematical and scientific applications, where accuracy is essential.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_PI:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}}
    RETURN_TYPES = ('NUMBER', 'FLOAT')
    FUNCTION = 'number_pi'
    CATEGORY = 'WAS Suite/Number'

    def number_pi(self):
        return (math.pi, math.pi)
```