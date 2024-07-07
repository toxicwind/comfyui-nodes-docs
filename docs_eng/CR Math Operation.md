# Documentation
- Class name: CR_MathOperation
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_MathOperation node is designed to perform a variety of mathematical calculations for given input values. It abstractes the complexity of mathematical functions and allows users to easily apply sine, cosine and logarithm calculations. The node emphasizes simplicity and ensures easy access to mathematical conversions without going into the bottom algorithm details.

# Input types
## Required
- a
    - The parameter 'a'indicates that the input value of the mathematical operation will be performed. It is the core of the node function because it directly affects the result of the operation. The selection of this value can significantly influence the outcome, making it a key component of the node execution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- operation
    - The parameter 'option 'indicators will be applied to the mathematical function of the input value. It is vital because it determines the type of change that will occur. Selecting an operation is key to achieving the expected outcome of the node execution.
    - Comfy dtype: COMBO['sin', 'cos', 'tan', 'sqrt', 'exp', 'log', 'neg', 'abs']
    - Python dtype: str
- decimal_places
    - The parameter 'decimal_places' specifies that the result will be rounded to the decimal places. It plays a key role in determining the output accuracy by allowing the user to control the level of detail of the final result.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- a
    - Output 'a'provides the value of the mathematical results rounded to the specified decimal places. It is important because it represents the end result of node processing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Output'show_help' provides a URL link to the node document page, providing additional information and guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_MathOperation:

    @classmethod
    def INPUT_TYPES(cls):
        operations = ['sin', 'cos', 'tan', 'sqrt', 'exp', 'log', 'neg', 'abs']
        return {'required': {'a': ('FLOAT', {'default': 1.0}), 'operation': (operations,), 'decimal_places': ('INT', {'default': 2, 'min': 0, 'max': 10})}}
    RETURN_TYPES = ('FLOAT', 'STRING')
    RETURN_NAMES = ('a', 'show_help')
    FUNCTION = 'do_math'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def do_math(self, a, operation, decimal_places):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-math-operation'
        if operation == 'sin':
            result = math.sin(a)
        elif operation == 'cos':
            result = math.cos(a)
        elif operation == 'tan':
            result = math.cos(a)
        elif operation == 'sqrt':
            result = math.sqrt(a)
        elif operation == 'exp':
            result = math.exp(a)
        elif operation == 'log':
            result = math.log(a)
        elif operation == 'neg':
            result = -a
        elif operation == 'abs':
            result = abs(a)
        else:
            raise ValueError('CR Math Operation: Unsupported operation.')
        result = round(result, decimal_places)
        return (result, show_help)
```