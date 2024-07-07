# Documentation
- Class name: SeargeOutput7
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node serves as an interface for data recovery, separating input data into different streams for further processing. It aims to enhance workflows by organizing and prioritizing data streams to ensure that specific data attributes receive the appropriate attention they need.

# Input types
## Required
- parameters
    - This parameter is essential because it contains the data that nodes are to be recycled and allows for the separation of different properties according to the predefined structure.
    - Comfy dtype: COMBO[{"type": "dict", "schema": {"lora_strength": "float"}}]
    - Python dtype: Dict[str, float]

# Output types
- parameters
    - The output retains the original structure of the input data to ensure that the deactivated data are organized and easily accessible for follow-up.
    - Comfy dtype: dict
    - Python dtype: Dict[str, Any]
- lora_strength
    - This output represents the recovery of specific properties from the input data and highlights its importance in the data processing workflow.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput7:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'FLOAT')
    RETURN_NAMES = ('parameters', 'lora_strength')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        lora_strength = parameters['lora_strength']
        return (parameters, lora_strength)
```