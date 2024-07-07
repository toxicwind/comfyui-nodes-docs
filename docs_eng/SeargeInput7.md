# Documentation
- Class name: SeargeInput7
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

This node, as a multi-routine repeater for input parameters, simplifys the process of integrating various settings into the system. It ensures that parameters are correctly routed and managed so that the whole operation does not require manual intervention.

# Input types
## Required
- lora_strength
    - Lora intensity is a key parameter that affects the system’s sensitivity to input signals. It is essential to adjust responsiveness and ensure that desired output is achieved.
    - Comfy dtype: FLOAT
    - Python dtype: float
- operation_mode
    - The mode of operation determines the general working state of the system, influencing its behaviour and the way in which it is processed. This is essential to align the functionality of the system with the expected usage.
    - Comfy dtype: ENUM
    - Python dtype: str
- prompt_style
    - The reminder style shapes the way the system presents and interacts with its users, ensuring that input is sought and processed in a manner consistent with user expectations and system design.
    - Comfy dtype: ENUM
    - Python dtype: str
## Optional
- inputs
    - Input is an optional parameter that allows additional customization and fine-tuning of the system. It provides a range of options to further optimize operations according to specific requirements.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]

# Output types
- inputs
    - The output represents an integrated and processed set of parameters that are essential for the subsequent operational phase of the system. It encapsulates the configuration of the system and ensures the maintenance of the intended functionality.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput7:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'lora_strength': ('FLOAT', {'default': 0.2, 'min': -10.0, 'max': 10.0, 'step': 0.05}), 'operation_mode': (SeargeParameterProcessor.OPERATION_MODE, {'default': SeargeParameterProcessor.OPERATION_MODE[0]}), 'prompt_style': (SeargeParameterProcessor.PROMPT_STYLE, {'default': SeargeParameterProcessor.PROMPT_STYLE[0]})}, 'optional': {'inputs': ('PARAMETER_INPUTS',)}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, lora_strength, operation_mode, prompt_style, inputs=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['lora_strength'] = lora_strength
        parameters['operation_mode'] = operation_mode
        parameters['prompt_style'] = prompt_style
        return (parameters,)
```