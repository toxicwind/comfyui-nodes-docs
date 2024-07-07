# Documentation
- Class name: CR_Value
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Value node is designed to provide a multifunctional interface for converting input values to different data types. It emphasizes the flexibility and practicality of data operations, allowing users to extract values and text expressions from a single input, thereby enhancing the adaptability of nodes in various workflows.

# Input types
## Required
- value
    - The `value' parameter is essential because it is the main input into the node conversion process. It is the source of derivative floating points and integer expressions, making them essential elements in node operations.
    - Comfy dtype: FLOAT
    - Python dtype: Union[float, str]

# Output types
- FLOAT
    - The `FLOAT' output provides an indication of the floating point of the input value, which is very useful for numerical calculations and analysis that require precise small values.
    - Comfy dtype: FLOAT
    - Python dtype: float
- INT
    - The `INT' output provides an integer form of input value, applicable to cases where only an integer is required, thus simplifying calculation and reducing complexity.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The `show_help' output provides a URL link to the node document, which is very useful for users seeking additional guidance or information about the node function.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Value:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('FLOAT', {'default': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT', 'STRING')
    RETURN_NAMES = ('FLOAT', 'INT', 'show_help')
    CATEGORY = icons.get('Comfyroll/Utils/Other')
    FUNCTION = 'get_value'

    def get_value(self, value):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-value'
        return (float(value), int(value), show_help)
```