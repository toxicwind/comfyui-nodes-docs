# Documentation
- Class name: SeargeLoras
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to process and manage lora signals and to integrate their strength and configuration into structured data formats.

# Input types
## Required
- lora_1
    - The first lora parameter is essential to define the initial signal in the lora counter, which affects the overall structure and output of the node.
    - Comfy dtype: LORAS_WITH_NONE()
    - Python dtype: Union[str, None]
- lora_1_strength
    - The strength of the first lora signal is very important because it determines the influence of the signal in the warehouse and contributes to the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_2
    - The second lora parameter further refined the signal pad, adding additional complexity and nuances to the operation of the nodes.
    - Comfy dtype: LORAS_WITH_NONE()
    - Python dtype: Union[str, None]
- lora_2_strength
    - The strength of the second lora signal is essential because it adjusts the relative weight of the signal to affect the final disposition of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_3
    - The third lora parameter contributes to the diversity of signal pads and enhances the adaptive and multifunctional nature of nodes.
    - Comfy dtype: LORAS_WITH_NONE()
    - Python dtype: Union[str, None]
- lora_3_strength
    - The strength of the third lora signal is important because it fine-tunes its contribution to the pad and fine-tunes the output of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_4
    - The fourth lora parameter increases the depth of the signal counter, affecting the combined analytical and synthesis capacity of the nodes.
    - Comfy dtype: LORAS_WITH_NONE()
    - Python dtype: Union[str, None]
- lora_4_strength
    - The strength of the fourth lora signal is essential because it adjusts the salience of the signal in the pad and shapes the overall performance of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_5
    - The fifth lora parameter is indispensable for the signal pad, providing a wealth of information and enhancing the processing capacity of nodes.
    - Comfy dtype: LORAS_WITH_NONE()
    - Python dtype: Union[str, None]
- lora_5_strength
    - The strength of the fifth lora signal is important because it helps to fine-tune the role of the signal in the warehouse and influences the integrated output of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- data
    - The output data stream is the result of node processing and the structured lora and associated strength are enclosed.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeLoras:

    def __init__(self):
        self.expected_lora_stack_size = None

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'lora_1': (UI.LORAS_WITH_NONE(),), 'lora_1_strength': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.05}), 'lora_2': (UI.LORAS_WITH_NONE(),), 'lora_2_strength': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.05}), 'lora_3': (UI.LORAS_WITH_NONE(),), 'lora_3_strength': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.05}), 'lora_4': (UI.LORAS_WITH_NONE(),), 'lora_4_strength': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.05}), 'lora_5': (UI.LORAS_WITH_NONE(),), 'lora_5_strength': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.05})}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(loras, lora_1, lora_1_strength, lora_2, lora_2_strength, lora_3, lora_3_strength, lora_4, lora_4_strength, lora_5, lora_5_strength):
        loras += [{UI.F_LORA_NAME: lora_1, UI.F_LORA_STRENGTH: round(lora_1_strength, 3)}, {UI.F_LORA_NAME: lora_2, UI.F_LORA_STRENGTH: round(lora_2_strength, 3)}, {UI.F_LORA_NAME: lora_3, UI.F_LORA_STRENGTH: round(lora_3_strength, 3)}, {UI.F_LORA_NAME: lora_4, UI.F_LORA_STRENGTH: round(lora_4_strength, 3)}, {UI.F_LORA_NAME: lora_5, UI.F_LORA_STRENGTH: round(lora_5_strength, 3)}]
        return {UI.F_LORA_STACK: loras}

    def get(self, lora_1, lora_1_strength, lora_2, lora_2_strength, lora_3, lora_3_strength, lora_4, lora_4_strength, lora_5, lora_5_strength, data=None):
        if data is None:
            data = {}
        loras = retrieve_parameter(UI.F_LORA_STACK, retrieve_parameter(UI.S_LORAS, data), [])
        if self.expected_lora_stack_size is None:
            self.expected_lora_stack_size = len(loras)
        elif self.expected_lora_stack_size == 0:
            loras = []
        elif len(loras) > self.expected_lora_stack_size:
            loras = loras[:self.expected_lora_stack_size]
        data[UI.S_LORAS] = self.create_dict(loras, lora_1, lora_1_strength, lora_2, lora_2_strength, lora_3, lora_3_strength, lora_4, lora_4_strength, lora_5, lora_5_strength)
        return (data,)
```